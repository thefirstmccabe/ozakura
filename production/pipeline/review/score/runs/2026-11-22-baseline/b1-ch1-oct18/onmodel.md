# On-model image check (§9 step 4): Pilot v2 Ch1, Oct 18 build

**Scope.** These are the images Ch1 shows according to `production/pilot-v2/script/ch01.ozs`: `@cg` lines for cg_cold_mirror (shown twice), cg_cold_hand, cg_cold_mist, cg_collar, cg_natsuki_intro, cg_natsuki_intro_falter and cg_dream. The script has no `@anim`, `@insert` or `@panel` lines. I treated the two "living stills" in `v2/img/live/` (cg_cold_mist.mp4 and cg_dream.mp4) as Ch1's animated moments, on the assumption that the player swaps each one in for the CG of the same name. I didn't check that in the player code, because the player is outside this check's read list. cg_title isn't called by Ch1, so it's out of scope.

**Method.** I checked the game files (`v2/img/bg/*.webp`, 2400×1340) at full size and at reader size (iPad landscape, about 1194 px wide). I measured on pixel grids drawn over the game files; all y values below are game-file pixels. I sampled colors as medians over small regions and compared them with the §1a swatches. For the loops I pulled frames at 0.0, 0.5, 1.3, 2.0, 2.7, 3.5 and 3.95 s and diffed the first frame against the last. I diffed the falter against the base to bound the composite. References used: style guide §1–§2; `prompts.md`; the Nanoha, Natsuki and Kōhei sprites; `handoff/Nanoha-School-Braid.png`; `inventory/full-nanoha.png`, `full-kohei.png`, `past-natsuki-A/B.png` and `ronin-B.png`; `design-oct10/r3/kohei-short-A.png`; `natsuki-v2/01-restyle-uniform.png`; `locations/past-tree-bloom.png` and `past-mist-path.png`; the plates `bg_river_morning` and `bg_classroom_day`; and the layout `art/layout/cg_collar_layout.jpg`. Canon itself isn't on this check's read list, so canon points rest on the style guide's own summaries of canon.

---

## 1. cg_cold_mirror (P.0, wordless cold open). **PASS**
- **On model, scale:** no characters in frame.
- **Text:** none (wordless).
- **Location:** a misty residential road with a hedge on the left, a block wall on the **right**, an orange convex mirror at the left corner and utility poles. There's no blossom, tree, boulder or figure.
- **Content:** the plate on the mirror pole and the plates on the right-hand pole are blank, with no text. There's no border: edge strips match the strips just inside them within 3 levels.
- **Palette:** sky L\* 87.6 and mid-distance mist L\* 79. This is the reference for the other two cold-open images.

## 2. cg_cold_hand (P.0). **FAIL (minor)**
- **Anatomy:** five digits, a plausible fist on the tsuka, and no blade visible. The diamond wrap is on the grip, not the blade side.
- **Palette:** the background mist is L\* 81.1 against L\* 79.4 for the mirror image's mid-distance mist, so the two read as the same morning.
- **Problem: it reads as the wrong hand for the intended beat.** The prompt asks for "a young man's **right** hand… about to draw". The jacket's zipper runs down the left third of the frame (x ≈ 330–430), with a slash pocket on the panel to the zipper's right. That puts us in front of him, and the arm hanging to the right of his torso is his **left** arm. A left hand closing on the tsuka of a sword sheathed at the left hip isn't a draw grip (the left hand holds the saya and the right hand draws). It reads as carrying the sword. No narration depends on which hand it is, but a kendo-literate reader could catch it.
- **Fix:** if "carrying" is acceptable, log it and keep the image. If the "about to draw" beat matters, reroll from the same refs with "his right hand reaching across his body to the hilt of the sword sheathed at his left hip". That's new spend of about 2 takes. Mirroring the image isn't a fix: it would put the sword on his right hip.

