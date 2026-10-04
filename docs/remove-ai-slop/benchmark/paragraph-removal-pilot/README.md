# Does the validation paragraph improve the prose?

Two models, three new drafts each, one edit with the current explicit validation language and one without it. All **12 requests completed**. "With validation" means review instructions within one editing call; there is no separate validator or verified output. Pilot cost: **$0.0447355**. Subsequent diagnostic controls cost **$0.0068435**; total spend including earlier work and those controls is **$1.032510372**. No automated judge was used.

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

Requested IDs: `openai/gpt-6.1-sol` and `anthropic/claude-sonnet-5.5`, using catalog metadata refreshed at `2026-10-04T02:19:27.880377+00:00`. Each pair has identical user text and API settings. Condition order alternates across cases and models. Each request edits one draft and asks only for the revised prose.

GPT supported a seed but no temperature parameter: seed 20261004, provider-default sampling. Claude supported temperature but no seed: temperature 0.3. Both used low reasoning where supported and a 3072-token output allowance. No retries or paid judging calls were made.

All Claude pairs reported the same provider, Azure. GPT's email pair reported OpenAI for both; its README and personal-post pairs reported Azure with validation and OpenAI without. Those two pairs therefore include a route difference, and their wording differences cannot be cleanly attributed to the validation paragraph. Provider reports and served IDs are preserved in the records.

One observation per condition cannot separate the paragraph's effect from generation variation. The [frozen plan](plan.json) contains both exact prompts, hashes, cases, order, and pricing. Every response retains its full request, original API output, timestamps, settings, and usage receipt. The report generator verifies matched settings and cost receipts without making API calls.
