# Build review: Pilot v2, Prologue + Ch1 (Oct 17 build), §9 steps 7 and 9

Reviewer: independent QA agent, no part in making the build. Nothing in ROOT was edited.
Build: `b0-ch1-oct17/v2/`, served on port 8160. Scope: the whole of Prologue + Ch1, first handover. There is no diff or snapshot for this run, so step 3 (changed frames) and the regression run were skipped as instructed. This is the first handover, not a fix round, so step 2 had no fixes to confirm.

**Verdict: not ready to hand over yet.** One engine bug (#1) can fill the stage with characters who aren't in the scene. Four transition and staging problems (#2–#5) are visible on a normal read. The rest are small.

Doc gap: this checkout's `story/style-guide.md` has no §3b–§3c (speech and address sheets) and no §9. I checked against §3, §3a and the README's Build and QA sections, and used the brief's step list for process.

---

## Problems, most important first

### 1. HIGH: Hidden sprites come back as "ghosts", and stale expressions stick, when taps outrun image loading
- **What you see:** characters who left earlier scenes stay on stage for the rest of the chapter, and the right character shows the wrong face. In one run, at c1_0238 in the night scene (Nanoha alone, "Good. She noticed the squeaky stairs."), the stage showed Akane, Ryōsuke, Rika and Natsuki. Nanoha had the wrong face (deadpan instead of happy) and was half hidden behind Ryōsuke. See `shots/01_ghost_sprites_night_c1_0238.png` and `shots/01_ghost_sprites_intro_c1_0134.png`. The intro shot shows the empty classroom before Natsuki arrives, with four ghosts.
- **Repro:** iPad 1180×820. From Begin, turn on **Skip**. Throttle the network to 3 Mbps with 150 ms latency, a slow iPad connection. Stop Skip at the first line of any scene and wait 6 s. In two runs out of two, the ghosts were still there 6 s after Skip stopped (`shots/ghost_skip_3mbps*/ghost.json`). At 20 Mbps with 60 ms latency there were no ghosts. But stopping at c1_0113 still showed Nanoha "surprised" and Rika "scheme" when the script wanted "happy" and "grin", still wrong 6 s later (`shots/ghost_skip_20mbps`). Tapping every 120 ms at 3 Mbps only showed one-line lags, which recovered: Natsuki late at c1_0153, Nanoha's previous face at c1_0222.
- **Cause:** in `showSpr()` (index.html line 528), the preloader's `pre.onload` always sets `el.src` and adds `on`. It doesn't check whether that character is still meant to be on stage, or whether a newer expression was asked for since. `hideSpr()`, `hideAll()` and a background change don't cancel pending loads. So a load that finishes late shows a hidden sprite again, and an older expression that arrives last replaces the newer one.
- **Fix:** keep a per-character "wanted" key. Set `el.dataset.want=url` in `showSpr`, and clear it in `hideSpr`. In `onload`, return unless `el.dataset.want===url && state.spr[who]`. Optionally preload each scene's sprites when the scene starts.

### 2. MEDIUM: `@flash white` doesn't flash. It slowly fades the dream CG to plain white and holds it for three lines
- **Repro:** Prologue, tap past p_0011 ("Hands that aren't mine…"), any size and speed. The CG dims slightly at about 150 ms, washes out to white by about 600 ms, and then p_0012–p_0014 play over pure white. `@bg black slow` then takes 0.6 s, not the slow 1.8 s. Frames are in `shots/freeze_ipad/F02_flash_*.png` and `shots/02_flash_white_600ms.png`.
- **Cause:** `compile_script.py` turns `@flash` into `{"t":"bg","name":"white","tr":"flash"}`. In the engine, `setBg('white')` returns before the `flash()` call at line 503, so the `#flash` keyframe never runs. The engine's own `case 'flash'` handler is never sent anything. The dream's living still is turned off as a side effect.
- **Fix:** make the compiler emit `{"t":"flash"}`. If a held white screen really is wanted after the flash, write it as an explicit `@bg white`. Either way, decide which one is intended. The script syntax promises a flash.

### 3. MEDIUM: Every background crossfade dips about 25% toward black halfway through
- **Measured** (mean brightness of the stage above the text box, exact freeze-frames, iPad): room→kitchen 150 → **115** → 167. Kitchen→river 167 → **128** → 184. Entrance→classroom 171 → **133** → 162. Classroom day→evening 161 → **108** → 122. Night→lit (slow): 62 → **46** → 65. The "her upstairs light comes on" beat (c1_0256 → c1_0257) darkens the whole street by a quarter before the window glows. See `shots/03_night_lit_dip_450ms.png` and `shots/freeze_ipad/F04_*, F08_*, F12_*, F18_*, F19_*, F20_*`.
- **Repro:** any `@bg` change at normal speed. It is most visible at c1_0006 (room to kitchen) and c1_0257 (night to lit).
- **Cause:** `setBg()` fades the old image out while it fades the new one in. Halfway, both are partly see-through, and the black `#bgSolid` shows through.
- **Fix:** keep the outgoing image at full opacity underneath, fade only the incoming image in on top, and then drop the old one.
- **Related edge case:** `restore()` never resets `#bgSolid`. If you load a Ch1 save from the white part of the prologue, the backdrop stays white. Every crossfade then flashes brighter instead (room to kitchen measured 150 → 178; night to lit 62 → 109, in `shots/freeze_ipad_whitebackdrop`). Reset `#bgSolid` to black in `restore()`.

### 4. MEDIUM: The CG-to-classroom hard cut shows an empty room, then Natsuki fades back in
- **Repro:** c1_intro, tap past c1_0145 ("I do kendo…"), any size and speed. Frame 0 is the empty classroom, and Natsuki's sprite fades in over 0.35 s. She vanishes, then comes back. See `shots/04_cg_cut_empty_classroom_0ms.png` and `shots/freeze_ipad/F14_*`.
- **Cause:** the script runs `@cg - cut` before `@show natsuki school_grin c`, and the sprite only starts fading in after its image load event.
- **Fix:** swap the two lines so the sprite is already on stage under the CG. Then use `@cg - fade`, or a short dissolve, so the CG resolves onto her.

### 5. MEDIUM: Dimming of characters who aren't speaking works only in the interlude
- **Repro:** compare lunch c1_0185 (Nanoha speaks, Natsuki on stage) with interlude c1_0205 (Nanoha speaks, Natsuki on stage), iPad. Natsuki has the `dim` class in both, but her computed filter is `none` at lunch, and she is visibly darkened in the interlude (`shots/05_lunch_interlude_dim_compare.jpg`). The same happens in the morning (Akane at c1_0027) and at the entrance.
- **Cause:** `.spr.dim{filter:var(--bgf,) brightness(.78) saturate(.9)}`. On day backgrounds `--bgf` is `none`, which makes the filter `none brightness(…)`. That value is invalid, so it is dropped.
- **Fix:** use an identity filter such as `brightness(1)` instead of `'none'` in `setBg`. Or remove dimming everywhere if it isn't wanted (§3a doesn't call for it).

