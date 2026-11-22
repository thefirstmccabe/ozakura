# Build review: Pilot v2, Prologue + Ch1 (build of Oct 18), before handover

Independent QA. Scope: all of Ch1 (no diff or snapshot regression this run). Build: `b1-ch1-oct18/v2/`, served on port 8151.
Screenshots: `runs/b1-ch1-oct18/shots/` (key evidence in `shots/evidence/`, numbered to match the problems below). qa_play output: `runs/b1-ch1-oct18/qa/`.

**Verdict:** no blockers. The engine is solid: every line plays, every voice plays, there are no hard cuts, and the text box behaves through every CG change, including under fast tapping. What's left is staging and art-versus-text: one empty set the text calls "chaos," a few expressions that contradict their line, a sprite that doesn't leave when the text says she does, a speaker-dimming feature that never renders, and two dream voice lines that need a listen on the iPad. 16 problems, most of them small.

---

## Problems (most important first)

### 1. The entrance hall is empty while the text calls it "chaos" (art vs. text)
- **Where:** c1_entrance, from c1_0099 ("The entrance hall is chaos. Two hundred students trying to read six sheets of paper at once.") through c1_0127 ("I squeeze toward the board… Nanoha has already slipped through somewhere at elbow height"). Any size and tap speed. `evidence/01_…`
- **What:** `bg_school_entrance` shows a spotless, empty hall with no students anywhere. The scene's first line and its whole squeeze-through-the-crowd gag rest on a crowd, and it's the first thing he sees on arriving at school. The Oct 17 cold reads flagged exactly this kind of mismatch.
- **Fix:** one edit pass on the background adding a crowd at the shoe lockers and notice board (blurred or silhouetted figures are fine), ideally kept inside the iPad crop (the middle 80% of the width). Otherwise ask the Story thread to soften the line.

### 2. c1_0230: the narration describes a different, smaller smile, but the sprite shows her standard smile
- **Where:** c1_interlude, c1_0229 → c1_0230 ("She just smiled, and it was a different smile from the one she'd used in front of the class. Smaller. It looked like it cost her something."). iPad, normal tap. `evidence/02_…`
- **What:** Natsuki is still on `natsuki_school_smile`, the same open smile she wears for most of the chapter. `wistful` only arrives on the next line (c1_0231).
- **Fix:** put `@show natsuki school_wistful` before c1_0230, or give c1_0229 `natsuki<wistful>`.

### 3. c1_0159: Natsuki stays front and centre after the text says she has gone past him to the seat behind
- **Where:** c1_intro, c1_0159 ("And then she's past me, settling into the seat at my back…"). Any size. `evidence/03_…`
- **What:** her sprite stays on until the `@hide` after c1_0159, so the line plays with her still facing him.
- **Fix:** move `@hide natsuki` to before c1_0159.

