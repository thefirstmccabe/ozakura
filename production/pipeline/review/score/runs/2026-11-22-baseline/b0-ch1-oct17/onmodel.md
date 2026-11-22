# On-model image check (§9 step 4): Pilot v2, Prologue + Ch1 (build b0, Oct 17 checkout)

**Scope.** `production/pilot-v2/script/ch01.ozs` has two `@cg` lines and no `@anim`, `@insert` or `@panel` lines:
- `@cg cg_dream slow` (line 24). In the player this still also runs a "living still" loop, `v2/img/live/cg_dream.mp4` (index.html `LIVE` map, line 362), so I checked the loop as Ch1's one animated moment.
- `@cg cg_natsuki_intro` (line 215).

`cg_title` (and its loop) appears only on the title screen, and no Ch1 line names it, so I didn't review it.

**Inputs.** I read style guide §1–§2 (reference hierarchy, design lock, swatches, inventory, character sheet, uniform), the script around each image, the location plates (`v2/img/bg/bg_classroom_day.webp`, `production/refs/locations/past-*.png`) and the references named below.

Two inputs are missing:
- **`production/pilot-v2/art/prompts.md` doesn't exist in this checkout.** `art/` holds only `masters/`. I couldn't check either CG against its prompt.
- **No layout sketch exists for either CG.**

**Method.**
- I measured on the 2752×1536 masters using 10 to 50 px coordinate grids.
- I confirmed that the shipped 2400×1340 files are the masters, downscaled. The mean absolute difference after resizing is 1.2/255 for `cg_dream` and 0.9/255 for `cg_natsuki_intro`.
- Swatches are per-region medians.
- I checked the loop frame by frame: 96 frames at 24 fps, 4.0 s long.

---

## 1. `cg_dream` (prologue, line 24): still. Verdict: PASS with one minor fix

**Text around it (lines 22–39):**
- "The sound of a river, close by."
- "a cut across the back of [my wrist] … held it closed the whole way home from training"
- "a branch moving in the wind. Petals."
- "Hands that aren't mine wind a strip of cloth around a wrist that is."
- `@flash white`, then "And then I wake up, and the only thing left is a feeling…" (two more lines follow before `@bg black slow`)

**References:**
- `inventory/past-natsuki-A.png` (everyday look)
- `turnarounds/past-natsuki.png`
- `inventory/ronin-B.png` (chosen)
- `turnarounds/ronin.png`
- `locations/past-tree-bloom.png`, `past-tree-site.png`

**On model: pass.**
- **Past Natsuki.** She wears the blue-gray striped kimono with a cream obi, which matches `past-natsuki-A`. Her face and hair stay out of frame.
  - Kimono stripes measure #444a65 in the CG against #576170 on the reference: the same hue family, darkened by the dream's mist grade.
  - A's cream work apron isn't shown. That's fine for an off-duty moment.
- **The rōnin's sleeve** is slate-navy, #3e465b in the CG against #455667 for `ronin-B`. The sleeve is pushed back to the elbow and the forearm is bare, as in the reference. A katana hilt (black ito wrap, kashira) is visible beside him.
- **The bandaged wrist matches the turnaround,** which puts the bandage on his **left** wrist. Read as his point of view, the arm enters from the lower left, which is consistent. The crop alone can't prove which hand it is.

**Problem D1 (minor, on model / craft): the rōnin's hand reads as an old man's hand.**
- His hand is at the visual center of the frame (master x≈1430–2060, y≈400–800). It is drawn with deep wrinkle hatching across the back and knuckles, raised veins, and tightly clenched fingers whose tips curl back toward the wrist.
- Next to past Natsuki's smooth hands it reads as a hand of 50 or older. `ronin-B` and the turnaround show a young man in his twenties with smooth forearms and hands.
- The clenched pose also takes a moment to parse: it is a loose fist seen from the thumb side, with four nails visible along the top and the thumb at the right.
- **Scale is not the problem.** Thumbnail widths measure about 55 px for him and about 50 px for her (master), a 1.1× ratio, which is normal for a 5′9″ man and a 5′2″ woman.
- **Fix:** a masked edit pass on the hand only (`nano-banana-pro/edit`, with `ronin-B` passed). Ask for a young man's hand, lighter creasing, the fingers relaxed and loosely curled, and everything else identical.