### 6. MEDIUM-LOW: The two dream voice lines are about 6 dB quieter than every other line
- `voice_levels.py` flags p_0007 ("You're late.") at −26.5 dB and p_0010 ("Hurt again…") at −26.8 dB, against a median of −20.4 dB. Integrated loudness is −26.5 and −27.4 LUFS, against −20.7 to −24 LUFS for ordinary lines. These are the first voices the reader hears, and they play over the ducked `memory` track.
- **Repro:** Prologue, at default volumes, any size.
- **Fix:** re-level after the dream echo in `voice_pack.py`. Or, if a softer dream voice is intended, make it a documented exception of about −2 to −3 dB.

### 7. LOW-MEDIUM: Akane's "sleepy" sprite isn't sleepy
- **Repro:** c1_0011 "Morning, Onii-chan…" followed by narration c1_0012 "eyes still at half-mast". `akane_school_sleepy` has wide-open eyes and an open "O" mouth, so it reads as surprised (`shots/07_akane_expressions.jpg`).
- **Fix:** redo the expression edit with half-closed eyes, a yawn, or a hand at her eye.

### 8. LOW: A quick second tap skips the hold after a CG appears, so the text describing the CG starts before the CG is visible
- **Repro:** iPad. Tap past c1_0137 ("The door opens."), then tap again within about 0.3 s. "She walks to the front of a room…" starts typing over the empty classroom while Natsuki's CG is only about 5% visible (`shots/10_quicktap_cg_natsuki.png`). Doing the same at p_0002 puts the dream text over black (`shots/fast_cg_dream.png`). The fade still finishes behind the text, so this isn't a hard cut.
- **Fix:** ignore taps for about 0.6 s after a CG starts, like the 450 ms guard on cards. Or have the tap snap the CG to full opacity.

