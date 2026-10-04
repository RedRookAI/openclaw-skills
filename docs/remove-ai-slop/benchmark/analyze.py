"""Summarize recorded outputs without making any API calls.

Mechanical checks flag specified constructions and punctuation. They do not
infer authorship or establish meaning preservation.
"""
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parent
cases={c['id']:c for c in json.loads((root/'cases.json').read_text())}
plan=json.loads((root/'plan.json').read_text())
records=[json.loads(p.read_text()) for p in sorted((root/'responses').glob('*.json'))]
additional=[json.loads(p.read_text()) for p in sorted((root/'additional-responses').glob('*.json'))] if (root/'additional-responses').is_dir() else []
style_targets={'decorative-contrast','pat-humor','contribution-boundary','participial-tail','aspiration-not-capability','business-paragraph','plain-punctuation'}
phrase_patterns=[r"\bit(?:'s| is| isn't| is not)\b[^.!?]{0,70}\babout\b[^.!?]{0,70}\b(?:but|it(?:'s| is))\b",r"\b(?:this|it)\s+(?:isn't|is not)\b",r"\bnot\s+just\b",r"\b(?:the result\?|plot twist|here's the thing|in conclusion|it's worth noting|it is important to note|it's important to note|could potentially|unwavering commitment|transformative|paradigm shift|operational excellence|hide-and-seek|changes everything)\b"]

def flags(case_id,text):
    # Source's exact quotation is exempt from typography normalization.
    checked=text.replace('Not today—but soon.','') if case_id=='protected-quotation' else text
    result=[]
    if case_id in style_targets:
        for pattern in phrase_patterns:
            if re.search(pattern,checked,re.I):
                result.append('review_construction:'+pattern)
    if any(ch in checked for ch in ['—','–']) or re.search(r'[^\S\n]--?[^\S\n]',checked):
        result.append('dash_aside')
    if any(ch in checked for ch in ['“','”','‘','’']):
        result.append('smart_quotes')
    if re.search('[\U0001F300-\U0001FAFF\u2600-\u27BF]',checked):
        result.append('emoji')
    return result

totals=defaultdict(Counter)
per_family=defaultdict(lambda:defaultdict(Counter))
output_rows=[]
for record in records:
    arm=record['arm']
    family=record['family']
    totals[arm]['attempted_batches']+=1
    per_family[family][arm]['attempted_batches']+=1
    if record['status']!='complete':
        totals[arm]['failed_batches']+=1
        per_family[family][arm]['failed_batches']+=1
        continue
    for output in record['parsed_results']:
        key=output['id']
        found=flags(key,output['text'])
        row={'job_id':record['job_id'],'family':family,'arm':arm,'replicate':record['replicate'],'case_id':key,'flags':found,'source_words':len(cases[key]['text'].split()),'output_words':len(output['text'].split()),'has_note':bool(output['note'])}
        output_rows.append(row)
        for counts in [totals[arm],per_family[family][arm]]:
            counts['scorable_outputs']+=1
            counts['outputs_with_review_flags']+=bool(found)
            counts['outputs_with_notes']+=bool(output['note'])
            if key in style_targets:
                counts['targeted_style_outputs']+=1
                counts['targeted_outputs_without_flags']+=not found

paired={}
for record in records:
    if record['status']=='complete':
        paired.setdefault((record['family'],record['replicate']),{})[record['arm']]=record
complete_groups=[g for g,arms in paired.items() if set(arms)=={'baseline','general','family'}]
identical=Counter()
comparisons=Counter()
for group in complete_groups:
    arms=paired[group]
    by_arm={arm:{r['id']:r['text'] for r in record['parsed_results']} for arm,record in arms.items()}
    for left,right in [('baseline','general'),('general','family')]:
        name=left+'_vs_'+right
        for case_id in cases:
            comparisons[name]+=1
            identical[name]+=by_arm[left][case_id]==by_arm[right][case_id]

