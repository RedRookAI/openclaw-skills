"""Render untouched output pairs for human inspection; no model-based scores."""
from collections import Counter
from decimal import Decimal
import hashlib
import html
import json
from pathlib import Path

root = Path(__file__).resolve().parent
plan = json.loads((root / 'plan.json').read_text())
records = [json.loads(p.read_text()) for p in sorted((root / 'responses').glob('*.json'))]
assert len(records) == len(plan['jobs'])
by_key = {(r['family'], r['case_id'], r['condition']): r for r in records}
cost = sum(Decimal(str(r['reported_cost_usd'])) for r in records)
total = cost + Decimal(plan['previous_work_spend_usd'])
controls = [json.loads(p.read_text()) for p in (root / 'controls').glob('response-*.json')]
control_cost = sum((Decimal(str(r['reported_cost_usd'])) for r in controls), Decimal('0'))
overall = total + control_cost
for record in records:
    assert record['request_sha256'] == hashlib.sha256(json.dumps(record['request'], sort_keys=True).encode()).hexdigest()
    assert record['reported_cost_usd'] == record['response']['usage']['cost']
    assert record['request']['messages'][0]['content'] == plan['prompts'][record['condition']]
    assert record['status'] == 'complete'
for k, v in plan['prompts'].items():
    assert plan['prompt_sha256'][k] == hashlib.sha256(v.encode()).hexdigest()

observations = {
    'gpt': {
        'team-email': 'Both remove the corporate padding and keep a straightforward request. The version without validation adds "to see how we can make it clearer" to the final question. The guarded version is slightly more concise; neither has an obvious stylistic failure.',
        'project-readme': 'Near-identical. The wording changes from "previews the changes" to "shows a preview." Both strip the promotional paragraphs. The API reported different providers for this pair.',
        'personal-post': 'Identical output, including the shopping-list joke. Both remove the canned lesson and reversal while retaining a conversational ending. The API reported different providers for this pair.',
    },
    'claude': {
        'team-email': 'Near-identical. Word order and "looked" versus "checked" change; both sound like the same colleague writing the update.',
        'project-readme': 'The version without validation gives a short explanation of what the tool is and keeps "You choose the sorting rules." The guarded version uses "(typically Downloads)" and "You write the sorting rules yourself." The guard does not produce an obviously more natural introduction.',
        'personal-post': 'Almost identical. The only changed sentence is "For now, I\'m using notes.txt" versus "For now, my tool is notes.txt." Both retain the joke and remove the stock lesson.',
    },
}

def quote(text):
    return '\n'.join('> ' + line for line in text.splitlines())

stats = {}
panels = []
for family, label in [('gpt', 'GPT'), ('claude', 'Claude')]:
    text = f'''# {label}: with and without validation

Requested model: `{plan['model_metadata'][family]['id']}`. One pass per condition on three new authored drafts. Outputs below are untouched. "With validation" means extra review instructions in the same editing call; no separate output validator was run. No AI judge or naturalness score was used. The comments are the assistant's reading of the samples, for you to agree or disagree with.

[Exact prompt difference](prompt-diff.txt). [Full experiment plan](plan.json). [Side-by-side view](comparison.html).

'''
    model_stats = {'pairs': 0, 'identical_outputs': 0, 'same_reported_provider_pairs': 0}
    blocks = []
    for case in plan['cases']:
        key = case['id']
        pair = {a: by_key[(family, key, a)] for a in ['with_validation', 'without_validation']}
        left, right = pair['with_validation'], pair['without_validation']
        # Aside from the content of the system instructions, the requests match.
        def settings(r):
            result = dict(r['request'])
            result['messages'] = result['messages'][1:]
            return result
        assert settings(left) == settings(right)
        model_stats['pairs'] += 1
        model_stats['identical_outputs'] += left['output_text'] == right['output_text']
        model_stats['same_reported_provider_pairs'] += left['response'].get('provider') == right['response'].get('provider')
        text += f'''## {key}

Request: {case['request']}

### Source

{quote(case['text'])}

### With validation

{quote(left['output_text'])}

[Raw response](responses/{left['job_id']}.json). Reported provider: `{left['response'].get('provider')}`.

### Without validation

{quote(right['output_text'])}

[Raw response](responses/{right['job_id']}.json). Reported provider: `{right['response'].get('provider')}`.

### What changed

{observations[family][key]}

'''
        columns = []
        for condition, title in [('with_validation', 'With validation'), ('without_validation', 'Without validation')]:
            record = pair[condition]
            columns.append('<section class="edit"><h3>' + title + '</h3><div class="prose">' + html.escape(record['output_text']) + '</div><p class="meta">Reported provider: ' + html.escape(str(record['response'].get('provider'))) + '. <a href="responses/' + record['job_id'] + '.json">Raw response</a></p></section>')
        blocks.append('<article><h2>' + html.escape(key) + '</h2><p>' + html.escape(case['request']) + '</p><details><summary>Read the source draft</summary><div class="prose source">' + html.escape(case['text']) + '</div></details><div class="columns">' + ''.join(columns) + '</div><p class="observation">Assistant observation: ' + html.escape(observations[family][key]) + '</p></article>')
    (root / (family + '.md')).write_text(text)
    stats[family] = model_stats
    panels.append('<div id="' + family + '" class="model"' + (' hidden' if family == 'claude' else '') + '><p class="meta">Requested model: ' + html.escape(plan['model_metadata'][family]['id']) + '</p>' + ''.join(blocks) + '</div>')

