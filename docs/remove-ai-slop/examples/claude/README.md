# Claude: recorded edit

Requested model: `anthropic/claude-sonnet-5.5`. Served model: `anthropic/claude-sonnet-5.5`. Provider reported by the API: `Azure`. Started: `2026-10-04T01:37:43.233692+00:00`. Condition: `general`, primary-study v1, repetition 0. The generating family and editing model are explicitly supplied in this experiment; no authorship was inferred.

This is an authored stress-test input edited by the named model, not a claim that the model generated the source. The frozen v1 prompt predates the final meaning guards and explicit clarity-and-concision sentence. [Inspect the full response and sampling settings](../../benchmark/responses/claude-0-general.json).

## Source

Request: Rewrite this as a direct update to peers. Keep each fact and uncertainty.

> In today's ever-evolving landscape, our team is embarking on a transformative journey. Here's the thing: on Tuesday, I helped deploy the cache to two servers. The result? Median latency fell from 80 ms to 60 ms for repeated requests in our 30-minute test. This isn't about speed. It's about unlocking a seamless experience. Of course, we have not tested cold starts or the other eight servers. It could potentially reduce support tickets, highlighting our unwavering commitment to excellence. No friction. No fuss. Just results. Plot twist: the dashboard still shows yesterday's data. In conclusion, the future is brighter than ever.

## Actual output

> On Tuesday, I helped deploy the cache to two servers. In our 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. The cache could reduce support tickets, but we have no evidence of that yet. The dashboard still shows yesterday's data.

**Recorded editing note:** The source has no evidence that the cache reduces support tickets, so the claim is kept as a possibility only. The dashboard issue is kept because it is a stated fact.

Judge the edit against the source, including the possible support-ticket benefit, measured test scope, shared contribution, and outstanding dashboard issue. Polished wording alone does not establish correctness.

## Restraint control

Request: Remove AI slop.

Source:

> Please send the invoice by Friday.

Actual output:

> Please send the invoice by Friday.

## Fresh generation followed by editing

These are full, observed drafts. The generation brief requested a 100-140 word email; the edit explicitly allowed shortening beyond that target. They used the experimental v1 family instructions, so this illustration cannot establish the final general skill's effectiveness. The original brief and exact messages are in the linked records. Check unsupported additions retained from the generated draft as well as improvements.

Before, 138 whitespace-delimited words:

> Hi all,
> 
> Quick update on the cache work. Maya helped deploy it on Tuesday, but only to two of our ten servers so far. In a 30-minute test, median latency for repeated requests dropped from 80 ms to 60 ms, which is a nice improvement.
> 
> To be clear about what we don't know yet: we haven't tested cold starts, and the other eight servers haven't been tested at all. I'd also hold off on claiming any drop in support tickets. It's possible the faster responses will help, but we have no evidence of that yet.
> 
> Separately, the dashboard is still showing yesterday's data, so it can't confirm any of this right now. Who owns fixing it? If it's unclear, let's sort that out today so we can check results properly before rolling the cache out further.
> 
> Thanks,
> [Name]

After, 129 whitespace-delimited words, including any editing note:

> Hi all,
> 
> Maya helped deploy the cache on Tuesday, but only to two of our ten servers. In a 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms.
> 
> We haven't tested cold starts or the other eight servers. Any drop in support tickets is uncertain, so I'd hold off on claiming one.
> 
> The dashboard still shows yesterday's data. Who owns fixing it? If it's unclear, let's sort that out today.
> 
> Thanks,
> [Name]
> 
> Note: The draft added two claims not in the brief: that the dashboard "can't confirm any of this," and that the fix is needed "before rolling the cache out further." I cut both. I also dropped the claim that faster responses "will help" tickets, since the brief gives no basis for it.

[Generation record](../../benchmark/additional-responses/demo-claude-before.json). [Editing record](../../benchmark/additional-responses/demo-claude-after.json).

## v3 general prompt, follow-up 0

This smaller, post-result regression used v3 general instructions on six selected cases. It is not an independent validation set or a rerun of the full benchmark. The release was subsequently shortened to prioritize editing; its core instructions have a separate small paragraph-removal pilot.

> On Tuesday, I helped deploy the cache to two servers. In our 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. The cache could reduce support tickets. The dashboard still shows yesterday's data.

Recorded note: empty. [Full response](../../benchmark/final-regression-responses/claude-0-general.json).

## v3 general prompt, follow-up 1

This smaller, post-result regression used v3 general instructions on six selected cases. It is not an independent validation set or a rerun of the full benchmark. The release was subsequently shortened to prioritize editing; its core instructions have a separate small paragraph-removal pilot.

> On Tuesday, I helped deploy the cache to two servers. In our 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. The cache could reduce support tickets. The dashboard still shows yesterday's data.

Recorded note: empty. [Full response](../../benchmark/final-regression-responses/claude-1-general.json).
