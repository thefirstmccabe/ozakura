# On-model image check: Pilot v2 Ch1 (Oct 18 build)

**Scope.** `ch01.ozs` has no `@anim`, `@insert` or `@panel` lines. It shows seven CGs: `cg_cold_mirror`, `cg_cold_hand`, `cg_cold_mist`, `cg_collar`, `cg_natsuki_intro`, `cg_natsuki_intro_falter` and `cg_dream`. Two of them play as animated moments: the `LIVE` map in `v2/index.html` swaps in `v2/img/live/cg_cold_mist.mp4` and `cg_dream.mp4` after the crossfade. `cg_title` isn't a Ch1 image, so I didn't check it.

**Method.** I checked the game files (`v2/img/bg/*.webp`, 2400×1340) against the masters (`art/masters/`, 2752×1536). For all seven, the game file matches its master (mean abs difference 0.9–2.3 levels after downscaling, which is compression only). Coordinates below are game-file pixels.
- **Heads:** measured on drawn 10 px grids.
- **Swatches:** medians of sampled patches, compared as CIE ΔE76 against the hex values in style guide §1a.
- **Live clips:** I extracted all 96 frames of each clip and compared them with the still, scaled to 1920×1072.

References used:
- **Kōhei:** `r3/kohei-short-A`, the face windows and `full-kohei`.
- **Nanoha:** `handoff/Nanoha-School-Braid` and the sprites.
- **Natsuki:** `natsuki-v2/01-restyle-uniform` and the sprites.
- **Past life:** `past-natsuki-A`, `ronin-B`, `past-tree-bloom` and `past-mist-path`.
- **Scale and plates:** `lineup/lineup-1-school.png`, `art/layout/cg_collar_layout.jpg`, `bg_river_morning` and `bg_classroom_day`.

**Severity.** FAIL means fix before the author sees it. MINOR means fix if it's cheap, or accept knowingly. Notes aren't counted as problems.

---

## 1. cg_cold_mirror (P.0, wordless): PASS
- **Content:** misty residential road, hedge on the left, block wall on the right, orange convex mirror on its own pole at the corner. No people or animals, no blossoms or petals, no large tree or boulder.
- **Text and frames:** the white plate on the mirror pole is blank, there's no other signage, and there's no edge frame line (edge rows are within ±4 levels of the rows inside them).
- **Palette:** mist sky band L\* 87 (median RGB 211/220/223), cool and low-contrast as briefed.
- Nothing to fix.

## 2. cg_cold_hand (P.0, wordless): PASS, with a note
- **Sword:** the grip has diamond-pattern wrapping, a round dark guard and a sheathed blade (no steel visible). No blood and no face.
- **Hand:** five digits. The finger order is slightly muddled at full size but reads as a clenched grip at screen size.
- **Palette:** the mist behind the hand is darker than in the other two shots (L\* median 80.6, against 87 in the mirror shot). That's acceptable for a close-up; no fix.
- **Note (not counted):** the prompt asked for his **right** hand, but the image draws his **left**. The jacket zipper puts his torso on the left of the frame, so an arm hanging to its right, seen from the front, is his left arm. It's a left hand on the grip, just behind the guard, of a sword at his left hip. No narration depends on this. If the P.0 outline wants a right hand ready to draw, that takes a reroll; a mirror flip would put the sword on his right hip.

