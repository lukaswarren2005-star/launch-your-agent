# UGC stills, avatars and the staged build

How to get an approved start frame: a believable person, in a believable place, holding the real product, in the right colours. Built from Caleb Kruse's character-sheet and UGC-selfie workflows (MIT, see `../ATTRIBUTION.md`) and the founder's approved Hydré staged recipe.

## The staged build (Route A in `ugc-video.md`)

One generation per step. Show it. Wait for approval. Then the next step **edits the approved frame**: name exactly what changes and end with "Keep everything else exactly the same."

| Step | What changes | Model (Higgsfield) |
|---|---|---|
| 1. Face | The avatar: candid iPhone photo of the person | `soul_2` (avatar photo as reference if one exists) or `nano_banana_2` |
| 2. Outfit | Clothes only | `flux_3_image` edit, or `nano_banana_2` edit |
| 3. Background | Setting only — name 3–4 lived-in objects and the light source | same |
| 4. Product | Product into the hand, from the product photos; how it's held, height, which side faces camera | same, product photos as references |
| 5. Colour | Colour by part with hex codes: which parts change, which stay | same |
| 6. Video | Animate the approved frame (see `ugc-video.md`) | `seedance_2_0` / `flux_3_video` |

Save every approved frame's media ID to `projects/<slug>/recipes.md` in memory — approved frames are reusable start points for the next ad.

## Still-image prompt formula

`[camera hardware] + [framing] + [person with skin cues] + [action with product] + [candid expression] + [outfit] + [setting] + [imperfection block] + [negative cues]`

Start with: `Raw iPhone front-camera selfie video frame grab.`

**Imperfection block (use 4–5):** slight motion blur on hair strands · slightly overexposed highlights on forehead and nose · visible grain and noise · front-camera wide-angle distortion on the extended arm · off-centre framing tilted a few degrees · washed-out flat colour · soft focus, nothing tack sharp · one side of the face slightly in shadow · caught mid-word, not a perfect expression.

**Negative cues (always):** `No retouching, no beauty filter, no studio lighting, not a professional photo, not perfectly composed, no airbrushed skin, no flawless complexion.`

**Skin cues** go inline with the person description (bank in `ugc-video.md`).

**Fixes**

| Problem | Fix |
|---|---|
| Too polished | Add the full imperfection block, not some of it |
| Face doesn't match the avatar | Fewer style references (max 2), avatar reference first |
| Product label garbled | Describe the product by colour/shape/material; don't rely on rendered text; logo off until branded stock exists |
| Hands wrong | "Naturally gripping the {product}, anatomically correct hand with five fingers"; regenerate |
| Background too clean | Name the mess: "cluttered counter, charging cable visible, towel over the rail" |
| NSFW filter trips in bathroom/bed scenes | Cover shoulders: satin slip top, ribbed tank, tee. No swimwear, no towels-only |

## Creating a new recurring avatar (character sheet)

Do this once per avatar so every future ad uses the same person.

1. Expand the founder's description into: `A {age}-year-old {gender} with {hair colour, texture, length}, {skin tone} skin with {one distinguishing feature}, {eye colour} eyes, {build}, {makeup level}, wearing a fitted white t-shirt and jeans. Clean white background, photorealistic, visible skin texture, individual hair strands catching light.` No celebrity or real-person names.
2. Show the expanded prompt and a name tag (`emma-redhead-wavy-freckles-green-eyes-fair`). Get a yes.
3. Generate the **hero: full body front, head to toe**, relaxed stance, eye contact, even light (`nano_banana_pro` or `soul_2`, 9:16). Full body, so later angles don't invent the lower half.
4. **Wait for approval.** Iterate here, not after 9 more images.
5. Generate the other 9 angles with the hero as reference, each starting "The exact same person from the reference image — same face, same hair, same {feature}, same eyes, same build, same clothing.": 3/4 left · 3/4 right · profile left · profile right · face close-up · over-the-shoulder · waist-up portrait · full body 3/4 walking · slightly-above angle.
6. QA for drift (hair, face shape, skin tone, clothes). Note any that drift.
7. Record the avatar in `/mnt/memory/avatars.md`: name tag, description, hero media ID, all 10 media IDs, which brands use them. Higgsfield `manage_reference_elements` / Soul Cast (`soul_cast`) can also store the identity for reuse.

## Product shots (no person)

Clean product hero for references: white background, all SKUs visible, even soft light. For lifestyle placements use the static-ad templates (`image-ad-templates.md`, e.g. T7 sticky-note flatlay, T10 letter board, T36 daily-kit flatlay) or `marketing_studio_image` for one-click variations.
