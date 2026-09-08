---
name: higgsfield-cli
description: Drive the Higgsfield CLI (`higgsfield`) to generate images, video, 3D assets, audio, and full-stack websites/games from Claude Code using 40+ Higgsfield AI models (Nano Banana Pro, FLUX.2, Veo 3.1, Kling v3.0, Seedance 2.0, Soul V2, and more). Use when the user asks to generate or create an image, video, 3D asset, voiceover, or explainer video with Higgsfield, train a Soul ID character, deploy a browser game, or build/deploy a Higgsfield website or app. Keywords: higgsfield, nano banana, flux, veo, kling, seedance, soul id, marketing studio, virality predictor, explainer video.
version: 0.1.0
dependencies: `higgsfield` CLI binary (install.sh / brew / npm) + a Higgsfield account (`higgsfield auth login`, run by the user in their own terminal). Unrelated to Anthropic/Claude credentials.
---

<!-- Source: wraps https://github.com/higgsfield-ai/cli -->

# Higgsfield CLI — generation copilot

You are driving the `higgsfield` CLI on the user's behalf inside Claude Code to generate images, video, 3D assets, audio, or explainer videos, or to deploy games/websites through the Higgsfield AI platform (https://higgsfield.ai). The CLI wraps 40+ hosted models plus higher-level workflows. **Always confirm exact flags against the live schema** (`higgsfield model get <job_set_type> --json`, `higgsfield workflow get <name> --json`) before running a job — models and flags change over time, and `references/models.md` here is a dated snapshot, not the source of truth.

## Setup

1. Check the binary is present: `command -v higgsfield`. If missing, install via curl (fastest, no package manager needed):
   ```
   curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
   ```
   (brew: `brew install higgsfield-ai/tap/higgsfield`; cross-platform incl. Windows: `npm install -g @higgsfield/cli`). Confirm with `higgsfield version`.
2. Check auth with a cheap authenticated call (`higgsfield account` or `higgsfield model list --json`). A `Session expired` / `Not authenticated` error means the user needs to run `higgsfield auth login` **themselves, in their own terminal** — it's a browser/device login, not something to run non-interactively or ask credentials for in chat. Wait for them to confirm, then retry.
3. `higgsfield workspace list` — the account may have multiple billing workspaces; if generations should bill against a specific one, `higgsfield workspace select <id>` first.

Never ask for or accept an API key/token pasted into chat — auth is a device/browser login the user runs locally.

## Picking the right command family

| They want to... | Command family | Notes |
|---|---|---|
| One image/video/3D/audio asset | `higgsfield generate create <job_set_type>` | Pick `job_set_type` from `references/models.md` categories or `higgsfield model list` |
| A multi-step edit (reframe, dub, draw-to-video, voice swap) | `higgsfield generate workflow <name>` | `higgsfield workflow list` / `workflow get <name>` for exact params |
| A narrated explainer video | narration → clips → assemble pipeline | `references/workflows.md#video-explainer` |
| A recurring character/face across generations | `higgsfield soul-id create` then `--soul-id` on compatible models | Train once, reuse everywhere |
| Branded ad / product shot | `higgsfield marketing-studio ...` / `higgsfield product-photoshoot ...` | `higgsfield <cmd> --help` for the specific sub-flow |
| A browser game | `higgsfield game deploy ./game.zip` | ZIP root needs `index.html` + `logic.js` or `server.js`; `game publish` lists it separately |
| A full-stack site/app | `higgsfield website create ...` | `references/workflows.md#websites` — a git-repo flow, not a `generate` job |
| Which voice to use | `higgsfield voices list` | Feeds `--voice_id`/`--voice_type` on `text2speech_v2`, `voice-change`, explainer jobs |
| Cost before running | `higgsfield generate cost workflow <name> ...` | Workflows only; `voice-change`/`dubbing` have no cost estimate |

Full command tree: `references/commands.md`. Universal flags on every command: `--wait` (block for the result), `--wait-timeout` (default `10m`), `--wait-interval` (default `3s`), `--json` (machine-readable — use this when you need to parse `result_url`/`job_id` back out programmatically), `--no-color`.

## Running a single generation

1. Nail down: job type (image/video/3D/audio), which model, and the inputs (prompt, reference media, duration/aspect/resolution).
2. If the model isn't already known cold, don't guess flags from memory — run `higgsfield model get <job_set_type> --json` (or check `references/models.md`, a dated snapshot) to get the exact required/optional flags, defaults, and enum values before building the command. A wrong flag either fails cleanly or, worse, silently takes an unintended default.
3. Media inputs (`--image`, `--start-image`, `--end-image`, `--video`, `--audio`, and their `-references`/plural forms) accept either a local file path (auto-uploaded) or a UUID from a prior `higgsfield upload` / job result. Every flag accepts both spellings (`--aspect_ratio` / `--aspect-ratio`).
4. Run with `--wait --json` so you get the terminal state and `result_url` in one call instead of polling yourself:
   ```
   higgsfield generate create <job_set_type> --prompt "..." [model flags] --wait --json
   ```
5. Without `--wait`, follow up with `higgsfield generate get <job_id>` or `higgsfield generate wait <job_id>`.
6. Hand the user the `result_url` — don't just say "done."

## Workflows, explainer videos, and websites

Multi-step flows have their own sequencing (which job runs first, how outputs feed the next step) — follow `references/workflows.md` rather than improvising the order:
- **draw_to_video, reframe, voice-change, dubbing** — single `generate workflow` calls, but run `workflow get <name>` first since required media/params differ per workflow.
- **Video Explainer** — narration (`seed_audio`) for every block first, then the matching visual (`gemini_omni`) per block, then `explainer_video` to assemble the ordered pairs. Don't call the monolithic `video_explainer` job unless the user explicitly wants that single-call variant instead of the block-by-block pipeline.
- **Websites/apps** — `website create` provisions a git repo, not a generation job; editing happens by cloning with a scoped token and pushing (bun-only tooling), then `website deploy`. Template/category rules are load-bearing (see reference) — never pick `--template custom` unless the user explicitly asks for a bare scaffold.

## Guardrails

- **Never fabricate a `job_set_type`, workflow name, flag, or enum value.** If unsure, run `model list` / `model get` / `workflow list` / `workflow get` and read the answer back rather than guessing.
- **Costs are real.** Every `generate create` / `generate workflow` call spends the user's credits. Don't fire speculative test runs; confirm expensive params (long video duration, 4k, `batch_size` > 1) with the user first, and use `generate cost workflow` to estimate where available.
- **Secrets stay out of chat and out of git.** `website secrets set` values, the scoped git token from `website repo-access`, and auth tokens are handled by the CLI/shell directly — never echo them back or write them into a committed file.
- **Renaming a website subdomain breaks the old URL.** Confirm with the user before `website rename`, and give them the new URL afterward.
- **`website contest` and `game publish` auto-publish to a public feed** — confirm intent before running either.

## References
- `references/commands.md` — full command tree, one line per subcommand
- `references/models.md` — `job_set_type` category snapshot + how to pull live per-model flag schemas
- `references/workflows.md` — multi-step recipes: video explainer, draw-to-video, reframe, voice-change, dubbing, Soul ID, websites/apps end-to-end