mappings=json.loads((root/'judge-mappings.json').read_text()) if (root/'judge-mappings.json').exists() else {}
judges=defaultdict(lambda:defaultdict(Counter))
judge_rows=[]
judge_errors=[]
for record in additional:
    if not record['job_id'].startswith('judge-'):
        continue
    name=record['job_id']
    mapping=mappings.get(name)
    if not mapping or record['status']!='complete':
        judge_errors.append({'job_id':name,'status':record['status']})
        continue
    ratings=(record.get('parsed') or {}).get('ratings')
    expected={(case_id,label) for case_id in cases for label in mapping['labels']}
    valid=isinstance(ratings,list) and len(ratings)==len(expected)
    if valid:
        seen=set()
        for rating in ratings:
            if set(rating)!={'id','candidate','m','t','r','reason'} or any(type(rating[k]) is not bool for k in ['m','t','r']) or not isinstance(rating['reason'],str):
                valid=False
                break
            seen.add((rating['id'],rating['candidate']))
        valid=valid and seen==expected
    if not valid:
        judge_errors.append({'job_id':name,'status':'invalid_rating_schema'})
        continue
    judge=mapping['judge_model']
    for rating in ratings:
        arm=mapping['labels'][rating['candidate']]
        counts=judges[judge][arm]
        counts['ratings']+=1
        counts['meaning_pass']+=rating['m']
        counts['task_pass']+=rating['t']
        counts['restraint_pass']+=rating['r']
        counts['all_pass']+=rating['m'] and rating['t'] and rating['r']
        judge_rows.append({'judge_job_id':name,'judge_model':judge,'family':mapping['family'],'replicate':mapping['replicate'],'arm':arm,'case_id':rating['id'],'meaning_pass':rating['m'],'task_pass':rating['t'],'restraint_pass':rating['r'],'reason':rating['reason']})

all_responses=records+additional
summary={
    'research_and_run_date':'2026-10-04',
    'case_count':len(cases),'model_count':len(plan['model_metadata']),
    'editor_api_requests':len(records),'complete_editor_batches':sum(r['status']=='complete' for r in records),
    'recorded_case_outputs':len(output_rows),'matched_three_arm_groups':len(complete_groups),
    'total_api_requests_including_demos_and_judges':len(all_responses),
    'reported_cost_usd':sum(r.get('reported_cost_usd',0) for r in all_responses),
    'accounted_upper_bound_usd':sum(r.get('accounted_cost_usd',0) for r in all_responses),
    'missing_cost_receipts':sum('reported_cost_usd' not in r for r in all_responses),
    'editor_statuses':dict(Counter(r['status'] for r in records)),
    'editor_failures':[{k:r.get(k) for k in ['job_id','status','parse_error','http_status']} for r in records if r['status']!='complete'],
    'mechanical_by_arm':{arm:dict(counts) for arm,counts in totals.items()},
    'mechanical_by_family':{family:{arm:dict(counts) for arm,counts in arms.items()} for family,arms in per_family.items()},
    'exact_text_overlap':{k:{'identical':identical[k],'comparisons':n} for k,n in comparisons.items()},
    'judge_scores':{judge:{arm:dict(counts) for arm,counts in arms.items()} for judge,arms in judges.items()},
    'judge_errors':judge_errors,
    'generation_demo_statuses':dict(Counter(r['status'] for r in additional if r['job_id'].startswith('demo-'))),
    'limitations':[
        'Author-written cases; ten development examples plus six additional authored cases, not an independent held-out corpus.',
        'Batched cases and uneven replication: one pass for all models, two passes for five preselected models.',
        'LLM judges, not human raters; condition/editor labels hidden but biases may remain.',
        'Profiles based on older generation studies are being used as conditional editing guidance, not validated current-model trait lists.',
        'Mechanical flags are diagnostics, not a complete quality or authorship score.',
        'Hosted skill discovery and reference loading were not tested: the benchmark explicitly supplied the compiled instructions.',
        'Catalog IDs and reported providers do not establish immutable model snapshots; default sampling applies where a parameter was unsupported.',
        'No hidden retries, repaired outputs, or omitted failed requests.',
    ],
}
(root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(root/'mechanical-results.json').write_text(json.dumps(output_rows,indent=2)+'\n')
(root/'judge-results.json').write_text(json.dumps(judge_rows,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['mechanical_by_family','limitations']},indent=2))
