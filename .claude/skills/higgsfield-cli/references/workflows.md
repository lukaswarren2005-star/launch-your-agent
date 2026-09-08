# Higgsfield CLI — multi-step recipes

These flows chain more than one `higgsfield` call, or aren't plain `generate create` jobs at all. Confirm exact flags with `--help` / `workflow get` before running — this file documents *sequencing*, not a frozen flag list.

## Single-call workflows: draw-to-video, reframe, voice-change, dubbing

Discover and inspect before running:
```
higgsfield workflow list
higgsfield workflow get draw_to_video
higgsfield workflow get reframe --json
higgsfield workflow get voice-change
higgsfield workflow get dubbing
```

Then create via `generate workflow`:
```
higgsfield generate workflow draw_to_video \
  --video ./source.mp4 --sketch ./frame.png --timestamp 3.2 \
  --prompt "make the jacket red" --wait

higgsfield generate workflow reframe \
  --video ./source.mp4 --aspect-ratio 9:16 --resolution 720p --wait

higgsfield generate workflow voice-change \
  --video ./source.mp4 --voice_type preset --voice_id <voice_id> --wait

higgsfield generate workflow dubbing \
  --video ./source.mp4 --target_language spa --wait
```
`--target_language` on dubbing is an ISO-639-3 code (`eng`, `spa`, `fra`, `deu`, `jpn`, …) — run `higgsfield workflow get dubbing` for the full list.

Estimate cost first where supported:
```
higgsfield generate cost workflow draw_to_video --duration 8.2 --resolution 720p
higgsfield generate cost workflow reframe --duration 7.1 --resolution 1080p
```
`voice-change` and `dubbing` don't support cost estimation.

Fetch/wait on workflow jobs the same way as model jobs: `higgsfield generate get <job_id>` / `higgsfield generate wait <job_id>`.

## Video Explainer

Two distinct paths — pick the block-by-block pipeline unless the user explicitly wants the single monolithic call:

- `explainer_video` (assembler) + separately generated `seed_audio`/`gemini_omni` blocks — the block-by-block pipeline, gives explicit control over which narration take maps to which clip. **Prefer this.**
- `video_explainer` — a single monolithic server-run job. Simpler, less control over the narration/clip mapping.

### Block-by-block pipeline

1. Resolve a style and browse presets:
   ```
   higgsfield preset list video-explainer --json
   higgsfield preset resolve video-explainer <preset_id> --json
   higgsfield voices list --json
   ```
2. Generate **all narration first**, one `seed_audio` job per 10-second block:
   ```
   higgsfield generate create seed_audio \
     --prompt "<Block 1 narration>" \
     --voice_type preset --voice_id <voice_id> --wait --json
   ```
3. Generate the **matching visual clip second**, per block, using the resolved style's media id:
   ```
   higgsfield generate create gemini_omni \
     --prompt "<Block 1 visual prompt>" \
     --image <resolved_style_media_id> \
     --duration 10 --resolution 720p --aspect_ratio 16:9 --wait --json
   ```
4. Repeat steps 2–3 once per block, in playback order.
5. Build `blocks.json` — an ordered array mapping each clip job to its matching audio job (see `models.md` / `explainer_video` schema: each item is `{"video": {"id": ..., "type": "video_job"}, "audio": {"id": ..., "type": "audio_job"}}`).
6. Assemble:
   ```
   higgsfield generate create explainer_video \
     --items @blocks.json --width 1280 --height 720 \
     --subtitles '{"font":"patrick"}' --wait --json
   ```
   Subtitle fonts: `patrick`, `caveat`, `marker`, `anton`.

### Monolithic alternative

```
higgsfield generate create video_explainer \
  --prompt "Explain compound interest to teenagers. Narration language: English." \
  --duration 60 --aspect_ratio 16:9 --preset_id <preset_id> --wait
```
`--duration` must be 20–600 and a multiple of 10. `--prompt` is required unless at least one image/file is attached; video/audio attachments are rejected here (image/file only). `--voice_type` and `--voice_id` must be supplied together if used.

## Soul ID (recurring character/face)

