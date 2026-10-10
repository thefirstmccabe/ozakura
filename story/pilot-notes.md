# Ōzakura — Pilot Notes

**What this covers:** the shipped VN pilot (Prologue + Ch1–3) and manga Vol. 1. It records what the pilot invented, how it maps to canon, and the fixes agreed so far.

**Who wins:** `ozakura/canon.md` governs. Where the shipped script disagrees with canon, the script is non-canon until it's revised.

This document replaces the old working bible (`ozakura/story-bible.md`). Last updated 2026-10-10 (Ch3 feedback complete; P1–P5 and Yuzu's later introduction approved).

**Markers:**
- **[P]:** invented by Claude for the pilot. Provisional until the author approves or replaces it.
- **[Fix]:** an agreed change, waiting on the revision hold (see the production log).
- **[Proposed]:** Claude's suggestion, not yet approved by the author.

---

## 1. Revision hold and fix list
**Hold:** don't revise the shipped VN or manga yet. The hold started Oct 5 while the production process was re-examined. Since Oct 7 it also waits on the author's full playthrough and complete feedback. Then make all the changes in one pass.

**Status Oct 8:** feedback is complete for the Prologue through Ch3 (§1b). Part of it was given in the original VN production thread by mistake and is recorded here.

**Planned order before the revision pass:** lock the character designs, finalize the voices, then map the first chapters (production log §6).

### Agreed fixes, Oct 6–7 (updated Oct 8)
**Story and script:**
1. **[Fix] Scale back the Ch3 past-life flash.** In week one Kōhei gets a full vision and "recognizes the girl." Make it a fragment: a feeling and a detail, with no recognition. The author confirmed Oct 8 that the cherry-tree scene needs this rework because it tells too much too soon.
2. **[Fix] Thin out the supernatural beats in week one.** Keep the catch and tear, the prologue dream, and the fairy's light. Move Natsuki's "Did you just hear someone?" at the tree, and most of the "You're late" uses (currently four), later in the story. **Added Oct 8:**
   - **Ch1 Natsuki intro:** cut the sensory flash and the narrated certainty ("rain on cedar… I am absolutely, completely certain… that I've kept her waiting"). Keep only the physical reaction: her grin stutters, and he grips his pen hard enough to hurt.
   - **Ch1 ending:** cut the dream's return. The prologue already established it.
   - **Ch2:** cut Kōhei's own flash mid-catch ("I'm somewhere outside… someone in my arms"), the "like I've put down something heavy" paragraph, and the bridge's last line ("Like a promise I don't remember making"). The tear and "cedar pollen" / "It's April" stay, unexplained.
   - **Fairy:** one mention in week one; feed more in later.
3. **[Fix] Pull back Nanoha's near-confession.** "What if someone… was already just around?" / "Then they'd be you" / "I'll keep asking" is a month-three beat. In week one she's still hiding her feelings well.
4. **[Fix] Warm up Kōhei.** Canon wants easy smiles and playful mock-seriousness. Cut his "doesn't laugh" framing and Yuzu's "dead-fish eyes" line.
5. **[Fix] Recast the Saturday best of five** as casual sparring rather than a draw with a "Next Saturday" rematch setup. Kōhei usually has the edge. This also changes the Ch2 setup lines ("Again next week. Best of five." and "Then best of five. Saturday."). The bridge invitation and "Saturday mornings. Club practice. You'll be there?" stay.
6. **[Fix] Recast the sparring recognition** as one-sided. Natsuki anticipates him; they don't move "in perfect sync." She never sparred with him in the past life, but she watched him train.
7. **[Fix] Takatsuki:** remove the needling about Kōhei's missed practices. Rewrite him as the technically perfect kendoka baffled by Kōhei's instinctive swordsmanship (canon §8).
8. **[Fix] Natsuki's voice:** "loud" becomes warm, confident and charismatic, in line with her restyle.
9. **[Fix] Akane's lines** move from sardonic to sweet and playful, and she calls him "Onii-chan" instead of "Onii." This includes the Ch2 Tuesday recap ("none of my business").
10. **[Fix] Fix the house distance.** Two lines say "three meters apart"; change them to about three feet, an arm's length (and use imperial units in the script).
11. **[Fix] Fix Dad's calendar line.** "From a long time ago" overstates one year; change to "from last spring" or similar.
12. **[Fix] The past-life girl** wears a simple real kimono, not a "peasant kimono." Her family is modestly propertied. **This means redrawing the prologue CG** (`cg_hands_strap`), where she's in a faded work kimono.
13. **[Fix] Show more and tell less** throughout. **Sharpened Oct 8:**
   - **Openings:** a fact goes in only if the scene shows it happening. Cut the backstory narration in Ch1: the maternity ward (twice), "since before either of us was born," the bio-style intros for Rika and Ryōsuke (the science project, the 40-minute hot-dog argument) and the river walk's list of things almost nobody knows Nanoha does (goldfish funeral, arguing with the TV). Save that material for real scenes later; for example, Ryōsuke has the hot-dog argument on screen.
   - **Keep what's shown:** the cups, the sticky drawer, the window latch, the collar, Dad's handwriting on the calendar.
13a. **[Check] Nanoha's grades:** the pilot gives her "top grades," but canon says "very good rather than necessarily best." Align when revising.

**Presentation:**

14. **[Fix] Hide the invented kanji** in the backlog and scene chart until the names' kanji are chosen.

**Art:**

15. **[Fix] Akane:** a full redesign (lavender-silver hair, sailor uniform, cute outfits, younger look). New sprites are needed. Refs: `production/refs/akane-v2/`.
16. **[Fix] Natsuki:** shoulder-length hair restyled per `production/refs/natsuki-v2/01-restyle-uniform.png`, at 5′3″ with corrected proportions. **Added Oct 8:** her CGs show long hair too and need redrawing (`cg_natsuki_intro`, `cg_catch`, `cg_jigeiko` where visible, `cg_shrine_meeting`, `cg_pastlife`, and the title art).
17. **[Fix] Kōhei:** dark-brown hair at about 5′9″. The manga's black, spiky hair at 5′10″ is drift.
18. **[Fix] Houses:** `bg_street_houses` (the alley and stairs between the houses) and `cg_window_night` (the wide gap). Redraw both with the houses about three feet apart, Muv-Luv Extra style. **Replacements made Oct 10** (style guide §1b). Text prompts failed four times; build a layout sketch for the model to paint over. **This also fixes the window-scene bug (fix 31).**

**Voice:**

19. **[Fix] Re-cast Nanoha and Akane.** Both sound like much older women. The author will choose from an audition sheet of younger-sounding candidates; spend approval is pending. Kōhei and Natsuki are fine. **Oct 8:** Emi's and Takatsuki's voices are approved too; the rest haven't been reviewed yet. Kirishima needs a male voice (fix 28).

### 1b. Author playthrough feedback, Oct 8 (Prologue–Ch3)
**Agreed (new fixes):**

20. **[Fix] Morning, the food.** Keep Nanoha walking in with the kinpira and the "It's a sickness" exchange. Cut the narration explaining it ("It is the fourth time this month… I know exactly what it is… a conversation neither of us wants to have before seven"); it's too on the nose. Replace it with one beat: she's been bringing food over for a year; he used to protest; then he gave up.
21. **[Keep] Morning, Mom:** the closed fusuma, the knock, no answer, the creak.
22. **[Keep] Prologue.** The author likes it. Apply fix 12 (kimono) and fix 23 (the strap). Its atmospheric fragments ("Petals.") stay.
23. **[Fix] The wrist strap becomes binding a cut on his wrist.** He has come back late and hurt from training, and she ties it off while scolding him ("You're late"). It makes the canon motif concrete (echoed when Natsuki treats his wounds in August). It also says what that life was like: patching him up afterward was all she could do, which the climax reverses. Agreed Oct 8; canon §5 updated to match.
24. **[Keep] The river walk and class lists** are basically fine; they get only the global fixes.
25. **[Fix] Writing rule: no telegraphic name-tag intros or trait lists.** "Hoshikawa Rika. Nanoha's best friend since middle school, art club…", "Tokiwa Ryōsuke. Go club. Glasses.", "Tachibana Nanoha. The house next door.", "Kirishima Aoi, third-year, club captain.", "Takatsuki Shō, second year." read as trying to be edgy. Let people arrive through what they do and say (Rika's "Nano-chaaaan!" tackle already does it). Narration uses complete sentences by default.
26. **[Fix] Writing rule: no manga self-reference.** Cut Natsuki's "Like in manga" and Nanoha's echo in the Ch1 Nanoha interlude. Characters never compare their own situation to manga. Kōhei owning manga, Nanoha reading them (Ch3) and the scene-bank childhood-friend manga stay.
27. **[Fix] Face windows and dialogue colors (rules locked Oct 10; full spec in style-guide §3a).**
    - **Kōhei:** a window on every spoken line.
    - **Others:** a window only when they speak and their sprite isn't on screen.
    - **Never:** for texts, sprite-less speakers or "???".
    - **Art needed:** a ~10-expression face set for Kōhei; everyone else is cropped from their sprites.
    - **Colors:** name tags in full character color, dialogue in a pale tint of it, narration neutral. Test screen first.
28. **[Fix] The kendo captain becomes male.** Kirishima keeps his role and deadpan humor. "Aoi" works as a boy's name, so the name can stay (still [P]). Needs pronoun edits, three new sprites and a new voice.
29. **[Keep] The catch and the tear** (the author leans toward keeping them; Claude agrees). See fix 2 for the narration cut around them.
30. **[Keep] Ch2's Chie texts and the Natsuki interlude** ("great").

**Ch2 changes proposed by Claude, approved by the author Oct 8 (now fixes):**
- **P1. [Fix]** Cut the debrief line "I wasn't thinking about something. I was remembering something."
- **P2. [Fix]** With "You're late" moved out of the Natsuki interlude, end it on her cheerful "yeah i'm good! made a friend today" to Chie, then have her photograph the cherry trees to send. Flip one text for fix 6: "he moves exactly how i would move" becomes something like "i knew what he was going to do before he did it. every time."
- **P3. [Fix]** Kendo accuracy: jigeiko has no referee or points. Since the captain calls "Kote ari!", make it a practice match (shiai-geiko) and keep the calls.
- **P4. [Fix]** In the mop scene, keep Kōhei staying late but cut the explanation ("It doesn't make up for anything. It just makes me feel like I've paid something toward it").
- **P5. [Keep]** The back-of-the-neck prickle in class ("she's always looking at the board"); it now fits canon, since she watches him.

**Ch3 notes from the author (complete Oct 8):**
- **Yuzu: introduce her later (approved Oct 8).** Her look and dialogue are great; she stays as someone who annoys the other two girls from time to time.
  - **When:** around May–June, near the girls' pact, when there's a triangle for her to annoy. Kōhei training a new hire still works then.
  - **[Fix] Scene 3.1** keeps the manager and the job but drops Yuzu. Her pilot introduction moves intact to the later chapter.
- **Liked:** the home-from-work scene (3.2), the fairy bit, Natsuki with Sōta, Emi's look and voice, Takatsuki's look and voice.
- **Music:** he likes most of it and will give notes chapter by chapter as the rework goes. **He dislikes the music in scene 3.4** (Saturday practice, track `kendo`, which also plays in the Ch2 dojo scenes). He may spend time on music style.
- **The cherry-tree scene** (3.5) needs the rework already agreed (fixes 1–2).
- **Fairy:** slow it down; one mention in week one, more later (fix 2).
- **General:** the strangeness should be more subtle across the longer runtime.
- **31. [Fix] Window-scene bug (3.3):** Nanoha's sprite appears over Kōhei's bedroom background, so she looks like she's in his room. Redraw it Muv-Luv style, viewed from his room through his window into hers, so she's visibly in her own window across the gap. Optionally add a reverse shot from her side. Fold into fix 18.
- **[Keep] Tea at the shrine (3.6) and lunch at the Tachibanas' (3.7):** fine apart from the agreed fixes.

### Still needs an author decision
1. **Pilot names.** All are [P] and need approval or replacement:
   - Places: the town (Shirasawa), the school (Shirasawa High), the shrine (Hanaoka) and the restaurant (Hoshino Kitchen).
   - Cast: Ryōsuke, Rika, Yuzu, Kirishima, Takatsuki, Sōta, Kazuo, Emi, Genji, Chie and Ōno-sensei.
   - Details: Natsuki's father's job and Akane's clinic day.
2. **The address guide (§4), including "Kō-chan."** Canon scene bank #6, the nickname that later hurts, depends on this choice.
3. **POV** (canon: Open).

## 2. The pilot as shipped
**Pilot voice:** dry, warm and funny on the surface, with grief and obligation underneath. Characters deflect with banter.

**Format:**
- A kinetic novel, with no choices.
- **POV:** Kōhei in first-person present tense, plus short third-person past-tense interludes labeled "Interlude: Nanoha" and "Interlude: Natsuki."
- **Language:** English text with Japanese voices; narration is unvoiced.

**Motifs:**
- **"You're late"** is the past-life girl's line. It appears in Kōhei's dream, in Natsuki's head in her own voice, from Nanoha at the shrine as an accidental echo, and in the flash. It's load-bearing, so don't overuse it (see fix 2).
- **The fairy** is never shown clearly: a drifting point of light that only Nanoha reacts to ("…You came back.").
- **Kōhei's deflection** is "I don't have time." Three girls confessed to him last year, and all three got it.

### Timeline (April, second year; Apr 7 is a Monday)
| Day | Chapter | Beats |
|---|---|---|
| Recurring | Prologue | The dream: river, branch, hands tying a strap, "You're late." |
| Mon Apr 7 | Ch1 "The House Next Door" | Morning routine, river walk, the 2-B list, Natsuki's intro and déjà vu, lunch banter (the three confessions), Nanoha's tour interlude, "You smiled" on the trash walk, the dream returns |
| Tue Apr 8 | Ch2 "Kendo" | Shift; Natsuki becomes "Nacchan" |
| Wed Apr 9 | Ch2 | First practice: Kirishima, Takatsuki, jigeiko (kote to her, dō to him), the mop race and the catch with her tear, the bridge invite, Natsuki texting Chie |
| Thu Apr 10 | Ch3 "Windows" | Training Yuzu (moving later; fix in §1b); Akane's dizzy spell, Nanoha stayed with her; window talk with Usagi-san, "Then they'd be you" |
| Sat Apr 12 | Ch3 | Best of five ends in a draw; shrine sweeping; Natsuki arrives with her camera; the past-life flash; Nanoha's "…You came back"; lunch at the Tachibanas'; "I'll keep asking" |

Manga Vol. 1 = Prologue + Ch1–2. Ch3 has not been adapted.

**Developer mode** (`…/ozakura/#dev`) labels scenes by number (Prologue = P; Ch1 = 1.1–1.7; Ch2 = 2.1–2.7; Ch3 = 3.1–3.7). Ch3: 3.1 shift (Yuzu), 3.2 home late, 3.3 windows, 3.4 Saturday practice, 3.5 the Great Cherry, 3.6 tea at the shrine, 3.7 lunch at the Tachibanas'.

## 3. Pilot inventions by character
**Kōhei:**
- Class 2-B. Up at 5:40, makes two lunches, knocks on his mother's door.
- A thick tsuka callus on his left palm.
- Works at Hoshino Kitchen [P] Tue/Thu/Sun.
- Nanoha's catalogue of his faces: No. 1 is "Secret"; No. 4 is "Somebody wants to fight me."

**Nanoha:**
- 2-B, top grades (see 13a), the class representative's assistant ("owns a clipboard"). Underclassmen bow to her.
- Their mothers shared a maternity ward.
- Privately: a goldfish funeral with a eulogy, arguing with the TV, conspiracy theories, keeping score against Kōhei.
- Walks into his kitchen without knocking and knows every sticky drawer. Fixes his collar.
- Calls him "Kō-chan" to tease [P].
- Decided to like Natsuki "the way you shut a window against the wind."
- Childhood: called the light "the fairy" and left it cookies; Kōhei "heard someone in the next room."

**Natsuki:**
- "Professional new girl," instantly popular. Classmates call her "Nacchan" by Tuesday.
- Copper hair "the color of a temple bell in late afternoon."
- Six moves for her father's job [P: "fixes struggling branches"]: Sendai → Niigata → Okayama → Sapporo → Sendai → Shirasawa. She has never been to Kanagawa but feels she has.
- Apartment near the station.
- Kendo since age 7; fights "fast like water"; a faded, much-washed indigo keikogi.
- Photographs every town "so I have proof I was there."
- "I'm amazing at first days. It's the second semesters I never get to."
- Chie [P] in Sendai is the only friend she's kept.
- Her involuntary tears at the catch ("cedar pollen" / "It's April").
- **Cut or move per the fixes:** the "loud" framing (fix 8); "Did you just hear someone?" at the tree (fix 2).

**Akane:**
- Clinic day is the 18th [P]. Dizzy spells and fatigue. "I know. That's why I didn't [call]."
- **Superseded by the redesign:** the old look (dark-brown bob, sleepy eyes, gray hoodie) and the sardonic voice.

**Mom and Dad:**
- Mom stays behind a closed fusuma.
- Dad's handwriting is still on the kitchen calendar (see fix 11). The wrong-day garbage follows his handwriting.

**Tachibana family [P]:**
- **Emi (mother):** warm and brisk, yellow apron. Her chronic "made too much" kinpira is quiet charity (fix 20: no longer explained in narration).
- **Kazuo (father, the mentor):** big and quiet, a former karate club member, an office job at the city water bureau. Not yet on screen.
- **Sōta (brother):** 7, in second grade, a fighting-game gremlin who calls Kōhei "Kō-nii."
- **Genji (grandfather, shrine caretaker):** his "very convenient back" only hurts on petal days. Mentioned only.

**School [P]:**
- **Tokiwa Ryōsuke:** the best friend. Glasses, go club. Precise and smug. His middle-school science project (he did all of it). Will argue whether a hot dog is a sandwich for 40 minutes. Calls Kōhei "Fujisawa."
- **Hoshikawa Rika:** Nanoha's best friend. Art club, no indoor voice, novelty clips (strawberry, star, a frog wearing a crown). Calls Nanoha "Nano-chan."
- **Ōno-sensei:** 2-B homeroom, classical Japanese. Tall, tired, "born in a cardigan."

**Kendo club [P]:**
- **Kirishima Aoi:** third-year captain. **Becoming male (fix 28).** Quiet authority, deadpan jokes no one gets. "You stopped for half a second. Don't."
- **Takatsuki Shō:** the Rival, fast "like a whip." Being rewritten per fix 7. Look and voice approved Oct 8.

**Hoshino Kitchen [P]:**
- **Shiina Yuzu:** the work kōhai, a first-year at Shirasawa Commercial. Cheeky ("Point to Shiina"), flustered by sincerity, a brilliant customer handler. Honey-brown hair with a red clip. Look and dialogue approved Oct 8; **her introduction moves to around May–June** (§1b).
- **The manager:** harried and balding. "You're a lifesaver," about nine times a shift.

**Elsewhere [P]:**
- **Chie:** Natsuki's confidant, by text only. Close to her in 4th and 8th grade. Sends zunda mochi every New Year.

**The past-life girl:** speaker label "???". She waits under the low branch. Thatched roofs and flooded paddies; a stone and a shimenawa rope before the shrine existed. In the pilot she ties a strap around the dreamer's wrist; per fix 23 she binds a cut on his wrist. See fix 12 for her costume.

## 4. Address guide (pilot; Open in canon)
| From → To | Form |
|---|---|
| Kōhei ↔ Nanoha | Bare given names; Nanoha teases with "Kō-chan" |
| Akane → Kōhei / Nanoha | "Onii-chan" (fix 9) / "Nanoha-chan" |
| Natsuki ↔ Kōhei | "Fujisawa" / "Mizuno" |
| Nanoha → Natsuki | "Mizuno-san" → "Natsuki-san" ("I'm working up to it"); "-chan" saved for a later beat |
| Natsuki → Nanoha | "Nanoha" from day one |
| Rika → Nanoha | "Nano-chan" |
| Sōta → Kōhei | "Kō-nii" |
| Yuzu → Kōhei | "Senpai" / "Fujisawa-senpai" |
| Kendo juniors → Kirishima | "Captain" |
| Classmates → Natsuki | "Nacchan" |

## 5. World as the pilot built it [P]
- **Shirasawa (白沢):** the Shirasawa River runs fat with snowmelt in April. A cherry-lined embankment path leads to school, and a bridge marks where the routes split.
- **The houses:** behind them is a hill of wet earth and trees, and the shrine is a 20-minute walk uphill. Distance per canon (fix 10).
- **Shirasawa High:** prefectural, six second-year classes. The pool is green. The art-room stairs squeak on steps 4 and 11. The third-floor girls' bathroom window faces the mountains. A cedar-walled dojo.
- **Hanaoka Shrine:** locals call it "Ōzakura-sama." Stone stairs through cedars to a weathered torii.
  - **The Ōzakura:** a trunk wider than three adults can circle; a low branch at shoulder height "as if offering you its arm"; a flat boulder; a view of the whole valley.
  - **Its age:** the shrine records go back about 300 years and only call it "the great tree."
- **Hoshino Kitchen:** a family restaurant by the station.
- **Street Brawlers:** a fictional fighting game. Natsuki mains Kagero, "a coward's character" (Sōta).

## 6. Seeds planted
- Who the past-life girl is; the wrist strap and its knot (now a bound cut, fix 23).
- Why Natsuki hears the line in her own voice and recognizes the town.
- What Nanoha sees under the branch, and "You came back."
- Kōhei's "I don't know yet."
- Akane's dizziness, Mom's withdrawal, Dad's absence.
- Nanoha's unspoken feelings.
- Natsuki's "second semesters" (will she move again?).
- **Takatsuki's grudge:** being reframed per fix 7.

## 7. Running bits worth keeping
- Nanoha's catalogue of Kōhei's faces.
- **Usagi-san,** the white rabbit plushie Kōhei bought Nanoha, in recurring time-out ("He knows what he did"; facing the corner means a reduced sentence).
- Emi's kinpira: "She's very bad at measuring burdock. It's a sickness."
- "Cedar pollen" / "It's April."
- Nanoha's score-keeping ("That's two points for me").
- "Point to Shiina."
- The manager's "Lifesaver!" count.
- Wrong-day garbage.

**Claude's read on what works best:** Nanoha's private oddness, Emi's kinpira, the kitchen familiarity Natsuki notices, and Natsuki's "second semesters" line. The pilot's warmth and humor are its strongest asset.

**The author's Oct 8 likes:** the prologue, Nanoha's morning arrival with food and familiarity, the river walk, the class lists, Natsuki's texts with Chie and her interlude, Yuzu, the home-from-work scene, the fairy bit, Natsuki with Sōta, tea at the shrine, lunch at the Tachibanas', and most of the music.
