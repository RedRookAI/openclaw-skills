"""Small matched prose-editing pilot, with and without meaning validation.

Two models, three new drafts, two conditions. No judges, scores, retries,
or modifications to the skill. API credentials remain in memory.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from decimal import Decimal
import argparse
import difflib
import fcntl
import hashlib
import json
import re
import shlex
import threading
import time
from pathlib import Path
import urllib.error
import urllib.request


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key-file', type=Path, required=True)
    parser.add_argument('--skill', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    lock_file = (root / '.runner.lock').open('a')
    fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
    match = re.search(r'(?m)^\s*(?:export\s+)?(?:OPENROUTER_API_KEY|OPENROUTER_KEY|OPENROUTER_TOKEN)\s*=\s*(.+?)\s*$', args.key_file.read_text())
    key = shlex.split(match.group(1), comments=True)[0] if match else ''
    if not key.startswith('sk-or-'):
        raise SystemExit('Credential unavailable; no paid calls made.')

    original = args.skill.read_text().split('---', 2)[2].strip()
    # No reference content is compiled into either condition. Remove unavailable
    # file-routing instructions from both, rather than insert a second guard.
    route_start = original.index('## Use the relevant evidence')
    route_end = original.index('## Check and deliver', route_start)
    with_validation = original[:route_start] + original[route_end:]
    start = with_validation.index('## Keep material meaning intact')
    end = with_validation.index('## Check and deliver', start)
    removed = with_validation[start:end]
    without_validation = with_validation[:start] + with_validation[end:]
    extra_check = 'Check for material changes in meaning; allow fresh wording and structure.'
    assert extra_check in without_validation
    without_validation = without_validation.replace(extra_check, 'Allow fresh wording and structure.')
    prompts = {'with_validation': with_validation, 'without_validation': without_validation}
    cases = [
        {
            'id': 'team-email',
            'request': 'Remove AI slop from this email. Make it sound like a colleague writing to the team. Return only the edited email.',
            'text': "Hi team,\n\nI wanted to take a moment to share an update on the new signup flow. I helped test it on Wednesday with six people. Four finished without help; two got stuck on the confirmation screen. That's encouraging, but there's still room for improvement.\n\nThis isn't about chasing perfection. It's about creating a seamless experience. The smaller test suggests we may get fewer support requests, though we haven't looked at that yet.\n\nCould someone from design take a look at the confirmation screen before Friday? At the end of the day, a little clarity goes a long way.\n\nThanks,\nSam"
        },
        {
            'id': 'project-readme',
            'request': 'Remove AI slop from this README introduction. Write naturally for developers deciding whether to try the tool. Return only the revised introduction.',
            'text': "Meet FolderSweep, a lightweight tool designed to streamline the way you manage downloaded files. It watches one folder, groups files by type, and shows you a preview before moving anything. You choose the sorting rules. It currently runs on Linux; Windows support is planned.\n\nBut here's the thing: this isn't just about tidying files. It's about reclaiming your focus. No clutter. No chaos. Just a calmer desktop.\n\nFolderSweep aims to save you time, whether you're a busy developer or someone who simply wants a more organized workspace. Ready to transform your downloads folder? Let's dive in."
        },
        {
            'id': 'personal-post',
            'request': 'Remove AI slop from this short personal post. Keep it conversational, with any humor that earns its place. Return only the revised post.',
            'text': "I spent Saturday trying three note-taking apps and ended up back in a text file. The file opens quickly, I know where it lives, and it has never congratulated me for writing a shopping list.\n\nTo be clear, the other apps weren't bad. One had search I liked. Another made sharing notes easy. But somewhere between choosing a color scheme and connecting a calendar, I'd forgotten what I wanted to write down.\n\nThe lesson? Sometimes simplicity is the ultimate sophistication. It's not about finding the perfect tool. It's about finding the tool that gets out of your way. For now, mine is notes.txt. We'll see how long that lasts."
        },
    ]
    models = {'gpt': 'openai/gpt-6.1-sol', 'claude': 'anthropic/claude-sonnet-5.5'}
    frozen = root / 'plan.json'
    if frozen.exists():
        plan = json.loads(frozen.read_text())
        assert plan['prompts'] == prompts and plan['cases'] == cases
    else:
        catalog = json.load(urllib.request.urlopen('https://openrouter.ai/api/v1/models', timeout=30))
        found = {m['id']: m for m in catalog['data']}
        jobs = []
        for family, model in models.items():
            for i, case in enumerate(cases):
                order = ['with_validation', 'without_validation'] if (i + (family == 'claude')) % 2 == 0 else ['without_validation', 'with_validation']
                for condition in order:
                    jobs.append({'family': family, 'model': model, 'case_id': case['id'], 'condition': condition})
        plan = {
            'created_utc': utc(), 'purpose': 'Inspect natural prose with and without the explicit material-meaning validation passages.',
            'model_selection': 'Two preselected models, GPT and Claude, before observing this pilot.',
            'case_selection': 'Three newly authored drafts, selected before this run, covering team email, README, and personal post. No scoring rubric or preservation checklist is sent to the editors.',
            'case_limit': 'Synthetic drafts by the skill author, not independent human writing or a representative sample.',
            'prompt_scope': 'v4 main instructions only. Reference-routing section omitted identically from both; supporting references and frontmatter omitted from both. Remaining general editorial instructions are matched.',
            'ablation_scope': 'Remove the entire Keep material meaning intact section and the final material-meaning check sentence. Both conditions retain ordinary author-voice, genuine-contrast, terminology, and plain-punctuation guidance. This isolates explicit validation language, not all ordinary editorial judgment.',
            'removed_section': removed, 'removed_check': extra_check, 'prompts': prompts,
            'prompt_sha256': {k: digest(v) for k, v in prompts.items()}, 'cases': cases,
            'jobs': jobs, 'local_cap_usd': '0.50', 'user_total_authorized_usd': '20',
            'previous_work_spend_usd': '0.980931372', 'max_output_tokens': 3072,
            'concurrency': 2, 'repetitions_per_pair': 1, 'seed': 20261004,
            'model_metadata': {f: {k: found[m].get(k) for k in ['id', 'pricing', 'supported_parameters', 'context_length']} for f, m in models.items()},
            'catalog_fetched_utc': utc(), 'rating_method': 'Raw per-model outputs for user inspection. No automated judges or naturalness scores.',
        }
        frozen.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + '\n')
        (root / 'prompt-diff.txt').write_text(''.join(difflib.unified_diff(with_validation.splitlines(True), without_validation.splitlines(True), fromfile='with-validation', tofile='without-validation')))
        for name, text in prompts.items():
            (root / (name + '.md')).write_text(text + '\n')

    output = root / 'responses'
    output.mkdir(exist_ok=True)
    prior = [json.loads(p.read_text()) for p in output.glob('*.json')]
    spent = sum(Decimal(str(r['accounted_cost_usd'])) for r in prior)
    reserved = Decimal('0')
    cap = Decimal(plan['local_cap_usd'])
    lock = threading.Lock()
    stop = threading.Event()

    def call(job):
        nonlocal spent, reserved
        name = '{family}-{case_id}-{condition}'.format(**job)
        path = output / (name + '.json')
        if path.exists() or stop.is_set():
            return
        case = next(c for c in cases if c['id'] == job['case_id'])
        messages = [{'role': 'system', 'content': prompts[job['condition']]}, {'role': 'user', 'content': case['request'] + '\n\n' + case['text']}]
        metadata = plan['model_metadata'][job['family']]
        in_cap = Decimal(metadata['pricing']['prompt']) * 2
        out_cap = Decimal(metadata['pricing']['completion']) * 2
        reserve = (len(json.dumps(messages, ensure_ascii=False).encode()) + 1024) * in_cap + plan['max_output_tokens'] * out_cap
        with lock:
            if spent + reserved + reserve > cap:
                stop.set()
                raise RuntimeError('Local cap reached; stopped.')
            reserved += reserve
        body = {'model': job['model'], 'messages': messages, 'max_tokens': plan['max_output_tokens'], 'stream': False,
                'provider': {'sort': 'price', 'require_parameters': True, 'max_price': {'prompt': float(in_cap * 1000000), 'completion': float(out_cap * 1000000), 'request': 0}}}
        supported = metadata.get('supported_parameters', [])
        if 'temperature' in supported:
            body['temperature'] = 0.3
        if 'seed' in supported:
            body['seed'] = plan['seed']
        if 'reasoning_effort' in supported:
            body['reasoning'] = {'effort': 'low', 'exclude': True}
        elif 'reasoning' in supported:
            body['reasoning'] = {'enabled': False, 'exclude': True}
        record = dict(job, job_id=name, started_utc=utc(), request=body, request_sha256=digest(json.dumps(body, sort_keys=True)), reservation_usd=float(reserve))
        cost = reserve
        clock = time.monotonic()
        try:
            request = urllib.request.Request('https://openrouter.ai/api/v1/chat/completions', data=json.dumps(body).encode(), headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
            response = json.load(urllib.request.urlopen(request, timeout=120))
            record['response'] = response
            actual = response.get('usage', {}).get('cost')
            if actual is not None:
                cost = Decimal(str(actual))
                record['reported_cost_usd'] = float(cost)
            else:
                record['cost_missing_reserved_in_full'] = True
            choice = (response.get('choices') or [{}])[0]
            text = choice.get('message', {}).get('content')
            record['output_text'] = text
            record['status'] = 'complete' if isinstance(text, str) and text.strip() and choice.get('finish_reason') != 'length' else 'response_failure'
            if cost > reserve:
                stop.set()
                record['reservation_exceeded'] = True
        except urllib.error.HTTPError as error:
            record.update(status='http_error', http_status=error.code, cost_missing_reserved_in_full=True)
        except Exception as error:
            record.update(status='transport_or_decode_error', error_type=type(error).__name__, cost_missing_reserved_in_full=True)
        record.update(accounted_cost_usd=float(cost), finished_utc=utc(), latency_seconds=round(time.monotonic() - clock, 3))
        serialized = json.dumps(record, indent=2, ensure_ascii=False)
        if key in serialized:
            stop.set()
            raise RuntimeError('Credential appeared in output; publication blocked.')
        with lock:
            path.write_text(serialized + '\n')
            spent += cost
            reserved -= reserve
            (root / 'ledger.json').write_text(json.dumps({'accounted_cost_usd': str(spent), 'reserved_usd': str(reserved), 'cap_usd': str(cap), 'updated_utc': utc()}, indent=2) + '\n')
            print(json.dumps({'job': name, 'status': record['status'], 'cost_usd': record.get('reported_cost_usd'), 'total_usd': str(spent)}), flush=True)

    with ThreadPoolExecutor(max_workers=2) as pool:
        for future in as_completed([pool.submit(call, j) for j in plan['jobs']]):
            future.result()
    print(json.dumps({'finished': True, 'pilot_accounted_usd': str(spent), 'prior_plus_pilot_usd': str(spent + Decimal(plan['previous_work_spend_usd']))}), flush=True)


if __name__ == '__main__':
    main()
