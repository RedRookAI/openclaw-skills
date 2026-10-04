# Tests

Recorded 2026-10-04. [See the latest before-and-after examples](../assets/examples/README.md).

## Released prompt

The released v7 adds guidance on natural sentence variety and keeps useful marketing slogans. GPT-6.1-Sol and Claude Sonnet 5.5 each edited one authored marketing sample with identical instructions. Both removed the filler and all em and en dashes while retaining the useful tagline. These examples are demonstrations, with no baseline or AI judge. [Exact requests and outputs](marketing-demo/plan.json).

## Earlier paragraph comparison

GPT and Claude each edited three new authored drafts, once with extra meaning-review instructions and once without. The outputs were mostly similar, and one pair was identical. The extra instructions showed no clear naturalness benefit in this sample, so v5 used the lighter prompt. V6 then added genre guidance that preserves useful marketing slogans.

Each condition ran once. Both received deslop instructions, so the comparison does not measure the skill's advantage over ordinary editing. Two GPT pairs used different reported providers. No separate validator or AI judge ran. Supporting references were not loaded in that pilot. [Exact prompts, inputs, settings, and outputs](paragraph-removal-pilot/README.md).

## OpenClaw

[ClawHub registry installation](clawhub-install.json) succeeded for v1.0.0. All eight downloaded files matched the published source, including the previously tested SKILL.md.

[Agent installation from the public link](handoff-test.md) passed on Haymitch using local Qwen Spark. The agent downloaded and installed all six files itself, then loaded the skill on the next request.

[Eight live turns](openclaw/README.md) ran on Seven's installed OpenClaw in isolated test state. Three used v5, two used v6, and three used the released v7. The v7 turns loaded the exact released skill and edited marketing copy, an explanation, and a personal update. Tool traces show the actual skill and reference reads. Earlier imperfect edits remain in the records.

## Earlier draft

An earlier prompt compared basic editing, general deslop, and family-specific instructions on 16 authored cases across 14 model IDs. Of 57 requests, 55 returned complete batches, producing 880 case outputs. GLM's general request returned malformed JSON, and Mistral's exhausted its output allowance. Both failures remain in the records.

On 119 matched cases targeting specified style patterns:

| Instructions | Outputs without review flags |
| --- | ---: |
| Basic clarity and concision | 107 |
| General deslop | 115 |
| Family-specific | 116 |

These flags check selected wording and punctuation. They do not measure overall quality. General and family outputs were identical in 236 of 272 matched comparisons.

Two blinded AI judges recorded a modest net improvement over basic editing. Their [ratings and reasons](judge-results.json) are not human ground truth. Those scores describe the earlier prompt, not the current release. [Study plan](plan.json). [Analysis](summary.json). [All-model examples](../examples/README.md).

Earlier generation trials produced five complete draft/edit pairs. Gemini's and Mistral's generation requests exhausted their token allowances. Later small checks and their failures are in the [record manifest](manifest.json). The cases are synthetic and partly drawn from development examples. Unseen drafts and independent human review have not been tested.

## Records

The studies and pipeline controls made 126 requests costing $1.032510372. Every request has a usage receipt. The manifest records prompts, settings, dates, providers, and hashes. Original responses are kept, and request text is stored once in files referenced by its hash.

Check the records offline:

```sh
python3 -B benchmark/verify_records.py
python3 -B benchmark/analyze.py
```

The second command summarizes the earlier study. [Earlier v5 pilot](paragraph-removal-pilot/summary.json). [Pipeline controls](paragraph-removal-pilot/controls/README.md).
