# System-message transport controls

The user questioned whether identical edits indicated a pipeline error. Two new calls reused the GPT personal-post inputs, appending an explicit instruction to add a different diagnostic marker to each response.

- [First response](response-with_validation.json) ended with `CONTROL-CEDAR-6V4Q`, as required by its system message.
- [Second response](response-without_validation.json) ended with `CONTROL-BIRCH-8R2M`, as required by its system message.

Both requests completed. API-reported cost: $0.0068435. [Plan](plan.json).

This is a positive control for system-message changes reaching the generation behavior. It does not establish that a silent meaning review occurred, validate the deslop prompt, or provide a naturalness score. The editing test itself used one call per condition, with and without extra review instructions; neither output passed through a separate validator.
