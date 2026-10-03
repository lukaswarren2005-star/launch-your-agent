# Claude OS: ROOKAS's operating system

A hierarchical multi-agent system that runs on **Claude Code + this repo**. Read `ARCHITECTURE.md` first.

## Run it
```bash
cd claude-os && claude          # local; the root CLAUDE.md makes this session the Master PA
```
Or open this repo in claude.ai/code (web/mobile) for the same thing from anywhere.

## Commands
| Say / type | What happens |
|---|---|
| `/new-project hydre` · `/new-project stocks --pack stocks` | Scaffold + onboarding + register |
| "HYDRÉ's CAC is up, figure out why" | Master PA routes → data-analyst → marketing + cfo → synthesis |
| `/decide …` · `/decide review all` | Log a decision · grade past decisions |
| `/experiment new` · `/experiment close EXP-003` | Pre-registered tests |
| `/report weekly hydre` · `/report daily all` | Decision-relevant reports only |

## Layout
```
CLAUDE.md                 Master PA (imports GLOBAL, REGISTRY, ROUTING)
_system/                  L1 memory + protocols: GLOBAL, REGISTRY, ROUTING, PROTOCOLS, CONNECTORS, TASKS
.claude/agents/           16 project-agnostic specialist subagents (the Master Agent Library)
.claude/skills/           new-project · decide · experiment · report
.claude/settings.json     external write tools → "ask" (human checkpoint enforced by tooling)
_templates/project/       universal project structure
_templates/packs/         stocks · crypto extensions
scripts/new-project.sh    deterministic clone + register
projects/<slug>/          L2 project memory, ledger, reports, L3 agent memory
```

## First 30 minutes
1. Fill `[FILL]` lines in `_system/GLOBAL.md`.
2. `/new-project hydre` with real numbers.
3. Ask one real question end to end. Fix whichever prompt broke.
