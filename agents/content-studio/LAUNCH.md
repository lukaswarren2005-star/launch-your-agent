# Content Studio — launch & run

## ⏳ Pending setup (do these first next time — ~3 steps)

| # | What | How |
|---|---|---|
| 1 | Anthropic API key | platform.claude.com → API keys (note the workspace). Either `export ANTHROPIC_API_KEY=…` in the shell, or paste it into `my-agent/.env`. Never into chat. |
| 2 | Let the build session reach Higgsfield | Claude Code cloud environment → Edit → Network access → Custom → add `mcp.higgsfield.ai` + `higgsfield.ai` (keep package managers). Only needed for the one-time sign-in. |
| 3 | Higgsfield sign-in → vault | `python3 launch.py model skills env memory vault` then `python3 higgsfield_auth.py start` → open link → approve → `python3 higgsfield_auth.py finish '<landing URL>'` |

Then: `python3 launch.py agent session` starts eval case 1 (Hydré Radar).

## Steps (each is resumable; IDs land in IDS.env)

| Step | Call | Creates |
|---|---|---|
| `model` | `GET /v1/models` | newest Opus-class slug → `MODEL` |
| `skills` | `POST /v1/skills` ×9 (zip per folder in `skills/`) | 📄 `SKILL_*` IDs |
| `env` | `POST /v1/environments` (`environment.json`) | 📦 `ENV_ID` |
| `memory` | `POST /v1/memory_stores` + one `POST …/memories` per file in `memory-seed/` | 🧠 `MEMSTORE_ID` |
| `vault` | `POST /v1/vaults` | 🔐 `VAULT_ID` (Higgsfield credential via `higgsfield_auth.py`) |
| `agent` | `POST /v1/agents` (`agent.json` + model + skills) | 🤖 `AGENT_ID`, `AGENT_VERSION` |
| `session` | `POST /v1/sessions` + outcome kickoff (`kickoff.json`) | ▶️ `SESSION_ID` |
| `status` | `GET /v1/sessions/:id` | verdict + usage |
| `outputs` | `GET /v1/files?scope_id=…` | downloads to `outputs/<session>/` |
| `deploy` | `POST /v1/deployments` (`deployment.json`) — only after a run passes | 🗓️ `DEPLOYMENT_ID` |

Manual deployment test: `curl -X POST -d '{}' "https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID/run?beta=true" -H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01" -H "anthropic-beta: managed-agents-2026-04-01" -H "content-type: application/json"`

## Day-to-day

- **Monday 7:00 Brisbane** — the 🗓️ Weekly Radar writes `radar.md`, `plan.md`, `briefs/`, `approvals.md`, `questions.md`. Nothing is generated.
- **Production** — start a session (Console → Sessions → new, or `python3 launch.py session` with your own prompt), say which approved jobs to make. Each Higgsfield call pauses for your allow/deny (`requires_action` → `user.tool_confirmation`).
- **New project** — start a session: "New project: <name, site>". The agent runs the intake questionnaire first.

Console: https://platform.claude.com/workspaces/default/agents (swap `default` for your key's workspace).