**Scale: pass.**
- No heads are in frame, so I measured hands instead. The 1.1× thumbnail ratio is above.
- The man's forearm looks heavy because it is close to the camera and runs diagonally. It isn't oversized for its depth.

**Matches the text: pass, with one script problem (D2).**
- Visible: a strip of cloth wound around the wrist by hands that aren't his; blood showing through on the side facing the viewer, which is the back of the wrist, since the back of his hand faces the viewer; an overhead branch; petals.
- The river is heard, not seen. The framing is a close-up, so nothing contradicts it.

**Problem D2 (minor, text vs. image): the dream image stays on screen after he wakes up.**
- `@flash white` (line 34) is only a momentary overlay; `index.html` line 606 calls `flash()` and leaves the CG layer alone.
- So the bandaging image, with its loop running, stays up through "And then I wake up, and the only thing left is a feeling I can't put a name to." and the next two lines. It is cleared only by `@bg black slow` at line 39.
- The narration says the image is gone while it's still showing.
- **Fix (script, one line):** add `@cg - slow` right after `@flash white`. The bg underneath is already black, so the following lines play over black, and `@bg black slow` becomes a harmless no-op.

**Location and continuity: pass, with one question for Story (not counted).**
- The light is soft and even, under an overcast misty sky. There's no mirrored layout.
- **Question for Story:** the style guide's past-era plates are set in winter, with blossoms falling on snow and frost on the branches (§1b, `past-tree-bloom.png`). The dream's branch carries no snow or frost.
  - If this dream is meant to be the Great Cherry in that winter, an edit pass should add a dusting of snow along the branch's top edges to match the plate.
  - If it's another tree or season, it's fine as it is.
  - Canon wasn't in my reading list, so I'm leaving this as a question rather than a failure.

**Canon and content: pass.** The framing is modest. There's no text, watermark or frame line; I checked all four corners and the edge rows and columns.

**Craft: pass** apart from D1.

---

## 2. `cg_dream` living-still loop (`v2/img/live/cg_dream.mp4`). Verdict: FAIL

The player fades the loop in over the still 1.95 s after `@cg cg_dream slow`. The loop is 1920×1072, H.264, 24 fps, 4.0 s.

**Registration: pass.**
- Phase correlation against the still finds a 0 px offset in all five regions I tested.
- The mean color is within 0.6 levels of the still.
- The seam from frame 95 to frame 0 has no camera jump, only a brightness shift of about 1.3 levels on the keyframe, which isn't visible.

**Problem D3 (blocking, craft and text): the only motion is one petal blinking on and off in place.**
- I measured per-region frame differences. The petal over the left branch (video px about 180–360 × 180–300) differs from an empty frame by 20 levels while it's there and by about 0 when it's gone. By frame:
  - visible on frames 0–20;
  - fades out over 21–25;
  - gone on 26–45;
  - pops back on 46–49;
  - visible on 50–61;
  - **vanishes in a single frame, from 61 to 62**;
  - gone on 62–84;
  - back on 85–92.
- That is three pop-ins every 4 seconds, with no fall or drift. It reads as a glitch.
- **Nothing else moves.** Differences in the branch regions (0.6–1.0) are the same as in static regions such as the kimono and the hands, so they're encoder noise. The other mid-air petals are frozen.
- Line 27 says "a branch moving in the wind", and the loop shows a still branch.
- **Smallest fix:**
  1. Remove `cg_dream` from the `LIVE` map (`v2/index.html` line 362; one line, reversible), so the clean still shows.
  2. Then reroll the living-still pass with a gentle branch sway and two or three petals drifting down through the frame, keeping the hands and figures locked.

