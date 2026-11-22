# On-model image check (§9 step 4): Ch1, build b0-ch1-oct17

Reviewer: independent art check. Coordinates are in pixels on the shipped 2400×1340 still (`v2/img/bg/…`) unless noted. Measurements come from gridded crops (20 px and 50 px grids) and pixel scans of color masks, not from eyeballing.

## Scope

`production/pilot-v2/script/ch01.ozs` puts up two images:

| Directive | Image | Script lines shown over it |
|---|---|---|
| `@cg cg_dream slow` (line 24) | `v2/img/bg/cg_dream.webp` **plus its living loop** `v2/img/live/cg_dream.mp4` (`LIVE` map in `v2/index.html`, which fades the video in over the still) | 25–37 (the prologue dream) |
| `@cg cg_natsuki_intro` (line 215), cleared by `@cg - cut` (line 224) | `v2/img/bg/cg_natsuki_intro.webp` | 216–223 (the self-introduction) |

There are no `@anim`, `@insert` or `@panel` lines in Ch1. `cg_title` only appears on the title screen, not from a Ch1 directive, so it's out of scope.

**Inputs I couldn't check:** `production/pilot-v2/art/prompts.md` doesn't exist in this checkout. `production/pilot-v2/art/` holds only `masters/`, with no layout sketches, and there's no `production/design/`. That means there's no prompt entry to compare either CG against, and no record of the intended camera (for example, whether the intro CG is Kōhei's POV). The masters in `art/masters/` match the shipped stills (mean absolute difference 1.2/255 after resizing), so every finding below also applies to the masters.

---

## 1. `cg_dream`, the still: **FAIL**

**References:** `refs/inventory/ronin-B.png` and `refs/turnarounds/ronin.png` (blue kosode with sleeves rolled to the elbow, dark hakama, two swords at the left hip, **bandage on his left wrist**); `refs/inventory/past-natsuki-A.png` (everyday: blue-gray and cream striped kimono, cream obi); `refs/turnarounds/past-natsuki.png`; and the past-era plate `refs/locations/past-tree-bloom.png`. Style guide §2 (past-life Natsuki: simple everyday kimono, face hidden) and §1b (past era is **winter**: light snow, frost and mist, with blossoms falling on snow).

| Check | Result | How I checked |
|---|---|---|
| On model: past Natsuki | Pass | The striped kimono and cream obi with a cord knot match `past-natsuki-A`. Sampled dark stripe #4c536c vs ref #535c6a. Her face and hair are out of frame, which is consistent with "face hidden." |
| On model: rōnin | Pass on costume, **minor fail on the hand** | Sleeve #434b60 vs ref kosode #465869 (close under the cool dream grade). The bare forearm with the sleeve ending near the elbow matches the rolled sleeves. The hilt's dark wrap with diamond windows matches. Only one hilt shows, and the crop allows the wakizashi to sit out of frame. His hand, though, is drawn with deep creases, knotted tendons and large knuckles (the region x 1350–1850, y 450–780) and reads middle-aged. ronin-B's hands are young and smooth. |
| Which wrist | Pass | In this POV framing his arm enters from the lower left, which is how his left arm would appear. That matches the left-wrist bandage on both rōnin references. |
| Scale | Pass (measured) | His hand breadth is about 295 px (at x≈1600, from the top to the bottom edge of the back of the hand). Her lower hand across four fingers measures about 240 px (y 860–1100 at x≈1500). The ratio is 1.23×, plausible for 5′9″ vs 5′2″. Her upper forearm is about 125 px wide and his forearm about 2× that just below the bandage. Part of that is foreshortening (his arm comes toward the camera), so it isn't flagged. |
| **Hands and anatomy** | **FAIL (blocking)** | Laid across the top of his hand, between the end of her upper forearm and his curled fingers, there are **four extra fingertips with nails**. They point back toward his wrist, at about (1450–1500, 430–470), (1500–1567, 413–458), (1589–1683, 380–452) and (1689–1783, 352–447). They can't be his: his fingers are already curled into a fist at the right, x 1700–1850, y 380–700, and we're looking at the back of his hand. They can't be hers either: her upper hand is at the far left end of her forearm, holding the strip (x 980–1200), and her lower hand is holding the strip below (x 1350–1900, y 760–1100). So this reads as a third hand gripping his, or as a hand with too many fingers. This is the image whose whole subject is "Hands that aren't mine wind a strip of cloth around a wrist that is," so readers will look right at it. |
| Matches the text | Pass | Line 26, "a cut across the back of it": the blood spot sits on the top (back) of the wrapped wrist. Line 27, "a branch… above us": the branch is top-left. Line 28, "Petals": falling petals are visible. Line 33, she winds a strip of cloth slowly: yes. The river (line 25) is sound only. |
| **Location and continuity** | **FAIL** | The past era is winter (style guide §1b, citing canon §5, Oct 10), and the past-era plate `past-tree-bloom.png` shows snow lying along the branches and blossoms falling on snow. The CG shows a spring bloom: bare dark bark with no snow on the branch (x 0–1600, y 0–420), no frost, and no flakes among the petals. There's mist (a pale gray-blue field), but no winter cue at all. The text doesn't mention the weather, so the image is the only thing setting the season, and it sets the wrong one. Light is diffuse with no conflicting shadows. The image isn't flipped. |
| Content rules | Pass | No baked-in text, watermark or border. The edge rows and columns aren't uniform: edge pixel std is 17–63 per channel. The small blood spot is fine. |
| Craft | Pass, apart from the hands above | |

**Smallest fix (one edit pass, then re-render the loop):**
1. Inpaint the mask x≈1440–1800, y≈340–470 (on the 2752 master: about x 1650–2065, y 390–540) so that strip continues the back of his hand and her sleeve, leaving his hand a plain loose fist with no fingertips on top. In the same pass, soften the hatching on his hand to a lean young man's hand (ronin-B as image 1). If one edit can't make the fist read cleanly, reroll the CG with `ronin-B.png` and `past-natsuki-A.png` as references.
2. In the same pass, add a thin line of snow along the upper edges of the branch and a few snowflakes mixed in with the petals, keeping the gray mist. Use `past-tree-bloom.png` as the reference.
3. **Re-render `cg_dream.mp4` from the corrected still.** The engine fades the loop in about 0.9 s after it starts playing, so the old loop would put the old hands back on screen. See section 2.

---

## 2. `cg_dream` living loop (`v2/img/live/cg_dream.mp4`, the animated moment): **FAIL (minor), and it must be redone anyway**

**How I checked:** I extracted all frames with ffmpeg: 96 frames, 24 fps, 4.0 s, 1920×1072. That's the same 1.79:1 aspect as the 2400×1340 still, so `object-fit: cover` lines up. The still against frames 0, 1, 2, 48 and 95 gives a mean absolute difference of 2.1–2.5/255, so the loop is aligned with the still and there's no jump when it fades in. I built a per-pixel max-minus-min map over frames 3–96 to find what moves, measured the seam (last frame against first) against ordinary frame-to-frame change, and made contact sheets of the regions that move.

| Check | Result | Measurement |
|---|---|---|
| On model, scale, anatomy | Same as section 1 | The loop is the still with tiny motion, so it carries the extra fingertips and the missing snow. |
| **Matches the text** | **Minor fail** | Line 27 says "a branch moving in the wind," but the branch doesn't move. Only **0.30%** of pixels change by more than 20 levels anywhere in the loop, and the median frame-to-frame change is 0.07/255. |
| **Craft: blinking petal** | **Minor fail** | Nearly all the motion is one out-of-focus petal at about (300, 290) in still coordinates. It's present in frames 1–12, fades at frame 24, is gone at 36, **reappears in the same spot** at 48, is gone again at 72–84, and is back at 96. So it blinks in place twice per 4-second loop instead of falling. Readers sit on this CG for 13 lines. |
| Loop seam | Pass (note) | Frames 1–2 are about 1.1 levels darker overall than frames 3–96 (mean RGB 159.4/156.3/169.7 vs 160.6/157.6/170.9). The seam difference is 1.61 against a median step of 0.07, spread evenly across the frame, with no object jump. That's a ~0.4% brightness step every 4 s, probably invisible, but it's free to fix while re-rendering. |
| Content | Pass | No text, watermark or frame lines in any frame. |

**Smallest fix:** this is needed anyway once section 1's fixes land. Re-render the loop from the corrected still with a gentle sway of the branch and two or three petals drifting all the way through the frame, with no in-place fades. Then check that the last frame matches frame 1 and that there's no brightness step in the first frames (trim them or re-encode). If the still can't be fixed before handoff, the minimum stopgap is to remove `cg_dream` from the `LIVE` map so the blinking petal doesn't play. That doesn't fix the hands.

---

## 3. `cg_natsuki_intro`: **FAIL on minor items (nothing blocking)**

**References:** `refs/natsuki-v2/01-restyle-uniform.png` (the locked school look); `refs/turnarounds/natsuki.png`; `refs/lineup/lineup-1-school.png` (5′3″; the 6-inch grid lines are 48 px apart, so 8 px = 1 inch); the sprite shown right after the CG, `v2/img/ch/natsuki_school_grin.webp`; the plate `v2/img/bg/bg_classroom_day.webp`. Swatches from style guide §1a.

**Measured landmarks:**

| | Crown | Chin | Head height (H) | Crown→waistband | Waistband→hem (skirt) | Hair end past shoulder line |
|---|---|---|---|---|---|---|
| CG | y 254 | y 518 | 264 px | 644 px = **2.44 H** | 352 px = **1.33 H** | her left (viewer-right): 16 px = 0.06 H; her right: 46 px = 0.17 H |
| Lock (`01-restyle-uniform`) | 122 | 272 | 150 px | 375 px = 2.50 H | 248 px = **1.65 H** | runs long (known) |
| Sprite `natsuki_school_grin` | 9 | 414 | 405 px | 966 px = 2.39 H | 589 px = 1.45 H | about 0.03 H |

The lock's total height is 1093 px = 7.29 H. At 5′3″ that makes one head ≈ 8.6 in.

| Check | Result | How I checked |
|---|---|---|
| Face, eyes, hair color | Pass | Side-swept fringe, amber-brown eyes, same face as the lock. Hair median #b25e38 vs swatch #b55e36. Skin #fcd2be vs #f5dbca (a touch warmer, fine). |
| Hair length, "cut neat at her shoulders" | Pass (note) | The ends sit 0.5 in past the shoulder line on one side and about 1½ in on the other. That's shoulder length, a little longer than the sprite. |
| "Tucked behind one ear" | Pass | Her left ear is exposed with the hair behind it. Her right side is fully covered: I zoomed on the hatched shape at x≈1130, y 435–465, and it's cheek shading, not a second ear. |
| Uniform | Pass | Blazer #3c3c4e (uniform blazer swatch #3f4050) with gold buttons, white shirt, burgundy bow #763745, charcoal plaid #4a4141 (lock #404246). Pressed and neat, matching line 217, "ironed by someone who meant it." |
| **Skirt length** | **Minor fail** | The skirt is 1.33 H against the lock's 1.65 H: about **19% shorter, roughly 2¾ in shorter at her 5′3″ scale**. It's also shorter than the sprite (1.45 H). Crown→waistband (2.44 H vs 2.50 H) rules out a larger head as the cause. The frame cuts off at y 1340, about 0.34 H of bare thigh below the hem. The camera is straight-on and eye-level, so this isn't a content-rule breach, but it moves off the lock in the less modest direction. |
| Scale | Pass where measurable | She has no other named character in frame and no floor contact, so absolute height can't be checked. Body proportions match the lock (see the table). The foreground classmates' larger heads come from their distance to the camera. |
| Expression | Pass (note) | Open-mouthed toothy grin. Style guide §2 asks for a "quietly confident, slightly knowing smile," but the script calls it "her grin" (line 230) and the next sprite is `school_grin`, so the text supports it. |
| **Matches the text: gesture** | **Minor fail** | The CG shows a raised open-palm wave. While it's up, the narration says "She counts on her fingers" (line 220), and no line mentions a wave. |
| Hands and anatomy | Pass | Raised right hand: five digits, thumb toward her midline, correct for a palm-out right hand. The lowered left hand is fine. |
| Location | Pass | Matches `bg_classroom_day`: windows on the left wall with cream tie-back curtains, cherry trees and mountains outside, the small green side panel left of the main board, a cabinet with books left of the board, the speaker and then the clock above the board, a lectern. Light comes from the left windows in both, so it isn't mirrored. Morning light is right for homeroom. |
| **Continuity: clock** | **Minor fail** | The plate shown just before and after the CG (line 206, back at line 225) reads **10:10**; I checked a crop of its clock. In the CG the clock is cut in half by the top edge (the hub is at y≈0), and its one visible hand points at **the 8**, which reads as :40 or 8 o'clock. At 10:10 both hands would be in the hidden upper half. |
| POV (note only) | — | Kōhei sits in the second-to-last row by the window (line 208). The CG has the window on the left as his seat would, but only one row of heads between the camera and the front, which reads as front-row depth. Nothing in the text requires a POV, and there's no prompt record, so I'm not flagging it. |
| **Craft: cloned extras** | **Minor fail** | Three of the four foreground classmates (x 0–260, x 330–900, x 1700–2190) are the same girl from behind: jet-black hair, perfectly straight, center part, the same length past the frame bottom, the same blazer. Hair-mask widths sampled every 50 px down each figure follow the same profile, scaled about 0.8× for distance. It reads as copy-paste. The fourth figure is a short-haired boy. |
| Baked-in text, watermark, frame lines | Pass | The clock numerals are props and correctly ordered (9–4). No watermark. Edge std is 44–117, so there's no border. |

**Smallest fixes:**
- **Gesture:** a text change. Add a beat that matches the wave, for example change line 216 to "…like she's walking onto a court she's already won on, and lifts a hand to the room." Leave line 220 as it is.
- **Clock:** an edit pass. Paint out the single visible hand. With both hands in the hidden upper half, the clock is then consistent with the plate's 10:10.
- **Cloned extras:** an edit pass on two of the three girls (for example, a shoulder-length dark-brown bob and a low ponytail), leaving the boy as he is.
- **Skirt:** an edit pass lengthening the hem about 0.3 H (≈80 px at 2400 wide) to match the lock. Alternatively, ask the author whether the sprite's length (1.45 H) is the accepted target, and if so lengthen about 0.12 H (≈30 px).

All four fixes fit in a single edit pass, with no reroll needed.

---

## Summary of failures

| # | Image | Problem | Severity | Smallest fix |
|---|---|---|---|---|
| 1 | `cg_dream` | Four extra fingertips with nails across the top of the rōnin's hand (x 1450–1783, y 352–470), so it reads as a third hand or too many fingers | **Blocking** | Inpaint that strip to a plain fist; reroll with ronin-B and past-natsuki-A if needed |
| 2 | `cg_dream` | No winter cues (snow, frost) although the past era is winter and the bloom plate shows snow on the branches | Fail | Same edit pass: snow along the branch and a few flakes among the petals |
| 3 | `cg_dream` | The rōnin's hand is heavily lined and reads older than ronin-B | Minor | Same edit pass |
| 4 | `cg_dream.mp4` | Almost no motion (0.30% of pixels): the branch is static despite "a branch moving in the wind," and the only motion is a petal blinking in place at (300, 290) | Minor | Re-render the loop from the fixed still (required after fixes 1–2 anyway), with branch sway and petals that fall through the frame |
| 5 | `cg_natsuki_intro` | Waving hand while the narration says "She counts on her fingers"; no wave in the text | Minor | Text: add a wave beat to line 216 |
| 6 | `cg_natsuki_intro` | Clock hand points at the 8, while the flanking plate reads 10:10; clock cut in half by the frame | Minor | Edit: paint out the visible hand |
| 7 | `cg_natsuki_intro` | Three foreground classmates are identical long-black-haired girls | Minor | Edit: restyle two of them |
| 8 | `cg_natsuki_intro` | Skirt 1.33 H against the lock's 1.65 H (about 2¾ in shorter at 5′3″) | Minor | Edit: lengthen the hem about 80 px, or confirm the target with the author |

**Not checkable:** there's no `production/pilot-v2/art/prompts.md` and no layout sketches in this checkout, so neither CG could be checked against its prompt entry or its intended camera.
