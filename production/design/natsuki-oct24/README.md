# Natsuki sprite tweaks, Oct 24 (exploration; nothing installed)

**Asked (author, Oct 24):** fix the waist mismatch with Nanoha ("option 1 works"), and "explore revised sprites for her in general… i find nanaho prettier currently and wonder if we need some natsuki tweaks." **Status: options only.** Nothing here is in the build or on `main` (the author's Ch1 hold: "dont commit or make changes yet").

## Files
| File | What it is |
|---|---|
| `sheet_waist.jpg` | The same line (c1_0194) at iPad landscape: as built; option 1, Natsuki's waist lowered 1.7 in; option 2, Nanoha's raised 2 in instead. |
| `preview_recommended.jpg` | The recommendation at the same line: face A on Natsuki's as-built body, Nanoha raised 2 in. |
| `sheet_faces.jpg` | Head crops from the game screen: Nanoha for reference, Natsuki as built, option A (seed 254), option B (seed 251). Both options sit on the waist-fixed body. |
| `heads_grid.jpg` | All four head edits as generated, before compositing. |
| `heads/head_25{1..4}.png` | The four edits, resized to the crop (746 px). Paste at master x 474, y 0. |
| `preview/*.webp` | Drop-in test sprites for `v2/img/ch/` (smile only): Natsuki face A, waist lowered, waist lowered + face A or B; Nanoha raised 2 in. |
| `refs/` | The inputs: crops of the Natsuki master (x 474–1220, y 0–746) and of Nanoha's smile sprite, and Nanoha on white. |

## The waist
Measured on the rendered iPad screen (1640 px tall at 2×; the engine's scale is 32.4 px per inch there), at each girl's shirt-to-skirt line, height above the shared floor:

| | Natsuki (5′3″) | Nanoha (4′11″) | Apart |
|---|---|---|---|
| As built | 40.6 in | 34.4 in | 6.1 in |
| Natsuki lowered (option 1) | 39.0 in | 34.4 in | 4.5 in |
| Option 1 + Nanoha raised 1.5 in | 39.0 in | 36.0 in | 3.0 in |
| **Option 2:** Nanoha raised 2 in, Natsuki as built | 40.6 in | 36.5 in | 4.1 in |

A natural waist sits at about 0.62 of height: 39.1 in for her and 36.6 in for Nanoha, about 2.5 in apart. By that measure option 1 puts Natsuki where a real 5′3″ girl's waist is, and Nanoha's waist sits low (0.58 of her height). The earlier estimate (4.75 in before the fix) was taken from the sprites, not the screen; this one supersedes it.

**But the blind check disagreed with the tape measure** (below): it found as-built Natsuki the most natural (a high waist and long legs read as normal for the style), and lowered Natsuki the least natural ("the gap between the bow and the waistband is too long"; her open blazer shows a long white shirt panel). It found raised Nanoha (the 1.5 in take it was shown) better than as built; the 2 in take was made after the check and only I have looked at it. So **the recommendation is option 2**: leave Natsuki's body, raise Nanoha's waist 2 in. Option 1 is still available.

**Tool:** `production/pipeline/vn/torso_warp.py` moves one row of the sprite and stretches or squeezes the rows between a fixed line and the bottom, so the head, the face and the overall height don't move. It works on the finished sprites directly (RGBA), and the face windows are untouched (they're above the fixed line).
- Natsuki: `--keep-above 0.367 --move 0.544 0.585` (her sprites are the master at full height, so the fractions are the same on both).
- Nanoha: `--keep-above 0.26 --move 0.566 0.520` (2 in up; `0.531` is 1.5 in). Her face doesn't move; her bow and the end of her braid sit a little higher and the braid comes out slightly shorter (the check noticed it side by side); her hands and hem rise with the waist.

Natsuki's sprites differ only inside the face, so one warp setting applies to all seven, and Nanoha's likewise.

## The face
Edits of a head crop of the master (`refs/natsuki-head-crop.png`) with Nanoha's head as image 2, `fal-ai/nano-banana-pro/edit`, 2K, 1:1. Each result is pasted back through the same face oval the expression set uses (`face_composite.py --center 0.495 0.15 --radius 0.112 0.093 --feather 24`), so her hair outside the face stays the shipped hair.

| Seed | Prompt (short) | Result |
|---|---|---|
| 251 (**B**) | "Redraw ONLY her eyes and face construction in the drawing style of image 2: larger, rounder eyes with a strong dark upper lash line, big glossy irises with large soft highlights, fine lower lashes; a softer, slightly rounder face shape and chin; a smaller, simpler nose; warm soft blush on the cheeks; delicate, slightly thicker outer line work. Keep HER identity… green irises, her copper hair with side-swept bangs exactly as it is, her gentle closed-mouth smile. Keep the framing…" | Bigger, rounder irises; a heavy orange blush. Hair kept. |
| 252, 253 | 251 plus "her hair drawn with many fine individual strands and soft highlights instead of large flat shiny panels" | Hair went lighter and more orange (off the sprite's copper). Rejected. |
| 254 (**A**) | 253 plus "tuck the hair on the right side of her face (the viewer's right) neatly behind her ear" | Rounder eyes, a light hatched blush like Nanoha's, finer strands at the bangs. No tuck. Color held. |

Batch 1 (same day, not kept): two whole-body proportion edits (241, 242) barely moved the waist, so the waist became the deterministic warp; three whole-body face edits (244, 245, 247) changed too little and one (246) reframed the picture; one prompt (243) was declined by the content filter and wasn't retried.

## Blind check (fresh agent, shuffled labels, Natsuki described in words only)
- **Faces:** A first ("big and bright eyes… moderate blush… pretty and lively"; "balances confident and warm best"; "matches Nanoha's soft blush best"); B second (the cheeks "overpower the face… reads flushed"); as built last ("smaller, heavier-lidded… more mature and a bit plainer"; "cool rather than warm… drifts toward sleepy"). The difference shows at scene size, mostly in the blush. No seams. It flagged "a small dark dot" under the eye: on inspection that's the white cheek highlight the shipped sprite and Nanoha's both have, so nothing to fix.
- **Bodies:** as built most natural, Nanoha raised second, Natsuki lowered last (see above). Also: "Nanoha's head looks noticeably bigger, as if she's closer to the camera." That's how her sprite is drawn, not something this pass changes; noted for the backlog.

## If one is picked
1. Waist: run `torso_warp.py` with the same setting on every school sprite of whoever moves (Nanoha's set for option 2, Natsuki's seven for option 1). The face windows don't change.
2. Face: the six other expressions have to be remade from the new base (the Oct 20 recipe, `../natsuki-oct20/README.md` step 3: NB2 edits, about $0.60), then the face windows (`faces.py h0.25 0.04 0`), then the arrival CG, its falter and the title art get the same face (region edits, about $0.45).
3. A punch-list batch check (snapshot diff, one independent check).

## Spend
About $1.50: 10 NB Pro edits at 2K (the declined one produced nothing). Not yet in `../../pilot-v2/ledger.md` (that's on `main`, which is on hold); add it when this is installed or dropped.
