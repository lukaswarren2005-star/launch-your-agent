# Content Studio — next directions

Each item: what · why it's not in v0 · exactly how.

## v1 — more senses, more voices

| What | Why later | How |
|---|---|---|
| **ElevenLabs voiceovers** (VO for product videos, voice design for avatars) | Needs a credential | ElevenLabs API key → vault `environment_variable` credential (`ELEVENLABS_API_KEY`, `allowed_hosts: ["api.elevenlabs.io"]`, header injection). Add a `voice.md` reference to content-studio. Gate by instruction: propose VO jobs in approvals.md. |
| **Competitor ad-spend & performance data** | Needs credentials | Meta Ad Library API token (vault env var, host `graph.facebook.com`) and/or Motion creative analytics via MCP + vault. Radar then reads real run-lengths/spend instead of public pages. |
| **TikTok, YouTube and Marketing skill packs** | Deliberately left out of v0 | Bundle like the Instagram pack (`skills/<name>/` + `shared/` refs + LICENSE + adaptation note), `python3 launch.py skills`, then agent update with the new `skills[]` (bumps the version → re-run evals). Packs: sergebulaev/tiktok-skills (trend-mapper, hook-scripter, humanizer), sergebulaev/youtube-skills (title-optimizer, hook-scripter, thumbnail-brief), realjaymes/marketingagentskills (competitive-intelligence, ad-creative, icp-persona, storytelling-framework). |
| **Phone approval inbox** | Out of scope for v0 | Generated interface: a small web app over the Sessions API that lists `requires_action` events with Allow / Deny buttons and shows approvals.md + generated media. Built by Claude Code in a follow-up session. |
| **Sync memory → Content Brain doc** | Out of scope for v0 | Weekly: read the memory store (`GET /v1/memory_stores/:id/memories`) and mirror it into the Content Brain Claude Doc so it's readable on your phone. |
| **Save eval case 1 baseline** | Needs the first verified run | After the first passing Radar, copy its outputs to `evals/case-01-hydre-radar/expected.md`. |

## v2 — earned autonomy

| What | Why later | How |
|---|---|---|
| **Loosen the gate for trusted formats** | Trust is earned per format | Once a format has ~10 approvals with no rejections, set Higgsfield read-only tools (`models_explore`, `balance`, `show_generations`) to `always_allow` via `configs`, then allow scheduled runs to generate drafts for those formats only (budget cap in the prompt). |
| **Gated publishing** | Write-action into external systems | Instagram/TikTok/Meta MCP or Windsor.ai write actions + vault, toolset `always_ask`. Drafts-only until then. |
| **Memory consolidation** | Research preview; needed once memory grows | Dreams job over the content-brain store + recent sessions → review and swap in the cleaned store. |
| **Specialist team** | Only if one agent gets overloaded | Multiagent coordinator: Researcher (Radar) + Producer (Higgsfield) + Copywriter. |
| **Network hardening** | Read-mostly agent; fine for v0 | Environment `networking: limited` with research hosts + `mcp.higgsfield.ai`. |

## Always

- Re-run `evals/run_evals.py <new_version>` before pointing the deployment at a new agent version; promote only when verdicts hold.