**Problem D4 (minor, craft): the loop is softer than the still it replaces.**
- I computed edge energy (mean of a FIND_EDGES filter) at the iPad's 2732 px width: 6.9 for the video against 12.5 for the still, which is about 55%.
- Side by side, the bandage and knuckle hatching visibly blur as the loop fades in.
- **Fix:** when rerolling for D3, encode at the still's 2400×1340 and a higher quality setting (around CRF 16).

---

## 3. `cg_natsuki_intro` (c1_intro, line 215; cleared at 224). Verdict: PASS on model and scale; three minor fixes

**Text around it (lines 208–233):**
- Kōhei is in "the second-to-last row by the window". The door opens.
- "She walks to the front of a room full of strangers like she's walking onto a court she's already won on."
- "Copper hair, cut neat at her shoulders and tucked behind one ear. Her uniform looks like it was ironed by someone who meant it."
- "She counts on her fingers." (line 220)
- "Someone in the front row actually claps."
- After the CG: "Her grin stutters… the grin is back where it was."

**References:**
- `natsuki-v2/01-restyle-uniform.png` (the lock)
- the sprite `v2/img/ch/natsuki_school_grin.webp`
- `design-oct10/natsuki-casual-A.png` (face)
- plate `v2/img/bg/bg_classroom_day.webp`

**On model: pass.**
- **Face** matches the grin sprite almost exactly: the eyes, the lash wing, the brows, and the small mark in front of her left ear.
- **The toothy grin is right for this moment.** The text calls it a grin twice, and it's bright rather than a tomboy grin.
- **Eyes** are amber-brown.
- **Hair** is #b25c38 at the side and #c56a3d at the crown highlight, against the #b55e36 swatch. It's glossy, layered and side-swept, and **tucked behind her left ear** (viewer's right) with the ear visible, which matches both the sprite and the text.
- **Hair length:** it ends 0.25–0.32 head-heights below the chin (master y≈663 and 685, chin at 588), at the top of the shoulder. The reference measures 0.24–0.39, which the guide says runs long; the sprite measures 0.20–0.24. That's within "at her shoulders".
- **Skin** is #fcd3c0 against the #f5dbca swatch.
- **Uniform:**
  - Navy blazer, open and neat, with gold buttons.
  - White shirt, collar button open, crisp.
  - Burgundy bow.
  - Charcoal plaid pleated skirt.
- **Build:** crown to waistband measures **2.47 heads** in the CG, against 2.45 on the reference and 2.43 on the sprite. Head height is 299 px in the CG (crown y=289, chin y=588), 155 px on the reference (118 to 273) and 399 px on the sprite (6 to 405).

**Problem N1 (minor, content rule / on model): her skirt is shorter than on the locked design.**
- Waistband to hem at center measures **1.36 heads** in the CG (y≈1022 to 1430). The reference measures **1.56 heads** (497 to 739) and the sprite **1.45 heads** (976 to 1553).
- The reference figure is 7.05 heads tall (crown 118, sole 1213), so at 5′3″ one head is about 8.9″. The CG skirt is therefore about **1¾ inches shorter** than the lock.
- The shot is low-angle: the horizon is at chest height, y≈850 on the master. That is the direction §1's rule against framing the school-age cast for appeal warns about.
- **Fix:** an edit pass that lowers the hem by about 0.2 head-heights (about 60 px on the master) to match `01-restyle-uniform.png`, with everything else identical. Re-measure after.

**Scale: pass.**
- She's the only figure who can be measured.
- Her proportions match the lock (see Build).
- Foreground head widths are about 475 px (center-left girl's hair) against 275 px (Natsuki's hair at eye level), a ratio of **1.73×**. That's coherent with the horizon at seated eye height.

**Not counted:** a 1.73× ratio with only one row of heads in front puts the camera at about the second row, not at Kōhei's second-to-last-row window seat. Nothing says the CG is his literal point of view, so I'm not counting it.

**Problem N2 (minor, matches the text): the CG holds a wave while the text says she counts.**
- The CG is still on screen when line 220 says "She counts on her fingers." It shows an open-palm wave with five fingers spread (right hand, correctly drawn: thumb on the inside, five digits).
- The reader looks at a wave while reading about counting.
- **Fix (text):** change line 220 to "She lowers her hand and counts on her fingers." That makes the wave the beat just before. The alternative is to move `@cg - cut` up to just before line 220, but that cuts the CG to two lines.