### 4. c1_0114: Rika has the shocked face on her confident line
- **Where:** c1_entrance, c1_0114 `rika<surprised>`: "Tail first! You save the best part for last! Everybody knows that!" iPad, normal tap. `evidence/04_…`
- **What:** the wide-eyed shock sprite belongs to the realization two lines later, c1_0116 ("…Oh no."). On c1_0114 she's certain of herself.
- **Fix:** use `grin` on c1_0114 (or `pout`, which exists and isn't used anywhere in Ch1) and keep `surprised` for c1_0116.

### 5. The two dream lines are about 6 dB under the rest (needs a listen on the iPad)
- **Where:** c1_dream, p_0007 "You're late." (−5.9 dB from the median) and p_0010 "Hurt again. Give me your hand… Hold still." (−6.6 dB). Any size.
- **What:** `voice_levels.py` flags only these two (159 lines, median speech level −20.4 dB, range −27.0 to −20.0). §9 step 5 already records the flag, and whether it's intended softness has to be judged by ear, which this harness can't do. They play over `memory`, which is itself about 2 dB quieter than `daily`, and the music ducks to 55% under voices, so they may be fine.
- **Fix:** check on the iPad at normal volume. If they're hard to catch, raise them about 3–4 dB in `voice_pack.py` and keep the dream echo.

### 6. Kitchen: the "whiteboard on the fridge" the narration reads from isn't on screen, and a man's gray jacket is
- **Where:** c1_morning, c1_0007–c1_0009 ("reading the whiteboard on the fridge… All of it in my handwriting… still says 'Garbage: burnables, Mon/Thu' in Dad's"). iPad 1180×820. `evidence/06_…` (the red box is what the iPad shows).
- **What:** `bg_fujisawa_kitchen` has a printed wall calendar on the right-hand wall, not a handwritten whiteboard on the fridge. On iPad both the fridge (far left) and the calendar (far right) fall outside the crop; they only appear on phones and wide desktop windows. A gray men's suit jacket hangs over a chair in the middle of the iPad view. With "Dad's" handwriting and "He wrote it last spring" right beside it, the reader may wonder whether Dad still lives there.
- **Fix:** if the board matters (three lines point at it), edit in a whiteboard on the fridge with the fridge moved inside the iPad crop. Then decide whether the jacket is a deliberate Dad prop; if not, remove it or make it Kōhei's navy blazer.

### 7. Speaker dimming is coded but never renders in any day scene
- **Where:** every multi-character shot in Ch1 (kitchen, entrance, lunch). For example c1_0027 at iPad: Akane has class `dim`, but her computed `filter` is `none`. `evidence/07_…`
- **What:** `.spr.dim{filter:var(--bgf,) brightness(.78) saturate(.9)}`, and `setBg` sets `--bgf` to `none` on day backgrounds. The result, `none brightness(.78) saturate(.9)`, is an invalid filter, so it's dropped. Dimming would only work on night and evening plates, and Ch1 has nobody else on stage there. The author has never seen dimming, so this is latent rather than a visible regression.
- **Fix:** decide whether you want non-speaker dimming at all. If yes, in `setBg` use `BG_LIGHT[name]||''` (an empty value removes the property, so `.spr` falls back to `none` and `.dim` becomes valid), then look at a two-shot on the iPad, because it changes the look of every multi-character scene. If no, delete `dimFor` and the `.dim` rule.

### 8. The night tint is too light, so Nanoha looks lit for daytime
- **Where:** c1_night, c1_0237–c1_0256. iPad. `evidence/08_…`
- **What:** the sprite gets `brightness(.8) saturate(.82) hue-rotate(-6deg)` against a deep-blue night plate. Her white shirt and face stay close to daylight values, so she reads as pasted onto the street. The evening tint on the interlude works fine.
- **Fix (taste):** try about `brightness(.66) saturate(.75)` with a slightly stronger blue shift for both night plates, and compare on the iPad.

### 9. The three wake-up lines play over a full pure-white screen
- **Where:** c1_dream, p_0012–p_0014, until `@bg black slow`. Any size. `evidence/09_…`
- **What:** `@flash white` compiles to `bg white` plus the flash, so after the dream CG cuts to white the screen stays solid white behind the dark box for three taps. That's harsh on an iPad read at night. It may be intended ("I wake up").
- **Fix (taste):** if you only wanted a flash, follow it with `@bg black slow`, or fade to Kōhei's room, before p_0012.

### 10. Fast tapping skips the falter's silent beat and cuts the falter short
- **Where:** c1_intro, c1_0146 ("Then they get to me.") → `@bgm -`, `@wait 0.8`, falter CG → c1_0147 → back to the intro CG at c1_0148. iPad, tapping about every 0.1–0.3 s.
- **What:** a tap skips the 0.8 s silence where the music drops out, and a tap during the falter crossfade sends it back before it finishes (it peaked at 81% opacity in my run). It fades back without a cut, so this isn't a bug, but the chapter's key beat is the one a quick reader loses. The cold open already protects its timing with `@hold`.
- **Fix:** wrap `@wait 0.8` and the falter `@cg` in `@hold on` / `@hold off`, or at least the wait.

### 11. Small phones: long narration covers the characters' faces
- **Where:** c1_0038 (the cupboard and latch paragraph, 5 lines) at 667×375, and other long narration. `evidence/11_…`
- **What:** the box grows to 197 of 375 px (53% of the screen) and covers both girls' faces in the kitchen two-shot. At 844×390 it's 169 px (43%), and faces stay visible. Text never overflows, and the controls never collide with it.
- **Fix (low priority; phones are secondary):** shrink the type on short viewports (e.g. `@media (max-height:400px)` with about 15px text and line-height 1.5), or accept it.

### 12. Ōno-sensei: hair clipped at the top of the screen, and he reads younger than his 40s
- **Where:** c1_intro, c1_0135–c1_0137, every size. `evidence/12_…`
- **What:** the engine puts a 5′9″ head top at 95% of stage height. At 6′0″ (§1b) Ōno's head top lands at 100.9%, so his hair tips are cut off by the top edge (about 7 px at iPad). Separately, the sprite looks late 20s to early 30s, not "40s, droopy and tired" (§2). That belongs to the on-model check, but it shows here first.
- **Fix:** let tall characters fit, e.g. cap `top` at 98% of stage height or set the 95% anchor from the tallest character on stage. Age him up with grayer temples and deeper lines in an expression-edit pass.

### 13. c1_0024: Akane's puffed-cheek pout on her one quiet, sincere line
- **Where:** c1_morning, c1_0024 `akane<pout>`: "…You always are." (narration: "She says it to the rice cooker, not to me."). iPad. `evidence/13_…`
- **What:** the comic pout (cheek puffed) undercuts the quiet line under the teasing (§3b: "a quiet sincere line under the teasing").
- **Fix:** use `smile`. Better, generate a soft, downcast Akane expression (about one expression edit) for her sincere beats.

### 14. No visual cue for the jump to lunch
- **Where:** c1_intro → c1_lunch (c1_0160 → c1_0162). Any size.
- **What:** both scenes use `bg_classroom_day`, so the scene change crossfades the image into itself and nothing marks the time skip except the words "By lunch".
- **Fix (optional):** a short fade through black (`@bg black` then `@bg bg_classroom_day`), or a lunch variant of the classroom with bags and lunch boxes on the desks.

### 15. The name tag says "Ryōsuke", but everything else in Ch1 says "Tokiwa"
- **Where:** c1_entrance, c1_0108 onward.
- **What:** per §3c, narration and dialogue call him "Tokiwa", and his given name is never spoken in Ch1, so a first-time reader has to infer that the "Ryōsuke" tag is Tokiwa. This is a Story thread call, not a build bug.
- **Fix:** tag him "Tokiwa" (as the narration does), or have one line give his full name.

### 16. Props in the text that the sprites can't show
- **Where:** c1_0187 ("her lunch held in front of her in both hands") and c1_0236 ("her school bag over her shoulder"). iPad.
- **What:** neither sprite has the prop. These are minor, and they're the kind of art-versus-text mismatch cold readers notice.
- **Fix:** probably accept. If you do a Nanoha expression pass anyway, a "holding bento" variant would also serve later lunch scenes.

**Note (not counted):** in `cg_natsuki_intro_falter` her eyes go off to the right of the frame, away from the window side where Kōhei sits, while the intro CG has her looking into the camera. It can read as her glancing away after seeing him, which works; if the falter should read as her looking *at* him, her eyes need to go to the camera. `evidence/note_falter_eyes_…`

---

## What I checked and found fine

**Automated run (qa_play.py, iPad 1180×820, `--every`):** 259 of 259 lines seen, none missed. No failed requests. All 159 voiced lines decode; of the 160 spoken lines, the one unvoiced line is c1_0222 "…", as intended. The only console error is Google Fonts being blocked by this sandbox's proxy (an environment issue, not the build). qa_play takes no frames during the wordless cold open, so I made timed captures for it (`evidence/cold_open_timed_ipad.png`).

**Source vs. build:** recompiling `ch01.ozs` with `compile_script.py` gives a `script.json` identical to `v2/script.json`. `voice/ja.json` matches the source Japanese line for line.

**Replays with real taps, iPad landscape:**
- *Normal speed* (waits for each voice to finish): all 259 lines.
- *Fast* (a tap every 0.11 s, 614 taps): all 259 lines.
- On every poll I checked four invariants:
  - the text box is up whenever a line is up;
  - sprites on screen match the engine's state;
  - the face window matches the §3a expectation for that line;
  - the CG images shown match the engine's state.
- **Zero violations in either run.**

**Transitions, measured frame by frame** (an in-page sampler recording the opacity of every layer, with a normal tap and with extra taps 0.1–1.6 s into each transition):
- **Background crossfades:** room→kitchen, kitchen→river, →entrance, →classroom, →lunch, →interlude (with its tint), →night, the slow cut to the lit plate, and the fade to black. All are fades.
- **Sprite fades:** sprite entrances, exits and moves (Akane's entrance, Nanoha's arrival, hide-all, the board, the lunch two-shot) are all fades.
- **CGs and endings:**
  - Bg→CG: collar, Natsuki intro, dream.
  - CG→bg: collar out, intro out.
  - CG→CG: falter, and back.
  - The dream's living still, the flash, and the end card.
  - All are fades. The only instant changes are the intended cold-open `@cg - cut` / `@bg black cut`, the flash to white, and the swap of the image underneath in CG→CG, which only happens after the top image is fully opaque, so it's invisible.
- **Text box:** stays up through CG→CG and CG→bg; hides only on bg→CG (1.1 s, intended) and on black or white.
- **Oct 17 regressions:**
  - The text box stays visible during CG changes.
  - CG orientation matches the sets: the river is on the left in both the collar CG and the river background, and the windows are on the left in the intro CG and the classroom.
  - A tap mid-fade back to the CG still underneath fades rather than cuts (tested with taps at 0.15 s and 0.35 s).

**Cold open:** the first time, taps are ignored (6 taps tested) and it plays through in about 17 s: mirror → hand → mist (living still) → mirror, cut to black, chapter card, date card. The second time, one tap skips to the chapter card. The mist and dream loops are seamless (first frame vs. last frame differ by a mean of 1.6–1.8 levels), and switching between still and video doesn't jump visibly (mean difference 3–6 levels). The mist loop barely moves (0.3% of pixels change), which is fine if a near-still is what you want.

**Face windows (§3a):**
- Kōhei has a window on all 44 of his spoken lines, each with an expression set, and none on narration.
- Others get one only when off-stage: Ōno during the intro CG (c1_0151, rule 2), and Nanoha as the interlude's POV (rule 3).
- None for Natsuki inside her own CG, and none for "???" in the dream (rule 4).
- Name-tag and dialogue colors match the §3a hue table.

**Sprite heights (measured, not eyeballed):** rendered head tops are 58.9 / 62.9 / 59.9 / 66.8 / 60.9 / 72.0 in for Nanoha / Natsuki / Akane / Ryōsuke / Rika / Ōno, against the §1b lineup's 59 / 63 / 60 / 67 / 61 / 72. Everyone stands on one floor. Akane standing 1″ taller than Nanoha in the kitchen is correct per §1b (5′0″ vs. 4′11″).

**Other staging:**
- Positions never overlap faces at iPad, 844×390 or 1440×789.
- The evening tint (interlude) and night tints are applied (computed filters verified).
- Kōhei's face expressions fit their lines throughout.
- The intro→falter change in Natsuki's face is clearly visible.
- The lit-window plate's glow in the gap is subtle but visible (about 2% of the image, inside the iPad crop).

**Voices:**
- **Levels:** `voice_levels.py` runs. No clipping, no clip under 0.25 s, none mostly silent; the only flags are #5.
- **Playback:** in the engine, every one of the 159 voiced lines starts and produces output, measured on the voice bus.
- **Clip lengths:** plausible for their Japanese text. The fastest are c1_0046 (Akane) and c1_0088 (Nanoha's quiet "So you'd hear yourself say it."), worth half an ear if you're listening anyway.

**Other sizes:**
- **Phone landscape** (844×390 at 3×, 667×375 at 2×) and **desktop Chrome** (1440×789): spot-checked the title, the menu and 20 scene starts or key lines.
- Layout holds, there's no text overflow, controls stay clear of the text, and the face window rising about 16 px above the box on phones looks intended. Small phones only have the box-height issue in #11.
- Portrait not tested (canon §2: landscape only).

**Menus:** Chapters → Chapter 1 starts at the cold open. Save and Load restore the exact line. Continue appears after play and resumes at the start of the scene (by design). The backlog lists the lines.

**Not checked here:** the snapshot diff (out of scope for this run), real Safari on the iPad, and anything by ear (the music loop seams and the dream lines' softness).
