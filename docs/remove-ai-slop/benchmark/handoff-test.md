# Give it to your Claw: installation test

Tested 2026-10-04 on Haymitch's existing OpenClaw 2026.9.7 with local Qwen Spark. The agent received the public ZIP link and the same installation message shown in the README. It downloaded, inspected, and installed the skill itself. All six files matched the published bundle. A second request loaded the installed SKILL.md and edited a draft.

The test used a fresh workspace and state. The running bot's config and gateway stayed unchanged. No helper installer, new OpenClaw runtime, paid provider, or AI judge was used. One installation and model were tested; the marketing edit still retained a stock joke.

[Requests, outputs, tool calls, and file hashes](handoff-test.json).
