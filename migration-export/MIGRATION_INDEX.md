# MIGRATION_INDEX — Claude → ChatGPT export

Export date: 2026-10-10 · Source: one Claude Code cloud session (claude.ai/code), repo `lukaswarren2005-star/launch-your-agent`, branch `claude/claude-to-chatgpt-migration-yp1ui5`, base commit `c9e0f1378a252bd42deb7e9eb02ac0cbd07160bc`.

## Read this first — honest scope statement

This package is **partial**. It is a faithful export of what this session could actually read, not of your whole Claude environment.

| Status | Count | What |
|---|---|---|
| Exported in full (originals, unmodified, in git at their original paths) | 1 repo, 18 files | `launch-your-agent` |
| Identified but NOT exported (access blocked in this session) | 4 repos | `HYDRE` (private), `lukas-overview-` (private), `gpt-researcher` (public fork), `plugboard` (public fork) |
| Custom skills exported | 2 | `launch-your-agent`, `wrap-up` — **authored by Anthropic, not you** (see below) |
| Custom skills identified, NOT exported | 3 | `hydre-ugc-video`, `morning`, `import-memory` (claude.ai synced skills; content blocked) |
| Custom agents (subagent definitions) found | 0 | None exist in any accessible location |
| Projects identified | 4 | Hydré (brand/product), Personal CoS / overview (lukas-overview-), CMA agent toolkit (launch-your-agent), Research tooling (gpt-researcher, plugboard) |
| Claude memory exported | 0 files | No memory files are accessible from this cloud container; claude.ai memory lives server-side |

**Critical finding:** every commit in `launch-your-agent` was authored by Anthropic staff (`Lamis Mukta` / `lamis-ant`, June–July 2026). It's Anthropic's Apache-2.0 reference implementation that you forked. The `CLAUDE.md`, both skills and all the docs are **not your operating system**. They're a public tool you cloned. The only user-authored artifact in this fork is open PR #1 ("Add Hydré clean source images for first video build"). Your real business material is in the repos and skills listed as NOT exported.

## Package contents

| File | Purpose |
|---|---|
| `MIGRATION_INDEX.md` | This file — inventory, scope, migration steps, gaps |
| `GLOBAL_MEMORY.md` | Your explicit preferences + inferred context, labelled by provenance |
| `AGENT_REGISTRY.md` | Existing agents (none custom) + target hierarchy mapping |
| `SKILL_REGISTRY.md` | Every skill visible in this environment, with compatibility notes |
| `PROJECT_REGISTRY.md` | Projects and repos, with status and access |
| `DECISION_LOG.md` | Decisions, constraints and open questions |
| `INTEGRATIONS.md` | Connected MCP servers / integrations, with setup steps (no secrets) |
| `COMPATIBILITY_MATRIX.md` | Claude feature → ChatGPT equivalent or limitation |
| `manifest.json` | Machine-readable inventory of every artifact and its export status |
| `GAPS.md` | Everything not exported and exactly how to get it manually |
| Original files | Unmodified at their original repo paths (`../.claude/skills/...`, `../CLAUDE.md`, etc.). The ZIP bundles them under `repositories/launch-your-agent/` |

## How to use this in ChatGPT (target workflow)

1. **Get the gaps first.** Do every step in `GAPS.md`. The missing items are the ones that matter most.
2. **Custom Instructions** (ChatGPT → Settings → Personalization): paste the "Explicit user instructions" block from `GLOBAL_MEMORY.md`, plus the mandatory operating constraints from `DECISION_LOG.md` §1.
3. **ChatGPT Memory:** don't bulk-paste. Add the confirmed facts from `GLOBAL_MEMORY.md` §2 one at a time ("Remember that…").
4. **Projects:** create one ChatGPT Project per row in `PROJECT_REGISTRY.md`. Upload that project's repo snapshot or README as Project files and paste its instructions into the Project instructions.
5. **Agents and skills → Custom GPTs:** build each agent in `AGENT_REGISTRY.md` §3 as a Custom GPT (or a Project with instructions). For each skill, upload `SKILL.md` + `references/` as Knowledge files and paste the frontmatter `description` into the GPT description. Read `COMPATIBILITY_MATRIX.md` first: shell, file-system and Claude-API steps do not carry over as-is.
6. **Integrations:** reconnect each service in `INTEGRATIONS.md` through ChatGPT Connectors/Apps or Actions. Use fresh OAuth. No credentials are in this package.
7. **Keep Claude Code for repo work** until the Codex/ChatGPT path is proven on one project. `launch-your-agent` is a Claude Managed Agents tool and only targets Anthropic's API.

## Verification performed

- Secret scan (patterns: `sk-ant-`, `ghp_`, `github_pat_`, `xoxb-/xoxp-`, AWS `AKIA…`, `PRIVATE KEY`) over the exported repo: **no matches**.
- File list, byte sizes and SHA-256 prefixes for all 18 repo files are recorded in `manifest.json`.
- Duplicate check: 3 byte-identical pairs found (intentional per CLAUDE.md: `ui/` mirrors the skill's `references/`). See `manifest.json` → `duplicates`.
- ZIP: see the final report in chat for whether the archive was built and verified. This file does not claim it.
