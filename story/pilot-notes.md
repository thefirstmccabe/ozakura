# Ōzakura — Pilot Notes

**What this covers:** the shipped VN pilot (Prologue + Ch1–3) and manga Vol. 1. It records what the pilot invented, how it maps to canon, and the fixes agreed so far.

**Who wins:** `ozakura/canon.md` governs. Where the shipped script disagrees with canon, the script is non-canon until it's revised.

This document replaces the old working bible (`ozakura/story-bible.md`). Last updated 2026-10-17 (Pilot v2 Ch1 built; its new [P] details are noted in §3).

**Markers:**
- **[P]:** invented by Claude for the pilot. Provisional until the author approves or replaces it.
- **[Fix]:** an agreed change, waiting on the revision hold (see the production log).
- **[Proposed]:** Claude's suggestion, not yet approved by the author.

---

## 1. Revision hold and fix list
**Hold:** don't revise the shipped VN or manga yet. The hold started Oct 5 while the production process was re-examined. Since Oct 7 it also waits on the author's full playthrough and complete feedback. Then make all the changes in one pass.

**Status Oct 8:** feedback is complete for the Prologue through Ch3 (§1b). Part of it was given in the original VN production thread by mistake and is recorded here.

**Status Oct 17:** Pilot v2 (`v2/` in the repo, separate from the shipped build) applies the Prologue and Ch1 share of the fixes: 2, 4, 8–14, 16, 20, 23, 25–27 and the term glosses from 32, plus Akane's new sprites (15) and the final cast (19), and keeps 21, 22 and 24. It's waiting on the author's review. The shipped pilot is unchanged; the fixes stay marked [Fix] until v2 replaces it.


### Agreed fixes, Oct 6–7 (updated Oct 8)
**Story and script:**
1. **[Fix] Scale back the Ch3 past-life flash.** In week one Kōhei gets a full vision and "recognizes the girl." Make it a fragment: a feeling and a detail, with no recognition. The author confirmed Oct 8 that the cherry-tree scene needs this rework because it tells too much too soon.
2. **[Fix] Thin out the supernatural beats in week one.** Keep the catch and tear, the prologue dream, and the fairy's light. Move Natsuki's "Did you just hear someone?" at the tree, and most of the "You're late" uses (currently four), later in the story. **Added Oct 8:**
   - **Ch1 Natsuki intro:** cut the sensory flash and the narrated certainty ("rain on cedar… I am absolutely, completely certain… that I've kept her waiting"). Keep only the physical reaction: her grin stutters, and he grips his pen hard enough to hurt.
   - **Ch1 ending:** cut the dream's return. The prologue already established it. **Superseded Oct 18:** the game now opens on the cold open, and the dream's first appearance is the end of Ch1.
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
16. **[Fix] Natsuki:** restyled at 5′3″ with corrected proportions. Her look is now **long, soft waves and green eyes** (Oct 20, style guide §1–§2; it replaced the Oct 6 shoulder-length cut). Every CG that shows her must be redrawn to the current look (`cg_natsuki_intro`, `cg_catch`, `cg_jigeiko` where visible, `cg_shrine_meeting`, `cg_pastlife`, and the title art).
17. **[Fix] Kōhei:** dark-brown hair at about 5′9″. The manga's black, spiky hair at 5′10″ is drift.
18. **[Fix] Houses:** `bg_street_houses` (the alley and stairs between the houses) and `cg_window_night` (the wide gap). Redraw both with the houses about three feet apart, Muv-Luv Extra style. **Replacements made Oct 10** (style guide §1b). Text prompts failed four times; build a layout sketch for the model to paint over. **This also fixes the window-scene bug (fix 31).**

**Voice:**

19. **[Fix] Re-cast Nanoha and Akane.** Both sound like much older women. The author will choose from an audition sheet of younger-sounding candidates; spend approval is pending. Kōhei and Natsuki are fine. **Oct 8:** Emi's and Takatsuki's voices are approved too; the rest haven't been reviewed yet. Kirishima needs a male voice (fix 28).

