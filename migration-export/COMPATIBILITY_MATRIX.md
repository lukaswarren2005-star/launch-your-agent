# COMPATIBILITY_MATRIX — Claude → ChatGPT

Verdicts: ✅ direct equivalent · 🟡 partial / needs rework · ❌ no equivalent. ChatGPT product features change often, so verify each 🟡 against current OpenAI docs before relying on it.

| Claude feature (used in your setup) | ChatGPT equivalent | Verdict | What changes |
|---|---|---|---|
| claude.ai personal preferences | Custom Instructions | ✅ | Paste the block from GLOBAL_MEMORY §1 |
| claude.ai memory | ChatGPT Memory | 🟡 | No bulk import. Add facts individually; review Memory settings |
| claude.ai Projects (knowledge + instructions) | ChatGPT Projects | ✅ | Re-upload files; size/count limits differ |
| Claude skills (SKILL.md + references, auto-triggered by description) | Custom GPTs (instructions + Knowledge files) | 🟡 | No auto-triggering by description. You pick the GPT (`@name`). Scripts inside skills don't execute unless rewritten for Code Interpreter |
| Slash-command invocation (`/morning`, `/wrap-up`) | `@CustomGPT` mention or a saved prompt | 🟡 | Manual invocation |
| `CLAUDE.md` project instructions auto-loaded per repo | Project instructions / `AGENTS.md` for Codex | 🟡 | Codex reads `AGENTS.md`. Copy CLAUDE.md → AGENTS.md if you use Codex on that repo |
| Claude Code (terminal agent: Bash, edit, git) | OpenAI Codex (CLI / cloud) | 🟡 | Different permission model, tools and harness |
| AskUserQuestion (structured choice prompts) | None (plain chat) | ❌ | The GPT asks in text; you answer in text |
| Subagents / Agent tool, background tasks | Agents SDK handoffs (code) / Agent mode | 🟡 | No in-chat subagent spawning; hierarchy is manual (see AGENT_REGISTRY) |
| Hooks (`settings.json` PreToolUse/Stop etc.) | None in ChatGPT; Codex has limited config | ❌ | Enforce approvals through instructions plus your own review |
| MCP connectors (Gmail, Calendar, GitHub) | Built-in ChatGPT connectors | ✅ | Re-auth |
| MCP connectors (Shopify, Higgsfield, ElevenLabs, Motion, Windsor) | App directory / custom remote MCP (developer mode) / GPT Actions | 🟡 | Availability per service unverified; see INTEGRATIONS.md |
| Scheduled routines / `morning` recurring brief | ChatGPT Tasks | 🟡 | Task output is chat/notification, not a styled HTML artifact |
| Artifacts (HTML pages) | Canvas (code preview) | 🟡 | Canvas renders HTML/React; no hosted private URLs with capabilities/db |
| Claude Managed Agents (agents, environments, sessions, outcomes, deployments, vaults, memory stores) | OpenAI Agents SDK + Responses API + your own hosting/cron | ❌ (no managed equivalent) | `launch-your-agent` and `wrap-up` can't run against OpenAI. A rewrite is needed |
| Outcome rubric grading (`user.define_outcome`) | OpenAI Evals / graders | 🟡 | Rubric text ports; the runtime loop doesn't |
| Deep research skill | ChatGPT Deep Research | ✅ | Built in |
| docx/xlsx/pptx/pdf skills | Code Interpreter file generation | ✅ | Built in |
| Computer use / Chrome extension | ChatGPT Agent mode (virtual browser) | 🟡 | Runs in OpenAI's VM, not your browser/sessions |

## Do NOT silently drop
- Approval gates (`always_ask`, drafts-only) only exist in ChatGPT as written rules. Put the universal agent contract (AGENT_REGISTRY §2) in every GPT.
- Key hygiene rules from launch-your-agent (never paste keys into chat) apply even more on ChatGPT: never put API keys in GPT instructions or Knowledge files.
