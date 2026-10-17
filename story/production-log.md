# Ōzakura — Production Log

Current state, decisions, budget, open issues and what's next. Update it at the end of every thread. Rebuilt 2026-10-05; updated 2026-10-10.

---

## 0. Doc map (reorganized Oct 8)
| Doc | Role |
|---|---|
| `ozakura/canon.md` | **The single living story bible.** Edit it in place when the author decides something. |
| `ozakura/pilot-notes.md` | The shipped pilot: what it invented ([P]), the agreed fix list, and pending approvals |
| `ozakura/style-guide.md` | Visual designs, references, art, lettering and voice pipelines |
| `ozakura/production-log.md` | This log: the dated decision record, budget, issues, next steps |
| `ozakura/source/story-bible-current.md` | **Archived** Oct 1 snapshot of the author's bible. Superseded by canon.md; don't use it for current canon |
| `ozakura/source/manga-pilot-handoff-brief.md` | The author's brief for an 8-page color manga test |

The old working bible (`ozakura/story-bible.md`) was retired Oct 8. Its contents now live in canon.md and pilot-notes.md.

**Since Oct 10 the four living docs are also in the public repo under `story/`, with git history.** Edit them there, commit, then upload to the Project (the repo's `CLAUDE.md` has the steps).

## 1. What exists
| Deliverable | Where | Status |
|---|---|---|
| **VN pilot**: Prologue plus Ch1–3, about 9,450 words, 22 scenes | Play: https://thefirstmccabe.github.io/ozakura/. Source: github.com/thefirstmccabe/ozakura (`index.html`, `script.json`). Private artifact copy: "Ōzakura" | Shipped 10-04. **Under revision hold** (see §6) |
| **Manga Vol. 1**: cover, Prologue plus Ch1–2, 48 pages | Reader: artifact "Ōzakura Volume 1." PDF: `manga/ozakura_vol1.pdf`. Pages: `manga/p/` | Shipped 10-05. Under the same hold |
| **Developer mode (VN)** | `…/ozakura/#dev`, or tap 大桜 five times on the title screen | Shipped |
| **Redesign refs** | `production/refs/akane-v2/`, `production/refs/natsuki-v2/` | Added 10-06 |

**Asset counts:**
- 72 sprites, 16 backgrounds and 9 CGs.
- 8 music tracks and 4 SFX.
- 423 Japanese voice lines in 51 per-scene files.

## 2. Decision log
| Date | Decision |
|---|---|
| 10-03 | VN over manga for the pilot. A custom HTML engine for iPad Safari. Commercial use is not a goal. |
| 10-03 | POV: Kōhei in first person with third-person interludes. A linear kinetic novel. |
| 10-03 | Claude invents missing cast and places and flags them as provisional. |
| 10-03 | Pilot scope: Natsuki's first week, 3 chapters. |
| 10-03 | Japanese voices, English text. |
| 10-04 | Hosting on GitHub Pages from a public repo. |
| 10-04 | Developer mode: fully unlocked scene chart. |
| 10-05 | Manga test: B&W with screentone, NB Pro 2K, lettered in code, right to left, B6. The reader defaults to single page. |
| 10-05 | Project organization: standing docs plus Planning, Story/Bible, and per-deliverable Production threads. |
| 10-05 | Storage: text canon in the Project; all files in the repo. |
| 10-05 | Natsuki 5′3″ with shoulder-length hair; Kōhei about 5′9″ with dark-brown hair; charcoal plaid skirt. |
| 10-05 | **Hold on revising the shipped VN and manga** while the process is re-examined. |
| 10-06 | **Project working hours:** no Ōzakura work on weekdays 9–5, and nothing after 8 pm any day (America/New_York). |
| 10-06 | **Kendo is setting and practice, not a sports manga.** Competitions are rare; no tournament arcs. |
| 10-06 | Proposal: Kōhei's solo practice (dawn suburi at the tree); a real old blade among the heirlooms. |
| 10-06 | **Full-year calendar:** late-August street fight and kiss; October dating; New Year bloom and memories; early-January past-life disclosure; mid-Jan to late Feb/early Mar deaths and battle; ends Mar–Apr. The bloom is tied to the start of the Beast phase. |
| 10-06 | **Natsuki asks to be the one to tell Nanoha** about the kiss, and does within about a week. Kōhei owns his half, and Nanoha dates him knowing. The winter disclosure covers the past life only. |
| 10-06 | **Nanoha senses the past-life connection**, independent of the kiss. |
| 10-06 | Parked: total length (a ~40-chapter spine plus an expandable layer was proposed) and reader-ahead past-life interludes. |
| 10-06 | **Akane redesigned:** cute, frail, sweet and playful; "Onii-chan"; lavender-silver hair (option A); sailor uniform on school days; cute outfits; a plushie-filled room. |
| 10-06 | **Hair color is a medium convention,** never commented on in-world. |
| 10-06 | **Natsuki restyled:** more feminine and self-assured, still shoulder-length. The school image locks the direction. Her appeal comes through personality and styling, never figure-focused design (Claude's boundary for the school-age cast). |
| 10-06 | **Houses about three feet apart, no alley** (the Muv-Luv Extra model). The art fix needs a layout-sketch method. |
| 10-06 | **Pilot critique accepted:** scale back the Ch3 flash, thin out the week-one supernatural beats, pull back Nanoha's near-confession, warm up Kōhei, casual sparring, hide the invented kanji, fix the calendar line. |
| 10-07 | **Past life rewritten:** Kōhei a rōnin, Natsuki an ordinary woman in a traditional role from a modestly propertied family; an arranged marriage for her father's heir; deeply in love; a misty morning walk; a long fight lost to attrition, so he deliberately takes a fatal wound to kill the beast; she helpless; they never sparred. |
| 10-07 | **Consequences:** her kendo means she isn't helpless now; recognition in sparring is one-sided (she watched him train). In the climax, Kōhei's old instinct pulls him toward the same opening without his choosing it, and Natsuki recognizes it and stops it. |
| 10-07 | **Past-life costume:** a real kimono, simple and not elaborate. |
| 10-07 | Working: about 40% of chapters for the April–August romcom first half. |
| 10-07 | Voices: Nanoha and Akane sound like much older women. The author will pick from audition sheets. Kōhei and Natsuki are fine. |
| 10-07 | **Rival redesigned:** technically perfect kendo versus Kōhei's instinctive, "incorrect" but equal swordsmanship. Clashing temperaments, not a bad guy, never mocks the missed practices. **Keep both the Rival and the best friend.** Proposal: the battle needs both styles. |
| 10-07 | **Scene bank:** the umbrella scene (both girls secretly have umbrellas; Natsuki soaks herself). |
| 10-07 | **The girls' pact:** they recognize they're both into him, talk about it and agree to compete fairly. The kiss breaks it. |
| 10-07 | Writing note: show more, tell less. |
| 10-08 | **Kiss-scene song wanted.** The title is unverified, and the rights need permission for the public build. |
| 10-08 | **Docs consolidated** (see §0). |
| 10-08 | **What the reunion is for:** Natsuki finds him, saves him and lets him go; the payoff is rescue and closure, not the romance. She chooses not to be loved because of a past life. The January comparison becomes shared grieving. Kōhei and Nanoha must win as this life's love story on their own merits. Proposals: the two-half promise ("I'll find you" / "Live"); a farewell to the past selves at the tree. Canon §5. |
| 10-08 (eve) | **Author playthrough feedback, Prologue–Ch3, now complete** (part of it given in the original VN production thread by mistake; full detail in pilot-notes §1b, fixes 20–31). |
| 10-08 (eve) | **Writing rules:** in openings, a fact goes in only if the scene shows it happening (backstory saved for real scenes); no telegraphic name-tag intros or trait lists, complete sentences by default; no manga self-reference (characters never compare their situation to manga; Kōhei reading manga is fine). Now in canon §1. |
| 10-08 (eve) | **Week-one strangeness made subtler:** Ch1 keeps the prologue dream and only a physical reaction at Natsuki's intro; the dream's return at the end of Ch1 is cut; Kōhei's flash at the catch and the explanatory narration around it are cut; the catch and tear stay; the fairy gets one mention in week one. |
| 10-08 (eve) | **The wrist strap = binding a cut on his wrist** after he comes back late and hurt from training ("You're late"). Echoes the August wound care. Now in canon §5. |
| 10-08 (eve) | **The kendo captain (Kirishima) becomes male.** Canon §8 updated. |
| 10-08 (eve) | **Speaker portraits:** a face window beside the dialogue, Baldr Sky style, cropped from the sprites. |
| 10-08 (eve) | **Approved as is:** Emi's look and voice; Takatsuki's look and voice; Yuzu's look and dialogue. Music mostly liked; the `kendo` track (scene 3.4, also Ch2 dojo) is disliked; music notes will come chapter by chapter. |
| 10-08 (eve) | **Ch2 proposals P1–P5 approved** (pilot-notes §1b). |
| 10-08 (eve) | **Yuzu's introduction moves to around May–June**, near the girls' pact. Ch3's shift scene keeps the manager and the job and drops her. |
| 10-08 (eve) | **Window-scene bug (3.3):** Nanoha appears in Kōhei's room. Redraw it Muv-Luv style, viewed from his room into her window; folded into the house fix. Tea at the shrine (3.6) and lunch at the Tachibanas' (3.7) are fine. |
| 10-08 (eve) | **Plan before the revision pass:** lock the character designs → finalize the voices → map the first chapters. |
| 10-10 | **Story docs go in the public repo** (`story/`) for version history. The author is fine with the story being public. The repo stays public, and GitHub Pages keeps serving the pilot. |
| 10-10 | Format details (insert style, presentation, the jigeiko test) restored to §6 after the Oct 8 rewrite dropped them. |
| 10-10 | **Manga inserts are full color** in the VN art style; no B&W. Sprites and backgrounds serve directly as references. Per-character color swatches added to the design lock. Proposal: a distinct past-life treatment within color. Canon §2. |
| 10-10 | **Anime cutscenes (Working):** the author is willing to pay for short animated cutscenes at a few pivotal moments. Which moments and the method are Open; a test clip is proposed (§6). Canon §2. |
| 10-10 | **Family spine:** the family putting itself back together after Dad's death is a main arc. A September flashback to Dad's death (the hospital request, his private request to Nanoha's father, the bills scene). Dad's regret is revealed through Nanoha's father, who apologizes for not pressing his help. Mom's recovery starts when Emi confronts her and they cook the favorite dish; it stays partial, with setbacks, this year. Canon §1, §6. |
| 10-10 | **Face windows and dialogue colors locked** (style guide §3a). Kōhei gets a window on every spoken line; others only when their sprite isn't on screen. A ~10-expression face set is needed for Kōhei. Name tags in full color, dialogue in pale tints, narration neutral; test screen first. |
| 10-10 | **Rival arc mapped** (canon §8): the two halves of the sword. Friction (Apr–Jul) → he witnesses the fight and offers to go to the adviser *with* Kōhei so Kōhei can own up (Decided) → they learn from each other (Oct–Dec) → caught in the path distortion himself in January (accepted) → the anchor in the battle (Proposal). Akane's perceptiveness about the romance reconfirmed. |
| 10-10 | **The bloom in both eras:** in the present the beast is already active at a low level before the bloom (rumors, people lost, maybe injured, possibly one disappearance), and the bloom marks it ramping up. In the past there are rumors but no bloom; he goes armed and she teases him; after he kills the beast and they promise, the tree blooms, the distortion falls away, and there's the CG of her cradling him under falling blossoms. Proposals: they'd been circling the tree all along; the modern bloom triggers the memory flood. Canon §5, §6, §9. |
| 10-10 | **Cutscene test passed** ("not bad"; ~$1.36). **Three-tier video plan (Working):** living-still loops on many CGs, 5–10 s animated beats at emotional peaks, and a handful of full cutscenes plus an opening movie. Model chosen per shot. No video before the design lock. Canon §2; details in §6. |
| 10-10 | **Fairy timeline and function decided** (canon §8): visibility tracks the danger (a light Apr–Aug, plus small item displacements in Nanoha's room; a half-form in autumn; full and speaking at the bloom, recognizing Kōhei and Natsuki; visible to all Jan–Mar; a real goodbye to Nanoha at the end). Female (Working). Look and personality are proposals for the design step. |
| 10-10 | **The beast:** wolf-like, physical but mainly spiritual, leaves no corpse. Folklore source is the okuri-ōkami (the escorting wolf). Canon §6. |
| 10-10 | **Design pass approved, cap $10.** |
| 10-10 | **Design pass delivered for approval** (style guide §1a): shorter-haired Kōhei plus a 10-face set, teen-proportioned Akane, Natsuki's casual outfits, a masculine Kirishima, the fairy at scale, and the beast at big-dog size with a size reference. Draft color swatches. |
| 10-10 | **Design lock: all humans approved** (Kōhei and his face set, Akane, Natsuki's casual outfits, the male Kirishima). Beast scale approved; the author wants it slightly more ethereal and multicolored. Next: complete the visual inventory before voices, planning for more animation (three-tier video plan). |
| 10-10 | **Visual inventory phase approved, cap $20:** new characters (families, adviser, past life, one-scene antagonists), a supporting-cast check, a cast scale lineup, seasonal outfits, the fairy's season forms, turnarounds for the animation principals, and key locations (houses, shrine/tree in both eras, past village). Ordinary backgrounds and event CGs stay per chapter. |
| 10-10 | **Visual inventory delivered for review** (style guide §1b), all self-reviewed and fixed before delivery: scale lineups for the whole cast; families, school adults, past life and antagonists; full color for the supporting cast (grayscale drafts replaced); seasonal outfits and kendo armor; the fairy's four forms; the beast's ethereal tweak; turnarounds for eight animation principals; key locations (the houses about three feet apart and both window views, Nanoha's room, the tree in four seasons plus the New Year bloom, the past-era site, path and village). Boards: `production/refs/lineup/` and the review sheets sent in the Story thread. Supporting heights and a few picks are [P]. |
| 10-10 | **Inventory review (author):** everything approved except these changes, all made the same day: **no metric units anywhere** (docs, lineups, prompts); the beast a little taller (about 4′3″ to the ears, back at a man's belt); **Kazuo version B**; **the past-life death is in winter** (canon §5), so the past-era backgrounds are now winter; the tournament opponent has **bleached-blonde hair**; one of Kōhei's friend or rival gets a slightly unusual hair color for readability (Claude picked **Takatsuki: deep slate blue** [P]); the rōnin wears **two swords** (version B kept). Also [P]: the street-fight thug's hair changed from blonde to a black undercut so the opponent's blonde stays distinctive. Nanoha's skin reads too pale in some images: fix in the final sprite pass, no redo now. |
| 10-10 | **Kiss song: an original vocal song**, made for the scene in the feel of the author's reference. The rights question is dropped. Vocal language and lyrics Open. (Music thread.) |
| 10-10 | **Voice auditions widened:** audition every voice the author hasn't explicitly approved (approved: Kōhei, Natsuki, Emi, Takatsuki). 20 characters, 71 takes plus +2-semitone variants for Nanoha and Akane; audition page published. About $0.55. Waiting on picks. |
| 10-11 | **Voice picks, round one** (style guide §7 table): 16 characters cast, including Nanoha (Erinome +2) and Akane (Aoede +2). Rika, Yuzu, Sōta and the fairy sent back (not high enough); a callback page offers each take as recorded, +2 and +4 semitones. |
| 10-11 | **Voice cast complete:** Rika Laomedeia +4, Yuzu Autonoe +2, Sōta Leda +2, the fairy Leda +4. Every speaking character now has an approved voice (style guide §7). |
| 10-11 | **Shared-past flashbacks** for Kōhei and Nanoha (childhood and middle school, being there for each other) added to canon §6; six candidate scenes are proposals. **Next (from Oct 12): the chapter summary**, then back to music. Art to add later: child and middle-school versions of both. |
| 10-12 | **Accepted:** all six shared-past flashbacks. **Decided:** the night before the battle includes "I love you" and, in effect, a marriage proposal ("that's why we all have to live tomorrow"); Kōhei's illness comes from double shifts for Akane's birthday present; full-time or near-full-time work during school breaks; dueling lunches with Emi teasing Nanoha (canon scene bank 13c). |
| 10-12 | **Accepted Claude's staging:** the proposal is a promise for after graduation, no ring or a makeshift one, echoing the past life; Akane's birthday is around May; the dueling lunches start after the umbrella scene and run as a bit (he eats both, Ryōsuke and Rika keep score, Natsuki's cooking improves). |
| 10-12 | **Accepted:** hiding in Akane's room (canon scene bank 13d); the reverse (Kōhei hiding at Natsuki's) is not used. No separate rom-com brainstorm; go straight to the chapter map. **First chapter map drafted** (`chapter-map.md`, 40 chapters plus epilogue), awaiting review. |
| 10-12 | **Length decided:** 40-chapter spine; chapter length floats (~4,000–5,000 words), about 12–15 hours; slice-of-life added as needed. Cost isn't a concern for length. Minor characters stay light. |
| 10-12 | **The beach is cut;** a backyard watermelon day replaces it (canon 13e); the reassurance scene's setting is Open. **Kendo explainer:** Natsuki teaches Rika the rules in openly expository teacher mode (canon 13f; Ch2, pilot fix 32); kendo calls and terms shown in Japanese and English (style guide §5). Hours cutoff moved to 8:30 pm. |
| 10-13 | **Reassurance scene cut** (author's call for that scene only, not a general filter). **Wound care and kiss** as a *Fragrant Flower*-style close-up sequence with half- and full-page images; Natsuki's deleted text to Chie ("I wish it had been me he fought for" / "I wouldn't have run"). **Fairy appears** in the epilogue. Under discussion: making Nanoha's sibling a girl. Hours now weekdays 8–5 and after 8 pm off-limits. |
| 10-13 | **Kiss test (filter risk):** 6 images (NB Pro and NB2, the hug, she kisses him, he kisses her back; B&W shoujo homage and one soft-color version). **None refused.** Notes for production: specify modest clothes (one drifted to a camisole and short shorts); keep compositions on faces (one NB2 image added a panel framed on his lap); faces need tighter matching to the designs (Natsuki's hair came out long). Video models are a separate, still-untested risk. Files: `production/tests/kiss-oct13/`. About $0.85. **Style homages:** kiss sequence in a *Fragrant Flower* style (Decided); past-life beast fight in a *Vagabond* style (Working). |
| 10-13 | **Decided:** Nanoha's sibling becomes a little sister (same gremlin personality, a little more girly; Kōhei as Kazuo's "son I never had"); new name ([P] Mio), design and voice (Leda +2 still read as a boy). **The kiss-sequence text is from Kōhei.** **Era:** contemporary with smartphones, pre-generative-AI. |
| 10-13 | **Little sister's personality:** a blend of the gremlin and the tiny boss (Kōhei is her "retainer"). New designs and voice takes for that personality. Audition pages now go on the public site as plain web pages (the artifact player doesn't work for the author). |
| 10-13 | **Little sister's design locked: D** (bob with a side braid, star T-shirt, arms crossed). |
| 10-13 | **Little sister's voice: Kore, +4 semitones.** Cast complete again. |
| 10-13 | **Little sister's name: Mio** (approved). |
| 10-11 | **Pilot music review** (review page `production/music/review-oct11/`): keep `title`, `nanoha`, `night` (extend it); maybe `daily` (his wife likes it), `natsuki` (too generic and upbeat; possibly the Persona-style direction) and `memory`; replace `comedy` (feel of the Muv-Luv main theme) and `kendo`. Style guide §7. |
| 10-11 | **Music test round 1:** all three comedy takes rejected; Natsuki C and F (both ElevenLabs) and memory C (ElevenLabs, built on the current track) are maybes. **ElevenLabs only from now on.** Next directions: Natsuki in the feel of P4's "Heartbeat, Heartbreak"; memory as ethereal with twin lead guitars. |
| 10-11 | **Music plan approved** (style guide §7): piano-led house sound with strings; a color per story area; Steins;Gate's "Gate of Steiner" as the reference for sad cues and its electronic textures for strangeness and danger; no lyrics under voiced scenes; approved tracks as style references; one cue at a time, about $2 each. Lyria takes alongside ElevenLabs for now. |
| 10-11 | **Natsuki cue, take 1:** the ElevenLabs takes were his favorites but sounded too much like Nanoha's theme (the medium-strength `nanoha` reference). **Lyria dropped; ElevenLabs only.** Next: lighter or no reference and distinct lead instruments per character. |
| 10-11 (eve) | **Music approach paused and rethought.** The author doesn't want to spend weeks on music and will likely accept almost all of the original pilot tracks. Next: he works out in the Story thread exactly what the first few chapters need, then this Music thread finishes up (extend, loop, level, plus any must-have new cues). Hiring a human composer later stays an option. The Oct 11 music plan (style guide §7) and the test rounds are kept for reference, not in force. |
| 10-13 | **Pilot v2 music, must-haves only** (cue sheet `production/pilot-v2/music-cues.md`): a practice cue to replace `kendo`, settle Natsuki's theme, and a new childhood cue for the Ch4 flashback (must sound clearly different from `memory`). Then extend, loop and level `title`, `daily`, `nanoha`, `night`, `memory`. The author wants Natsuki and practice gotten right. **MiniMax is back on the approved generator list** (most kept tracks were made with it), alongside ElevenLabs. Listening page: `production/music/pilot-v2/`. |
| 10-13 | **Natsuki: all current options rejected** (the pilot track and the Oct 11 takes A, B, E, F). On hold until practice and childhood are settled. Practice and childhood takes generated (2 ElevenLabs + 2 MiniMax each) and posted on the pilot-v2 page. |
| 10-13 | **Natsuki from the author's own guitar:** he supplied a clip (0:10–0:49 used). 2 ElevenLabs takes with the clip as style reference, 3 Stable Audio takes transforming the clip itself; on the pilot-v2 page. The raw recording is kept out of the public repo. |
| 10-14 | **Music review:** childhood **A approved**. Practice round 1 all rejected; new direction from the author: a **tribal fight song, lots of percussion, no vocals** (4 new takes). Natsuki guitar takes A and B are maybes (B's drumstick count-in to be trimmed); 2 more ElevenLabs takes (G, H) made from his clip so he can pick a favorite of the four. Stable Audio takes rejected. |
| 10-14 (eve) | **Music picks:** **practice = F** (tribal percussion, `production/music/practice-v2/a/el2.mp3`; replaces `kendo`). **Natsuki = G** (built from the author's guitar clip, `production/music/natsuki-guitar/a/el-G.mp3`). Practice E is **saved as a future fight cue** for more intense scenes, not regular practice. With childhood A, all three pilot-v2 must-haves are settled. Next: extend, loop and level the eight pilot tracks (title, daily, nanoha, natsuki, practice, night, memory, childhood). |
| 10-14 (eve) | **Finished loops built** (`production/music/finished/`, script `production/pipeline/audio/make_loops.py`): eight pilot tracks plus `fight`, trimmed of fade-outs, crossfaded end-to-start (3 s, equal-power) and leveled to −19 LUFS; seam previews on the page. Shipped `audio/bgm/` untouched (revision hold). Short loops (night 34 s, daily and memory 52 s, title 63 s) still need real extension, which means paid generation. |
| 10-14 (eve) | **Extension attempt declined:** ElevenLabs' content checker refused all four extension jobs (night, daily, memory, title; each used the shipped track as an audio reference). No output, so nothing should be charged. Not retried or worked around; the author decides next steps. The seamless loops in `production/music/finished/` stand meanwhile. |
| 10-16 | **Pilot music closed.** The author keeps the four short loops as they are (night 34 s, daily 52 s, memory 52 s, title 63 s); no extension for the pilot. Claude's note: `night` is the one most worth extending later (it runs under the whole window talk). The eight finished loops in `production/music/finished/` are the pilot-v2 set; they go into the game in the revision pass. |
| 10-17 | **Kiss-scene theme, exploration** (for later, not the pilot): the author hummed a melody; 3 ElevenLabs arrangements built on it (violin and cello duet; violin with string orchestra; violin over nylon guitar), brief: violin-heavy, longing, bittersweet. A fourth (solo violin and piano) was declined by ElevenLabs' content checker and not retried. Page: `production/music/kiss-hum/`. The humming itself stays out of the public repo. Canon §2 still plans an original vocal song for the kiss; this instrumental may be its melody or a companion cue (author's call). |
| 10-17 | **Kiss theme: take B kept in mind for the kiss scene** (violin and cello duet from the author's humming, `production/music/kiss-hum/a/B-duet.mp3`). Not final; revisit when the late-August chapter is produced. |
| 10-12 | **Video tests 2, 10 s, locked designs** (`production/cutscene-test/oct12/`, ~$3.40). **Action (rōnin vs. beast):** Kling v3 Pro gives real choreography, with one spatial jump at ~7.6 s; H3 Max manages one slash, then a long static bind, and added a blood streak. Action shots look viable on Kling with 2–3 takes. **Cut (Kling multi-shot, wide → close-up):** the cut works and Natsuki is recognizable, but the close-up drifts: longer hair, a softer generic anime look and an invented ear stud. **Method:** build each shot from its own approved start frame, not in-generation cuts. Awaiting the author's verdict. |
| 10-12 | **Author's verdict on tests 2:** the animation is "pretty far from commercial quality"; manga is much closer. **Approved two follow-up tests** (Claude's proposal): (A) an anime-structure fight and (B) the jigeiko insert in color and B&W. |
| 10-12 | **Test A: anime-structure fight** (`production/cutscene-test/oct12b/`; `fight_kling_12fps.mp4`, `fight_veo_12fps.mp4`; script `production/pipeline/anime/build_fight.py`). 8 cuts in about 14 s: key poses drawn as stills (NB Pro), only the in-betweens generated (start + end frame), three limited cuts made in ffmpeg (push, impact hold with flash and shake, pan), retimed to anime pacing at 12 fps. **Claude's read:** clearly better than one long take. Short cuts hide drift, and start + end frames keep each shot on model. **Kling v3 Pro ≈ Veo 3.1:** Veo adds cel-style fog that clashes with the painted backgrounds and did leap-land-leap in C4; Kling is closer to the stills at about a quarter of the price. **The weak link is now the key stills:** C5 (impact) and C6 drift in rendering style, lighting and location props (stone lantern vs. jizō), and C5 gave the rōnin bandaged forearms. Fix: one style anchor and one location plate for every key in a sequence. **Error caught:** several first-pass stills drew a plain wolf face; redone with `turnarounds/beast.png` as a reference (the canon mask). Awaiting the author's verdict. |
| 10-12 | **Test B: jigeiko insert, 2 pages** (`production/cutscene-test/oct12b/`: `insert-script.md`, `insert-spec.json`, `pages/`). Every panel in color and as a B&W redraw of the same panel, so only the treatment differs. Lettering is set in code by the rebuilt compositor (`production/pipeline/manga/compose.py`, fonts in `fonts/`). Two color panels first drew the fighters with bare faces and baked-in text; redone with men helmets. Panel-by-panel reveal inside the VN not built yet. Awaiting the color vs. B&W verdict. |
| 10-12 | **Decided: no animated beats or cutscenes; living stills on CGs stay** (subtle 2–4 s loops). The other two video tiers are dropped; getting them to commercial quality would cost too much in takes and review time. Pivotal moments use CGs and manga inserts (canon §2; chapter map Ch39 updated). **Inserts stay full color** (reconfirmed after the B&W comparison). **Experiment: a B&W storyboard ("name")** for the author to approve before finished art, to cut his review time, not cost (style guide §4a). The author notes Vol. 1 worked fine without one; its main flaw was dialogue covering faces, so balloon areas are now reserved in panel prompts and checked in the lettering pass. Sample: `production/cutscene-test/oct12b/pages/page{1,2}_name.jpg`. |
| 10-12 | **Revised (evening):** very short animated moments are allowed where the models do well (e.g. the fall and catch, Ch2), alongside the living stills; nothing longer. **Storyboard step dropped:** Claude makes inserts from the script directly with a robust self-review (per-panel checks, a page lettering check, an independent reviewer agent) and presents only finished work (style guide §4a). |
| 10-13 | **Insert presentation decided: panel by panel**, exactly as in the test page (`production/insert-presentation-test/`): whole page first, then a zoom to each panel with the rest of the page dimmed but visible. The author: "It's awesome... Don't change a thing." (Canon §2, style guide §4a.) |
| 10-13 | **Inserts are designed for panel-by-panel reading** (author's point: guided view works badly on comics drawn for print). Design rules added to style guide §4a: every panel reads alone, one beat per tap, landscape-friendly panel shapes, surprises at the start of a new page. **To do before the first real insert:** compose VN pages at 2× (3200 × 4544) so zoomed panels stay sharp on a Retina iPad. |
| 10-16 | **Pilot v2 goes to its own Production thread** (brief: `production/pilot-v2/README.md`). **Review rule:** the author reviews only finished, playable chapters (art, voice, music included), never script-only drafts; produce all four chapters before handing over. Budget cap pending (proposed $40). |
| 10-16 | **Pilot v2 review flow approved:** the author approves a one-page-per-chapter scene outline (scenes, CGs, inserts, backgrounds) first, then gets all four chapters as a finished build. **Budget: $40 cap** for the whole pilot. |
| 10-17 | **Pilot v2 scene outline approved** (review delegated to the Story thread). All six [P] stagings kept. **Era treatments decided:** past life cool and desaturated, childhood warm and faded (canon §2). Changes: Ryōsuke's hot-dog argument moves to 1.3; the catch gets its short animated moment; FB1 shows the earlier "…You came back"; child Kōhei is a face window only. |
| 10-17 | **The author approved the revised outline.** **Review flow changed:** chapter by chapter instead of all four at once; each chapter (Prologue with Ch1) arrives as a finished, playable build and is reviewed before the next starts (brief updated). |
| 10-17 | **Pilot v2 Prologue + Ch1 built** and handed to the author for review: https://thefirstmccabe.github.io/ozakura/v2/ (the shipped pilot at the site root is untouched). Script rewritten with the Prologue/Ch1 fixes (pilot notes §1: 2, 4, 8–14, 20, 23, 25–27, the glosses from 32); new CGs (the dream in the past-life treatment, Natsuki's arrival, title); Akane school and Natsuki uniform sprites from the locked designs; Kōhei's face windows; every line re-voiced with the final cast; the finished music loops. Living stills on the title and the dream. Sources and pipeline: `production/pilot-v2/README.md` (Build). |
| 10-17 | **Claude's calls in the Ch1 build [P]:** the shipped night street (`bg_street_night`) shows the alley and stairs canon rules out, so 1.7 uses a night version of the Oct 10 houses plate, plus a variant where Nanoha's upstairs light glows in the three-foot gap (outline said "reuse street at night"). Natsuki's stutter plays on her sprite rather than over the arrival CG, so her face can actually falter. Akane's home outfit waits for Ch3 (she's in uniform all of Ch1). Nanoha's shipped school sprites were checked against her skin swatch and are fine; the pale-skin issue is in the lineup and turnaround images only. Sprites take a light tint on night and evening backgrounds. |
| 10-17 | **Independent review before handover** (a separate agent that hadn't seen the build being made): fixed Natsuki's hitch (now before her bow, on her face only, nothing voiced), the trash-day logic, the "laugh before I can stop it" framing (fix 4), the class-list order (names sort in kana order, so ふくだ sits right above ふじさわ), Nanoha's clipboard (last year's job, not day one's), Natsuki's stacked exclamation marks (fix 8), and Kōhei's cocky lines (his confident smile, not the eyes-shut laugh). 9 lines re-voiced; backlog now resets on Load. **New [P] details:** Dad's calendar line is the old Mon/Thu pickup and the town now collects Tue/Fri, so 1.7 is Kōhei going with Dad's handwriting; there's no Fukuda in 2-B this year, which is how Kōhei knows Nanoha looked for his name first; Natsuki answers "Sendai, most recently" all morning (pilot-notes [P]). **Kept:** her interlude question "someone you've met before?" (the author reviewed that scene and cut only the manga line); the reviewer would trade it for something lighter, since Ch1 now has two recognition beats. |
| 10-17 | **Author's Ch1 punch list, round 1** (as he plays): **Rika's voice down to +2 semitones** (style guide §7). **An interlude's POV character uses face windows, not a sprite** (style guide §3a), so Nanoha is a portrait in her interlude. **Ōno-sensei is shown on screen** (new sprite from `inventory/full-ono.png`; face window when he talks over a CG). **Natsuki's arrival stays on the front-of-class CG** through the hitch until she walks to his seat; the hitch is a variant of that CG with her smile faltering (face only, crossfaded). Natsuki isn't tall any more, so the "taller than the vice-principal" rumor is cut. Prologue: the cut is on the inside of the wrist, matching the CG. "Which I'm also fast at" rephrased. **Added [P]:** a CG of Nanoha fixing his collar on the river walk (the VN never had one; the manga did). **Prologue music:** the author doesn't love `memory` there; he'll decide after hearing it under the catch in Ch2 (options: no music, just river and wind, or a new dream cue at about $2). |
| 10-17 | **Image motif added (the author's idea):** past-life Natsuki in the white wedding hood (*wataboshi*), a late fragment before the long dreams, paid off by the wedding in Ch30 (canon scene bank 23; chapter map Ch27 and Ch30, placement a Proposal). |

## 3. Budget
| Line | Cap | Spent | Notes |
|---|---|---|---|
| Pilot v2 (Prologue + Ch1–4), Oct 16 | $40 | about $7.00 after Ch1 | Ch1: ~30 images, 2 living stills, 26 voice takes, 2 transcript checks. Ledger: `production/pilot-v2/ledger.md` |
| VN pilot | $100 | about $30–35 | |
| Manga Vol. 1 | $50 | $33.01 | About $17 left |
| Concept art, Oct 6 | none set (author-requested) | about $1–2 | 7 character images (NB2 1K) plus 4 house tests (NB2 2K) |
| Design pass (Oct 10) | $10 | about $4.50 (≈55 NB2 images; failed jobs uncharged) | Kōhei + face set, male Kirishima, Natsuki casual, Akane check, fairy, beast concepts, swatches |
| Visual inventory (Oct 10) | $20 | about $9 (≈90 images, NB2 1K/2K and NB Pro 2K, incl. review fixes; failed jobs uncharged) | see decision log and style guide §1b |
| Voice auditions (Oct 10) | approved with the scope (author: audition all unapproved voices) | about $0.55 | Gemini 3.8 Flash TTS, 71 takes |
| Cutscene test, Oct 10 | $10 (approved) | about $1.36 | 2 × 8 s clips (H3 Max 768P, Kling v3 Pro) |
| Cutscene tests 2, Oct 12 | same $10 cap | about $3.40 | 2 start frames (NB Pro 2K), 2 × 10 s action, 1 × 10 s Kling multi-shot |
| Fight test (A), Oct 12 | $10–15 (approved) | about $12.50: ~16 NB Pro 2K key stills (~$2.40), 5 × 3 s Kling v3 Pro ($2.10), 5 × 4 s Veo 3.1 (~$8 at $0.40/s; may be less with audio off) | `production/cutscene-test/oct12b/` |
| Jigeiko insert test (B), Oct 12 | about $5 (approved) | about $3: ~20 NB Pro 2K (9 color panels, 2 redos, 9 B&W) | same folder |
| Music style test, Oct 11 | $5 (approved) | about $4.30 (8 MiniMax takes, 492 s; 4 ElevenLabs takes, 330 s) | Natsuki (Persona-style), comedy (Muv-Luv feel), memory variations; `production/music/oct11-test/` |
| Music test round 2, Oct 11 | $5 (approved) | about $5.20: 6 ElevenLabs takes × 80 s ($4.80) + 4 Lyria ($0.40). **About $0.20 over cap**; Claude underestimated the ElevenLabs cost | Natsuki, memory, comedy; ElevenLabs vs Lyria; `production/music/oct11-test2/` |
| Music cue: Natsuki, Oct 11 | about $2 (approved per cue) | about $1.98: 2 ElevenLabs × 90 s ($1.80, `nanoha` as style reference) + 2 Lyria ($0.20) | `production/music/cue-natsuki/` |
| Music cue: Natsuki take 2, Oct 11 | $1.80 (approved) | $1.80: 2 ElevenLabs × 90 s (guitar + violin lead; one with a light `title` reference) | same folder, takes E and F |
| Music: practice + childhood, Oct 13 | $5 (approved) | about $3.94: 4 ElevenLabs × 90 s ($3.60) + 4 MiniMax (171 s, $0.34) | `production/music/pilot-v2/` |
| Music: Natsuki from guitar, Oct 13 | within the author's $2–4 OK | about $1.90: 2 ElevenLabs × 90 s ($1.80) + 3 Stable Audio audio-to-audio (~$0.10) | `production/music/natsuki-guitar/` |
| Music: Natsuki G/H + tribal practice, Oct 14 | requested by the author | about $3.75: 4 ElevenLabs × 90 s ($3.60) + 2 MiniMax (72 s, $0.15) | `production/music/natsuki-guitar/`, `production/music/practice-v2/` |
| Music: kiss theme from humming, Oct 17 | requested by the author | $2.40: 3 ElevenLabs × 80 s (the declined take produced nothing) | `production/music/kiss-hum/` |

**Cumulative fal spend:** about $90–95. fal's dashboard has the exact figure.

## 4. Known issues
**Manga Vol. 1, worst first:**
1. Ch1 p20, last panel: chibi Kōhei is in the wrong uniform.
2. Ch2 p9: garbled kanji on the name tag, covered by SFX.
3. Ch1 p19: Kōhei standing where the script has him seated.
4. Ch2 p2: Kōhei's hair is wilder than his model.
5. Cover: the past-life girl's face is faintly visible.
6. Stray frame lines in some panels.
7. Side characters drift.
8. The reader's control bars cover the page edges until they auto-hide.

**VN:** the pilot-notes §1 fix list. Not yet confirmed on a physical iPad. Voice QA was automated.

**Pilot v2 Ch1 (Oct 17):** tested in Chromium at iPad sizes (landscape 1180×820, portrait 820×1180), not yet on a physical iPad. Voices checked by transcript, not by ear. Web fonts couldn't load in the test browser, so the title's vertical 大桜 was checked only in code.

## 5. Infrastructure risks
- **Storage:** text canon lives in the Project; every file lives in the repo. Its `CLAUDE.md` holds the working rules.
- **The Vol. 1 manga pipeline code is lost.** The page compositor was rebuilt Oct 12 (`production/pipeline/manga/`); Vol. 1's own page layouts and lettering were not recovered. Commit pipeline code as you go.
- **The repo is public, story included** (author's call, Oct 10). Never commit credentials or anything personal.
- **Archived bible:** the Oct 1 snapshot is still in the Project and could confuse a search. It's marked archived in the project instructions; delete it if the author prefers.
- **Parallel threads:** Project writes replace the whole doc, so two threads can overwrite each other. Edit through the repo copy (`story/`), which has history, and fetch before editing.

## 6. Next up
**Agreed order (Oct 8):**
1. **Lock the character designs.** *(Done Oct 10: humans approved; visual inventory delivered, awaiting review.)* Kōhei (no approved image yet), the male Kirishima, a redo of Natsuki's casual outfit, final checks on Akane, and a consistency pass on the supporting cast. **Also lock a color swatch per character** (hair, eyes, skin, key outfit colors) in the style guide; color inserts make palette drift the main consistency risk.
2. **Finalize the voices.** *(Done Oct 11: full cast picked, style guide §7.)* An audition sheet for Nanoha, Akane and the male Kirishima; the author approves the cast he hasn't reviewed yet (Ryōsuke, Rika, Yuzu, Sōta, Kirishima, Ōno-sensei, the manager). He picks by ear.
3. **Map the first chapters.** The revised Ch1–3 plus the next few (late April into May) against canon §4, with the fix list applied. Place Yuzu's introduction and the build toward the June umbrella scene and the girls' pact.

**Waiting on the author:**
- **Spend approval** for steps 1–2 (about $1–3).
- **Pending approvals:** pilot names, address guide, kanji, POV (pilot-notes §1).
- **Music (Oct 13):** must-haves for pilot v2 are practice, Natsuki and childhood; then extend, loop and level the five kept tracks. The author picks Natsuki on the listening page; practice and childhood takes wait on spend approval. A composer may be hired later.
- **Format details** (Planning thread; canon §2 has the leaning: VN-primary with manga inserts). Insert style is settled: **full color** (Oct 10).
  - **Presentation: DECIDED Oct 13, panel by panel** (decision log).
  - **Which scenes get manga (working rule of thumb):** sequence-dependent beats go to manga (sparring, the street fight, the beast, the near-wordless kiss, montages, the full-page Nanoha moment); dialogue stays with sprites; emotional peaks get CGs.
  - **Test:** the Ch2 jigeiko as a 2-page insert. *(Done Oct 12, `production/cutscene-test/oct12b/`: color kept; storyboard step tried and dropped.)*
  - **Presentation test (Oct 13; panel by panel chosen):** `production/insert-presentation-test/` (GitHub Pages) plays the jigeiko inside a VN scene in four modes: panel by panel (zoom with the rest of the page dimmed), split (big panel plus the whole page beside it), build-up (page fills in panel by panel) and full page. Measured dialogue size on an iPad in landscape: about 44 px panel by panel, 28 px split, 13 px for build-up and full page, which is too small to read; on a phone, 22 / 22 / 6 px.
  - **Anime cutscenes and animated beats: DROPPED Oct 12; living stills on CGs kept** (decision log). Notes kept for reference:
    - **Cost isn't the constraint.** Image-to-video on fal runs about $0.03/s (MiniMax H3 Max) to $0.14/s (Kling v3 Pro), checked Oct 10. A 30–60 s cutscene of 5–10 s shots with 3–5 takes each is roughly $5–40.
    - **The real constraints:** identity drift between shots; clips of 10–15 s each; content filters, likely strictest on the kiss (teen characters) and on blood or the beast; and no usable lip sync. Keep dialogue as voiceover over shots, as anime often does.
    - **Method:** animate from approved CGs as first and last frames, so each shot starts and ends on-model.
    - **Candidates:** an opening movie (the classic VN spot for animation), the New Year bloom, the past-life walk and the trade, the climax lunge and save, and the epilogue. Pair the kiss with its song only if the filters allow.
    - **Test done Oct 10** (`production/cutscene-test/`): `cg_catch` animated for 8 s on MiniMax H3 Max and on Kling v3 Pro, about $1.36 total. **Both held the art style, faces and outfits with no visible morphing.** H3 Max pushed in hard to a close two-shot (more cinematic, crops her body). Kling stayed wide and restrained, closer to the prompt. **Author's verdict: "not bad."** At this cost, more video than first planned.
    - **Three-tier video plan (Working, Oct 10):**
      1. **Living stills (many):** subtle 2–4 s loops on most CGs and some backgrounds (hair, petals, breathing, the river). About $0.10–0.20 each; low risk.
      2. **Animated beats (dozens):** 5–10 s at emotional peaks, like the catch test.
      3. **Full cutscenes (a handful):** an opening movie plus about 4–6 pivotal moments, 30–60 s each.
    - **Choose the model per shot:** Kling for held, restrained moments; H3 Max for dramatic push-ins.
    - **Limits:**
      - **No video before the design lock.** The test already shows superseded designs.
      - **Use motion as punctuation,** so the static scenes don't feel dead.
      - **Review time is now the bottleneck,** not cost.
    - **Tests 2, done Oct 12** (`production/cutscene-test/oct12/`; decision log 10-12):
      - **Fast action:** viable on Kling with 2–3 takes per shot, so animation can replace some manga action pages.
      - **Two-shot cut:** in-generation cuts drift in close-ups. Give each shot its own approved start frame (a CG or close-up still), then edit the shots together.
    - **Tests 3, done Oct 12** (`production/cutscene-test/oct12b/`; decision log 10-12): the anime-structure fight (start + end key poses, 1–2 s cuts, 12 fps, limited cuts in ffmpeg) works better than long takes; Kling v3 Pro is the default in-betweener. Next lever: style and location consistency across the key stills of one sequence.
  - **Manga pipeline rebuilt (Oct 12):** `production/pipeline/manga/compose.py` lays out pages from a JSON spec and letters them in code (balloons, narration, SFX), in color or B&W from the same spec.

**After that:**
- **One revision pass on the pilot.** That covers:
  - Script fixes.
  - New sprites for Akane, Natsuki and the male Kirishima, plus Natsuki's CGs and Kōhei's hair.
  - The prologue CG (kimono, binding a cut).
  - The house backgrounds and window scene via a layout sketch.
  - Speaker portraits and the re-cast voices.
- **Rebuild the manga pipeline** before Ch3 or any manga fixes.
- **The 8-page color manga test** (`source/manga-pilot-handoff-brief.md`). It needs a spend cap. It **may be superseded** by the jigeiko insert test, now that full manga isn't the primary format.