## 3. cg_cold_mist and its live clip (P.0, wordless): MINOR, 1 problem
- **Content:** nothing in the mist. I checked the master at full size over the center 1200×600 and frames 1, 30, 60 and 90 of the clip: no shape, silhouette or eyes.
- **Grade:** the Oct 18 grade holds. The sky band is L\* 88.8 here against 87.1 in the mirror shot.
- **Live clip:** 1920×1072, 24 fps, 96 frames, 4.0 s. It's locked to the still: the best alignment offset is 0,0 px at every 8th frame over a static wall patch. The loop seam is clean (first frame against last: mean 1.6 levels, 99th percentile 6). The poles and wall don't move.
- **Note (not counted):** the clip runs about 3 levels darker than the still (mean RGB 159.7/169.7/171.8 against 162.8/172.3/173.8). It's invisible under the 0.9 s fade.
- **Problem 3a, MINOR (continuity, flipped layout):** the block wall and its pole are in the **left** foreground here, but in `cg_cold_mirror` the wall is on the **right** and the hedge on the left. The two images alternate (mirror, hand, mist, mirror), so the wall swaps sides twice in about ten seconds. The prompt asked for "the same road, just past the bend", and the scenery also changes from houses to open grass past the wall. It reads as the same place, so the flip shows.
  - **Smallest fix:** flip `cg_cold_mist` (master, game file and loop) horizontally. There's no text in the frame and the curls are roughly symmetric, so it's no spend. Or accept it as a different wall.

## 4. cg_collar (c1_0071–c1_0078): FAIL, 3 problems
**What passes:**
- **Braid, clip and petal:** the braid and clip are on her left, which faces the camera, and match `nanoha_school_smile` and `Nanoha-School-Braid`. The c1_0071 petal is on the braid, clearly visible (around x 1520, y 580).
- **Uniforms:** burgundy ribbon on her, striped burgundy tie on him, charcoal plaid skirt, open blazer with gold buttons on him.
- **Location:** river, fence, petal-strewn path, cherry row, utility pole and the mountains all match `bg_river_morning`. It's morning light.
- **Craft:** modest framing; no text, watermark or frame line. Kōhei has two hands at his sides, and her two forearms read separately.

**Swatches:**

| Element | CG | Swatch | ΔE |
|---|---|---|---|
| Kōhei's hair | #453939 | #3d3232 | 3.3 (not black) |
| Nanoha's hair | #5a4748 | #51423d | 4.9 (slightly cool and pink from the blossom light) |
| Kōhei's blazer | #383545 | #3f4050 | 4.8 |
| Nanoha's blazer | #403d4d | #3f4050 | 1.9 |
| Nanoha's skin | #fdd6c9 | #eddace | 7.8 (her sprite is 6.1, so consistent with it) |

**Problem 4a, FAIL (scale: head sizes).** Measured on a 10 px grid:

| | Crown | Eye center | Chin | Crown to chin |
|---|---|---|---|---|
| Kōhei | y 107 (cowlick tips 85) | y 296 | y 407 | 300 px (322 with the cowlick) |
| Nanoha | y 298 | y 434 | y 540 | 242 px |

- **Ratio:** her head is **0.81×** his crown to chin (0.75× counting his cowlick). Eye to chin is 0.95×, so the shortfall is all cranium: crown to eye is 136 against 189 px, **0.72×**.
- **Reference:** in the scale lineup (`lineup-1-school.png`, 8.0 px per inch), Kōhei's head is 70 px (8¾″) and Nanoha's 71 px (about 8⅞″). That's a ratio of **about 1.0**. Flat-footed, her crown sits about 1″ below his chin.
- **Cause:** the model enlarged Kōhei, not shrank her. At the layout's scale (32 px per inch at 2752 wide, so 27.9 px per inch here), his crown lands where the layout puts it (y 84 predicted, 85–107 drawn). But his head measures 300 px (10¾″) against 250 px in the layout (about 9″) and 8¾″ in the lineup, so it's **about 1.2× too big**. Her head is 242 px (8¾″), which matches the lineup.
- **Side effect:** her crown sits level with his eye line (298 against 296), 109 px (0.36 of his head) above his chin. For 4′11″ on full tiptoe (about 3″) against 5′9″, the top of her head should reach roughly his mouth or nose, not his eyes. The record in `prompts.md` ("0.77×, right for tiptoe") misses both points.
- **Smallest fix:** one `nano-banana-pro/edit` pass on Kōhei only, about 1 to 2 takes.
  - Make his head and hair about 10–15% smaller, keeping the top of his hair where it is and his neck and shoulders unchanged.
  - Then paste back only a feathered region around his head, so Nanoha and the petal stay untouched.
  - Targets: his crown to chin about 255–270 px; ratio at least 0.9; her crown 0.25–0.3 of his head above his chin.
  - Re-measure on the grid afterward.

