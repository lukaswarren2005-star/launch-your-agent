# Higgsfield CLI — model catalog snapshot

This is a point-in-time list of `job_set_type` values by category, to help pick a starting point. **The live catalog wins**: run `higgsfield model list --json` for what actually exists today, and `higgsfield model get <job_set_type> --json` for that model's exact required/optional flags, defaults, and enum values before building a command — new models ship and old ones get renamed/retired.

## Image (23)

| job_set_type | name |
|---|---|
| `nano_banana_2` | Nano Banana Pro |
| `nano_banana_2_lite` | Nano Banana 2 Lite |
| `nano_banana_flash` | Nano Banana 2 |
| `nano_banana` | Nano Banana |
| `flux_2` | FLUX.2 |
| `flux_kontext` | Flux Kontext |
| `gpt_image_2` | GPT Image 2 |
| `text2image_soul_v2` | Higgsfield Soul V2 |
| `seedream_v4_5` | Seedream 4.5 |
| `seedream_v5_lite` | Seedream V5 Lite |
| `grok_image` | Grok Image |
| `openai_hazel` | OpenAI Hazel |
| `outpaint` | Outpaint |
| `recraft_v4_1` | Recraft V4.1 |
| `image_auto` | Image Auto |
| `image_background_remover` | Image Background Remover |
| `z_image` | Z Image |
| `kling_omni_image` | Kling O1 Image |
| `cinematic_studio_2_5` | Cinematic Studio 2.5 |
| `soul_cinematic` | Soul Cinematic |
| `soul_location` | Soul Location |
| `soul_cast` | Soul Cast |
| `marketing_studio_image` | Marketing Studio Image |

## Video (22)

| job_set_type | name |
|---|---|
| `brain_activity` | Virality Predictor (analyzes a finished video for hook/attention/retention/viral-potential scores) |
| `gemini_omni` | Gemini Omni Flash |
| `veo3_1` | Google Veo 3.1 |
| `veo3_1_lite` | Google Veo 3.1 Lite |
| `veo3` | Google Veo 3 |
| `kling3_0` | Kling v3.0 |
| `kling3_0_turbo` | Kling 3.0 Turbo |
| `kling2_6` | Kling 2.6 Video |
| `seedance_2_0` | Seedance 2.0 |
| `seedance_2_0_mini` | Seedance 2.0 Mini |
| `seedance1_5` | Seedance 1.5 Pro |
| `wan2_7` | Wan 2.7 |
| `wan2_6` | Wan 2.6 Video |
| `minimax_hailuo` | Minimax Hailuo |
| `grok_video` | Grok Video |
| `grok_video_v15` | Grok Video 1.5 |
| `cinematic_studio_3_0` | Cinematic Studio 3.0 |
| `cinematic_studio_video` | Cinematic Studio Video |
| `cinematic_studio_video_3_5` | Cinematic Studio Video 3.5 |
| `cinematic_studio_video_v2` | Cinematic Studio Video V2 |
| `marketing_studio_video` | Marketing Studio Video |
| `video_background_remover` | Video Background Remover |

## Video explainer jobs (related but distinct)

- `video_explainer` — alternate monolithic, single-call explainer job. Not what the block-by-block explainer pipeline uses.
- `explainer_video` — the assembler: stitches already-generated ordered video/audio block pairs. Plans nothing itself. See `workflows.md#video-explainer`.

## 3D (5)

| job_set_type | name |
|---|---|
| `multi_image_to_3d` | Multi-Image to 3D |
| `image_to_3d` | Image to 3D |
| `tripo_3d` | Text to 3D |
| `sam_3_3d` | 3D Objects |
| `3d_rigging` | 3D Rigging |

## Audio (5)

| job_set_type | name |
|---|---|
| `seed_audio` | Seed Audio 1.0 |
| `sonilo_music` | Sonilo Music |
| `mirelo_text_to_audio` | Mirelo Text to Audio |
| `text2speech_v2` | Text to Speech (engines via `--variant`: `elevenlabs`, `minimax`, `seed_speech`, `vibe_voice`, `cozy_voice`) |
| `inworld_text_to_speech` | Inworld Text to Speech |

## Conventions shared across models

- Every flag accepts both spellings: `--aspect_ratio` and `--aspect-ratio` are equivalent.
- Media-input flags (`--image`, `--image-references`, `--start-image`, `--end-image`, `--video`, `--video-references`, `--audio`, `--audio-references`) accept either a UUID (an upload id or a previous job id) or a local file path — paths are auto-uploaded.
- Most image/video models cap how many reference images/videos they accept (commonly 4, 8, 10, or 14) — `model get <job_set_type>` states the exact constraint; don't assume.
- `soul-id`-compatible models take `--soul-id <id>` from a trained Soul ID to keep a consistent character/face across generations.