summary = {
    'date': plan['created_utc'], 'api_requests': len(records), 'complete_requests': len(records),
    'models': stats, 'pilot_reported_cost_usd': str(cost), 'previous_plus_pilot_usd': str(total),
    'rating_method': 'No automated judges or ratings. Actual outputs displayed for human inspection.',
    'one_pass_per_condition': True, 'supporting_references_compiled': False,
    'skill_changed_during_experiment': False,
    'separate_output_validator_run': False,
    'diagnostic_control_requests': len(controls),
    'diagnostic_control_cost_usd': str(control_cost),
    'overall_spend_including_controls_usd': str(overall),
    'request_and_cost_integrity_checked': True,
}
(root / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
(root / 'README.md').write_text(f'''# Does the validation paragraph improve the prose?

Two models, three new drafts each, one edit with the current explicit validation language and one without it. All **12 requests completed**. "With validation" means review instructions within one editing call; there is no separate validator or verified output. Pilot cost: **${cost}**. Subsequent diagnostic controls cost **${control_cost}**; total spend including earlier work and those controls is **${overall}**. No automated judge was used.

## Read the pairs

- [Side-by-side comparison](comparison.html), with tabs for GPT and Claude.
- [GPT: every source and both edits](gpt.md).
- [Claude: every source and both edits](claude.md).

## Per-model observations

| Model | Team email | README introduction | Personal post |
| --- | --- | --- | --- |
| GPT | Similar natural prose; guarded version is slightly shorter | Near-identical; one phrase differs | Exactly identical |
| Claude | Near-identical | Some phrasing differs; no obvious naturalness advantage from the guard | One closing sentence differs |

These are the assistant's observations, not independent human judgments. Both variants remove the conspicuous filler, reversals, and stock endings in these drafts. We have not changed the skill based on the pilot or expanded to the full model set.

## What this comparison can establish

This is a test of removing the explicit validation passages from otherwise matching editing instructions. Both conditions still receive the deslop instructions. It does not compare the skill against ordinary editing, or establish the skill's added value. These three authored drafts deliberately contain easy, named patterns; a single pass on them cannot establish general naturalness or whether the paragraph helps or harms on other writing. The near-identical outputs are consistent with the paragraph having little effect here, but they are not proof that it never matters.

The raw records were checked after the user questioned the identical outputs: all six pairs used different system prompts and separate API responses, while their user inputs matched. Only GPT's personal-post pair is exactly identical; the other five pairs differ. No local saved output was substituted for a request. The GPT personal-post receipts reported 1043 input tokens with the extra paragraph and 933 without; both reported zero cached input tokens. Independent completion IDs and these receipts are evidence that different prompts were submitted, not proof of an internal review process.

Two subsequent positive controls used that same GPT case, adding distinct required suffixes in the system message. Both returned the requested distinct marker. This checks that system-message changes can affect live output; it is not a naturalness test or evidence that the meaning-review paragraph was followed. [Diagnostic details and records](controls/README.md).

The source drafts, reproduced in the model pages, contain these explicit targets: the email includes "I wanted to take a moment," a perfection/experience reversal, and "At the end of the day"; the README includes "streamline," the clutter/chaos/calmer slogan, and "Let's dive in"; the personal post ends with "The lesson?" and a perfect-tool/get-out-of-the-way reversal. Both variants cut those passages. Preserving the shopping-list joke in both personal-post edits is an observed choice, not evidence that the source had no unwanted phrasing.

## What was removed

The entire `Keep material meaning intact` section, including its paragraph about an evidence audit and a separate verifier, plus the final material-meaning check. [Inspect the exact difference](prompt-diff.txt), [with-validation instructions](with_validation.md), and [without-validation instructions](without_validation.md).

Both retain the same ordinary editing instructions about author voice, useful contrast, literal terminology, and punctuation. Frontmatter and reference routing are omitted from both. Supporting references are not loaded, so they cannot reintroduce a separate validation pass. No preservation rubric, protected-fact checklist, JSON wrapper, or scoring notes were sent with the source drafts.

The three authored drafts are a team email, developer README introduction, and personal post. They were selected before seeing these outputs. They are not independently sampled human writing.

## Settings and records

Requested IDs: `openai/gpt-6.1-sol` and `anthropic/claude-sonnet-5.5`, using catalog metadata refreshed at `{plan['catalog_fetched_utc']}`. Each pair has identical user text and API settings. Condition order alternates across cases and models. Each request edits one draft and asks only for the revised prose.

GPT supported a seed but no temperature parameter: seed 20261004, provider-default sampling. Claude supported temperature but no seed: temperature 0.3. Both used low reasoning where supported and a 3072-token output allowance. No retries or paid judging calls were made.

All Claude pairs reported the same provider, Azure. GPT's email pair reported OpenAI for both; its README and personal-post pairs reported Azure with validation and OpenAI without. Those two pairs therefore include a route difference, and their wording differences cannot be cleanly attributed to the validation paragraph. Provider reports and served IDs are preserved in the records.

One observation per condition cannot separate the paragraph's effect from generation variation. The [frozen plan](plan.json) contains both exact prompts, hashes, cases, order, and pricing. Every response retains its full request, original API output, timestamps, settings, and usage receipt. The report generator verifies matched settings and cost receipts without making API calls.
''')

page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Remove AI slop: validation comparison</title>
<style>
:root{color-scheme:light dark;font-family:system-ui,sans-serif;background:#faf9f6;color:#202020}body{margin:0 auto;max-width:1200px;padding:28px}h1{font-size:1.8rem;margin-bottom:10px}h2{font-size:1.35rem}p{line-height:1.5}nav{display:flex;gap:12px;margin:22px 0}button{font:inherit;padding:10px 22px;border:1px solid #777;border-radius:5px;background:transparent;color:inherit;cursor:pointer}button[aria-pressed=true]{background:#202020;color:#fff}article{border-top:1px solid #bbb;padding:16px 0 28px}.columns{display:grid;grid-template-columns:1fr 1fr;gap:22px}.edit{padding:18px;background:#fff;border:1px solid #d3d3d3;border-radius:6px}.edit h3{margin-top:0}.prose{white-space:pre-wrap;line-height:1.65;font-family:Georgia,serif;font-size:1.05rem}.source{margin:14px 0;padding:14px;background:#eee}.meta{font-size:.85rem;color:#555}.observation{font-size:.95rem}a{color:#245da8}summary{cursor:pointer;margin-bottom:16px}button:focus-visible,a:focus-visible{outline:3px solid #507ec9;outline-offset:3px}[hidden]{display:none!important}@media(max-width:700px){.columns{grid-template-columns:1fr}body{padding:18px}}@media(prefers-color-scheme:dark){:root{background:#151515;color:#eee}.edit{background:#202020;border-color:#555}.source{background:#282828}.meta{color:#bbb}a{color:#91baff}button[aria-pressed=true]{background:#eee;color:#151515}}
</style></head><body>
<h1>With validation / without validation</h1>
<p>Actual edits on the same drafts. Two models, three drafts each, one pass per condition. No AI judge scores.</p>
<p><a href="README.md">Method and per-model observations</a> · <a href="prompt-diff.txt">Exact prompt difference</a></p>
<nav aria-label="Choose model"><button type="button" data-model="gpt" aria-pressed="true">GPT</button><button type="button" data-model="claude" aria-pressed="false">Claude</button></nav>
''' + ''.join(panels) + '''
<script>
document.querySelectorAll('button[data-model]').forEach(button=>button.addEventListener('click',()=>{
document.querySelectorAll('.model').forEach(panel=>panel.hidden=panel.id!==button.dataset.model);
document.querySelectorAll('button[data-model]').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));
}));
</script></body></html>
'''
(root / 'comparison.html').write_text(page)
print(json.dumps(summary, indent=2))