**Problem 4b, MINOR (matches the text).** c1_0074 says she's "folding my shirt collar back down over my tie". At 4× zoom both of her hands grip the **tie knot**. The visible collar point, a button-down point on his right, lies flat and nobody touches it. A reader sees her straightening his tie.
- **Smallest fix:** a text change, e.g. "…up on her toes, straightening my tie and folding my collar back down over it."
- **Alternative:** a hands-only edit pass with a feathered paste-back.

**Problem 4c, MINOR (matches the text and continuity).** c1_0054 says "Nanoha walks on the river side." In the CG, **Kōhei** stands at the fence on the river side and Nanoha is on the inland side, under the trees. They face each other across the path, so she would have to have been on the tree side.
- The image can't be mirrored to fix this, because the braid and clip have to stay on the side that faces the camera.
- **Smallest fix:** a text change in c1_0054 (e.g. "on the side away from the river", or cut the line). Or accept it, if c1_0054 is a deliberate detail that Story wants kept.

**Notes (not counted):**
- **Hair clip:** a long wedge-shaped filigree clip in the CG against the small silver clip on her sprite. This is already open with the author in `prompts.md`; I didn't re-decide it.
- **Pole:** it has lost the yellow-and-black stripe sleeve that it has in the `bg_river_morning` plate.
- **Branch tangent:** a dark branch starts right at Kōhei's nose and upper lip and runs to her hairline (around x 1120–1400, y 330–380), so it visually links the two faces.

## 5. cg_natsuki_intro (c1_0138–c1_0152): MINOR, 1 problem
**What passes:**
- **Hair:** copper, glossy and neat, ending at the shoulders (hair ends around y 560, shoulder line around y 590), with the side-swept fringe and her left ear tucked and showing. That matches c1_0139 and §2.
- **Eyes and uniform:** amber-brown eyes; the uniform is neat and matches her sprite.
- **Swatches:**
  - Hair at the crown: #c4663a against #b55e36 (ΔE 5.3), where her sprite is 9.0.
  - Skin: #fbd7c3 against #f5dbca (ΔE 4.4).
- **Hands:** five fingers on the waving hand.
- **Classmates:** four distinct students seen from behind (buzz cut, ponytail, long black hair with a headband, bob). None of them can be read as Kōhei.
- **Location:** matches `bg_classroom_day`: windows and cherry tree on the left, sun shafts from the left on the board, the speaker and clock above the board, and the bookshelf and lectern in place.
- **Framing:** the camera is at seated height and the skirt length matches her sprite. Modest.
- **Expression:** the big open smile is consistent with c1_0147 ("Her grin stutters") and with c1_0230, which contrasts it with a smaller smile later.

**Problem 5a, MINOR (baked-in text and craft).** On the wall clock (top right, around x 1840–2040, y 0–120), the **8 is drawn as "B"**. The other numerals (9, 7, 6, 5, 4) are fine. At iPad size the numerals are about 25 px tall, so this is legible. `cg_natsuki_intro_falter` carries the same base.
- **Smallest fix:** a hand-paint or small inpaint of that one numeral on the base. Then rebuild the falter with the existing `face_composite.py` command, since the falter face patch (x 0.46–0.54) doesn't touch the clock. No spend if hand-painted.

**Note (not counted):** in landscape, CGs fill the screen with `object-fit: cover`. On a 4:3 iPad (12.9″ Pro), that crops about 12.8% from each side, so most of the cherry-blossom window at the left disappears. The falter's leftward gaze still reads as "left", and the curtain survives. Worth a glance on the device.

## 6. cg_natsuki_intro_falter (c1_0147): PASS
- **Composite:** I diffed it against the base.
  - Game files: every change over 32 levels falls inside x 0.462–0.542, y 0.240–0.398 of the frame.
  - Masters: outside the face box, at most 13 levels, on 175 pixels (encoder noise).
  - So nothing outside the face moves in the crossfade.