## 3. cg_cold_mist + living still `live/cg_cold_mist.mp4` (P.0). **FAIL (minor)**
- **Content:** no shape, silhouette or eyes in the mist in the still or in any of the seven frames I pulled. The camera stays locked.
- **Grade:** the earlier grade is applied. The sky is L\* 88.9 against 87.6 in the mirror image (RGB 219/224/229 against 213/221/225), and it stays cool (B > G > R). The loop runs 3–4 levels darker than the still (mean RGB 159/169/170 against 163/172/174), which isn't visible.
- **Loop:** the first and last frames differ by a mean of 1.6 levels, so the seam is clean.
- **Problem: the layout is flipped against cg_cold_mirror.** The prompt calls this "the next view along the same road, just past the bend". In the mirror image the block wall and its utility pole are on the **right** of the road. Here the wall's corner and its pole are at the near **left** (wall at x 0–615). Whichever way you turn at the junction or go straight through it, the wall can't end up on your left. The montage cuts mirror → hand → mist → mirror, so the wall jumps sides and then jumps back.
- **Fix (no spend):** flip cg_cold_mist horizontally in the master, the game file and the loop (`ffmpeg -vf hflip`, same encode). The image has no text and no asymmetric prop, so nothing else changes.

## 4. cg_collar (c1_river, c1_0073–c1_0078). **FAIL (minor, 2 problems)**
- **On model:**
  - Kōhei has short, unruly dark-brown hair (sampled 71/60/59 against swatch #3d3232) and a fringe above the brows. His navy blazer is open and his burgundy striped tie matches the sprite and the r3 reference.
  - Nanoha's braid and clip are on her **left** side, which faces the camera, matching the sprite and the handoff reference. She has brown eyes, a burgundy bow and a charcoal plaid skirt. Her skin samples at 253/214/203, so it isn't gray (the §1b known issue).
  - Her hair samples at 102/74/76 against swatch #51423d: lighter and pinker under the blossom light, but acceptable.
- **Scale (grid):**
  - Kōhei: crown y 95, eye line about y 295, chin y 400, belt y about 988.
  - Nanoha: crown y 297, eye line about y 445, chin y 541.
  - Head ratio (her head to his): **0.80** crown to chin and **0.91** eye to chin. The log's 0.77/0.88 is within measuring error, and her head now reads nearly as big as his.
  - Height: her crown is at his eye line, 202 px below his crown. At 31–33 px per inch (his crown-to-belt of 893 px against about 27–29 in for 5′9″) that's 6.1–6.5 in. At the layout's 27.9 px per inch it's 7.2 in. Either way she's 2.8–3.9 in above standing height, which is right for full tiptoe at 4′11″ against 5′9″. Standing flat she'd reach his chin (§2). **Pass.**
- **Text:**
  - Hands at his collar and tie knot, with two separate forearms: matches c1_0074.
  - One petal on her braid: matches c1_0071. The pasted petal has no seam at full size.
  - Morning light and the cherry tunnel: matches c1_0053.
  - "Up on her toes" can't be seen (feet out of frame) but is supported by the measured heights.
- **Location:** a crop of bg_river_morning: river and wooden fence on the left, path, the cherry row and the utility pole on the right, the same mountains and houses. Consistent.
- **Content and craft:** modest framing; Nanoha's skirt is about mid-thigh, as in her sprite. Both hands at his sides have five digits. No text and no border.
- **Problem A: the river side contradicts the text.** c1_0054 states pointedly that "Nanoha walks on the river side." Twenty lines later the CG shows **Kōhei** against the river fence and Nanoha on the tree side. Facing him doesn't move her across him. Mirroring the CG would make it match, but it would swing her braid and clip to the hidden side.
  - **Fix:** a text change in a handoff to Story: c1_0054 becomes something like "Nanoha walks on the inside, under the trees." Or cut the line.
- **Problem B: the hair clip doesn't match her sprite.** The CG draws a long pointed wedge about 46 px long, roughly 0.19 of her head height. The sprite shown just before and just after the CG has a small rounded clip, about 0.07 of her head height. §2 lists no clip for Nanoha at all, and the handoff primary reference has none. The prompts log already lists this as open for the author.
  - **Fix:** a local edit pass on the clip only, composited back with a feathered circle the way the petal was. Repaint it to the sprite's small clip, or remove it if the author rules no clip. Logging it is enough until the author decides.

## 5. cg_natsuki_intro (c1_intro, c1_0138–c1_0152). **FAIL (minor, 2 problems)**
- **On model:**
  - Copper hair (sampled 200/106/65 against swatch #b55e36 and the sprite's 194/101/54) ends at her shoulders and is tucked behind her **left** ear, the same side as the sprite. Amber-brown eyes, a neat uniform and a burgundy bow.
  - Measured on the grid: crown y 245, chin y 510, so her head is 265 px. Her skirt is 335 px, which is 1.27 heads, against 1.38 on the sprite and 1.06 on the approved 01-restyle reference. Crown to waistband is 2.47 heads, against 2.5 on the sprite. On model, and the framing is modest.
  - Her raised right hand has five digits, with the thumb on the correct side.
- **Text:** copper hair, shoulder length and tucked behind one ear, matching c1_0139. She looks along the rows toward the camera (c1_0146).
- **Location:** the bg_classroom_day room, with the windows and the cherry tree on the left, curtains, the bookshelf left of the board, the lectern, and the speaker and clock above the board. Light comes from the window side, as on the plate. The four foreground classmates are clearly different (buzz cut, ponytail, long black hair with a headband, bob), and their faces aren't shown.
- **Note, not counted:** the expression is an open-mouthed beaming smile with a wave. That's bigger than §2's "quietly confident, slightly knowing smile… not a tomboy grin", but the script itself calls it a grin (c1_0147), so I haven't counted it.
- **Problem A: malformed text in the image.** On the wall clock (top right, about x 1840–2050, y 0–100) the 8 is drawn as a **"B"**. The clock is also cut in half by the top edge, which the plate doesn't do.
  - **Fix:** one local edit pass on the clock only (correct the 8, or paint the numerals out to plain tick marks), composited back with a feathered mask. Apply the same pixels to cg_natsuki_intro_falter, since the two share everything outside the face. About 1–2 takes.
- **Problem B: the CG stays up over lines it contradicts.** `@cg -` sits after c1_0152, so the waving-at-the-front image is still on screen for "She bows" (c1_0149) and "I raise my left hand. She walks down the aisle." (c1_0152).
  - **Fix:** a one-line script move. Put `@cg -` directly after c1_0223 ("Looking forward to this year."), so the bow and the walk play over the classroom plate. At minimum, put it before c1_0152.

## 6. cg_natsuki_intro_falter (c1_0147). **PASS** (it also inherits the clock "B" from §5)
- **Composite:** the change is confined to x 0.462–0.542 and y 0.240–0.398 of the frame at a threshold of 30 levels. Outside the face box the maximum difference is 21 levels and the 99.9th percentile is 9, which is encode noise. Nothing moves in the crossfade.
- **Gaze:** at full size the irises sit in the left corners of both eyes, with the whites on the right. At iPad reader size it still reads as looking toward frame left, the window side where Kōhei sits. The smile is gone and the lips are parted: visible, but brief and not shocked. This fits c1_0147.
- **On model:** the hair and ear are unchanged from the base.

## 7. cg_dream + living still `live/cg_dream.mp4` (c1_dream). **FAIL (1 conditional problem, 1 minor problem)**
- **On model:**
  - His hand is palm up with five digits and the thumb on the far upper side. That makes it his **left** hand, which matches the callus line c1_0264 and the bandaged left forearm in ronin-B.
  - Her two hands each have five digits and are smooth and young. Her face and hair stay out of frame (§2: her face is hidden).
  - Her kimono is the blue-gray stripe of past-natsuki-A (everyday) with a pale obi and cord, and it closes **left over right**, which is correct for the living. His dark sleeve and the dark diamond-wrap tsuka fit ronin-B.
- **Text:**
  - The cut is on the inside of the wrist, with the stain showing through the cloth on the palm side (p_0004).
  - Cloth is being wound around his wrist (p_0011).
  - There's a branch overhead and petals (p_0005 and p_0006). The river is sound only.
- **Loop:** at 0.5, 1.3, 2.0, 2.7 and 3.5 s the hand stays palm up with five digits and the stain doesn't move. The first and last frames differ by a mean of 1.8 levels. The still-to-loop offset is 1–2 levels.
- **Problem A (conditional): no winter cues.** §1b says the past era is **winter** (canon §5, Oct 10): "light snow, frost and mist, so the bloom plate shows blossoms falling on snow". `past-tree-bloom.png` has snow along the top of every branch. The dream's branch is bare of snow, there's no frost, and the light is soft and spring-like, so the dream reads as an ordinary spring. I didn't open canon (it isn't on this check's read list).
  - **Fix:** Story confirms the dream's season. If it's winter: one edit pass adding a thin line of snow along the top of the branch and a few flakes among the falling petals, then re-render the loop (Kling, 4 s, same prompt). That's new spend. If the dream is meant to be spring, log it as an exception.
- **Problem B (minor, conditional): the CG is never cleared before the waking lines.** c1_dream has no `@cg -`, so "And then I wake up, and the only thing left is a feeling…" (p_0012–p_0014) plays over the dream image after the white flash. The cold open needed an explicit `@cg - cut` before its `@bg black`, which suggests `@bg` doesn't clear a CG. I didn't check the player itself.
  - **Fix:** add `@cg - slow` directly after `@flash white`.

---

## Summary of failures (8)

| # | Image | Problem | How I checked | Smallest fix |
|---|---|---|---|---|
| 1 | cg_cold_mist (+ loop) | Wall and pole flipped to the left against cg_cold_mirror (right), "next view along the same road" | Side-by-side layout comparison | Horizontal flip of the master, game file and loop (no spend) |
| 2 | cg_cold_hand | Reads as his **left** hand on the tsuka (zipper and left-panel pocket put the arm on his left), not the prompt's right hand "about to draw"; not a draw grip | Torso and zipper geometry, hand crop | Log as "carrying", or reroll with the right hand crossing to the hilt (about 2 takes) |
| 3 | cg_collar | Kōhei on the river side; c1_0054 says Nanoha walks on the river side | Plate and layout comparison against the script text | Text change to c1_0054 (handoff to Story) |
| 4 | cg_collar | Long wedge clip (about 0.19 of her head) against the sprite's small clip (about 0.07); §2 lists no clip | Grid measurement against the sprite and handoff reference | Local clip edit composited back, or remove per the author (already open for him) |
| 5 | cg_natsuki_intro and falter | Clock numeral 8 drawn as "B"; clock cut by the top edge | Full-size crop | Local clock edit applied identically to both files |
| 6 | cg_natsuki_intro | CG stays up through "She bows" and "She walks down the aisle" | Script directives around the image | Move `@cg -` to just after c1_0223 |
| 7 | cg_dream (+ loop) | No snow or frost, though §1b puts the past era in winter (canon §5) | Comparison with past-tree-bloom and past-mist-path | Story confirms; if winter, a snow edit and a loop re-render (new spend) |
| 8 | cg_dream | No `@cg -`, so the waking lines play over the dream image | Script directives (cold-open precedent) | Add `@cg - slow` after `@flash white` |

**Passes:** cg_cold_mirror and cg_natsuki_intro_falter (apart from the shared clock). Scale in cg_collar passes on the grid.