**Location and continuity: pass.** The CG matches `bg_classroom_day`:
- windows on the left with cream curtains tied back;
- cherry trees and a mountain outside;
- the speaker left of the clock above the board;
- the split green board;
- a low shelf with books under the left board section;
- the wooden lectern behind her, to her left (viewer's right).

Light comes from the left windows in diagonal bands across the board, as on the plate. Nothing is mirrored. It's morning: the clock's minute hand is at 8 (:40) and the hour hand is cut off by the top of the frame, which is consistent with homeroom after the ceremony. The cherry blossoms suit April 7.

**Problem N3 (minor, craft): the three foreground girls have identical hair.**
- All three foreground girls (far left, center-left, center-right) have the same waist-length straight black hair, with the same part, highlight and length.
- They're large, blurred and in the foreground, so the copy-paste is easy to notice.
- **Fix:** an edit pass, which can be batched with N1. Change two of the three heads, for example one to a low ponytail and one to a dark-brown bob.

**Canon and content:**
- **Pass** on text, watermarks and frame lines; I checked the corners and edges.
- The binder spines on the shelf carry tiny illegible pseudo-glyphs. They're diegetic and match the plate's shelf, so this is a note only.
- **Hands:**
  - The raised hand is correct.
  - The left hand, hanging at her side, is slightly mushy when zoomed, but it reads as a relaxed hand at 1:1 on the 2400 px file. Not counted; fix it only if N1's edit pass is redoing that area anyway.
- Modesty is covered under N1.

**Craft: pass** apart from N3.

---

## Summary of failures (7 problems: 1 blocking, 6 minor)

| # | Image | Severity | Problem | Smallest fix |
|---|---|---|---|---|
| D3 | `cg_dream` loop | **Blocking** | The only motion is one petal popping on and off in place: three times every 4 s, including a one-frame vanish at frame 61→62. The branch and the other petals are frozen, though line 27 says "a branch moving in the wind." | Drop `cg_dream` from `LIVE` (index.html line 362) now; reroll the loop with branch sway and drifting petals. |
| D4 | `cg_dream` loop | Minor | The loop is 1920×1072 with about 55% of the still's edge detail at iPad width, so the linework softens when it fades in. | Re-encode at 2400×1340, high quality, with the D3 reroll. |
| D1 | `cg_dream` still | Minor | The rōnin's hand (frame center) is heavily creased, veined and clenched, and reads 50 or older against young `ronin-B`. Scale is fine (thumbnails 1.1×). | Masked edit pass on the hand with `ronin-B` passed. |
| D2 | `cg_dream` still | Minor | The dream CG stays up through "And then I wake up… the only thing left is a feeling…", because `@flash white` doesn't clear it. | Add `@cg - slow` after line 34. |
| N1 | `cg_natsuki_intro` | Minor | The skirt is 1.36 heads long against 1.56 on the lock (1.45 on the sprite): about 1¾″ shorter at 5′3″, in a low-angle shot of a school-age character. | Edit pass: lower the hem about 60 px on the master; re-measure. |
| N2 | `cg_natsuki_intro` | Minor | "She counts on her fingers" (line 220) plays over a frozen open-palm wave. | Text: "She lowers her hand and counts on her fingers." |
| N3 | `cg_natsuki_intro` | Minor | The three foreground girls have identical cloned black hair. | Edit pass (batch with N1): vary two heads. |

**Not counted (for the record):**
- The dream branch has no winter snow or frost, while the past-era plates do. This is a question for Story.
- The intro CG's camera depth implies a front-row seat rather than Kōhei's.
- Past Natsuki's apron is absent.
- Natsuki's left hand is slightly soft.
- Binder-spine pseudo-glyphs.
- **Process gap:** `production/pilot-v2/art/prompts.md` and any layout sketches are missing from this build, so prompt intent couldn't be checked.
