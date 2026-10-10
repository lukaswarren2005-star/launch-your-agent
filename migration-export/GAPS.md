# GAPS — what was NOT exported and how to get it yourself

In this session, the automated permission guard **denied**: attaching the private repos, cloning the public forks, reading `~/.claude` synced-skill contents, and copying files into a separate bundle directory. Those items were not worked around. Below is how to retrieve each one manually.

| # | Missing item | Why | How to retrieve |
|---|---|---|---|
| 1 | `HYDRE` repo (private) | add_repo denied | `git clone https://github.com/lukaswarren2005-star/HYDRE` on your machine, or GitHub → repo → Code → Download ZIP. **Or** start a new Claude Code session with HYDRE selected as the source and re-run this export prompt there |
| 2 | `lukas-overview-` repo (private) | add_repo denied | Same as #1 |
| 3 | `gpt-researcher` fork | clone denied | GitHub → Download ZIP. If you never modified it, just record "fork of upstream gpt-researcher". Compare branches on GitHub ("This branch is N commits ahead") |
| 4 | `plugboard` fork | clone denied | Same as #3 |
| 5 | Skill `hydre-ugc-video` (**most important**) | synced-skill files not readable | claude.ai → Settings → Capabilities/Skills → open the skill → download/copy SKILL.md and any files |
| 6 | Skill `morning` | same | Same as #5 |
| 7 | Skill `import-memory` | same | Same as #5 (low priority) |
| 8 | claude.ai Memory | server-side, no API from this container | claude.ai → Settings → Memory → view/copy. Or ask Claude in a normal chat: "list everything you remember about me, verbatim" |
| 9 | claude.ai Projects (knowledge files + instructions) | server-side | claude.ai → each Project → copy instructions; download each knowledge file |
| 10 | Chat history | server-side | claude.ai → Settings → Privacy → Export data (emailed ZIP) |
| 11 | Scheduled routines/triggers | not queried | claude.ai/code → Routines; or ask a session to run `list_triggers` |
| 12 | Live Claude Managed Agents objects (agents, deployments, vaults, memory stores) | no Anthropic API key in session | platform.claude.com → Claude Managed Agents. Or `GET /v1/agents`, `/v1/deployments` with your key |
| 13 | `CLAUDE.local.md` (referenced by CLAUDE.md) | untracked by design; not present | Exists only on the upstream author's machine. Not yours, ignore |
| 14 | Connector settings/credentials | excluded by design (secrets) | Re-authenticate in ChatGPT |
| 15 | Content of PR #1 (Hydré images) | binary assets not fetched | https://github.com/lukaswarren2005-star/launch-your-agent/pull/1 → Files changed → download, or `git fetch origin pull/1/head` |