32. **[Fix] Kendo explainer and bilingual terms (Oct 12):** add Natsuki explaining kendo to Rika in Ch2, before the practice match (canon 13f), and show every kendo call and term in Japanese with English (style guide §5).

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
2. ~~The address guide (§4), including "Kō-chan."~~ **Decided Oct 17** (style guide §3c; delegated by the author): Nanoha keeps "Kō-chan" in private; the nickname that hurts (scene bank 6) is Kōhei's "Chibi" for her.
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
- 2-B, top grades (see 13a), the class representative's assistant ("owns a clipboard"); in v2 that was last year's job, since it's only the first day of the new year. Underclassmen bow to her.
- Their mothers shared a maternity ward.
- Privately: a goldfish funeral with a eulogy, arguing with the TV, conspiracy theories, keeping score against Kōhei.
- Walks into his kitchen without knocking and knows every sticky drawer. Fixes his collar. **v2 [P]:** the collar moment gets its own CG on the river walk (`cg_collar`); the VN never had one, the manga did.
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
- **v2 [P]:** on her first day she answers "Sendai, most recently" all morning, which is how Nanoha knows where she moved from.
- **v2 [P] (Story thread, Oct 17):** writes schedules on the inside of her wrist in ballpoint, a habit from six schools' worth of new timetables (水, for Wednesday, at lunch in Ch1). Replaces the narration's wrist simile.
- Her involuntary tears at the catch ("cedar pollen" / "It's April").
- **Cut or move per the fixes:** the "loud" framing (fix 8); "Did you just hear someone?" at the tree (fix 2).

**Akane:**
- Clinic day is the 18th [P]. Dizzy spells and fatigue. "I know. That's why I didn't [call]."
- **Superseded by the redesign:** the old look (dark-brown bob, sleepy eyes, gray hoodie) and the sardonic voice.

**Mom and Dad:**
- Mom stays behind a closed fusuma.
- Dad's handwriting is still on the kitchen calendar (see fix 11). The wrong-day garbage follows his handwriting. **v2 [P]:** his line is the old Mon/Thu burnables pickup; the town now collects Tue/Fri, so Kōhei takes the trash out on Monday night by Dad's handwriting.

**Tachibana family [P]:**
- **Emi (mother):** warm and brisk, yellow apron. Her chronic "made too much" kinpira is quiet charity (fix 20: no longer explained in narration).
- **Kazuo (father, the mentor):** big and quiet, a former karate club member, an office job at the city water bureau. Not yet on screen.
- **Sōta (brother):** 7, in second grade, a fighting-game gremlin who calls Kōhei "Kō-nii." **[Fix] Oct 13: becomes Mio, a little sister** (canon §8): a bossy gremlin; design D, voice Kore +4.
- **Genji (grandfather, shrine caretaker):** his "very convenient back" only hurts on petal days. Mentioned only.

**School [P]:**
- **Tokiwa Ryōsuke:** the best friend. Glasses, go club. Precise and smug. His middle-school science project (he did all of it). Will argue whether a hot dog is a sandwich for 40 minutes (v2: the topic becomes taiyaki, head or tail first; style guide §3b). Calls Kōhei "Fujisawa."
- **Hoshikawa Rika:** Nanoha's best friend. Art club, no indoor voice, novelty clips (strawberry, star, a frog wearing a crown). Calls Nanoha "Nano-chan."
- **Ōno-sensei:** 2-B homeroom, classical Japanese. Tall, tired, "born in a cardigan." On screen from v2 (sprite from `inventory/full-ono.png`).
- **v2 [P]:** there's no Fukuda in 2-B this year, which is how Kōhei knows Nanoha looked for his name before her own (names sort in kana order, so ふくだ sits right above ふじさわ).

**Kendo club [P]:**
- **Kirishima Aoi:** third-year captain. **Becoming male (fix 28).** Quiet authority, deadpan jokes no one gets. "You stopped for half a second. Don't."
- **Takatsuki Shō:** the Rival, fast "like a whip." Being rewritten per fix 7. Look and voice approved Oct 8.

**Hoshino Kitchen [P]:**
- **Shiina Yuzu:** the work kōhai, a first-year at Shirasawa Commercial. Cheeky ("Point to Shiina"), flustered by sincerity, a brilliant customer handler. Honey-brown hair with a red clip. Look and dialogue approved Oct 8; **her introduction moves to around May–June** (§1b).
- **The manager:** harried and balding. "You're a lifesaver," about nine times a shift.

**Elsewhere [P]:**
- **Chie:** Natsuki's confidant, by text only. Close to her in 4th and 8th grade. Sends zunda mochi every New Year.

**The past-life girl:** speaker label "???". She waits under the low branch. Thatched roofs and flooded paddies; a stone and a shimenawa rope before the shrine existed. In the pilot she ties a strap around the dreamer's wrist; per fix 23 she binds a cut on his wrist. See fix 12 for her costume. **v2 [P]:** she binds a strip of cloth around the inside of his left wrist, cut "where a blade got past me in training"; her voice is Despina (style guide §7).

