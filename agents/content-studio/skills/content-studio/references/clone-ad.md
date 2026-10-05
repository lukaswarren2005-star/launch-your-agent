# Clone a competitor or reference ad

Take an ad that works and rebuild its structure for our product. Adapted from Caleb Kruse's `clone-ad`, `analyze-video` and `image-ad-clone` workflows (MIT, see `../ATTRIBUTION.md`).

**The rule:** copy the *structure* (hook format, beat order, camera, pacing, layout), never the *expression* (their words, their people, their logo, their footage). Every line of dialogue and copy gets rewritten for our brand.

## Inputs

- The reference: a video file, an image, a link (TikTok/IG/Meta Ad Library), or a screenshot.
- Which brand/product (from `/mnt/memory/projects/<slug>/`), with product photos.
- Goal: **one-off clone** (make our version now) or **template** (save the format for reuse), or both.

## Video ad → our version

1. **Analyse.** Upload the reference to Higgsfield (`media_upload` / `media_import_url`) and run `video_analysis_create` (poll `video_analysis_status`). In Claude Code with ffmpeg available, you can also pull frames yourself (8 frames under 10 s, 12 for 10–20 s, 16 for 20–30 s, 20 beyond) and transcribe with whisper.
2. **Break it down** into a table: beat · seconds · framing/camera · action · spoken line · on-screen text. Then note: hook format, narrative arc, edit rhythm, tone (3 words), lighting/quality, audio, how the product is shown, the CTA style.
3. **Name the 2–3 defining traits** — the things that make someone say "oh, it's *that* kind of video". These must survive the clone.
4. **Compress to 15 s if needed.** Keep the hook, the one core moment and the kicker. Longer arcs become a 2–3 clip series.
5. **Adapt.** Map each beat to our product: same structure, our proof, our CTA, dialogue rewritten in our brand voice. Show the side-by-side (theirs → ours) and get a yes.
6. **Generate** via `ugc-video.md` (staged route when our product must look exact). For a near-identical motion/shot, `hf_mult_motion_control` transfers the reference's motion onto our approved frames; `hf_mult_replace_object` swaps a product inside footage *we own*.
7. **Log** the clone in `projects/<slug>/formats.md` (source link, defining traits, what we changed, result).

## Video style → reusable template

Same analysis, but the output is a written formula instead of a video: "What defines this style" (2–3 paragraphs) → its layers (as many as it really has) → for each layer a pattern with `{{VARIABLES}}` and an option bank → one complete filled example → an adaptation checklist. Save it in `projects/<slug>/formats.md` so future sessions can use it.

## Static ad → our version or a new template

1. **Describe the reference structurally**, top to bottom: canvas ratio, regions, typography (weight, case, colour), UI it mimics, imagery, count of elements (3 bubbles, 5 checklist rows). Mark what's brand-specific `[BRAND]` vs structural.
2. **Check the library first** — `image-ad-templates.md` may already have it (37 formats).
3. **Write the prompt**: canvas line, regions in vertical order, references by index, explicit "no platform UI" close, + the three safety suffixes. Model: `gpt_image_2` for type/UI-heavy, `nano_banana_2` for photoreal.
4. **Round-trip** with the reference attached until the structure is faithful (max 4 rounds; change one thing per round).
5. **Generalise**: replace `[BRAND]` bits with `{placeholders}`; test-fill with a second brand to prove it generalises.
6. **Save** as the next `T40+` entry (fields in `image-ad-templates.md`) in `projects/<slug>/formats.md`, with model notes for whichever models you validated.

## Where references come from

- Meta Ad Library (public), TikTok Creative Center, competitors' own feeds.
- Motion creative analytics (`get_inspo_creatives`, `get_workspace_competitors`) — what competitors are spending behind.
- The founder's saved posts and screenshots.
