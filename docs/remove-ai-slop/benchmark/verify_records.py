"""Offline integrity checks; this program makes no API calls."""
from decimal import Decimal
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'manifest.json').read_text())
count = 0
cost = Decimal('0')
for group in ['responses', 'additional-responses', 'regression-responses', 'final-regression-responses']:
    for path in sorted((root / group).glob('*.json')):
        record = json.loads(path.read_text())
        request = record['request']
        for message in request['messages']:
            source = (root / message.pop('content_file')).resolve()
            assert source.is_relative_to(root.resolve())
            raw = source.read_bytes()
            assert hashlib.sha256(raw).hexdigest() == message.pop('content_sha256')
            message['content'] = raw.decode()
        actual = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()
        assert actual == record['original_request_sha256'], path
        if 'request_sha256' in record:
            assert actual == record['request_sha256'], path
        assert record['response']['usage']['cost'] == record['reported_cost_usd'], path
        cost += Decimal(str(record['reported_cost_usd']))
        count += 1
assert count == manifest['api_requests']
assert cost == Decimal(manifest['reported_cost_usd'])
assert hashlib.sha256((root.parents[2] / 'skills/remove-ai-slop/SKILL.md').read_bytes()).hexdigest() == manifest['released_skill_sha256']
assert hashlib.sha256((root / 'tested-skill-v3.txt').read_bytes()).hexdigest() == manifest['latest_primary_study_follow_up_skill_sha256']
body = json.loads((root / 'openclaw/tested-v5-skill.json').read_text())['SKILL.md'].split('---', 2)[2].strip()
start = body.index('## Use the relevant evidence')
end = body.index('## Check and deliver', start)
core = body[:start] + body[end:]
assert core == (root / 'paragraph-removal-pilot/without_validation.md').read_text().strip()
pilot_cost = Decimal('0')
pilot_count = 0
for folder, pattern in [('responses', '*.json'), ('controls', 'response-*.json')]:
    for path in (root / 'paragraph-removal-pilot' / folder).glob(pattern):
        record = json.loads(path.read_text())
        actual = hashlib.sha256(json.dumps(record['request'], sort_keys=True).encode()).hexdigest()
        assert actual == record['request_sha256'], path
        assert Decimal(str(record['response']['usage']['cost'])) == Decimal(str(record['reported_cost_usd'])), path
        pilot_cost += Decimal(str(record['reported_cost_usd']))
        pilot_count += 1
assert cost + pilot_cost == Decimal(manifest['overall_reported_cost_usd'])
assert count + pilot_count == manifest['overall_api_requests_including_pilot_and_controls']
print(json.dumps({'verified_requests': count, 'recorded_cost_usd': str(cost)}))
