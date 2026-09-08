# Higgsfield CLI — command tree

Snapshot from the `higgsfield-ai/cli` README. Run `higgsfield <command> --help` (or `higgsfield <command> <subcommand> --help`) for the live, authoritative flag list — this file is for orientation, not for copying exact flags into a call.

Universal flags, valid on every command: `--wait` (block until the job finishes, print the result URL), `--wait-timeout` (default `10m`), `--wait-interval` (default `3s`), `--json` (machine-readable output), `--no-color`.

| Command | Purpose |
|---|---|
| `higgsfield auth login` | Browser/device login. Run by the user in their own terminal — never scripted, never given a token in chat. |
| `higgsfield auth logout` | Clear local session. |
| `higgsfield auth` (inspect) | Show current token/session info. |
| `higgsfield account` | Credits balance, transactions. |
| `higgsfield workspace list` / `select <id>` / `unset` | List / choose / clear the active billing workspace. |
| `higgsfield model list` | Live model catalog (job_set_type + name). Add `--json` for scripting. |
| `higgsfield model get <job_set_type>` | Full parameter schema for one model: required/optional flags, defaults, enums, constraints. |
| `higgsfield generate create <job_set_type> [flags] [--wait] [--json]` | Create a generation job for a single model. |
| `higgsfield generate cost workflow <name> [flags]` | Estimate credit cost for a workflow before running it (not all workflows support this). |
| `higgsfield generate wait <job_id>` | Block until a job finishes. |
| `higgsfield generate get <job_id>` | Fetch current job status/result. |
| `higgsfield generate list [--json]` | List recent jobs — pipe to `jq` to filter by status, e.g. `select(.status=="completed")`. |
| `higgsfield workflow list` | List available higher-level workflows. |
| `higgsfield workflow get <name> [--json]` | Parameter schema for one workflow. |
| `higgsfield generate workflow <name> [flags] [--wait]` | Run a workflow (draw_to_video, reframe, voice-change, dubbing, …). |
| `higgsfield preset list <group> [--query ...] [--group ...] [--category ...] [--json]` | List server-managed presets/styles/actions (e.g. `video-explainer`, `animation-action`). |
| `higgsfield preset resolve <group> <preset_id> [--json]` | Resolve a preset's inputs (e.g. explainer style → hidden style image/media id). |
| `higgsfield voices list [--json]` | List voices (presets + custom) — gives `id`/`type` for `--voice_id`/`--voice_type`. |
| `higgsfield voices get <voice_id> [--json]` | Inspect one voice. |
| `higgsfield upload <file>` | Upload an image/video/audio file, get back an id usable as a media input elsewhere. |
| `higgsfield soul-id create --name <n> --soul-2 --image ... [--image ...]` | Train a reusable Soul character from reference images. |
| `higgsfield soul-id wait <soul_id>` | Block until training finishes. |
| `higgsfield marketing-studio ...` | Branded ads: avatars, products, ad references, brand kits, ad formats, DTC Ads Engine. `--help` per sub-flow. |
| `higgsfield product-photoshoot ...` | Brand image generation with mode-specific enhancement. `--help` per sub-flow. |
| `higgsfield game deploy <zip> --title ... --description ... [--thumbnail ...] [--favicon ...] [--json]` | Deploy a browser-game ZIP (`index.html` + `logic.js`/`server.js` at its root). Re-run with `--game-id <id>` to update. |
| `higgsfield game publish <game_id> --name ...` | Publish a deployed game to the marketplace (separate step from deploy). |
| `higgsfield website create --type website\|app --category <slug> [--template ...] [--subdomain ...]` | Provision a full-stack site/app + its git repo. |
| `higgsfield website categories` | List valid `--category` slugs with label/description. |
| `higgsfield website repo-access <website_id>` | Get clone URL, branch, and a scoped git token for editing. |
| `higgsfield website deploy <website_id>` | Ship the live site — run again after every change. |
| `higgsfield website publish <website_id>` | List the site on the community feed (does not deploy). |
| `higgsfield website contest <website_id> --url <social_link> [--url ...]` | Enter the app contest — auto-publishes. Re-running overwrites the links. |
| `higgsfield website rename <website_id> --subdomain <new>` | Change the live subdomain (old one stops working). |
| `higgsfield website status <website_id>` | Deploy status + live URL. |
| `higgsfield website db tables/rows/query <website_id> ...` | Read-only inspection of the site's D1 database. |
| `higgsfield website secrets set/list <website_id> ...` | Manage secrets (staged until next deploy). |
| `higgsfield website list` | List sites you own. |
| `higgsfield version` | Print build info. |

## Auth troubleshooting
- `Session expired` / `Not authenticated` → user re-runs `higgsfield auth login`.
- `Unknown model "<name>"` → run `higgsfield model list` for the current catalog; a model may have been renamed/retired.
