# Ch2 backgrounds, catch CG and animated moment: on-model check, round 1 (Oct 24)

Fresh agent, no prior context; checked the build files in `v2/img/` (and the shipped mp4, 73 frames at 24 fps) against the style guide, the references and the Ch2 script. Frame numbers n are mp4 frames.

| Image | Verdict | Main problem |
|---|---|---|
| Animated catch (`anim/cg_catch`) | **FAIL** | His arm crosses her chest, then passes through her body; limbs tangle; faces morph; the tear flickers |
| `cg_catch` | **FAIL** | Kōhei's hair off model (longer and bulkier than `kohei-short-A`); extra sweat drops read as several tears. Scale passes |
| `bg_bridge_dusk` | **FAIL (minor)** | The Ōzakura is wider than a nearer cherry tree and reads as a crisp lit tree, not "a pale smudge" |
| `bg_natsuki_apartment_night` | **FAIL (minor)** | The balcony is level with the street; c2_0289 says "The street below ran down toward the river" |
| `bg_restaurant_night` | PASS | |
| `bg_dojo` | PASS | |
| `bg_dojo_evening` | PASS | |

## Animated catch
1. From n 18 to n 36 Kōhei's right arm sweeps across her front at chest height; by n 42 it is behind her back, so it has passed through her torso. At n 36 his forearm lies across her chest and a hand clutches her collar. Even for ¼ s this breaks the modest-framing rule. The script says "One arm behind her back."
2. Her far arm vanishes between n 0 and n 6.
3. Faces morph: Natsuki off model at n 30–36, Kōhei drifts at n 24–42 and winces at n 42; both recover by n 48.
4. The tear appears at n 12 (before the catch), disappears at n 30–54, returns from n 60.
5. Minor: in the start frame his left hand rests on his own stomach.
Works: locked camera; the last 11 frames match the CG within 3.4/255 (no jump at the handoff); continuous ponytail swing.
Fix suggested: re-make the start frame from the fixed CG with the arms already where they end up (her right hand toward his chest, his right arm low behind her back, not touching), no tear; add to the prompt "his right arm stays behind her back the whole time and never crosses in front of her; her right hand goes to his chest; the tear appears only in the last half second." Fallback: cut n 13–47.

## cg_catch
1. **Hair off model.** Hair above the brow line ≥ 1.31× brow-to-chin (runs off the frame) against 0.95× in `kohei-short-A`; fringe on the brows (design: above them); side and back locks to the jaw. Color right. Fix: hair-only edit pass with `kohei-short-A` as image 2.
2. **Scale passes:** eye-to-chin 1.04, ear height 1.06, ear-to-eye 1.02 (expected ~0.96–1.00 with her 8–12 inches nearer the camera; within noise). Hand and torso in proportion.
3. **Text match:** everything the narration states is there (arm behind her back, hand around her forearm, one tear, eyes wide, hairline sweat, strand on her cheek, his red ears, orange light, wet floor, bucket and cloth). Her copper hair, ponytail, green eyes on model; her paler gi reads against his navy. Problems: two teardrop-shaped sweat drops on her cheek and a droplet at her far eye read as several tears ("One tear"); the tear is on her right eye while the `natsuki_kendo_tears` sprite's main streak is on her left (minor).
4. **Location (minor):** clear-glass grid windows instead of the dojo's vertical wooden lattice; no shrine shelf or armor stands. Light direction and boundary line match.
5. **Style note:** heavier linework and flatter color than the backgrounds and Ch1 CGs; closing it needs a reroll with a Ch1 CG as style reference.
Outside this image: Kōhei's kendo face windows show a faded periwinkle gi (#666985), close to Natsuki's; §2 and c2_0074 make his navy and hers the faded one. Re-tint the windows toward navy or log a decision.

## bg_bridge_dusk
Tree 138 px wide (1/17 of the frame; prompt asked 1/25 ≈ 96 px), wider than a nearer cherry tree among the houses (120 px), so the distance cue is backwards; crisp outline, visible trunk and brightness read as a lit tree. Right place, catches the last light. Fix (code only): paste at ~60% anchored at the base, blur ~1.5 px, lower contrast, keep the power lines in front.

## bg_natsuki_apartment_night
All props present (note, rice cooker, crossed-out box labels, pen cup, rug, one cushion, one light, balcony door, cherry trees under streetlights, lit train); style matches `bg_fujisawa_kitchen`. Problem: the street is level with the balcony rail and runs along the riverbank. Fix: change c2_0289 to match, or edit the balcony view to a third-floor vantage looking down a street sloping to the river.

## Passes
`bg_restaurant_night` (only windows and doors changed, full night, clean); `bg_dojo` (identical to the pilot plate); `bg_dojo_evening` (aligned with `bg_dojo` within 1 px, low orange light from the same side, glossy wet floor).

## Production response
See `bg-cg-onmodel-r2.md`.
