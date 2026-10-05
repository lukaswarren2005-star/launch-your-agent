# UGC video playbook

Talking-head, selfie-style ads that look like a real person filmed them on a phone. Built from Caleb Kruse's Seedance/Veo UGC formulas (MIT, see `../ATTRIBUTION.md`) plus the founder's own approved Hydré recipe. **The founder's approved recipes in memory (`projects/<slug>/recipes.md`) beat anything in this file.**

## Two routes — pick one

| Route | When | How |
|---|---|---|
| **A. Staged (start-frame)** — default | A recurring avatar, a real product that must look exact, anything going into paid ads | Build an approved still one change at a time (`ugc-stills.md`), then animate it as the start frame |
| **B. One-shot (reference-driven)** | Fast tests of an angle/script, b-roll, variations of an already-winning format | Seedance 2.0 with the product photo (and avatar) as references, full 9-layer prompt |

Route A is slower but is the only one that holds product shape, colour and face reliably. Never fuse person + scene + product in one generation on Route A.

## Model routing (Higgsfield)

Check access first: `models_explore get <id>` — plan limits change. Fallbacks are in order.

| Job | First choice | Fallbacks |
|---|---|---|
| Animate an approved still (Route A) | `seedance_2_0` with the still as start/reference image | `flux_3_video` (start_image; Starter plan), `veo3`, `kling3_0` |
| One-shot UGC with product reference (Route B) | `seedance_2_0` | `seedance_2_0_mini` (cheap tests), `gemini_omni_flash_1_1` |
| B-roll / scene, no talking | `kling3_0` | `seedance_2_0`, `flux_3_video` |
| Edit an existing clip ("make the shirt black") | `flux_3_video_edit`, `kling_video_edit` | regenerate |
| Swap the product in a winning video | `hf_mult_replace_object` (Genjutsu) | — |
| Copy motion from a reference clip | `hf_mult_motion_control` (Genjutsu) | `kling3_0_motion_control` |

If Higgsfield offers a preset recommendation, decline it and generate literally unless the founder asks for presets.

## Duration from the script

Read every line out loud at a relaxed pace. AI voices rush — budget for pauses.

| Spoken words | Duration |
|---|---|
| 1–8 | 4–5 s |
| 9–15 | 6–8 s |
| 16–25 | 9–12 s |
| 26–35 | 13–15 s |
| 36+ | too long — split into 2–3 clips (hook clip, proof clip, CTA clip) and stitch |

Include at least one silent action beat per clip (inspecting, tapping, reacting).

## The 9-layer prompt (Route B, and the video step of Route A)

Stack in this order. 100–260 words for Seedance; 75–125 for Veo.

1. **Format header** — `{duration} UGC style {content type} video, filmed on smartphone, {light source}, {camera angle}.` Content types: honest review, first impression, unboxing, routine/GRWM, tutorial, day-in-my-life. Light: name the source (bedroom window, bathroom vanity, car dashboard) — never "good lighting". Angle: handheld selfie, propped on counter, mirror selfie, walking.
2. **Person** — natural-language age, casual hair, comfort clothes, and **2–3 skin reality cues** (bank below). Never a "model".
3. **Setting** — their own space + 3–4 specific lived-in objects + one atmosphere word.
4. **Product intro** — `holds the {product, described by shape/colour/material} {how}`: show to camera · already using · unboxing reveal · in-hand casual · held next to the result.
5. **Script beats** — one beat per jump cut: Hook (into camera) → Show (closer to lens) → Demo (close-up of use) → Result → Verdict. 10 s = 2–3 beats, 15 s = 3–4. Jump-cut language: "Quick jump cut —", "Cut to —", "Final shot —". Vary framing every beat. Dialogue in quotes, spoken English with filler ("okay so", "literally"), ends mid-thought or on a laugh.
6. **Tone + pacing** — 3 emotion words + behaviour, and ALWAYS an explicit pacing cue ("leaves a beat of silence after each sentence", "speaks at a relaxed, unhurried pace").
7. **Edit style** — default: "Each jump cut is slightly closer or at a different angle, as if she filmed multiple takes and kept the best bits."
8. **Technical flaws** — light flaw + 2–3 camera flaws + audio source. This is what makes it real; never skip.
9. **Vibe statement** — "The overall feel is {3 adjectives} — {relatable metaphor}." e.g. "trustworthy, relatable, real — a friend telling you about something she genuinely likes."

Close every prompt with consistency anchors and the no-text line:
`Keep her face, outfit and the product's exact shape and colour unchanged in every shot. No subtitles, no captions, no text overlays.`

### Banks

**Skin reality cues (pick 2–3):** natural skin with visible texture · visible pores across nose and cheeks · slight unevenness in skin tone · minor undereye shadows · a hint of shine on forehead from natural oils · slight pinkness on cheeks and nose · a few expression lines when smiling · light freckles. **Never** acne/blemishes/redness — real ≠ a skin condition.

