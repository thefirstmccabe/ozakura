# Ch3 "Windows": on-model image check (§9 step 4)

**Build:** pilot v2, Ch3 (Nov 1 art). **Reviewer:** independent, cold. **Method:** all measurements are on the full-res masters (2400×1340) with a labelled pixel grid, unless a different scale is stated. Living stills were decoded frame by frame (1920×1072, 84 frames each) and compared numerically against the masters and against each other.

**What Ch3 shows:** six CGs (`cg_window`, `cg_window_sill`, `cg_window_sill_turn`, `cg_tree_natsuki`, `cg_tree_light`, `cg_lunch`), four of them as living stills (`v2/img/live/`: sill, sill_turn, tree_natsuki, lunch). Ch3 has no `@anim` moments and no `@insert`/`@panel` pages.

**Missing inputs:** `production/refs/locations/window-night-from-kohei.png`, which prompts.md names as a ref for `cg_window`, isn't in this checkout. I checked the window against `refs/locations/sketches/sketch-window-night.png`, `refs/locations/nanoha-room-day.png` and the shipped plates instead. `production/pilot-v2/art/` has no layout sketch for the one multi-character CG (`cg_lunch`); the only sketch there is `cg_collar_layout.jpg` (Ch1).

---

## 1. `cg_window` (c3_0100–0105): FAIL (minor, shared with 2–3)

