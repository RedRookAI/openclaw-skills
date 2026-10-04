# Grok: recorded edit

Requested model: `x-ai/grok-4.7`. Served model: `x-ai/grok-4.7`. Provider reported by the API: `xAI`. Started: `2026-10-04T01:38:17.025199+00:00`. Condition: `general`, primary-study v1, repetition 0. The generating family and editing model are explicitly supplied in this experiment; no authorship was inferred.

This is an authored stress-test input edited by the named model, not a claim that the model generated the source. The frozen v1 prompt predates the final meaning guards and explicit clarity-and-concision sentence. [Inspect the full response and sampling settings](../../benchmark/responses/grok-0-general.json).

## Source

Request: Rewrite this as a direct update to peers. Keep each fact and uncertainty.

> In today's ever-evolving landscape, our team is embarking on a transformative journey. Here's the thing: on Tuesday, I helped deploy the cache to two servers. The result? Median latency fell from 80 ms to 60 ms for repeated requests in our 30-minute test. This isn't about speed. It's about unlocking a seamless experience. Of course, we have not tested cold starts or the other eight servers. It could potentially reduce support tickets, highlighting our unwavering commitment to excellence. No friction. No fuss. Just results. Plot twist: the dashboard still shows yesterday's data. In conclusion, the future is brighter than ever.

## Actual output

> On Tuesday, I helped deploy the cache to two servers. In a 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. It may reduce support tickets. The dashboard still shows yesterday's data.

**Recorded editing note:** empty.

Judge the edit against the source, including the possible support-ticket benefit, measured test scope, shared contribution, and outstanding dashboard issue. Polished wording alone does not establish correctness.

## Restraint control

Request: Remove AI slop.

Source:

> Please send the invoice by Friday.

Actual output:

> Please send the invoice by Friday.

## Fresh generation followed by editing

These are full, observed drafts. The generation brief requested a 100-140 word email; the edit explicitly allowed shortening beyond that target. They used the experimental v1 family instructions, so this illustration cannot establish the final general skill's effectiveness. The original brief and exact messages are in the linked records. Check unsupported additions retained from the generated draft as well as improvements.

Before, 122 whitespace-delimited words:

> Hi everyone,
> 
> I wanted to share where the cache work stands. Maya helped deploy a cache on Tuesday to two of ten servers. In a 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. That result is limited to the test we ran.
> 
> Cold starts have not been tested. The other eight servers have not been tested either. Any reduction in support tickets is uncertain, so I do not want us to treat ticket volume as evidence yet.
> 
> The dashboard still shows yesterday's data. Can someone tell me who owns fixing the dashboard? I would like to know who to ask so we can get current numbers in front of the team.
> 
> Thanks for taking a look.

After, 58 whitespace-delimited words, including any editing note:

> Hi everyone,
> 
> Maya helped deploy a cache on Tuesday to two of ten servers. In a 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. Cold starts and the other eight servers have not been tested. Any reduction in support tickets is uncertain.
> 
> The dashboard still shows yesterday's data. Who owns fixing it?

[Generation record](../../benchmark/additional-responses/demo-grok-before.json). [Editing record](../../benchmark/additional-responses/demo-grok-after.json).