**Camera physics (phone):** iPhone front camera, native wide lens · handheld sway and micro-jitter · autofocus breathes once / micro-pulses · slight exposure shift · auto white balance shift between cuts · soft focus, nothing tack sharp · mild grain in darker areas · not colour graded.

**Human motion (pick 3–4 — without these you get a frozen mannequin):** breaks eye contact, glances at the product, looks back · slight head tilts, nods along with own words · raises eyebrows for emphasis · one natural blink mid-sentence · leans toward camera then back · adjusts grip on the product · turns the product to show another angle · selfie arm visible, adjusts phone angle.

**Hands:** one hand holds the product steady; the free hand does ONE specific, repeated action (taps the product twice, points at the feature). "Natural hands, five fingers each, no warping."

**Audio:** direct from the phone mic — room tone, no music · front-camera mic, slightly tinny with room echo · car interior, road noise underneath. Name the accent if it matters ("natural Australian accent").

**Tone bank:** excited fan · chill recommender · skeptic converted · best friend sharing a secret · sleepy morning routine.

**Forbidden words** (they pull the model toward polished stock footage): cinematic, professional, stunning, 8k, studio, perfect, award-winning, color graded. For premium product work use "dramatic" or "premium" instead of "cinematic".

**Negative block:** no studio lighting, no stock-photo look, no heavy makeup, no centred perfect framing, no stabilisation or gimbal, no slow motion, no subtitles, no captions, no on-screen text.

## Timestamps for control

When beats rush or blur together, timestamp them, one main action each:
```
[00:00] Medium shot, she lifts the product to the lens: "Okay, I need to talk about this."
[00:05] Close-up on her hand twisting it on. Silent.
[00:09] Back to medium, she nods, half-smile: "Yeah. Not going back."
```

## Iterate one variable at a time

Framing off → change only the camera line. Rushed → cut words or add timestamps. Product drifts → add/strengthen the consistency anchor. Stiff → add degree adverbs (slowly, casually, deliberately) and motion cues. Never rewrite the whole prompt after a near-miss.

## Example (Route B, 15 s, kitchen, chill recommender)

```
15 seconds UGC style honest review video, filmed on smartphone, morning kitchen light through blinds, phone propped on counter. A guy in his late 20s with short dark hair and stubble, natural skin with visible pores and slight undereye shadows, wearing a worn-in black t-shirt, in his small apartment kitchen — coffee mug on counter, cutting board with a banana peel, blender in the background, morning mess and real. He has the product (matte chocolate-brown protein tub with cream label) sitting next to the blender.

The video opens with him looking at camera, half-smile: "Alright, everyone keeps asking what protein I use."

Quick jump cut — he picks up the tub and slowly turns it to show the label: "Nothing fancy. The macros are just really good."

Jump cut — close-up of the scoop coming out clean and tipping into the blender. Silent.

Jump cut — he holds the tub up and taps the lid twice: "Link's below." He laughs and walks off frame.

Throughout, the tone is relaxed, honest, conversational — he speaks slowly, leaves a beat of silence between lines, shrugs casually. Each jump cut is slightly closer or at a different angle, as if he kept the best takes.

The lighting is uneven — bright from the window side, shadow on the other. Natural phone quality, slight warm cast, not colour graded. Sound is the front-camera mic — slightly tinny, fridge hum in the background.

The overall feel is calm, honest, no-BS — a buddy telling you what he actually uses. Keep his face, shirt and the tub's exact shape and colour unchanged in every shot. No subtitles, no captions, no text overlays.
```

## Other video formats (product-only, no person)

**Premium reveal** — pure black void, rim light from above/behind, product centred; timestamped beats `[00:00]` rise into frame + bold white text line 1 → `[00:04]` slow rotation revealing a detail + text line 2 → `[00:09]` push-in on the hero feature + text line 3 → `[00:13]` brand lockup. "Camera moves slowly and deliberately, no handheld shake. The feel is premium, authoritative, restrained."

**Elemental product hero** — product on a reflective surface against a backdrop, one or two elemental effects (water splash, mist, light rays, ice, dust), 3–4 shots: extreme macro on a surface detail → hand lifts it, slow-motion → low hero angle → centred hero + tagline + end card. Describe surface condition (condensation, droplets) and the colour grade.

**Feature walkthrough** — UGC header, person wears/uses the product, one feature per jump cut with a physical demo and one short line each, confident tone. Long feature lists → a 2–3 clip series.

**Studio lookbook** — multiple looks/angles of the product with a voiceover script over styled shots; generate VO separately in ElevenLabs if the model's native audio is weak.

## Compliance (paid ads)

- The on-screen person speaks **as the brand or as a generic user describing the product**, not as a real customer claiming personal results ("it cured my eczema"). No health, medical or before/after claims the brand can't substantiate.
- AI-generated realistic people: label as AI where the platform requires it (Meta "AI info", TikTok AI-generated content label).
- No real brand logos on props; no celebrity likenesses.