### 9. LOW: Music loops have hard seams, and `natsuki.mp3` probably clicks on every loop
- `playBgm()` uses `source.loop=true`. The crossfading looper `bgmIter()` described in the code comment is never called. At the loop point, `natsuki.mp3` jumps by 0.095 (full scale), bigger than any sample-to-sample step inside the track (maximum 0.084). That is probably an audible click every 74.8 s, which you'd hear if you linger in c1_intro or c1_lunch. `nanoha.mp3` is borderline at 1.3× its 99.9th-percentile step.
- **For the Audio thread:** `night` is a 34 s loop, `daily` and `memory` 51.8 s, against §7's finishing rule of 2–3 minutes. `natsuki` measures −17.1 LUFS against the −19 target.
- **Fix:** call `bgmIter()`, which already exists, or re-cut the seams at zero crossings.

### 10. LOW: Two art details differ from the design sheet and the text
- **Akane's skirt:** §2 says "navy pleated skirt below the knee". The sprite's skirt ends mid-thigh (`shots/08_full_sprites.jpg`). The text box mostly hides it in play. It is still off-spec for the 14-year-old under the modesty rule.
- **Rika's frog clip:** it has no crown. Narration c1_0104 says "a small frog wearing a crown. The frog is new.", and §2 lists "frog with a crown".

