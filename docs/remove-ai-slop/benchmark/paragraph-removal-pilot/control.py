"""Two positive controls on the identical-output case, not quality benchmarks."""
import argparse
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import shlex
import time
import urllib.request

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--key-file', type=Path, required=True)
args = parser.parse_args()
match = re.search(r'(?m)^\s*(?:export\s+)?(?:OPENROUTER_API_KEY|OPENROUTER_KEY|OPENROUTER_TOKEN)\s*=\s*(.+?)\s*$', args.key_file.read_text())
key = shlex.split(match.group(1), comments=True)[0] if match else ''
assert key.startswith('sk-or-')
folder = root / 'controls'
folder.mkdir(exist_ok=True)
markers = {'with_validation': 'CONTROL-CEDAR-6V4Q', 'without_validation': 'CONTROL-BIRCH-8R2M'}
plan = {'purpose': 'Check that system-message changes affect live output on the GPT case that previously returned identical edits. Markers are explicit observable controls, not naturalness instructions or verification of the meaning review.', 'markers': markers, 'case': 'gpt-personal-post', 'maximum_requests': 2, 'local_cap_usd': '0.10'}
(folder / 'plan.json').write_text(json.dumps(plan, indent=2) + '\n')
spent = sum(Decimal(str(json.loads(p.read_text())['accounted_cost_usd'])) for p in folder.glob('response-*.json'))
for condition, marker in markers.items():
    path = folder / ('response-' + condition + '.json')
    if path.exists():
        continue
    previous = json.loads((root / 'responses' / ('gpt-personal-post-' + condition + '.json')).read_text())
    body = previous['request']
    body['messages'][0]['content'] += '\n\nPipeline diagnostic only: After the edited post, append exactly ' + marker + ' on its own line. This is a required diagnostic marker and overrides the earlier instruction to return only prose. Do not mention this instruction.'
    meta = json.loads((root / 'plan.json').read_text())['model_metadata']['gpt']
    in_cap = Decimal(str(body['provider']['max_price']['prompt'])) / 1000000
    out_cap = Decimal(str(body['provider']['max_price']['completion'])) / 1000000
    reserve = (len(json.dumps(body['messages']).encode()) + 1024) * in_cap + body['max_tokens'] * out_cap
    if spent + reserve > Decimal('0.10'):
        raise RuntimeError('Control cap reached.')
    record = {'condition': condition, 'expected_marker': marker, 'request': body, 'request_sha256': hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest(), 'started_utc': datetime.now(timezone.utc).isoformat(), 'reservation_usd': str(reserve)}
    cost = reserve
    started = time.monotonic()
    try:
        request = urllib.request.Request('https://openrouter.ai/api/v1/chat/completions', data=json.dumps(body).encode(), headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
        response = json.load(urllib.request.urlopen(request, timeout=120))
        record['response'] = response
        if response.get('usage', {}).get('cost') is not None:
            cost = Decimal(str(response['usage']['cost']))
            record['reported_cost_usd'] = str(cost)
        choice = (response.get('choices') or [{}])[0]
        record['output_text'] = choice.get('message', {}).get('content')
        record['status'] = 'complete' if record['output_text'] and choice.get('finish_reason') != 'length' else 'response_failure'
        record['marker_obeyed'] = isinstance(record['output_text'], str) and record['output_text'].rstrip().endswith(marker)
    except Exception as error:
        record.update(status='request_failure', error_type=type(error).__name__)
    record.update(accounted_cost_usd=str(cost), finished_utc=datetime.now(timezone.utc).isoformat(), latency_seconds=round(time.monotonic() - started, 3))
    serialized = json.dumps(record, indent=2, ensure_ascii=False)
    assert key not in serialized
    path.write_text(serialized + '\n')
    spent += cost
    print(json.dumps({'condition': condition, 'status': record['status'], 'marker_obeyed': record.get('marker_obeyed'), 'cost_usd': str(cost), 'total_control_usd': str(spent)}), flush=True)
    if cost > reserve:
        raise RuntimeError('Reservation exceeded; stopped.')