### v2 Ch1 revision, Oct 18: new provisional details [P]
Production thread; the full record is in `production/pilot-v2/reviews/ch1/` (continuity, cold reads round 1 and 2).
- **Cold open (P.0):**
  - A misty morning on a narrow modern road at a bend: an orange convex traffic mirror, a hedge, a block wall, utility poles.
  - A hand in a dark navy zip-up jacket on the grip of a sheathed sword.
  - The mist parting on both sides of the road, as if something huge were passing.
  - Wordless, about 12 seconds, opening the game before Ch1's title card.
- **Home:**
  - Dad's line is on the whiteboard on the fridge (not a calendar). Pickup moved to Tuesday and Friday last fall.
  - Kōhei asks Akane every morning how she slept.
  - The kitchen: the back door, mugs in the cupboard left of the sink, the drawer that sticks, the window latch. Nanoha has known the drawer since she was six.
  - He gave up arguing about the food around last summer.
  - The garbage point is at the corner; her front door is about ten feet from his.
- **Kōhei's week:** Saturday afternoons are his only free time; he gives them to the shrine sweep.
- **The walk and school:**
  - The Ōzakura, "older than anyone's records," looks like a pink cloud on the hillside from the bridge.
  - Same class four years running. ~~Kōhei spent five days in 1-C during last year's exchange program ("a scheduling error," per the minutes).~~ Cut Oct 24 with the rest of the old bit; Nanoha's theory is now a staff-room folder (see Oct 24 below).
  - About 200 second-years; the class lists go up at the entrance; they arrive at 7:50.
  - Fukuda is in 2-E this year.
  - The seating: Kōhei in the second-to-last row by the window, Natsuki behind him, Nanoha two rows over, Tokiwa near the front.
  - The full timetable is handed out on day one.
- **Natsuki:**
  - Loves horror movies, "the cheesier the better."
  - Two club invitations and karaoke on her first morning. ~~The gossip about Kōhei's three turned-down confessions came from "the girl by the door."~~ Out of Ch1 since Oct 24 (author): the confessions come up later, between Nanoha and Rika (Story thread).
  - Asks Nanoha whether the building is haunted (something knocking in the music room); "the pipes sound like a ghost."
  - She lives by the station; Nanoha walked her home after the tour.
- **Ryōsuke:** argues that taiyaki are eaten head first ("thermodynamics").
- **Rika:** a different novelty clip every day; matching keychains.
- **Shrine:** the Saturday sweep; Genji's back.
- **Engine:** the chapter menu starts Chapter 1 at the cold open (no separate Prologue entry); the developer scene chart labels it "COLD OPEN."
- **Ch1 punch list, Oct 19:**
  - Translator's notes on Japanese words (tap the underlined term; Settings → Notes lists them): karaage, fusuma, kinpira, taiyaki, shodan. The wording of each note is [P] (`production/pilot-v2/script/notes.txt`).
  - Nanoha's small hair clip (left side) is kept as the sprites draw it; the author approved it Oct 20, so it's no longer [P] (style guide §2).
  - Her height is played as one kitchen joke plus "Chibi"; the collar scene no longer has her on her toes.
- **Natsuki's Oct 20 look in Ch1:**
  - Her arrival line, with no hair color (author, Oct 20): "Her hair falls long, in soft waves, brushed until it shines."
  - In the title art she no longer carries her school bag (both redraws dropped it).