Train once:
```
higgsfield soul-id create --name me --soul-2 \
  --image ./me1.jpg --image ./me2.jpg --image ./me3.jpg
higgsfield soul-id wait <soul_id>
```
Reuse in any compatible model:
```
higgsfield generate create text2image_soul_v2 \
  --prompt "professional portrait, neutral background, soft daylight" \
  --soul-id <soul_id> --wait
```

## Games

Deploy a ZIP whose root has `index.html` and either `logic.js` or `server.js`:
```
higgsfield game deploy ./game.zip \
  --title "Space Runner" --description "Fast arcade survival game" \
  --thumbnail https://cdn.example/cover.png --favicon https://cdn.example/icon.png --json
```
Update the same game with `--game-id <id>`. Publishing to the marketplace is a **separate, explicit step** — confirm intent before running it:
```
higgsfield game publish <game_id> --name "Space Runner"
```
For 3D-rigging games, browse the catalog before picking an `animation_action_id`:
```
higgsfield preset list animation-action --query walk
higgsfield preset list animation-action --group Fighting --category Punching --json
```

## Websites / apps

`website create` provisions a React 19 + TanStack Start app served as a single Cloudflare Worker (D1, R2, KV, Durable Objects, Containers available), plus a git repo. This is a git-based edit loop, not a generation job.

**Required decisions before `create`:**
- `--type`: `website` (standalone, no Higgsfield integration) or `app` (users sign in with Higgsfield, generate via the Higgsfield SDK).
- `--category`: a slug from `higgsfield website categories` — validated server-side, use `other` when nothing fits; the taxonomy can grow, so don't hardcode a list from memory.
- `--type app` additionally requires `--template`, exactly one of:

  | Template | Pick when |
  |---|---|
  | `app-detail` | a single tool's public landing page, generator hero + how-it-works flow |
  | `preset` | pick-a-style generation, preset galleries, wizards, upload/configure/iterate |
  | `studio` | full creative workspace: projects, prompt dock, settings, generations feed |
  | `custom` | bare scaffold, no shipped layout — **only when the user explicitly asks for a custom/bare scaffold**; never default to it |

- `--subdomain`: derive one from the site's name (lowercase, DNS-safe) — set it explicitly rather than taking a random one. Reserved (`api`, `www`, …) and taken subdomains are rejected.

For every non-custom app template, the starter repo ships real code at `app/src/layouts/<template>.tsx`, already wired as the home page — **adapt it in place, don't rebuild or swap it**. After cloning, read `app/src/layouts/AGENTS.md` and `app/src/components/AGENTS.md` before editing.

```
higgsfield website create --type website --category other

higgsfield website create --type app --category ads-marketing \
  --template preset --subdomain my-app
```

End-to-end loop:
```
# 1. create (above)
# 2. clone with a scoped token
higgsfield website repo-access <website_id>
git -c http.extraHeader="Authorization: token <token>" clone <repo_url> <slug>
cd <slug>
git config user.email "agent@higgsfield.ai" && git config user.name "Higgsfield Agent"
# edit under app/ — bun-only repo: bun install / bun add / bunx / bun run typecheck|build
# never npm/npx/yarn; app/src/routeTree.gen.ts is generated, never hand-edit
git add -A && git commit -m "initial build"
git -c http.extraHeader="Authorization: token <token>" push origin <branch>

# 3. deploy (ships the live site — re-run after every change)
higgsfield website deploy <website_id>

# 4. optional: list on the community feed (does NOT deploy — deploy first)
higgsfield website publish <website_id>

# optional: enter the $100k app contest (type: app only) — auto-publishes,
# no separate `publish` needed; needs a live deploy + filled metadata;
# re-running overwrites the social links
higgsfield website contest <website_id> --url https://x.com/<user>/status/...

higgsfield website status <website_id>
```

Other website operations:
```
higgsfield website rename <website_id> --subdomain my-new-name   # old URL breaks — confirm with user first
higgsfield website db tables/rows/query <website_id> ...          # read-only DB inspection
higgsfield website secrets set/list <website_id> ...              # staged until next deploy; never echo values
higgsfield website list
```
