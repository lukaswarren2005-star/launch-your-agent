# PROJECT_REGISTRY

Source: `list_repos` for GitHub account `lukaswarren2005-star` on 2026-10-10. That's 5 repositories, all `can_push: true`.

| # | Repo | URL | Visibility | Fork | Last push | Owning project | Export status |
|---|---|---|---|---|---|---|---|
| 1 | HYDRE | https://github.com/lukaswarren2005-star/HYDRE | private | no | 2026-10-09 | Hydré | ❌ NOT EXPORTED: attach request denied by session permission guard |
| 2 | lukas-overview- | https://github.com/lukaswarren2005-star/lukas-overview- | private | no | 2026-10-07 | Personal overview / CoS (inferred) | ❌ NOT EXPORTED: attach request denied |
| 3 | launch-your-agent | https://github.com/lukaswarren2005-star/launch-your-agent | public | yes (upstream `anthropics/launch-your-agent`) | 2026-10-05 | CMA agent-building toolkit | ✅ EXPORTED IN FULL |
| 4 | gpt-researcher | https://github.com/lukaswarren2005-star/gpt-researcher | public | yes | 2026-08-27 | Research tooling (inferred) | ❌ NOT EXPORTED: clone denied by session permission guard |
| 5 | plugboard | https://github.com/lukaswarren2005-star/plugboard | public | yes | 2026-08-25 | Unknown | ❌ NOT EXPORTED: clone denied |

Nothing is claimed about the contents, purpose, bugs or dependencies of repos 1, 2, 4 and 5. They weren't read.

---

## 3. launch-your-agent — full record

- **Purpose (README):** Claude Code skill that helps a technical founder build on Claude Managed Agents: interview → scope v0 → launch → grade → iterate → scheduled deployment.
- **Upstream status (README):** "Reference implementation. Not maintained and not accepting contributions. Licensed under Apache 2.0."
- **Authorship:** every commit is by Anthropic (`Lamis Mukta` / `lamis-ant`). You've made no commits on `main`.
- **Default branch:** `main` @ `c9e0f13` (= HEAD of the export branch before this export).
- **History:** 163b35c license (2026-06-16) → db77842 initial import (06-17) → 05e9627 merge #1 → 8b4d6f4 README notice, overview-page token efficiency, skill hardening (07-02) → c9e0f13 merge #2 (07-07).
- **Open PRs on your fork:** #1 "Add Hydré clean source images for first video build" (open, created 2026-09-24). https://github.com/lukaswarren2005-star/launch-your-agent/pull/1. **Probably filed in the wrong repo**: Hydré assets belong in `HYDRE`, not a fork of an Anthropic tool. Decide: move it or close it.
- **Issues:** none.
- **Tree (18 tracked files):**
```
.claude/skills/launch-your-agent/SKILL.md
.claude/skills/launch-your-agent/references/{build-sheet.example.json, cma-api.md, examples-bank.md, interview.md, mock-connectors.md, overview-template.html, overview.css}
.claude/skills/wrap-up/SKILL.md
.gitignore  CLAUDE.md  CONTRIBUTING.md  LICENSE  README.md  cma-primitives.md
ui/{agent-overview-example.html, build-sheet.example.json, overview.css}
```
- **Tests:** none in the repo. Testing is manual: `/launch-your-agent` inside gitignored `test-runs/run-NN/`.
- **Dependencies / APIs:** Anthropic API (Claude Managed Agents: `/v1/agents`, `/v1/environments`, `/v1/sessions`, `/v1/deployments`, memory stores, vaults, Files API); curl, python3; optional `ant` CLI.
- **Env vars:** `ANTHROPIC_API_KEY` (in `my-agent/.env`, chmod 600, never committed).
- **Known debt / next steps:** see GLOBAL_MEMORY §5 (stale CLAUDE.md map, "60-minute" heading contradiction). Upstream is unmaintained, so you own any fixes.
- **Mentor note:** this repo doesn't make you money. It's only worth keeping if you'll actually build a Hydré agent on CMA. Otherwise archive it and stop paying attention to it.

## Projects (logical)

| Project | Repos | Skills | Integrations | Status |
|---|---|---|---|---|
| **Hydré** (core business, inferred) | HYDRE; PR #1 in launch-your-agent | hydre-ugc-video | Shopify, Higgsfield, ElevenLabs, Motion, Windsor.ai, Gmail | Active (push 2026-10-09). **Not exported.** |
| **Personal CoS / overview** | lukas-overview- | morning | Gmail, Google Calendar | Active (push 2026-10-07). **Not exported.** |
| **CMA agent toolkit** | launch-your-agent | launch-your-agent, wrap-up | Anthropic API | Dormant fork. Exported. |
| **Research tooling** | gpt-researcher, plugboard | — | — | Dormant forks (Aug 2026). Not exported. |