- **Ch1 punch list, Oct 24** (record: `production/pilot-v2/reviews/ch1/punch-oct24.md`):
  - Her arrival line, second sentence (author picked it from three): "She smiles at the whole room at once, which shouldn't be possible."
  - The classroom whispers when she walks in (author's request; the wording is [P]): "Whoa." "She's so pretty." "Is she an idol or something?" Someone two rows up leans into the aisle.
  - Nanoha's class theory (author approved the rewrite): a staff-room folder with both their names on it, "Do not separate," underlined twice; "If they split us up, I'd have to make new friends… Least of all the new friends"; "Rika-chan counts as several." Kōhei's narration later: Nanoha two rows over "apparently satisfies the folder."
  - Lunch (author's direction; the wording is [P]): what they like about kendo. Kōhei has done kendo "since I was little"; the best part is "having a sword in my hand… I've always been comfortable holding one. Since the first time I picked one up"; in narration, with one in his hands everything else goes quiet for a while. Natsuki's favorite part is the bow at the start: "Six new schools. Every dojo bows the same way." Also, you can yell in a room full of people and nobody calls your parents.
  - New faces: Nanoha's `dry` (a deadpan joke with a hidden smile) and Natsuki's `curious`; deadpan and smirk now go on punchlines only (style guide §3).
  - Natsuki's face A and her new voice (Zephyr, brighter direction, +1 semitone) are author decisions, not [P].

### v2 Ch2 "Kendo", Oct 24: new provisional details [P]
Production thread; the line-by-line list is in `production/pilot-v2/reviews/ch2/continuity.md` ("New [P] details"), the handover in `reviews/ch2/handover-oct25.md`.
- **Hoshino Kitchen:** closes at 9; Tuesday shift 5:30 to close; Kōhei on dish pit, drink bar and register; numbered tables, a window booth, a noisy dishwasher, an automatic door; the brown apron with a cartoon chef on the pocket, tied like a hakama. The manager mistakes Natsuki for staff ("Lifesaver" ×9). Kōhei's work clothes are drawn as a T-shirt and bib apron (style guide §2 says white shirt and waist apron; the author picks).
- **Home:** on shift nights Akane's dinner waits in the fridge with a note, and she texts a photo of the empty container at seven.
- **Natsuki at the restaurant:** with five 2-B girls after karaoke ("everybody gets the strawberry parfait"); the kids' plate isn't ID-checked; she photographs it from three angles and keeps the paper flag (later in her pen cup).
- **Town:** the mountain looks walkable from the station; a taiyaki stand at the north exit (good red bean, burnt custard); the convenience-store drink fridge that freezes everything; the lower river path floods in June, herons on the bike racks; the bridge lies between the station and his hill, with streetlights along the railing and trains toward the station; the Ōzakura shows at dusk as a small pale tree on the hill.
- **Club:** practices run two hours; Takatsuki does suburi alone before them; Kōhei's hakama knot has been off center for a year, and he and Takatsuki have trained together that long; Kirishima quiets a room without raising his voice; the session order (warm-ups, kirikaeshi, waza, break, shiai-geiko); a schedule whiteboard by the door and a lost-and-found box (Natsuki's borrowed glasses); first-years mop, Kōhei usually stays.
- **Kendo details:** form faults (Kōhei's low left heel, wandering tip, men from the wrong distance, left foot forward on dō; Natsuki's dropped left shoulder before men); the practice match ends 1–1, kote then nuki-dō, on time.
- **Rika:** her art-club assignment is "People in motion."
- **Natsuki:** she photographs every town she lives in ("Sapporo is four hundred pictures of snow," since the Oct 25 punch list; it was "mostly vending machines"); she's wanted to photograph the Ōzakura since Monday; she offers extra practice "mornings, weekends." Home: her mother's first-week notes ("curry in the fridge, back late, proud of you"); her father in Yokohama until Friday; unpacked boxes labeled SAPPORO→SENDAI→SHIRASAWA; Chie's pinned chat and their birthday calls; a small balcony over a cherry-lined street that runs along the river; eleven photos, one sent.
- **Production:** the match insert runs 3 pages (the outline said 2) so the dō is a page-turn reveal; the opening panel shows them crouched at the line (not full sonkyo); the kote panel has his hands at chin height as he starts to lift; the classmate at the restaurant is voiced by Callirrhoe (for the Audio thread); Natsuki's teach sprite holds the shinai up past her head.
- **Ch2 punch list, Oct 25** (record `production/pilot-v2/reviews/ch2/punch-oct25.md`):
  - **The Wednesday-morning kitchen scene** (new, c2_0303–c2_0324; the author asked for a little Nanoha in Ch2 and left the shape to Production): Akane upstairs "losing an argument with her hair"; Nanoha's "Again." with her mom's food (the Ch1 ritual; the Tuesday-night container line is cut); she hears at once that his voice is rough ("You sound like you've been talking." / "You work in the dish pit."); he tells her Mizuno came in after karaoke and stayed till close; "That one's new." "Face. I'll have to give it a number." / "I'll tell you when I've decided" (her catalogue of his faces); a honey throat lozenge, "For the talking"; on the walk she's quiet a little longer than usual, then asks how many first-years the club expects.
  - Natsuki's whiteboard (CG `cg_whiteboard`): a board on legs by the dojo door, her stick figure with the enormous worried head, labels "KENDO / lesson 1", "MEN / head", "KOTE / wrist (right one!)", "TSUKI / throat / not until high school!!", "DŌ / side".
  - Her interlude: "Natsuki liked her, and not the first-week way, where you like everyone." / "Nanoha lived next door to Fujisawa. Natsuki decided that was none of her business, and didn't quite believe herself."
  - Small wording: c2_0090 names "Mizuno"; "whoever stays after practice cleans the floor"; Wednesday's practice is "After school."

## 4. Address guide
**Superseded Oct 17 by style guide §3c** (address forms, Japanese pronouns and the planned name changes). The pilot's table matched it except: Sōta is now Mio ("Kō-nii" kept), and Kōhei teases Nanoha as "Chibi."

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