- **Expression:** the smile is half gone, lips parted, and the irises sit in the left corners of both eyes, toward the window and Kōhei's back-row window seat. That matches c1_0146–0147.
- **Shared defect:** the clock problem 5a applies here too (it's the same base); counted once.

## 7. cg_dream and its live clip (p_0003–p_0011): MINOR, 1 problem
**What passes:**
- **POV and costume:** the view is from his side. Her face and hair stay out of frame. Her blue-gray striped kimono and cream obi match `past-natsuki-A` (everyday).
- **His hand:** palm up, five digits. The thumb is on the far side, so it's his **left** hand. That matches the c1_0264 callus line and the bandaged left forearm in `ronin-B`.
- **Wound:** the red stain is on the cloth on the **inside** of the wrist, just below the heel of his hand (p_0004).
- **Her hands:** two hands winding the strip, five digits each (p_0011).
- **Setting:** a blossoming branch overhead and petals (p_0005–0006), and a sword grip at the left. No text, no frame line.
- **Live clip:** 96 frames, 4.0 s. Locked to the still (best offset 0,0 px at every 8th frame over the sword-grip patch). Loop seam: first frame against last, mean 1.8 levels, 99th percentile 9. At 3× zoom on frames 1, 30, 50, 70 and 90, the hand stays palm up with five digits and nothing morphs, and the stain stays put.
- **Note (not counted):** his sleeve (#464a5f) is darker and more slate than `ronin-B`'s blue kimono (#485b6b). It fits the dim dream light.

**Problem 7a, MINOR (location and continuity; confirm with Story first).** Style guide §1b sets the past era in **winter** (canon §5): "light snow, frost and mist, so the bloom plate shows blossoms falling on snow". `past-tree-bloom.png` shows snow on the branches and the ground. The dream is the reader's first look at the past era, and its blooming branch shows no winter cue at all: no snow on the branch, no flakes among the petals. Only blossoms in winter would be the out-of-season Great Cherry. So either:
- this moment is the winter tree, and the image contradicts the later past-era plates, or
- it's somewhere else, and that's fine.

**Smallest fix:** ask Story which it is. If it's the winter tree, do one edit pass (a light dusting of snow on top of the branch, a few flakes among the petals) and then regenerate the loop. The loop is a Kling run, so that's new spend; ask first. If not, close this item.

---

## Summary of failures

| # | Image | Severity | Problem | Smallest fix |
|---|---|---|---|---|
| 4a | cg_collar | **FAIL** | Head ratio 0.81× (0.72× crown to eye) against about 1.0× in the scale lineup. Kōhei's head is about 1.2× too big (300 px, 10¾″, against about 9″ in the layout and 8¾″ in the lineup). Her crown sits at his eye line instead of about his mouth on tiptoe. | Edit pass on his head only (10–15% smaller, crown fixed, feathered paste-back), then re-measure on the grid. |
| 4b | cg_collar | MINOR | Her hands grip his tie knot; c1_0074 says she's folding his collar down. | Text tweak to c1_0074 (or a hands-only edit). |
| 4c | cg_collar | MINOR | Kōhei is on the river side; c1_0054 says Nanoha walks on the river side. | Text tweak to c1_0054, or accept. |
| 3a | cg_cold_mist (and loop) | MINOR | The block wall is on the left here but on the right in cg_cold_mirror, and the shots alternate. | Mirror the still, master and loop horizontally (no spend), or accept. |
| 5a | cg_natsuki_intro / _falter | MINOR | The clock's 8 is drawn as "B". | Paint fix on the base, then rebuild the falter composite. |
| 7a | cg_dream (and loop) | MINOR | No winter cue, against the §1b past era (blossoms on snow). | Confirm with Story; if it's the winter tree, edit pass plus a new loop (spend: ask). |

**Passed clean:** cg_cold_mirror, cg_cold_hand (with the handedness note), cg_natsuki_intro_falter (composite and gaze), and both live clips (alignment, seam, no morphing, nothing appearing in the mist).

**Problems reported: 6** (1 fail, 5 minor).
