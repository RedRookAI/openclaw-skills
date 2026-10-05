# LogicTune: AI Strategist

Stop my AI from agreeing with everything I say. Help it choose useful work and finish the task.

Version: 0.1.0.

## Use

Use for planning, research, coding and long pipelines. Copy [AGENTS.md](AGENTS.md) into your operating instructions, or send your Claw:

> Get LogicTune 0.1.0 from https://github.com/RedRookAI/openclaw-skills/tree/logictune-v0.1.0/skills/logictune and merge its AGENTS.md into my active AGENTS.md. Preserve existing rules and preferences, combine duplicates, and flag conflicts. Confirm which file you updated and whether it loads.

To use it for one task, ask your agent to apply the supplied instructions without saving them as operating rules.

Persistent setup edits your active AGENTS.md only when you ask. Installing the skill alone does not apply the rules across sessions.

## References

- [Karpathy-inspired guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md)
- [OpenAI guidance on agent instructions](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)
- [honed-claude](https://github.com/itsnex1s/honed-claude)
- [Research on instruction-file growth](https://arxiv.org/abs/2608.11095)
- Fawning: [sustained pressure](https://arxiv.org/abs/2609.09090), [affective context](https://arxiv.org/abs/2608.21242), [agent memory](https://arxiv.org/abs/2607.01071).
- Independent judgment: [question reframing](https://arxiv.org/abs/2602.23971), [SWAY](https://arxiv.org/abs/2604.02423), [receptiveness](https://arxiv.org/abs/2609.26579).
- Correction and logic: [rational updating](https://arxiv.org/abs/2608.26511), [reasoning can mask sycophancy](https://arxiv.org/abs/2603.16643).
- Planning: [GAVEL](https://arxiv.org/abs/2609.19315), [PlanFence](https://arxiv.org/abs/2609.03340), [SAGE](https://arxiv.org/abs/2609.34342), [grounded foresight](https://arxiv.org/abs/2606.27483).
- Additional research: [factual agreement and uncertainty](https://arxiv.org/abs/2609.30986), [AI advice and decisions](https://arxiv.org/abs/2607.28133), [counterfactual strategic reasoning](https://arxiv.org/abs/2603.19167).
- Skill security: [semantic supply-chain attacks](https://arxiv.org/abs/2605.11418), [scanner disagreement](https://arxiv.org/abs/2606.01494), [ClawHub audit criteria](https://docs.openclaw.ai/clawhub/security-audits).
- Packaging: [skill format](https://docs.openclaw.ai/clawhub/skill-format), [OpenClaw workspace instructions](https://docs.openclaw.ai/concepts/agent-workspace), [ClawHub scan workflow](https://docs.openclaw.ai/clawhub/cli).
- GitHub security: [secret scanning](https://docs.github.com/en/code-security/reference/secret-security/secret-scanning-scope), [push protection](https://docs.github.com/en/code-security/concepts/secret-security/push-protection), [CodeQL coverage](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/).

Loading references: [OpenClaw](https://docs.openclaw.ai/concepts/agent), [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code](https://code.claude.com/docs/en/memory#agentsmd).

[MIT-0 license](LICENSE).
