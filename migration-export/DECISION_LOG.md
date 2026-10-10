# DECISION_LOG

## 1. Your constraints (EXPLICIT, 2026-10-10) — highest priority
1. The user retains final authority over consequential decisions.
2. Research agents must not autonomously approve or advance opportunities.
3. Explicit approval before material changes to repositories, production websites, financial commitments or external systems.
4. Preserve functioning implementations unless an approved migration plan establishes a reason to change them.
5. Distinguish facts, assumptions, estimates and recommendations.
6. Track sources, uncertainty, decisions and unresolved questions.
7. Never fabricate repository contents, research findings, integrations or test results.

Standing preference: "Direct and brutal. Be my mentor and remember we are building businesses."

## 2. Decisions made during this export (2026-10-10)
| Decision | Why |
|---|---|
| Export package committed only to the designated branch `claude/claude-to-chatgpt-migration-yp1ui5`. Nothing merged to `main`, no PR opened | Constraint 3 |
| Original repo files left untouched in place; registries reference them by path | Constraint 4 / "do not redesign" |
| Inaccessible repos and skills recorded as gaps, not reconstructed | Constraint 7 |
| Your email deliberately not written into files | `launch-your-agent` is a **public** repo; the branch is publicly readable |
| No credentials read or exported | Requirement §7 |

## 3. Historical decisions — launch-your-agent (UPSTREAM / Anthropic, not yours)
Source: `CLAUDE.md` (verbatim file preserved at repo root). Summary of its "Key decisions":
- Audience: technical founder in Claude Code; show the machinery.
- Build what they need, scoped into versions. Opus-class by default, full toolset, cloud env, Outcome kickoff `max_iterations: 3`, drafts-only.
- Open light; boundaries raised in context; let the founder explain before suggesting.
- Don't undersell: separate hard limits from defaults; gated write-actions possible in v0.
- No spend-limit step; no cost notes unless asked.
- Never stop to wait for the key: heads-up early, hand over late, key never in chat (rotate if it touches a transcript).
- Connectors named and mockable: mock in v0, wire in v1.
- Voice rules: emoji shorthand per primitive, real primitive names, no unverified durations.
- NEXT-DIRECTIONS.md written in the moment as numbered versions.
- Celebratory close owned by `/wrap-up`.
- Evals: real past cases = golden set; re-run before promoting.
- Overview page: describe-only live schema, CSS linked never inlined, Edit in place.
- Scheduled deployments only for genuinely recurring jobs; relative dates in `initial_events`.
- Sourcing rule: only officially grounded examples in the interview menu.

## 4. Conflicts / contradictions found (not resolved — flagged)
| # | Conflict | Where | Suggested resolution (needs your call) |
|---|---|---|---|
| C1 | "No clock/'hour' framing" vs heading "Design implications for the 60-minute skill" | CLAUDE.md vs `cma-primitives.md` | Upstream inconsistency. Ignore unless you maintain the fork |
| C2 | "Also installed at ~/.claude/skills/…" | CLAUDE.md | False in this environment. Treat as upstream-author context |
| C3 | Hydré PR #1 is in an Anthropic-tool fork | launch-your-agent PR #1 | Move the assets to `HYDRE` and close the PR |
| C4 | The harness default of "commit and push" vs your constraint 3 | session | The push went only to the designated non-default branch, as this session was set up for. Nothing reached `main` |

## 5. Open questions (yours to answer)
1. Do you want `HYDRE` and `lukas-overview-` exported? It needs a session where access to those repos is allowed (see GAPS.md).
2. Are `gpt-researcher` and `plugboard` used at all, or dead forks to archive?
3. What is `lukas-overview-`: a CoS dashboard, a personal site, or something else?
4. Do you have live CMA agents/deployments in your Anthropic account that must keep running during the move?
5. Do you want to keep Claude Code for repo work and use ChatGPT for the CoS layer (recommended), or move fully?
6. Should the export branch stay on a **public** repo? It reveals your project names and connected tools. Consider deleting the branch after downloading the ZIP.
