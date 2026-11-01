# Ch3 on-model check, round 1 (Nov 1)

Independent reviewer, following `production/pipeline/review/on-model-image.md`. I checked the build files in `v2/img/` against style guide §1a–§2, the Ch3 section of `art/prompts.md`, the references, and the script `production/pilot-v2/script/ch03.ozs`. All measurements were made in Python/PIL on pixel grids. Sprite scale was rebuilt from the engine's own numbers (`CHAR`, `VSET`, `HEADROOM`, `FLOOR`, `SCALE` in `v2/index.html`) on a 1-inch grid. I read heights to about ±0.3 in. The video checks used every frame (96 per loop) plus the requested frames at 0.5, 1.3, 2.0, 2.7 and 3.5 s. In-game iPad shots (`c3_ipad`, 227 of them when I checked) were used where they existed.

## Verdicts

| Image or set | Verdict | Main point |
|---|---|---|
| `cg_window` | PASS | The image is right. The script keeps it on screen 12 lines past c3_0106 (problem 3). |
| `cg_window_sill` | PASS | |
| `cg_window_sill_turn` | PASS with note | The rabbit faces Nanoha, not "the curtain" (problem 6). The engine shows a face window over it (problem 4). |
| `cg_tree_natsuki` | PASS with note | The edit redrew the whole plate. The layout is identical. |
| `cg_tree_light` | PASS | The light is visible and deniable, and it can't read as the sun. |
| `cg_lunch` | **FAIL** | Grandpa is at the near corner, not "the far end". There's no empty place for Kazuo and no extra bowls. Kōhei's sleeves are sage green. |
| `live/cg_window_sill.mp4` | PASS with note | Nothing morphs. The loop is almost static, with a faint sharpness pulse at the loop point. |
| `live/cg_window_sill_turn.mp4` | PASS with note | The clip is clean, but the engine never plays it (not in `LIVE`). |
| `live/cg_tree_natsuki.mp4` | **FAIL (minor)** | About 30 petals blink at the loop point, and the frame softens 4%. |
| `live/cg_lunch.mp4` | PASS with note | The faces are held and nothing morphs. Same faint pulse at the loop point. |
| `bg_shrine_steps` | PASS | |
| `bg_tachibana_living` | PASS with note | Pseudo-lettering on a magazine and book spines. It sits under the text box during play. |
| `natsuki_track_*` (8) | PASS with note | Face A, green eyes, copper ponytail, all on model. The top is close-fitting (author's eye). |
| `akane_home_*` (4) | **FAIL (text)** | `sleepy` has half-open eyes, but c3_0071 says "Her eyes are still closed." |
| `mio_home_*` (4) | PASS | |
| `genji_shrine_*` (3) | PASS with note | Matches the reference. His realistic face reads large beside the girls. |
| `nanoha_home_*` (7) | PASS | |
| `emi_home_*` (2) | PASS with note | The images are fine. `VSET .66` floats her 0.23 in above the screen bottom (problem 5). |
| face `natsuki_track_*` (8) | PASS | |
| face `nanoha_home_*` (7) | PASS | |
| face `akane_home_*` (4) | PASS with note | The face is about 13% smaller than in the school windows. These windows aren't shown in Ch3. |

## Problems, in order of priority

**1. `cg_lunch` contradicts c3_0413 (FAIL).**
- **"Grandpa at the far end."** Genji sits at the near-right corner, the closest diner to the camera (head at x 1890–2130, at the bottom-right edge of the table). Akane and Mio have the far end. The in-game shot 205_c3_0413 shows the line printed over that picture.
- **"Uncle Kazuo is at work, so his place has the extra soup bowls."** There's no empty place and no extra bowls. I counted six soup bowls, one beside each diner, no spare cushion, and nothing at Kōhei's own place.
- **The rest of c3_0411–0416 matches:**
  - Mio sits between Akane and Natsuki.
  - Nanoha sits next to Emi.
  - The POV hands are together.
  - The food is all there: the karaage mound, the onigiri stack, two plates of tamagoyaki, the kinpira bowl, and miso soup.
- **Fix (smallest):** change the text of c3_0413 to "Grandpa on my right. Mio at the far end between Akane and Mizuno, already supervising. Nanoha next to her mother. Uncle Kazuo is at work." If the Story thread wants Grandpa at the head of the table or the empty place on screen, the alternative is a reroll of 822 that spells out the seating: Grandpa centered at the far end, one empty cushion with stacked soup bowls.

**2. `akane_home_sleepy` against c3_0070–0074 (FAIL, text).**
- **The mismatch:** the sprite goes up at line 28 with `sleepy`, and c3_0071 says "Her eyes are still closed." Then c3_0074 says "She opens her eyes and squints up at me."
- **How I checked:** at 4× zoom the sleepy eyes are half open, with gray-violet irises and catch-lights. The iris-colored pixels in the eye band come to 3,743, against 4,632 for `smile`, so the eyes are about 81% as open as in the smile.
- **Fix (smallest, text):** change c3_0071 to "Her eyes are barely open." and c3_0074 to "She squints up at me."
- **Fix that keeps the "I'm asleep" joke:** make one more 1K head-crop edit, `akane_home_asleep` (eyes closed, soft mouth), the same way as seeds 761–764. Show it at line 28 and on c3_0073, then put `@show akane home_sleepy` before c3_0074.

**3. `cg_window` is held past the line that moves the rabbit (script placement).**
- **The mismatch:** c3_0106 says "She sets him on the corner of the sill with his back to me." For the 12 lines from c3_0106 to c3_0120, the CG still shows her holding him under her chin, facing us. `cg_window_sill`, which has the rabbit on the sill corner with his back to us, only arrives at c3_0312.
- **Fix:** move `@cg cg_window_sill` to just after c3_0106. Fold c3_0312 into c3_0106: "She sets him on the corner of the sill with his back to me and props her chin on her folded arms." Then drop c3_0312.

**4. Engine: Nanoha gets a face window while she's on screen in `cg_window_sill_turn` (code).**
- **The bug:** `CG_CAST` lists `cg_window` and `cg_window_sill` but not `cg_window_sill_turn`. On c3_0315 and c3_0162 the engine therefore shows `face/nanoha_home_smile` beside her own picture (shot 073_c3_0315).
- **Why it matters on iPad:** the window sits exactly over the rabbit's quarter turn, which is the visual point of c3_0314–0315.
- **Fix:** add `cg_window_sill_turn:['nanoha']` to `CG_CAST`.

**5. Engine: Emi's sprite floats above the bottom of the screen (code).**
- **The cause:** her sprite bottom is drawn at 62 × (1 − 0.66) = 21.08 in above the shared floor, against `FLOOR` 20.85 in. That puts the cut edge 0.23 in (7 device px on iPad, about 5 px at 1080p) above the bottom of the screen.
- **What a reader sees:** in shot 191_c3_0283, below the text box, her khaki trousers end in a hard straight edge at y 1631 with road underneath. None of the other Ch3 sets do this. Nanoha home, Mio, Genji and Akane run off the bottom of the screen, and Natsuki track sits exactly on it.
- **Fix:** set `VSET` `emi_home:.665`. That moves her bottom just below the screen edge, and she grows 0.8%. Alternatively, clamp `bottom` to ≤0 in `sizeSpr`.

**6. `cg_window_sill_turn`: the rabbit faces Nanoha, not "the curtain" (note).**
- **The image:** only the rabbit changed. Pixels differing by more than 25/255 from 842 fall only inside x 291–627, y 803–1202, which is within the documented box. There's no seam.
- **The mismatch:** he has turned a quarter turn into profile, and his eye and nose point right, at Nanoha. The pink curtain hangs behind him, so a reader sees him looking at her. c3_0314 says "so he's facing the curtain instead", and c3_0164 says "the rabbit is still facing the curtain."
- **Fix (text):** change c3_0314 to "…a quarter turn, so he's looking at her instead." and c3_0164 to "On her side of the glass, the rabbit is still sitting sideways." A rabbit-only re-edit to face left would point him at the window frame, which is no closer to "the curtain."

**7. `live/cg_tree_natsuki.mp4`: the loop point jumps (minor FAIL).**
- **Petals:** between f96 and f1, 31 petal-sized spots change by more than 40/255. An ordinary frame step has 3–7 (f10, f30, f48, f70, f90 measured). The mean change at the jump is 3.07/255, against 0.25 for an ordinary step. The wrap difference map shows them as petals blinking out and in across the canopy and the air.
- **Sharpness:** the image also softens 4% at the loop point (horizontal-gradient sharpness 9.88 → 9.48) and recovers over about 31 frames.
- **What is fine:** Natsuki, the camera and her hands are unchanged in all five sample frames. Only the ponytail sways (the range in her area is 24/255 at the 99th percentile). The clip lines up with the master at (0, 0) and scale 1.000.
- **Fix:** run `production/pipeline/vn/loop_crossfade.py` with `--frames 12`, from the untrimmed Kling output if it was kept, or else from this file. The result is 84 frames, 3.5 s. No reroll is needed.

**8. `cg_lunch`: Kōhei's sleeves (minor).**
- **The problem:** both cuffs are sage gray-green (median #9ca99f at x 1010–1080 and 1330–1400, y 1300–1335). None of his §2 outfits has that color, and his face windows in this scene show the school blazer (`@wear kohei school`, navy #3f4050).
- **Fix:** recolor the two cuff areas toward the blazer navy in code, keeping the line art. It's low priority because in play the text box covers everything below his fingertips after the CG's opening wait (shot 205).

## Notes (no fix required)

**`cg_window`, on model:**
- **Pajamas:** pale blue with white piping, as in `Nanoha-Pajamas-Bun`.
- **Bun and scrunchie:** the bun is on top of her head. The scrunchie is about 0.6× her head width (194 px against 325 px), so it's puffier than the concept, as §1 asks.
- **Rabbit and hands:** both hands are under the rabbit with four fingers each, and the rabbit sits at her chin.
- **Eyes, hair and room:** brown eyes. Hair #483433 under lamplight (swatch #51423d). The flower paintings have no text, and the posters have no lettering.

**Living stills:**
- **`cg_window_sill`, `cg_window_sill_turn` and `cg_lunch` barely move.** Across frames 5–96 only 0.01–0.02% of pixels change by more than 20/255, and I couldn't see the curtains stir or the steam in the five sample frames. Nothing morphs, the held faces (and the held rabbit in the turn) are identical in every frame, and Nanoha's eyes stay open.
- **Their loop points:** mean change 1.0–1.8/255 (95th–99th percentile 6–9) and a 3.5–4% sharpness step, against 0.03–0.08/255 for an ordinary frame step. That's a faint focus "breath" every 4 s. The same crossfade as in problem 7 would remove it if wanted.
- **Tone:** each clip is about 3/255 darker than its master. That's invisible.
- **The turn clip isn't wired:** `cg_window_sill_turn.mp4` isn't in `LIVE`, so it never plays. Because the loop is near-static, the difference can't be seen. Add it to `LIVE` or drop the file.

**`cg_tree_natsuki`:**
- **On model:** the navy track shirt, dark sweats, copper ponytail (#bb755b, muted by the plate's palette) and the camera raised at the tree all match c3_0368–0369.
- **The plate was redrawn:** the edit regenerated the background. The mean difference from `bg_shrine_tree_day` is 18–23/255 in every region (trunk, boulder, shrine, valley), lined up at (0, 1) px. The layout is the same, but twigs and petals are redrawn, so the crossfades from the plate to the CG and back shimmer lightly.
- **Optional fix:** paste her back onto the shipped plate with `region_composite.py`. That would keep the site pixel-identical, as the prompts note intended.

**`cg_tree_light`:**
- **Footprint:** the point sits at (1236, 757), just under the low branch where it leaves the trunk. Its peak brightness is 237/255 where the plate is 82 underneath. Changes over 40/255 stay inside x 1190–1290, y 703–805, and the rest of the plate is unchanged apart from compression noise.
- **In play (shot 156):** on iPad it's about a 4-css-px core with a 10 px halo, against bark and blossom, well away from the horizon. It reads as a glint or a petal, not the sun.

**`bg_shrine_steps`:**
- **Matches the text:** a steep stone stair through cedars with one landing, the rope rail on the left (c3_0269), drifting petals and daylight.
- **Style:** its ink density is 14.1%, against 18.0% for the tree plate and 12.5% for the houses plate. (Ink density is the share of pixels that are line art, measured with a black-hat filter.)

**`bg_tachibana_living`:**
- **Continuity with `cg_lunch`:** the same room. The TV with console and two controllers, the photo wall, the child's drawing, the calendar, the garden doors with stone lantern and cherry, the kitchen and the bookshelf all match.
- **Style:** ink density 13.5%. It's brighter and more saturated than the Fujisawa plate, which suits a daylight interior.
- **Pseudo-lettering:** the magazine at x 1780–2030, y 1170–1310 and the book spines carry pseudo-lettering. On iPad the magazine falls under the text box.

**`natsuki_track_*`:**
- **The face is the kendo face A:** the eye region differs by 3.1/255 at a fixed −103 px offset. The eye line is at 4′8.9″ on stage for the school, kendo and track sets alike.
- **Eye spacing:** 2.58, 2.69 and 2.75 in (school, kendo, track). The kendo and track faces are the same pixels, so their 2% gap is centroid noise.
- **Hair:** copper #cf7451 (kendo #ca7651). The ponytail isn't cut at the top: rows 0–15 are empty.
- **Consistency across expressions:** only the face box changes (x 302–538, y 249–480). The body differs by 0.27/255, with no shift. All eight expressions read as named.
- **Outfit and fit:** the outfit matches c3_0342 (black camera with a lens, on a neck strap). The shirt is close-fitting, and the two strap runs follow her chest down to the camera. At play size it reads athletic. I'm flagging it only for the author's eye under the modest-framing rule.
- **Camera pose:** she holds the camera one-handed at her waist, where c3_0359 and c3_0365 describe it raised or held to her chest. That's normal VN convention.

**`akane_home_*` (apart from problem 2):**
- **Outfit:** the cream cardigan with sweater-paw sleeves.
- **Scale:** on stage her crown is at 4′11.6″, the same as the school set, and crown-to-chin is about 10.3 in against 10.2.
- **Consistency:** only the face area changes (x 227–509, y 237–428). The body differs by 0.3/255.
- **Expressions:** smile, sleepy, tease (a wink) and happy read as named.

**`mio_home_*`:**
- **Against `sister-D`:** the bob with blunt bangs, the braid on her left, the mint star T-shirt, the tiered plaid skirt over bike shorts, the elbow bandage and the controller all match.
- **Scale:** her crown is at 3′11.75″ (she's 4′0″). Crown-to-chin is 9.2 in, against Akane's 10.2 and Nanoha's 9.6.
- **Consistency:** only the head changes. The body differs by 0.41/255, with no shift.
- **Expressions:** smug (lowered brows, toothy grin), grin (a wink, open laugh), pout and surprised read as named.

**`genji_shrine_*`:**
- **Against `genji.png`:** the white hair, hachimaki, navy samue, broom, sandals, stoop, and the hand at the small of his back (c3_0376) all match.
- **Scale:** his crown is at 5′1.6″. Only the head changes between expressions.
- **Head size:** crown-to-chin is 11.2 in (with headband and hair), against Natsuki's 8.8. Brow-to-chin is 6.0 in, against Emi's 4.5. He's drawn at the same 5.5 heads as the reference, so this is the realistic face design, not drift.
- **Framing:** at position `l` on iPad, his left sleeve is clipped by about 30 css px at the screen edge (shot 161). That's harmless.

**`nanoha_home_*` (the v1 set):**
- **Scale against the school set:** the crown is at 4′10.6″ in both. Crown-to-chin is 9.8 against 9.5 in. The eye line is the same, and eye spacing is 3.31 against 3.25 in, so `VSET .82` is right.
- **Hair and skin:** hair #4f3f3b (swatch #51423d). Skin #fde1d4, against #fbdcc9 for the school set: a shade pinker, not gray.
- **Consistency:** the expressions are full re-renders, but they don't shift (phase correlation 0, 0 for both head and body). `tease` is 720 px wide against 719, which is invisible.
- **No hair clip:** none in the home set. §2 doesn't say she wears it at home, and the window CGs agree.

**`emi_home_*`:** the low bun, light-blue shirt and mustard apron all match `full-emi` and c3_0282's "yellow apron". Her crown is at 5′1.6″.

**Face windows:**
- **`natsuki_track`:** the eye line is at y 223 of 384 for the school, kendo and track smile windows alike. Eye spacing is 104.4 / 105.4 / 105.8 px, and each expression is within 1 px of its kendo window.
- **`nanoha_home`:** eye spacing is about 122 px, the same as the school windows, and the eye line is about 14 px higher.
- **`akane_home`:** eye-to-chin is about 96 px against about 110 for the school windows, and eye spacing is about 118 against 135 (her head tilt accounts for part of that). So the face is about 13% smaller. Ch3 never shows these windows, because Akane's sprite is up whenever she speaks. If they're needed later, rebuild them with `h0.24`.

**`cg_lunch` in play:** on iPad the text box covers the bottom ~21% of the CG, so Kōhei's hands show only to the fingertips during the six lines. The full gesture is visible during the CG's opening wait.

**`cg_lunch` scale:** Mio's head is 0.80× Akane's at the same depth (crown-to-eye 90 px against 113 px). On stage the two are 0.90×. She reads as the younger child, so no fix is needed.