### 11. LOW: The scene change from c1_intro to c1_lunch has no visible change
- **Repro:** tap past c1_0160. The classroom crossfades into the same classroom, with a pointless brightness dip (see #3), and only the music changes before "By lunch…".
- **Fix:** add a quick fade through black or a time card.

### 12. LOW: Starting Chapter 1 from the Chapters menu skips the "CHAPTER 1 / The House Next Door" card
- **Cause:** `CHAPTERS[1].start` is `c1_morning`, the scene marker, which comes after the `@chapter 1` command.
- **Fix:** start at the chapter command instead.

### 13. LOW (QA tooling): `qa_play.py` skips lines without saying so
- It saw 259 of 272 lines, and it skipped a different 13 lines on each run (this run: c1_0015, c1_0036, c1_0042, c1_0072, c1_0091, c1_0110, c1_0116, c1_0136, c1_0148, c1_0165, c1_0183, c1_0209, c1_0225).
- **Cause:** when it sees `typing:true` it calls `advance()`. If typing finished in between, that call moves on to the next line. The report has no total to compare `lines_seen` against.
- **Fix:** finish typing and check inside the same `evaluate` call, and fail when `lines_seen` doesn't equal the number of spoken and narration lines. Also, its voice check only decodes the clips; it doesn't play them. I checked playback separately; see below.

### 14. LOW: Staging nits
- c1_0030 to c1_0044: Akane holds her closed-eye laugh ("happy") for about 12 lines while others talk. Reset her to smile after c1_0030.
- c1_0127: Ryōsuke and Rika leave the stage just before the narration "While they argue…". Hide them after that line.
- Rika's V-sign pose is part of every expression, including "surprised" (c1_0113, c1_0126). Acceptable, but odd.

### Worth listening to (unconfirmed, not counted)
- Kōhei c1_0083 ("Club doesn't start until Wednesday") and c1_0244 ("She seems fine.") have pitch tracks reaching 200–240 Hz, against his median of 129 Hz. That may just be expressive delivery, but listen for bleed.
- Natsuki c1_0148 "Please take care of me." (よろしくお願いします。) is 1.16 s: 8.6 characters/s against her median of 4.6. That is brisk for the subdued beat after her grin stutters.

---

## What I checked and found fine
- **Build matches source:** recompiling `ch01.ozs` gives a `script.json` identical to the shipped one (454 commands). `ja.json` matches the voice job list. The voice-pack index is contiguous, with no gaps or overlaps across the 8 packs.
- **qa_play report** (`runs/b0-ch1-oct17/qa/report.json`, iPad 1180×820, `--every`): no page errors and no failed requests. `voice_missing` is empty, and 169 of 170 spoken lines are voiced. The unvoiced one, c1_0221 "…", is marked `-` on purpose. The single console error is the Google Fonts stylesheet, which this sandbox's proxy blocks; that is the environment, not the build.
- **Voice playback:** I jumped to every voiced line in the browser. All 169 start playing, and 166 produced measurable signal while I sampled. The other three are short clips (c1_0091 0.33 s, c1_0255 0.51 s, c1_0153 with a mid-line pause) that I checked offline. Apart from #6, all levels are within ±3 dB of the median. No clipping, no clips that are too short, none that are mostly silence. Of the voice-level tool's flags, only the 2 dream lines in #6 remain.
- **Face windows (§3a):** Kōhei has a window on every spoken line, with the scripted expression. Every face file used exists. There is no window for Ōno-sensei, for "???", or for Natsuki while her own CG is showing. Ch1 has no other offstage speakers.
- **Name tags and tints** match the §3a hues. Narration is neutral. The tsuka and shodan glosses render small and pale, and plain text in the backlog.
- **Sprite heights:** head-top differences measure 8.0 in (Ryōsuke to Nanoha) and 6.4 in (Ryōsuke to Rika), against 8 in and 6 in expected from the §1b heights. Heads are drawn at the same scale.
- **Night and evening tints:** Nanoha is tinted in c1_night and the sprites are warm in the interlude. The interlude label and vignette show.
- **Living stills:** the first frame of each video matches its still (mean difference about 4/255, only at edges), and the first and last frames match. H.264 plays in Chromium, and the crop matches the still.
- **Text box during CG changes:** it hides as a CG starts, returns after the hold, and stays up when a CG is removed. There is no z-order problem; the box was never hidden behind a CG.
- **Cards:** the chapter, date and end cards show, and the 450 ms tap guard on cards works.
- **Tapping:** at normal speed, no sprite mismatches remained after loads settled. At fast speed (120 ms) on a 3 Mbps connection, only the one-line lags noted in #1.
- **Phone landscape (844×390, 667×375) and desktop Chrome (1440×900, 1920×1080):** scene starts and sample lines. No horizontal overflow, text never overflows the box, and the face window and name tag sit correctly. The longest narration line (c1_0203) fills about 60% of the screen height on a 667×375 phone; that is heavy but readable.
- **Expressions match the lines** across all scenes, except #7 and #14.

## Not checked, or limited
- Portrait was not tested, per the brief. Auto mode was not tested. From reading the code, if a scene's voice pack hasn't loaded yet, Auto can advance on its text timer before the voice starts.
- Real iPad Safari was not available. Everything ran in Chromium, with network throttling standing in for a slow connection.
- Environment issues: the first `qa_play` run crashed when the sandbox ran out of memory, and the second was spoiled when my local server stopped partway through. The third run is clean and is the report cited above.

## Files
- Report: `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score2/runs/b0-ch1-oct17/build.md`
- qa_play report and 261 screenshots: `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score2/runs/b0-ch1-oct17/qa/`
- Evidence: `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score2/runs/b0-ch1-oct17/shots/`. Key frames have numbered names matching the problems above. `freeze_ipad/` holds exact transition freeze-frames, `ghost_skip_*` the Skip ghost runs, and `spot/` the phone and desktop checks.
- Probe scripts I wrote: `/tmp/claude-0/-home-claude/8a181b96-a746-50e6-b79a-45dd7696162d/scratchpad/score2/runs/b0-ch1-oct17/work/` (`freeze.py`, `ghost.py`, `probe_voice.py`, `spot.py`).
