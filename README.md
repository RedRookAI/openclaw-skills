# OpenClaw Skills

Skills and copy-and-paste prompts for everyday problems with AI agents.

| Skill | What it does |
| --- | --- |
| [Remove AI slop](skills/remove-ai-slop/README.md) ([ClawHub](https://clawhub.ai/redrookai/skills/remove-ai-slop)) | Makes AI drafts read naturally. Cuts canned phrasing, forced jokes, and repetitive rhetoric. |
| [AI LogicTune: Better decisions, less wasted time 0.1.4](skills/logictune/README.md) ([ClawHub](https://clawhub.ai/redrookai/skills/logictune)) | Helps an agent question weak logic, check prior art, keep work scoped and finish useful work. |
| [AI Fiction: Pro Editor 0.1.0](skills/ai-fiction/README.md) ([ClawHub](https://clawhub.ai/redrookai/skills/ai-fiction)) | Edits fiction for dialogue, pacing and readable prose while respecting the author's style and story continuity. |
| [QuickTicket 0.1.0](skills/quickticket/README.md) ([ClawHub](https://clawhub.ai/redrookai/skills/quickticket)) | Turns ideas and projects into scoped, dependency-ordered tickets with clear acceptance and a practical next step. |
| [BugDoctor 0.1.0](skills/bugdoctor/README.md) ([ClawHub](https://clawhub.ai/redrookai/skills/bugdoctor)) | Helps an agent diagnose software failures, check existing remedies and verify a scoped repair. |
| [TestRight: Get Answers Without Endless Testing 0.1.2](skills/test-right/README.md) ([ClawHub](https://clawhub.ai/redrookai/skills/test-right)) | Runs scoped tests, checks actual outcomes and keeps comparisons fair. |

## TestRight

TestRight helps your AI test whether something actually works or improves results. Say “Use TestRight to test this,” and it examines the relevant project, chooses meaningful checks, runs them and inspects the outputs. It addresses common AI testing mistakes: testing the wrong thing, using incorrect expected answers, coaching the baseline, leaking information between comparisons and claiming success without evidence. It also keeps testing scoped, preserves useful results and directs the AI to stop when it has enough evidence to answer your question.

## Give It to Your Claw

Open a skill's page and send its install message to your Claw. Follow the setup steps on that page. [LogicTune has one message to install and activate its rules in AGENTS.md](skills/logictune/README.md#install-and-activate).

Where available, you can also download a skill ZIP from [Releases](https://github.com/RedRookAI/openclaw-skills/releases) and extract it into your OpenClaw workspace's `skills/` directory. [OpenClaw setup](https://docs.openclaw.ai/tools/skills).

Each skill also includes a standalone prompt you can paste into a chat.

Licenses are listed in each skill folder; the repository's default is [MIT](LICENSE).
