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
| 10-05 | Natsuki 160 cm with shoulder-length hair; Kōhei about 175 cm with dark-brown hair; charcoal plaid skirt. |
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
| 10-06 | **Houses about a meter apart, no alley** (the Muv-Luv Extra model). The art fix needs a layout-sketch method. |
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
| 10-10 | **Fairy timeline and function decided** (canon §8): visibility tracks the danger (a light Apr–Aug, plus small item displacements in Nanoha's room; a half-form in autumn; full and speaking at the bloom, recognizing Kōhei and Natsuki; visible to all Jan–Mar; a real goodbye to Nanoha at the end). Female (Working). Look and personality are proposals for the design step. |

## 3. Budget
| Line | Cap | Spent | Notes |
|---|---|---|---|
| VN pilot | $100 | about $30–35 | |
| Manga Vol. 1 | $50 | $33.01 | About $17 left |
| Concept art, Oct 6 | none set (author-requested) | about $1–2 | 7 character images (NB2 1K) plus 4 house tests (NB2 2K) |
| Designs and voice auditions | **approval pending** | — | Estimated $1–3 together |

**Cumulative fal spend:** about $65–70. fal's dashboard has the exact figure.

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

## 5. Infrastructure risks
- **Storage:** text canon lives in the Project; every file lives in the repo. Its `CLAUDE.md` holds the working rules.
- **The Vol. 1 manga pipeline code is lost.** Rebuild it in `production/pipeline/` and commit as you go.
- **The repo is public, story included** (author's call, Oct 10). Never commit credentials or anything personal.
- **Archived bible:** the Oct 1 snapshot is still in the Project and could confuse a search. It's marked archived in the project instructions; delete it if the author prefers.
- **Parallel threads:** Project writes replace the whole doc, so two threads can overwrite each other. Edit through the repo copy (`story/`), which has history, and fetch before editing.

## 6. Next up
**Agreed order (Oct 8):**
1. **Lock the character designs.** Kōhei (no approved image yet), the male Kirishima, a redo of Natsuki's casual outfit, final checks on Akane, and a consistency pass on the supporting cast. **Also lock a color swatch per character** (hair, eyes, skin, key outfit colors) in the style guide; color inserts make palette drift the main consistency risk.
2. **Finalize the voices.** An audition sheet for Nanoha, Akane and the male Kirishima; the author approves the cast he hasn't reviewed yet (Ryōsuke, Rika, Yuzu, Sōta, Kirishima, Ōno-sensei, the manager). He picks by ear.
3. **Map the first chapters.** The revised Ch1–3 plus the next few (late April into May) against canon §4, with the fix list applied. Place Yuzu's introduction and the build toward the June umbrella scene and the girls' pact.

**Waiting on the author:**
- **Spend approval** for steps 1–2 (about $1–3).
- **Confirm the kiss song** title and artist.
- **Pending approvals:** pilot names, address guide, kanji, POV (pilot-notes §1).
- **Music style:** he may spend time defining it; the `kendo` track needs replacing.
- **Format details** (Planning thread; canon §2 has the leaning: VN-primary with manga inserts). Insert style is settled: **full color** (Oct 10).
  - **Presentation:** manga pages are portrait and the VN is landscape. Claude recommends a panel-by-panel reveal inside the VN frame rather than full pages.
  - **Which scenes get manga (working rule of thumb):** sequence-dependent beats go to manga (sparring, the street fight, the beast, the near-wordless kiss, montages, the full-page Nanoha moment); dialogue stays with sprites; emotional peaks get CGs.
  - **Test:** turn the Ch2 jigeiko into a 2–3 page insert inside the existing VN. It costs a few dollars, answers the questions above, and needs a spend cap.
  - **Anime cutscenes** (Working; canon §2). Claude's notes:
    - **Cost isn't the constraint.** Image-to-video on fal runs about $0.03/s (MiniMax H3 Max) to $0.14/s (Kling v3 Pro), checked Oct 10. A 30–60 s cutscene of 5–10 s shots with 3–5 takes each is roughly $5–40.
    - **The real constraints:** identity drift between shots; clips of 10–15 s each; content filters, likely strictest on the kiss (teen characters) and on blood or the beast; and no usable lip sync. Keep dialogue as voiceover over shots, as anime often does.
    - **Method:** animate from approved CGs as first and last frames, so each shot starts and ends on-model.
    - **Candidates:** an opening movie (the classic VN spot for animation), the New Year bloom, the past-life walk and the trade, the climax lunge and save, and the epilogue. Pair the kiss with its song only if the filters allow.
    - **Test:** one 5–10 s clip from an existing CG (e.g. `cg_catch` or petals at the tree). Under $5; needs approval.

**After that:**
- **One revision pass on the pilot.** That covers:
  - Script fixes.
  - New sprites for Akane, Natsuki and the male Kirishima, plus Natsuki's CGs and Kōhei's hair.
  - The prologue CG (kimono, binding a cut).
  - The house backgrounds and window scene via a layout sketch.
  - Speaker portraits and the re-cast voices.
- **Rebuild the manga pipeline** before Ch3 or any manga fixes.
- **The 8-page color manga test** (`source/manga-pilot-handoff-brief.md`). It needs a spend cap. It **may be superseded** by the jigeiko insert test, now that full manga isn't the primary format.
