# Natsuki sprite tweaks, Oct 24

**Asked (author, Oct 24):** fix the waist mismatch with Nanoha ("option 1 works"), and "explore revised sprites for her in general… i find nanaho prettier currently and wonder if we need some natsuki tweaks."

**Decided (author, Oct 24 afternoon): face A, her original scale and body.** "i like a for nat face"; "maybe original scale with the new face us fine". No waist fix for either girl. **Status: the face-A set is built here and waits to go in with the author's Ch1 batch** (his hold: "dont commit or make changes yet"). Nothing is in the build or on `main`.

## The face-A set (drop-in)
| Folder | Goes to | What |
|---|---|---|
| `sprites/` | `v2/img/ch/` | The seven school expressions with face A, plus **`natsuki_school_curious`** (new; the Ch1 batch's approved "curious" face). Same size, crop and cutout as the shipped set; outside the face oval every pixel is the shipped sprite's. |
| `faces/` | `v2/img/face/` | Face windows, `faces.py h0.25 0.04 0` (reproduces the shipped smile window exactly). |
| `game/img/bg/`, `game/img/th/` | `v2/img/bg/`, `v2/img/th/` | `cg_natsuki_intro`, `cg_natsuki_intro_falter`, `cg_title`, exported with `export_cg.py` (which reproduces the shipped files exactly from the shipped masters). |
| `cg/*_faceA.webp` | `production/pilot-v2/art/masters/` (as `.webp`) | The three 2752×1536 masters. |
| `live/cg_title.mp4` | `v2/img/live/` | The title loop with her face replaced (an oval on the face only, from the new title still: `live_hold.py --oval 0.6868,0.5715,0.0150,0.0262 --feather 4 --crf 20 --still cg/cg_title_faceA.png (now saved as .webp)`). Re-encoded once; elsewhere the frames match the shipped loop within encoding noise. |
| `master/natsuki-school-base-faceA.png` | `../natsuki-oct20/master/` | The 2K base master with face A. Future Natsuki images start from it. |

### How it was made
All `fal-ai/nano-banana-pro/edit`, 2K, 1:1, on head crops (sprite space: x 91–622, y 0–531 of the 714×1800 sprite; the master crop is x 474–1220, y 0–746), each pasted back through a face oval only, so hair outside the face is the shipped hair.
- **Smile (the base):** seed 254 (below), through `face_composite.py --center 0.495 0.15 --radius 0.112 0.093 --feather 24` on the master; into the sprite through the same oval in sprite space (center 351, 270; radii 155, 187; feather 10).
- **The six other expressions:** image 1 = the shipped expression's head, image 2 = `refs/faceA-head-crop.png`. "Image 1 and image 2 show the same anime girl. Redraw ONLY her face in image 1 in exactly the drawing style of image 2: the same eye shape and size, lash line, iris rendering and highlights, face shape and chin, nose, soft blush style and line work. Keep image 1's facial expression exactly… Keep her hair, the framing… Green eyes. No text." Kept: laugh 262, smirk 263, surprised 264. Retaken: grin (261 added sweat drops; **271** with "Do not add sweat drops, tears or any other marks"), wistful (266 added a sweat drop and a worried brow; **272** spelled out "relaxed eyebrows… a faint, gentle closed-mouth smile; quietly wistful, not sad"), blush (265 lost most of the blush; **273** asked to keep "its strong red blush… and its two small sweat drops").
- **Curious (new):** image 1 = the face-A head. Seed 267's change was too small to see; **274**: "eyebrows clearly raised, eyes open wide, bright and attentive, looking straight ahead, lips slightly parted as if she's about to ask a question, with a hint of a smile. Interested, not surprised or shocked."
- **Arrival CG:** seed 268 on the CG's head crop (x 1100–1700, y 180–780), image 2 the face-A head; `face_composite.py --center 0.507 0.33 --radius 0.05 0.092 --feather 16`. Changed area x 0.45–0.56, y 0.23–0.43.
- **Falter:** seed 275 on the shipped falter's head crop, with the new arrival head as image 2 (so the two match), keeping "her smile half gone, lips slightly parted, eyes a little wider… the irises sitting in the left corners"; pasted onto the **new** arrival CG through the Oct 18 falter oval (`--center 0.503 0.318 --radius 0.042 0.082 --feather 16`). The two differ only at x 0.47–0.54, y 0.24–0.40, so the crossfade moves nothing else.
- **Title:** seed 276 on a 300-px crop (x 1735–2035, y 710–1010). The edit also turned her hair redder, so only the face is kept (`face_composite.py --center 0.6868 0.5715 --radius 0.0155 0.027 --feather 6`).
- Her small ear stud in the arrival CG is gone in the new face (the sprites never had it).

## Exploration files
| File | What it is |
|---|---|
| `sheet_set.jpg` | The face-A set: the shipped expressions above, face A below (with the new curious), and the arrival CG and falter before and after. |
| `sheet_waist.jpg` | The same line (c1_0194) at iPad landscape: as built; option 1, Natsuki's waist lowered 1.7 in; option 2, Nanoha's raised 2 in instead. |
| `sheet_build.jpg` | Face A at the same line: as built, 7% wider, played at 5′1½″. |
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

## Oct 24, afternoon: the author's read
**Author:** "i like a for nat face. i dint love any waist fix that much maybe its best left alone… i agree that lowerinf natsuki waist looks bad. simething about the placement and scake just makenat seem kind of too tall / lean in all of them." **So: face A; no waist fix** (the first blind check also ranked the as-built bodies most natural).

**Tall and lean** (`sheet_build.jpg`, all with face A): as built; 7% wider (a plain horizontal resize of the sprite); played shorter (the engine's `h` at 61.5 and 60). Measured on screen: Natsuki is drawn about 6.6 heads tall and Nanoha about 5.6; Nanoha's head is bigger in inches (10.5 vs 9.6) though she's 4 in shorter, and she's about an inch wider through the shoulders (16 vs 15 in). So Natsuki's eyes sit 6 in above Nanoha's while their crowns are 4 in apart.

**Second blind check** (four shuffled scenes): 7% wider was best ("the least lean"); as built next; played shorter was worse ("a smaller head on a long body, which is more model-like, not less"). Its verdict: **"Mostly the drawing, not the scale"**: narrower than Nanoha though taller; a long lower face, pointed chin and long neck ("reads 19 or 20"); a straight stance with her arms behind her back next to Nanoha's tilt and hunch; a fitted, tapered blazer; smooth glossy shading next to Nanoha's pencil hatching. (It thought Nanoha's sprite changed in the shorter takes; it didn't, but lowering Natsuki's `h` lowers the engine's shared floor, so everyone shrank about 1%.)

**The real fix would be a redraw of her base sprite**, not a tweak: face A, a slightly bigger head, broader shoulders, a boxier blazer, a shorter neck, a relaxed pose, and Nanoha's pencil-hatched rendering; then her six other expressions, the face windows and the three CGs she's in. Asked the author before starting.

**The author's call:** "like maybe original scale with the new face us fine." The redraw isn't happening now; revisit only if she still reads too tall and lean once face A is in and he plays it, or when a later chapter needs new Natsuki art anyway (casual and kendo outfits have to be regenerated regardless).

**Tool fix:** the first `torso_warp.py` ran one cubic through all four points, so the rows it promised to keep moved by up to 26 px in the master (the face-A previews in `sheet_faces.jpg`, `sheet_build.jpg` and `preview_recommended.jpg` sit about 18 px higher in the sprite than they should; the face itself is the same). Fixed: rows above the line are now exact. The face-A set above was built on the unwarped master.

## Pre-check (Oct 24, in a test copy of today's build with the set swapped in)
- `qa_play.py` at iPad landscape, every line, on both builds: 256 of 256 lines, every voiced line decodes, no bad requests (one blocked outside request in both, from the sandbox).
- `snapshot_diff.py --threshold 0.05`: 68 frames changed, each only at Natsuki's face (center slot, right slot, or the CG face), plus c1_0102, where Nanoha is caught at a different point of her slide when Rika hits her (timing; Natsuki isn't on screen). The title screen changes only at her face.
- `sheet_set.jpg`: every expression before and after, and the two arrival CGs.

## Installing (with the Ch1 batch)
1. Copy the folders above into `v2/` and the masters into `art/masters/`; copy the base master next to the Oct 20 one.
2. Style guide §2 (Natsuki's face), `art/prompts.md`, the ledger, the status board.
3. Punch-list batch check: snapshot diff against the handed-over build (only frames with Natsuki's face should change), the automatic checks, one independent check.

## Spend
About $3.60, all NB Pro 2K edits at about $0.15: 10 for the options (the declined one produced nothing) and 14 for the set (6 retakes and the new curious face included). Not yet in `../../pilot-v2/ledger.md` (that's on `main`, which is on hold); add it at install.
