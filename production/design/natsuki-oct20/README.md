# Natsuki restyle, Oct 20 (design pass)

**Decided (author, Oct 20):** long, soft brushed-out waves and green eyes, replacing the shoulder-length cut and amber-brown eyes. He picked option 5 from `options.jpg` ("I like 5 best too"). Canon §8 and style guide §1–§2 are updated.

## Files
| File | What it is |
|---|---|
| `options.jpg` | The eight looks shown to the author: 1 as shipped, 2–8 with green eyes. Tiles 4–8 are edits of the same sprite, so only the hair changes; 3 is the first-pilot sprite with only the eyes recolored. |
| `natsuki-lock-uniform.png` | **Full-body lock** (school uniform). Use it for CGs, lineups and scale. Same pose and body as `refs/natsuki-v2/01-restyle-uniform.png` (her legs still run a little long for 5′3″). |
| `sprites/natsuki_school_{smile,grin,laugh,smirk,surprised,blush,wistful}.webp` | **The school sprite set**, finished with `sprites.py` (one shared crop, 1800 px tall). Drop-in replacements for `v2/img/ch/` (same names and expressions). |
| `faces/natsuki_school_*.webp` | Face windows, `faces.py h0.25 0.04 0` (the settings the shipped set used). Drop-in for `v2/img/face/`. |
| `master/natsuki-school-base.png` | 2K master of the smile sprite on white. Every new school expression starts from this. |

## How the set was made
1. **Options:** `fal-ai/nano-banana-pro/edit`, 2K, 2:3, seed 7, on the shipped smile sprite (on white): "change ONLY her hairstyle and her eye color…" with the hair spec, copper #b55e36 (shadow #6c3c2f), green irises. Option 5's hair line: "long hair past her chest in soft, loose, brushed-out waves, polished and glossy (neat and deliberate, not messy or windswept), with soft side-swept bangs; some wavy lengths fall forward over the front of her shoulders."
2. **Base:** option 5 as generated is the smile sprite.
3. **Expressions:** `fal-ai/nano-banana-2/edit`, 2K, seed 7, inputs [base, the shipped expression sprite as image 2], "change ONLY her facial expression, to match the expression of the girl in image 2… ignore its hair and its eye color." The edits redrew the hair a little longer and redder, so **only the face was kept**: `face_composite.py base variant out --center 0.495 0.15 --radius 0.112 0.093 --feather 24`. The hair and body are pixel-identical across all seven, so nothing jumps when expressions swap.
4. **Cutout:** one bria cutout of the base; its alpha is shared by all seven (they differ only inside the face).
5. **Lock:** `nano-banana-pro/edit`, 2K, seed 31, inputs [`refs/natsuki-v2/01-restyle-uniform.png`, the base], "change ONLY her hair and her eye color, so that they match the girl in image 2"; length pinned ("ends a little below her chest, ABOVE her waist… moderate volume"). Seed 7 drew hip-length, much bigger hair and was rejected.

## Notes for production
- **Waves drift.** Left alone the model makes them longer, bigger and tousled (the first-pilot look). In every new image, check length (a little below the chest in front) and neatness against the sprite. Pass the base or the lock as a reference.
- The lock's hair renders slightly darker and more auburn than the sprite. **The sprite is the color reference.**
- The lock keeps the small ear stud from the Oct 6 image; the sprites, like the shipped ones, don't show one. Nobody has decided whether she wears one.
- The blush sprite has two small sweat drops (forehead, cheek). It reads as flustered; swap them out if they bother anyone.
- Iris green sampled from the sprite: about #6a8867 overall (light #8eaf85, dark #294030).
- Other Natsuki images (casual, athletic, kendo, seasonal outfits, turnaround, bogu) predate this. Regenerate them from the lock when a chapter needs them.

## Spend
About $2.10: 10 NB Pro edits (7 options, a bob retake, 2 lock takes; about $1.50), 6 NB2 edits (about $0.60), 1 bria cutout. Counted against the Pilot v2 cap.