| Check | Result |
|---|---|
| On model | **Pass, with one miss.** Brown eyes, soft oval face, dark-brown hair (crown sample #3e2f30 against swatch #51423d; darker, but she's backlit), side wisps as in `Nanoha-Pajamas-Bun.png`. Pale-blue pajamas with white piping match the ref. The cat detail is hidden behind the rabbit, which is fine. **Miss:** the scrunchie is no puffier than the ref's (see P4). |
| Scale | Pass. Her head (crown under the bun at y 540 to chin at y 830) is 290 px. The window opening is 855 px tall (about 2.9 heads, roughly 25 in) and 1610 px wide (about 5.5 heads, roughly 3′11″). That's a plausible small bedroom window. |
| Matches text | Pass. She's leaning on the sill in pajamas, the bun sits on top of her head, and she holds the rabbit in both hands with a solemn face. The rabbit's ears reach her chin, so it reads as "just under her chin." |
| Location | Fail (P5, P6): the sashes are drawn closed, and the curtains don't match the plate. |
| Canon/content | Pass. Modest framing, no text: the flower paintings are clean at 2× zoom. Hands: both grip the rabbit with correct finger counts. |
| Craft | Pass. |

## 2. `cg_window_sill` + living still (c3_0106–0313): FAIL

| Check | Result |
|---|---|
| On model | Pass, except the scrunchie (P4). |
| Scale | Pass. The rabbit sits 360 px tall, about 1.24 of her head heights, so about 10–11 in. That's right for a plushie. |
| Matches text | **Fail (P1, P3).** The rabbit sits on the sill corner with his back to us and the tail showing, and her chin rests on her folded arms, both as written. But she's smiling with her mouth, which contradicts c3_0119, "Her face is perfectly straight. Her eyes are laughing." That line plays while this CG is up. The same smile then holds through the clinic and "Dad's was cancer" lines (c3_0432–0437). |
| Location | Fail (P5, P6), plus the rabbit sits outside the glass (P3). |
| Canon/content | Pass. |
| Craft / living still | Pass. The still barely moves (median frame-to-frame change 0.02 levels; no pixel's std over time is above 12), so the curtains' "stir" can't be seen. It's harmless. The oval face hold leaves no visible edge. |

## 3. `cg_window_sill_turn` + living still (c3_0314–0322): FAIL

| Check | Result |
|---|---|
| On model | Pass, except the scrunchie (P4). The face is identical to 842; a pixel diff outside the composite box maxes at 36, which is webp noise around edges. |
| Matches text | **Fail (P2).** c3_0314 says "a quarter turn, so he's facing her," and c3_0164 says "still sitting sideways." The rabbit's head now faces right, toward her, but the body has barely turned. Measured across the rabbit's body width, the tail's center moved only from 0.29 to 0.20, and the tail is still fully in view. That's roughly a 20–30° turn, not 90°. The whole change covers about 1% of the frame, so at iPad size the payoff beat ("His sentence has been reduced") is easy to miss. |
| Location | Fail (P3, P5, P6). |
| Canon/content | Pass. |

## 4. `cg_tree_natsuki` + living still (c3_0368–0369): FAIL

| Check | Result |
|---|---|
| On model | **Fail (P8).** Copper hair (crown #d38563; the sprite's is #c85a3b, with the sun on it), navy track shirt (#383e58 against the sprite's #3e455f), dark sweats, black camera. **Ponytail:** at mid-length it's about 100 px wide against a 145 px head depth, so roughly 0.7–0.8 of the head's width. The track sprite's is about 85 px against a 275 px head, roughly 0.3–0.35. That makes it about twice as wide relative to the head, with big S-waves and splayed ends: exactly the drift style guide §2 names ("longer, bigger and messier"). **No camera strap:** c3_0342 has it around her neck, and the sprite draws it, but the back of her neck shows only the collar. |
| Scale | Pass. From the top of her head (y 683) to the shirt hem (y 1145) is 3.0–3.5 heads, depending on where her hidden chin falls (815–835). The sprite measures 3.16. Nothing at her depth gives a hard scale reference, and the figure reads natural. |
| Matches text | **Fail (P9, minor).** Natsuki is rendered as written (camera up, working). But the next line, c3_0185, puts Nanoha "on the stone path… a second broom… leaning against the stone lantern beside her." The CG shows that path and the only lantern, both empty, with the petals unswept. |
| Location | Pass. It's the shipped `bg_shrine_tree_day`, identical outside her figure. She hides the torii's right post (x 593–638) without breaking the lintel. The light is soft, from the upper right, on both. |
| Canon/content | **Fail (P7).** The sweats are drawn form-fitting, with seat contour lines and a center seam, and a bright highlight on the seat (x 650–680, y 1170–1210). The frame's bottom edge crosses her upper thighs (y 1340), so in a back view the composition lands on her seat. The track sprite's sweats are loose and straight-legged, with a drawstring. This breaks the "never frame the school-age cast for figure" rule, and it's outfit drift too. |
| Craft / living still | **Fail (P10, minor).** The figure holds on model across all 84 frames (checked at frames 1/21/42/63/84). But the loop doesn't close. Frame 84 is as far from frame 1 (mean 2.2) as the mid-loop frame 42 is (2.1). At the loop point the ponytail jumps by 2.1 where a normal frame step is 0.00, and canopy blocks jump 3–6× their normal step. The file has 84 frames, but prompts.md records "trimmed to 96 frames." |

## 5. `cg_tree_light` (c3_0263): PASS

| Check | Result |
|---|---|
| Matches text | Pass. The point sits just under the low branch where it meets the trunk (centroid x 1233, y 748), "a spot just under it" as c3_0260 says. Its core is about 40 px across and cool white (213, 234, 250), and it sits on the branch's shadowed underside, so it can't read as the sun or a sky gap. |
| Location | Pass. A diff against `bg_shrine_tree_day` finds changes only within a 120 px radius of the point (two stray pixels beyond, max 22, which is webp noise). |
| Canon/content | Pass (advisory: the plate's marker post and lantern have pseudo-glyphs. They're inherited, and illegible at play size). |

## 6. `cg_lunch` + living still (c3_0411–0416): FAIL (minor)

| Check | Result |
|---|---|
| On model | Pass, against each sprite. Emi: low bun, light-blue shirt, mustard apron ("yellow apron," c3_0282). Nanoha: hair down, cream cardigan, lavender top (her home set). Akane: lavender-silver hair, clip on her left, cream cardigan. Her hair runs to her chest, the same as `akane_home_smile` (the guide's text says shoulder length; the CG follows the sprite). Mio: bob, blunt bangs, braid on her left, gap-toothed open grin, mint tee with a yellow star. Natsuki: high ponytail with a dark tie, track shirt. Genji: hachimaki, navy samue, white brows. No Kazuo, as written. |
| Scale | Pass, measured top of hair to chin. Near pair: Emi 260 px, Genji 275 (both 5′2″, ratio 1.06, Genji slightly nearer). Middle pair: Nanoha about 200, Natsuki about 190 (Natsuki sits a little farther back, 5′3″ against 4′11″). Far end: Akane 185, Mio 165, a ratio of 0.89, which fits a 4′0″ child next to 5′0″. Mio's eye line sits 70 px (about 3.4 in) below Akane's, against about 6 in expected; that's slightly tall, which reads as her kneeling up to lead "itadakimasu." Akane against Nanoha at a similar depth: 185 vs 200, consistent with 5′0″ against 4′11″. |
| Matches text | **Fail (P11, P12).** The seating is right: Grandpa on Kōhei's right, Mio between Akane and Mizuno, Nanoha beside her mother. The food is right item by item: a mountain of karaage, a stack of onigiri, **two** plates of tamagoyaki (front left and back center), the big bowl of kinpira. But there are only six miso bowls for seven diners. Kōhei's place has no soup, rice or chopsticks, so "Miso soup for everyone" (c3_0412) isn't shown. Kōhei's sleeves are sage gray-green (#9aa89e) with no white cuff or blazer, while he's `@wear kohei school` for this scene. |
| Location | Pass. It matches `bg_tachibana_living`: photo wall, TV, calendar, garden door with yellow curtains, cherry tree and lantern, kitchen at right, bookshelf. The table is enlarged to seat seven, which is acceptable. Daylight comes through the garden door. |
| Canon/content | Pass. Modest framing; hands are all correct (7 pairs checked at 2×). Advisory: the calendar and book spines carry pseudo-text, inherited from the plate and illegible at play size. |
| Craft | Pass (advisory: all six diners have the same closed-eye smile, which fits "hands together" but reads a little stock). The living still is static: only 11 pixels have a time-std above 12, so the steam barely moves. The loop seam is invisible (mean 1.0). |

---

## Summary of failures (12)

| # | Image | Problem | How checked | Smallest fix |
|---|---|---|---|---|
| **P7** | cg_tree_natsuki | **Content rule.** Form-fitting sweats with seat contours and a seat highlight (x 650–680, y 1170–1210); the bottom edge crops at the upper thigh, so the back view lands on her seat. The sprite's sweats are loose and straight. | 1:1 grid crop beside `natsuki_track_smile` lower body | **Edit pass** on the area below the hem (x 470–740, y 1130–1340): relaxed, matte, straight-leg sweats from the sprite, no seat lines or sheen. Paste back by region, then hold that region in the living still (or rerun it). |
| **P1** | cg_window_sill | Mouth smile contradicts c3_0119, "face perfectly straight… eyes laughing," and holds through the cancer lines. | Face crop at 2× | **Expression edit** inside the existing face oval to her `dry` face (straight mouth, smiling eyes); re-hold the living still. Leave sill_turn smiling, so the softening becomes the beat. (Or change the text: "She's trying to keep a straight face.") |
| **P8** | cg_tree_natsuki | Ponytail about twice as wide relative to the head as the track sprite's, with big S-waves and splayed ends (the §2 drift); camera strap missing (c3_0342). | Grid measurement against the sprite | **Edit pass** on the ponytail and neck with the sprite as image 2 (smooth glossy ponytail, black strap at the nape), then **rerun the living still**, since it animates the ponytail. Batch with P7. |
| **P2** | cg_window_sill_turn | The rabbit turned only about 20–30° (tail center 0.29 → 0.20 of body width, tail still in view), not the "quarter turn"/"sideways" of c3_0314/c3_0164; the change is about 1% of the frame, so the beat is easy to miss. | Side-by-side crop, tail position measured | **Text change:** c3_0314 "turns Usagi-san partway round, so he's looking at her instead"; c3_0164 "the rabbit is still half turned." Or an edit pass compositing a true side-profile rabbit inside the same x .10–.255 box. |
| **P3** | cg_window_sill, _turn | The rabbit sits in front of the sash and jamb (it covers the left stile), so it's outside the glass, but c3_0164 says "On her side of the glass." | 2× crop of the frame | **Text change** to c3_0164: "On her sill, the rabbit is still sitting…" |
| **P4** | all three window CGs | Scrunchie not puffier than the ref, against the §1 rule and c3_0100's "enormous": 180×62 px on a 310 px head (0.58 wide, 0.20 tall) vs the ref's 0.54 / 0.19. | Color segmentation of the scrunchie, hair-width scan | **Text change** ("big soft scrunchie"). Or edit the scrunchie in 832/842/852 and re-hold both living stills. |
| **P9** | cg_tree_natsuki | The path and the only lantern are shown empty and unswept, but c3_0185 (the next line) puts Nanoha there sweeping, with a broom at the lantern. | Script read against the CG | **Text change** to c3_0185/c3_0370: Nanoha comes out from behind the shrine with a broom in each hand and gives one to Mizuno. |
| **P11** | cg_lunch | Kōhei's sleeves are sage gray-green (#9aa89e) with no cuff, which doesn't match `@wear kohei school`. | Color sample at the frame bottom | **Edit pass** on the bottom strip (y 1250–1340): white shirt cuffs (blazer off at the table). |
| **P12** | cg_lunch | 6 miso bowls (and 5 rice bowls) for 7 diners; Kōhei's place is bare, so "Miso soup for everyone" isn't shown. | Dish count on the grid | **Edit pass:** a soup bowl and chopsticks at the near edge beside his hands. Or accept (low). |
| **P10** | cg_tree_natsuki living still | The loop doesn't close: frame 84 differs from frame 1 as much as mid-loop does (2.2 vs 2.1), so the ponytail and canopy snap at each 3.5 s loop. The file is 84 frames; the record says 96. | Frame-by-frame diffs, seam against normal step per region | **Re-export** the full 96-frame take, or cross-fade the last ~8 frames into frame 1. The other three clips don't close either, but they barely move, so their seams can't be seen. |
| **P5** | all three window CGs | Her window is drawn **closed**: both sashes in closed position, the crescent lock at the meeting stiles (x ≈1110, y 700–750), the left sash's pull at y 700–760. But the left sash has no glass and she leans through it. The text says it's open, then "slides… shut." | 2× grid of the jamb and meeting stiles | **Edit pass** (low priority): remove the left sash's stile and pull so the left half shows only the jamb, with the left sash slid behind the right one. |
| **P6** | window CGs vs `bg_kohei_room_night` | The CG's curtains are pink and open (matching `nanoha-room-day.png` and the night sketch); the plate shown just before and after has cream curtains drawn across her window, while c3_0096 says she's waiting at the open window. | Plate crop against the CG | **Edit the plate**, not the CG: pink curtains, drawn back. |

**Advisories (not counted):** all four living stills run about 4 levels darker than their masters (RGB −3.6 to −4.1), which could pop if the engine swaps webp for mp4 (not checked; the engine is outside this check's files). The window living stills show no visible motion. In `nanoha-room-day.png` Usagi-san wears a pink bow, and the CG rabbit has none. The six closed-eye smiles in `cg_lunch` are identical. Plates carry illegible pseudo-text. The `window-night-from-kohei.png` ref is missing from this checkout.

**Priority:** P7, then P1, then P8 (bundle P7+P8 into one edit pass and one living-still rerun on `cg_tree_natsuki`). P2/P3/P4/P9 are text changes. The rest are minor polish.
