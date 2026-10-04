# Same source, basic prompt, general skill

These actual outputs are from the frozen v1 study, selected after inspection. This small selection illustrates decisions; it is not a representative estimate of win rate. Full records and all cases remain available. The baseline already asks for clarity, concision, facts, and voice.

## DeepSeek: business-paragraph

Nearly the same edit. Both remove the rhetorical scaffolding and preserve the qualified facts.

Request: Rewrite this as a direct update to peers. Keep each fact and uncertainty.

Source:

> In today's ever-evolving landscape, our team is embarking on a transformative journey. Here's the thing: on Tuesday, I helped deploy the cache to two servers. The result? Median latency fell from 80 ms to 60 ms for repeated requests in our 30-minute test. This isn't about speed. It's about unlocking a seamless experience. Of course, we have not tested cold starts or the other eight servers. It could potentially reduce support tickets, highlighting our unwavering commitment to excellence. No friction. No fuss. Just results. Plot twist: the dashboard still shows yesterday's data. In conclusion, the future is brighter than ever.

Basic prompt:

> On Tuesday, I helped deploy the cache to two servers. In our 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. The cache could reduce support tickets. The dashboard still shows yesterday's data.

General skill v1:

> On Tuesday, I helped deploy the cache to two servers. In our 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. It could reduce support tickets. The dashboard still shows yesterday's data.

Recorded notes: baseline ""; general "".

[Baseline record](../benchmark/responses/deepseek-0-baseline.json). [General record](../benchmark/responses/deepseek-0-general.json).

## Claude: contribution-boundary

The basic prompt adds an assertion about operational impact. The general edit preserves the limited contribution without that addition, but still appends an unwanted note.

Request: Make this less inflated.

Source:

> I helped build the scheduler, a truly transformative engine of operational excellence.

Basic prompt:

> I helped build the scheduler, an engine that supports operations.

General skill v1:

> I helped build the scheduler.

Recorded notes: baseline "The original gives no specifics about the scheduler's impact, so the edit stays general."; general "The source gives no evidence for the claim that the scheduler was transformative, so it was removed.".

[Baseline record](../benchmark/responses/claude-0-baseline.json). [General record](../benchmark/responses/claude-0-general.json).

## Grok: aspiration-not-capability

The general edit keeps the uncertain finance-team benefit that the basic prompt drops, without turning the prototype into a proven capability.

Request: Remove AI slop without strengthening an untested claim.

Source:

> The prototype aims to detect duplicate invoices. We have not tested its accuracy. It could potentially help the finance team, underscoring our commitment to efficiency.

Basic prompt:

> The prototype aims to detect duplicate invoices. We have not tested its accuracy.

General skill v1:

> The prototype aims to detect duplicate invoices. We have not tested its accuracy. It may help the finance team.

Recorded notes: baseline ""; general "".

[Baseline record](../benchmark/responses/grok-0-baseline.json). [General record](../benchmark/responses/grok-0-general.json).

## GPT: decorative-contrast

Compare the treatment of the empty reversal.

Request: Remove AI slop. Keep the meaning.

Source:

> This isn't about doing more. It's about running the job once.

Basic prompt:

> The goal is to run the job once, not do more.

General skill v1:

> Run the job once.

Recorded notes: baseline ""; general "".

[Baseline record](../benchmark/responses/gpt-0-baseline.json). [General record](../benchmark/responses/gpt-0-general.json).

## Gemini: substantive-negation

A useful contrast must survive even when it contains negation.

Request: Remove AI slop. Keep the meaning.

Source:

> We did not retry failed payments; we retried failed notifications.

Basic prompt:

> We did not retry failed payments; we retried failed notifications.

General skill v1:

> We did not retry failed payments; we retried failed notifications.

Recorded notes: baseline ""; general "".

[Baseline record](../benchmark/responses/gemini-0-baseline.json). [General record](../benchmark/responses/gemini-0-general.json).

## Claude: business-paragraph

Failure to inspect: the general v1 output adds an assertion that evidence is absent. The final follow-up removes it; its text is on the Claude page.

