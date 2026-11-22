# Continuity check (§9 step 3a): Pilot v2, cold open + Ch1 draft

**Draft:** `production/pilot-v2/script/ch01.ozs` (line numbers below are this file's unless another file is named).
**Read against:** `story/canon.md`, `story/chapter-map.md` (Ch1 row, running threads, windows, clue ledger), `story/pilot-notes.md` §3 (and §5 where cited), `story/style-guide.md` §1a–§2 and §3b–§3c (§3a where staging needed it), `production/pilot-v2/scene-outline.md`.

**Verdict:** no hard canon contradictions. Heights, dates, the schedule, family facts and every address form check out. There are 11 problems. The two that matter most are reader-knowledge problems: one exchange ties the Ōzakura to Nanoha's family in Ch1, against outline decision 5, and an unlogged Natsuki pointer sits right before the dream. Two more are checks on the art and labels that I couldn't run from the text alone; if either fails, the build reveals who the dream woman is.

---

## Problems, most important first

### 1. The shrine sweep ties the Ōzakura to Nanoha in Ch1, and it uses up Ch3's gag (medium-high)
**Lines 147–151:**
> nanoha: "Oh. Grandpa says the shrine's cherries are the best they've been in years. I'm helping him sweep up there Saturday."
> kohei: "His back again?"
> nanoha: "His back is a very convenient back. It only hurts on days with a lot of petals."
> kohei: "I'll come after practice. Somebody has to carry the trash bags while you supervise."
> nanoha: "I do supervise beautifully."

- **Why it's a problem:**
  - Outline decision 5 (`scene-outline.md` line 153) puts the Ōzakura sentence in the river walk "Neutral, not tied to either girl." Line 107 does that. Forty lines later, though, this exchange tells the reader that Nanoha's grandfather looks after the shrine where the Ōzakura stands, and the dream's branch and petals arrive that same night.
  - The Ch1 direction (outline line 146) says "don't leave Ch1 tilted toward Nanoha as the dream woman, since Ch3–4 tilt that way on their own."
  - The clue ledger (`chapter-map.md` lines 123 and 125) holds "The Ōzakura is her family's tree" back as a Ch3 pointer. In Ch1 it's an extra Nanoha pointer that nobody has logged.
  - It also spends the "very convenient back" bit, which the outline gives to 3.5 (outline line 81: "Sweeping with Nanoha; her grandfather's 'very convenient back'"). Ch3 would have to repeat it.
- **Fix:**
  - Cut 147–151. Line 152 ("She walks a little faster after that…") then has nothing to follow, so either cut it too or hang it on "Saturday afternoons are free" (she brightens because he has a free afternoon at all).
  - Ch3 sets up the sweep (the 3.3 window talk can do it) and keeps the back gag.
  - Update the pilot-notes §3 entries that record this as Ch1 material (lines 215 and 230).

### 2. An unlogged Natsuki pointer just before the dream, plus a line that makes her the trigger (medium)
**Line 357:** "In bed I run my thumb over the callus on my left palm." (#c1_0264, new)
**Line 365:** "Tonight, it comes back."

- **Why it's a problem:**
  - Neither beat is in the outline. Outline 1.7–1.8 (line 34) reads "that night he falls asleep, and the dream comes. Ending the day he met both girls on it keeps it from pointing at either."
  - The callus line isn't in the Ch1 clue ledger either (`chapter-map.md` line 123).
  - The callus is the thing Natsuki read at first sight (line 234). Make it the last image before sleep, follow it with "Tonight, it comes back" on the day she arrived, and the dream reads as cause and effect: she brought it back. That's the strongest spot in the chapter for a pointer.
  - A lean toward Natsuki is wanted, but the cap is 60% (outline lines 138 and 178; canon line 377).
  - The baseline for calibrating isn't settled. The outline's "Where Ch1 stands" (line 140) has Natsuki at 60 on the dream, if its triples run ending/wanting/dream. The chapter map's summary (line 9) says two of three readers leaned Nanoha. The two docs disagree, so nobody knows how much room is left.
- **Fix:** this is a clue-calibration call, so the Production thread decides it, but it should be made on purpose. My recommendation:
  - Keep 357 and add it to the ledger as a Ch1 Natsuki pointer.
  - Remove the trigger: change 365 to "Some nights it comes back." or cut it, since 363–364 already make the dream a recurring one.
  - Watch the end-of-Ch1 dream number in the cold reads.

### 3. The dream CG against canon's Oct 18 hair rule; the style guide is stale (medium, needs a visual check)
- **What's on the page:** the text is clean (lines 366–379: no face, no hair).
- **What canon says:** canon §5 (line 207, Oct 18) says "her hair is hidden too until the bloom… so nothing settles who she is."
- **Where the docs lag:**
  - Style guide §2 (line 92) still gives past-life Natsuki as "Copper, tied back with a plain cord." It was never updated.
  - The outline's living-still list for the dream (line 16) says "petals, **the cord**, her sleeve," but the text binds the wrist with "a strip of cloth" (line 375).
- **The risk:** if `cg_dream` was prompted from §2, one copper strand or a hair cord in frame settles the dream woman in Ch1.
- **Fix:**
  - Check `cg_dream` and its loop for any visible hair.
  - Make the binding read as cloth to match line 375, or change 375 to "cord" if the art shows a cord.
  - Add the Oct 18 rule to style guide §2's past-life row (Production owns §1–§6).

### 4. The speaker id `past_natsuki` names her (medium, needs a check of the compiled build)
- **Where:** lines 371 and 374, `past_natsuki: "You're late." …`
- **What the docs say:** pilot-notes §3 (line 200) and style guide §3a (line 155) both give the displayed label as "???". The id itself is the answer to a question canon keeps unsettled until Ch30 (canon line 377).
- **What to check:** I couldn't confirm what the compiler shows, because the compiler isn't among the files for this check. Make sure the name tag, backlog, dev scene chart and cold-read packet all show "???", and that no voice filename or alt text carries the id.
- **Fix:** rename the id to something neutral (say `dream_woman`) so it can't leak. The missing face window is correct (§3a rule 4).

### 5. "There's never a knock" contradicts the FB6 origin (low-medium)
- **Line 73:** "The back door slides open. No knock. There's never a knock."
- **Why:** canon §6 FB6 (line 351) is "the night Kōhei sits at the kitchen table with the bills… Nanoha comes in through the kitchen without knocking **for the first time**… The origin of her… walking in without knocking." Ch21 shows that origin. "Never" says there was never a knock at all.
- **Fix:** "No knock. There's never a knock anymore." The word "anymore" plants FB6 without explaining it.

### 6. Dad's death is implied, not shown (low; reader target)
- **What the target says:** outline "Know" (line 143) includes "Dad died last spring."
- **What the draft has:** it never says so. The reader gets his handwriting "last spring", "I've never written over it" (line 53) and the trash (line 327). Most readers will infer it; a few may read divorce or a father working away.
- **Fix:** ask the cold readers what happened to the father. If anyone misses it, add one detail that shows it instead of a statement. For example, in 1.1, a photo and incense on a small butsudan seen from the kitchen (new [P]).

### 7. Ōno-sensei speaks off-sprite without a face window (low; staging)
- **Line 227:** `teacher: "Thank you, Mizuno. Let's see…"`. His sprite was hidden at 207, and `cg_natsuki_intro` is up (209/222).
- **Rule:** style guide §3a rule 2 (line 126) puts a window on a speaker whose sprite isn't on screen, and line 128 says Ōno follows rule 2 since v2.
- **Fix:** `teacher(neutral): "Thank you, Mizuno. …"`

### 8. The class-list logic slips (low)
- **The sequence:**
  - Line 102: Rika tells Nanoha she's in 2-B, with Kōhei standing there.
  - Line 191: "You found mine before yours?"
  - Line 193: "She went looking for mine before her own."
- **Why:** she already knew her own class. The real tell, that Fukuda isn't in 2-B, still lands.
- **Fix:**
  - Line 191 becomes "That was fast." (早いな。).
  - Line 193 becomes "…He's in Two-E. She didn't find mine under his. She went looking for it."

### 9. "The Tanzawa" names the real range (low; an Open item)
- **Line 146:** "fat with spring rain off the Tanzawa."
- **Why:** canon §3 gives "a **Tanzawa-style** mountain backdrop" (line 103) and keeps the exact map Open (line 108). Naming the real range pins the fictional town to the real mountains.
- **Related change:** the line also replaces pilot-notes §5's "fat with snowmelt" (line 237). Spring rain fits canon's mild, little-snow winter (line 106) better, so keep that part.
- **Fix:** either log "the Tanzawa" as [P] and update §5, or write "fat with spring rain off the mountains."

### 10. The lunch thread needs a handover note (low)
- **What Ch1 sets up:** lines 50 and 67–70 have Kōhei making two lunches, his and Akane's, and Akane offering to make her own.
- **What canon expects later:**
  - Scene bank 13c (canon line 678) assumes that "Nanoha has been making Kōhei's school lunch" by the dueling lunches in Ch11.
  - The Akane proposal at canon line 571 has "Nanoha-chan made you lunch *again*."
- **Why it matters:** nothing conflicts in Ch1. But the switch to Nanoha making his lunch has to happen on screen somewhere in Ch2–10, or Ch11 reads as a jump.
- **Fix:** put it in the handover for the Story thread.

### 11. Rika's clips: a promise the sprites can't keep (low; art continuity)
- **Line 104:** "Today's clips are a strawberry, a star and a small frog wearing a crown. The frog is new."
- **Why:** pilot-notes §3 (line 229) records this as "a different novelty clip every day." Style guide §2 (line 93) and her sprites fix the set at strawberry, star and frog, so daily changes would show the same clips every day.
- **Fix:**
  - Change the line to "Her clips are a strawberry, a star and, new this week, a small frog wearing a crown."
  - Correct the pilot-notes entry to "adds a clip now and then."

---

## What's fine
- **Dates and schedule:**
  - The card reads Monday, April 7, matching the chapter-map row and pilot-notes ("Apr 7 is a Monday").
  - The whiteboard (52) and the spoken schedule (140) match canon §8's illustrative week: Mon/Wed/Fri plus Saturday morning, shifts Tue/Thu/Sun.
  - "Club doesn't start until Wednesday" matches Ch2's Wednesday first practice. Saturday practice followed by the sweep matches Ch3.
- **Heights and builds:**
  - The collar on her toes and "the extra inches since middle school" (75) fit 4′11″ against 5′9″ (head at his chin) and §3c's line that he shot past her at the start of middle school.
  - Nothing touches Natsuki's 5′3″ or her build, which canon keeps Open.
  - Her hair is "cut neat at her shoulders and tucked behind one ear," per canon §8. It's plain description, and nobody remarks on the color.
- **Family:**
  - Mom's fusuma, the knock, the silence and the creak follow fix 21.
  - Akane is in her sailor uniform all chapter (the outline moved her home outfit to Ch3). She's sweet and resists being managed by pouting, and her dizzy spells stay undiagnosed.
  - Dad's line dates from "last spring" (fix 11).
  - The food has come for "about a year" and he gave up arguing "around last summer," which lines up with FB6 after the funeral.
  - "Since we were born" and "sixteen years" are both right.
- **Who knows what:**
  - The gossip routes are plausible: Rika's rumor, Ōno's "channels", "the girl by the door".
  - Nanoha caught his smile while he thinks he alone saw Natsuki's falter, which is good dramatic irony.
  - Natsuki asks Nanoha, never him, to use her given name, with him sitting right there (§3c).
- **Open items kept open:**
  - His rank ("What are you, shodan?" / "We'll find out on the floor"), Akane's diagnosis, Natsuki's father's job, shrine architecture and travel times are all left vague.
  - Names are in kana throughout. There's no fairy and no beast shape.
  - Shirasawa, Hoshino Kitchen, Ōno, Fukuda, the clinic day and "Natsuki lives by the station" (a canon Proposal) are already listed as [P].
- **Address and pronouns (§3c):** every form matches.
  - Kōhei never says "Nanoha" aloud, which keeps Ch25 intact. "Night, Chibi" / おやすみ、チビ is planted, answering "Good night, Kō-chan."
  - "Kō-chan" comes up only in private (the river walk, the doorstep).
  - Natsuki uses *kimi* and a bare "Fujisawa", and says "Nanoha" from day one.
  - Nanoha goes "Mizuno-san" → "Natsuki-san" ("I'm working up to it") and is still on "-san" that night (334).
  - Rika uses *atashi*, "Nano-chan" and "Fujisawa-kun".
  - Akane uses "Onii-chan" and "Nanoha-chan".
  - Ōno says "Sensei" for himself and bare surnames for students.
  - Kōhei uses *Kaa-san* and *Oba-san*, *omae* to Nanoha and Akane, and never *omae* to Natsuki.
  - The past-life lines are in *desu/masu*, with no name.
  - The narration uses "Tokiwa," "Mizuno" and "Nanoha," and the interlude follows Nanoha.
- **Staging:**
  - Time of day runs straight through: 5:40 daylight (sunrise is about 5:20), 7:50, lunch, the evening sun on the tour, night, bed.
  - Nanoha is in uniform with her braid all day and still has her school bag at night, because she came straight from walking Natsuki home.
  - The left-hand chain holds: he raises his left hand (228), she reads the left palm (234), and he touches it in bed (357).
  - Natsuki sits behind him by the window, which pays off in "the desk in front of her own" (293).
  - Kōhei has a face window on every spoken line, and Nanoha has hers in the interlude (§3a rules 1 and 3).
- **Outline decisions:**
  - Decisions 1, 2, 3, 6, 7, 9, 10 and 11 are all in. Decision 5 is placed correctly, though see problem 1.
  - Decision 4 (the dream voice) is audio and wasn't checked here.
  - The cold open has no faces, no voices, nothing period, and the mirror appears twice.
- **The reader target otherwise holds:**
  - The cold open promises danger.
  - There's no snow anywhere, so Ch3's comes first.
  - Nothing hints at how the past life ended.
  - The dream carries every element the target asks for: the river, the branch, the petals, the bound wrist, "You're late," and a swordsman (implied by "a blade got past me in training").
  - Both girls read as love interests.
- **The trash-day logic:** the line says Monday, he takes the bag out Monday *night*, and pickup is Tuesday. That's wrong on both schedules, but his "I'm moving it closer to the right day" turns the gap into the joke.

---

## New [P] details the draft invents
**Not yet in pilot-notes §3** (for the handover and pilot-notes):
1. Akane's warning signs as Kōhei checks them: her color, leaning on the doorframe, holding her head "when the room starts tilting" (63). Canon wants her symptoms kept consistent.
2. House layout: Kōhei's room is upstairs; Mom's room is downstairs behind a fusuma off the kitchen (45, 54, 96–99).
3. Each morning he tells Mom through the fusuma that there's rice in the cooker and miso on the stove (97).
4. The two lunches are his and Akane's, and Akane offers to make her own (50, 68–69). This bears on canon 13c.
5. Nanoha calls out "I'm coming in" (おじゃましまーす) after she's already in (76–78).
6. Club practice starts on Wednesday of the first week (138, 263).
7. The river runs "fat with spring rain off the Tanzawa" (146). This replaces pilot §5's snowmelt and names the real range; see problem 9.
8. Nanoha walks on the river side, kept from the pilot and now unexplained (109).
9. Rika eats taiyaki tail first. Ryōsuke promises a diagram for lunch and is drawing it in homeroom (175, 178, 200).
10. Rika's clips change ("The frog is new") (104); see problem 11.
11. Fukuda was in their class in earlier years, implied by "always right under Fukuda-kun's" (192).
12. Day-one logistics: the opening ceremony comes after the class lists, and there's a first period and lunch (194, 239, 241).
13. School details: a shoe locker that sticks and a vending machine that eats coins; the tour covers the library, the music rooms and the gym; Kōhei knows the eleventh step squeaks (272, 319, 333).
14. The tour ends in 2-B's empty classroom in the evening sun, with Natsuki leaning on Kōhei's desk (293).
15. As far as Nanoha knows, Kōhei has never competed in Tōhoku (307–308).
16. Natsuki carries a ballpoint in her blazer pocket (265); the 水 itself is already recorded.
17. The bedtime callus beat (357); see problem 2.
18. The cold open plays with no music (24). The outline offered "none, or wind only."

**Already in pilot-notes §3 and matching the draft:** the cold-open images; the whiteboard and Dad's Mon/Thu line; pickup moving to Tue/Fri; asking Akane how she slept; the back door, mugs, drawer and latch; the drawer since she was six; food for a year, gave up last summer; the garbage point at the corner and her door ten feet away; Saturday afternoons free; the Ōzakura sentence; four years in one class and the 1-C exchange; about 200 second-years and 7:50; Fukuda in 2-E; the seating; horror movies; the two clubs, karaoke and "the girl by the door"; the haunted music room and its pipes; Natsuki living by the station; taiyaki; matching keychains; 水 on her wrist; "Sendai, most recently"; the collar CG.

**Pilot-notes §3 entries that overstate the draft:**
- "Saturday afternoons are his only free time; he gives them to the shrine sweep." The draft has only *this* Saturday's sweep, and canon's week also leaves part of Sunday free. See problem 1 as well.
- "Rika: a different novelty clip every day." See problem 11.
- "Cold open… about 12 seconds." The waits add up to 13.8 s before fades.
- The dream's cut is on "the inside of his left wrist." The text says only "wrist," which is fine if the CG shows the left.

---

## Outside this check (not counted)
- **Speech-sheet tics (§3b line 167):**
  - "She says it like…" appears three times in the dream (371–373). That's kept prologue text, but the rule allows it once per chapter.
  - "The way she holds things" (269) and "the way you shut a window" (320) both appear in the chapter.
  - Nanoha's public register gets three dry lines with Natsuki (272, 275, 280) against "at most one."
- **Plausibility:** a real Japanese opening-ceremony day usually ends around noon. The outline chose lunch and an after-school tour, which stands under canon §2's "manga plausibility."