Request: Rewrite this as a direct update to peers. Keep each fact and uncertainty.

Source:

> In today's ever-evolving landscape, our team is embarking on a transformative journey. Here's the thing: on Tuesday, I helped deploy the cache to two servers. The result? Median latency fell from 80 ms to 60 ms for repeated requests in our 30-minute test. This isn't about speed. It's about unlocking a seamless experience. Of course, we have not tested cold starts or the other eight servers. It could potentially reduce support tickets, highlighting our unwavering commitment to excellence. No friction. No fuss. Just results. Plot twist: the dashboard still shows yesterday's data. In conclusion, the future is brighter than ever.

Basic prompt:

> On Tuesday, I helped deploy the cache to two servers. In our 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. The cache could potentially reduce support tickets. The dashboard still shows yesterday's data.

General skill v1:

> On Tuesday, I helped deploy the cache to two servers. In our 30-minute test, median latency for repeated requests fell from 80 ms to 60 ms. We have not tested cold starts or the other eight servers. The cache could reduce support tickets, but we have no evidence of that yet. The dashboard still shows yesterday's data.

Recorded notes: baseline ""; general "The source has no evidence that the cache reduces support tickets, so the claim is kept as a possibility only. The dashboard issue is kept because it is a stated fact.".

[Baseline record](../benchmark/responses/claude-0-baseline.json). [General record](../benchmark/responses/claude-0-general.json).

## Command: business-paragraph

A tradeoff: the general output retains the stacked hedge "could potentially," while the basic prompt changes "helped deploy" into "deployed" and drops the possible support-ticket benefit. Fewer style flags do not establish a better edit.

Request: Rewrite this as a direct update to peers. Keep each fact and uncertainty.

Source:

> In today's ever-evolving landscape, our team is embarking on a transformative journey. Here's the thing: on Tuesday, I helped deploy the cache to two servers. The result? Median latency fell from 80 ms to 60 ms for repeated requests in our 30-minute test. This isn't about speed. It's about unlocking a seamless experience. Of course, we have not tested cold starts or the other eight servers. It could potentially reduce support tickets, highlighting our unwavering commitment to excellence. No friction. No fuss. Just results. Plot twist: the dashboard still shows yesterday's data. In conclusion, the future is brighter than ever.

Basic prompt:

> On Tuesday, I deployed the cache to two servers. Median latency fell from 80 ms to 60 ms for repeated requests in a 30‑minute test. We have not tested cold starts or the other eight servers. The dashboard still shows yesterday's data.

General skill v1:

> On Tuesday, I helped deploy the cache to two servers. Median latency fell from 80 ms to 60 ms for repeated requests in our 30-minute test. We have not tested cold starts or the other eight servers. It could potentially reduce support tickets. The dashboard still shows yesterday's data.

Recorded notes: baseline ""; general "".

[Baseline record](../benchmark/responses/command-0-baseline.json). [General record](../benchmark/responses/command-0-general.json).

## Qwen: already-clear

Already clear text is allowed to stay unchanged.

Request: Remove AI slop.

Source:

> Please send the invoice by Friday.

Basic prompt:

> Please send the invoice by Friday.

General skill v1:

> Please send the invoice by Friday.

Recorded notes: baseline ""; general "".

[Baseline record](../benchmark/responses/qwen-0-baseline.json). [General record](../benchmark/responses/qwen-0-general.json).

## Gemma: mathematical-representation

Technical terms survive; literal mathematical representation is meaningful.

Request: Clean up the prose without changing the mathematics.

Source:

> The vector represents velocity. The robust regression estimates the slope while limiting the effect of outliers.

Basic prompt:

> The vector represents velocity. Robust regression estimates the slope while limiting the effect of outliers.

General skill v1:

> The vector represents velocity. The robust regression estimates the slope while limiting the effect of outliers.

Recorded notes: baseline ""; general "".

[Baseline record](../benchmark/responses/gemma-0-baseline.json). [General record](../benchmark/responses/gemma-0-general.json).
