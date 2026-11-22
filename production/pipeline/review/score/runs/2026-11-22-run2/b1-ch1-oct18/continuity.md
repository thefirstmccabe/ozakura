# Continuity check: Pilot v2 Ch1 (cold open + Ch1), §9 step 3a

**Draft checked:** `production/pilot-v2/script/ch01.ozs` (all 383 lines).
**Against:** `story/canon.md`, `story/chapter-map.md` (Ch1 row, running threads, clue ledger), `story/pilot-notes.md` (§1 fixes, §3 [P] inventions), `story/style-guide.md` §1a–§2 and §3b–§3c, and the reader-knowledge targets and scene list in `production/pilot-v2/scene-outline.md`. There are no earlier chapters to check against.

**Verdict:** the draft is clean on the hard facts: schedule, calendar, family, heights, house layout, address forms. It applies all eleven of the outline's Ch1 decisions. I found **16 problems**. Two matter before handover: (1) a scene that ties the Ōzakura to Nanoha's family, which the outline puts in Ch3, and which pushes the dream-woman question toward Nanoha in the chapter that was supposed to correct that tilt; (2) the dream woman's speaker id names her. Two smaller logic slips can each be fixed by re-voicing one line. Everything else is low priority. I also list 6 checks I couldn't make from text alone.

Line numbers are file lines in `ch01.ozs`, with the line id.

---

## Problems, most important first

### 1. HIGH: The shrine-sweep exchange gives Ch1 an extra Nanoha clue and uses up a Ch3 beat (reader target; staging)
**Where:** lines 147–152 (c1_0093–c1_0098).
> nanoha: "Oh. Grandpa says the shrine's cherries are the best they've been in years. I'm helping him sweep up there Saturday."
> kohei: "His back again?"
> nanoha: "His back is a very convenient back. It only hurts on days with a lot of petals."

**Why it's a problem:**
- Outline decision 5 (scene-outline line 153) puts the Ōzakura sentence in the river walk so the tree is introduced "neutral, not tied to either girl." Forty lines later this exchange ties "the shrine's cherries" to Nanoha's family.
- The clue ledger (chapter-map line 125) places "The Ōzakura is her family's tree" in **Ch3**, in the Nanoha column. Canon §5 (line 379) uses that fact as one of Nanoha's red herrings.
- Ch1's only planned Nanoha clue is the collar (ledger line 123), and the outline's direction (line 146) is not to leave Ch1 tilted toward Nanoha "since Ch3–4 tilt that way on their own." With this exchange the reader gets a river, cherry trees, and Nanoha's family's sacred tree before a dream of a river, a branch and petals.
- It also spends Ch3's joke. Scene 3.5 (outline line 81) lists "her grandfather's 'very convenient back'" as a beat. Ch1 now uses it almost word for word.
- It isn't in the outline: 1.2 is "just the two of them, easy; she fixes his collar."

**Fix (preferred):**
- Cut lines 147–152 and end the walk on line 146 ("A few steps of nothing. The river is loud…") followed by `@hide nanoha`. Kōhei's "Saturday afternoons are free" / "Mm." still lands.
- Set up the sweep in Ch3 (3.2 at home, or on Saturday itself) and keep the back joke for 3.5.
- Update pilot-notes §3, lines 215 and 228, to match.

**Fix (if kept):** drop the back joke here (Ch3 keeps it), add the shrine link to the ledger's Ch1 Nanoha column, and let cold reads judge the balance.

### 2. HIGH: The dream woman's speaker id names her (reader target; verify the UI)
**Where:** lines 371 and 374 (p_0007, p_0010): `past_natsuki: "You're late."` and `past_natsuki: "Hurt again…"`.

**Why:** pilot-notes §3 (line 200) gives her name tag as "???", and §3a forbids face windows for "???". I can't confirm from these files that the compiler hides the id. If the id reaches a name tag, the backlog, the dev scene chart or the cold-read packet, it answers "who is the dream woman" in Ch1 and voids the measurement. Even if the UI hides it, the id sits in public source and in the voice job list (the repo is public).

**Fix:**
- Rename the speaker to something neutral, such as `dream_woman`, in the script, the voice jobs and the file names.
- Confirm the compiled name tag reads "???".
- Confirm the cold-read packet shows only "???".

### 3. MEDIUM: Kōhei's narration knows something nobody has told him (who knows what)
**Where:** line 328 (c1_0236).
> That's when Nanoha comes up the street with her school bag over her shoulder, back from walking Mizuno home to her place by the station.

**Why:** in first person, Kōhei can't know yet that Nanoha walked Mizuno home, or where Mizuno lives. She hasn't said a word. Mizuno living by the station is also only a Proposal in canon (line 110).

**Fix:**
- Line 328 becomes: "That's when Nanoha comes up the street from the station end, school bag over her shoulder."
- Line 332 (c1_0239) becomes: "Good. I walked her home after. She noticed the squeaky stairs. Both of them." / よかったよ。帰り、送ってきた。階段のきしむところ、気づいてた。二か所とも。
- That's one line to re-voice.

### 4. MEDIUM: Rika tells Nanoha her class, which spoils the class-list payoff (internal logic)
**Where:** line 163 (c1_0102), against lines 191 and 193 (c1_0129, c1_0131).
- Rika's line: "Two-B! You're in Two-B! I'm in Two-B! It's destiny!"
- Then Kōhei asks, "You found mine before yours?", and the beat that sticks with him all through the ceremony is "She went looking for mine before her own."

**Why:** Rika has just told Nanoha she's in 2-B, so Nanoha had no "own" left to look for. The payoff loses its footing.

**Fix:** Rika announces only her own class and begs.
- English: "Two-B! I'm in Two-B! Nano-chan, you have to be Two-B! If you're Two-B it's destiny! I'll make us matching keychains!"
- Japanese: 二年B組！ あたし二のB！ なのちゃんも二のBでいてよ！ 二のBだったら運命だよ！ おそろいのキーホルダー作るから！
- One Rika line to re-voice.

### 5. MEDIUM: Ch1 says Kōhei makes his own lunch; canon later has Nanoha making it (forward continuity; Story thread)
**Where:**
- Line 50 (c1_0006): "Two lunch boxes."
- Line 69 (c1_0023): "I'm already making two."
- Line 284 (c1_0202): "It's good rice. I made it myself."

**Against:**
- Canon scene bank 13c (line 678): "Nanoha **has been making** Kōhei's school lunch; Natsuki starts bringing him one too."
- Canon §8 Akane (line 571): "Nanoha-chan made you lunch *again*."
- Chapter map Ch11 (line 43): Nanoha's lunches are "the familiar food he likes."

**Why:** Ch1 is right as written. But nothing between Ch1 and Ch11 shows Nanoha taking over his lunch, so Ch11 would contradict Ch1.

**Fix:** a handoff to Story. Add a beat to the map, or reword 13c.
- **Proposal:** after his Ch6 collapse from double shifts, Nanoha quietly starts making his lunch. That's one less thing he carries, and it fits Akane's "again."
- No change to Ch1.

### 6. LOW–MEDIUM: "Dad died last spring" is only implied (reader target)
**Where:** line 53 (c1_0009), "…in Dad's. He wrote it last spring. I've never written over it."; and line 327 (c1_0235).

**Why:** the outline's Know list (line 143) includes "Dad died last spring." The text dates the handwriting, not the death, so a reader could take it as divorce or absence. Most readers will infer death, especially with Mom behind the fusuma.

**Fix:** watch for it in cold reads. If any reader misses it, add one shown action before he knocks on the fusuma. For example, he sets out rice and water at the family altar. That's a shown beat, not backstory, so the openings rule (canon line 70) is respected.

### 7. LOW: Natsuki's transfer count doesn't add up (facts)
**Where:** lines 213–214 (c1_0141/0143): "the new girl… six times now?" / 転校生をやるのは……六回目、かな？

**Against:**
- Pilot-notes §3 (line 158) lists six places (Sendai → Niigata → Okayama → Sapporo → Sendai → Shirasawa). That's five transfers if she started school in Sendai.
- Outline decision 2 (line 150) says "six schools' worth of new timetables," which also means five transfers.

**Fix (either way, easy to reverse):**
- Keep the line, since the hedge is in character. Add one earlier stop to the [P] town list and make the outline's wording "seven schools."
- Or change the line to "…fifth time? Sixth?" / 五回目……六回目だっけ？

### 8. LOW: Ch1 uses up two more beats the outline gives Ch3 (forward staging)
**Where:**
- Line 64 (c1_0018): Akane's "Onii-chan, you're hovering again." Outline 3.2 (line 75) uses "Onii-chan, you're hovering" as a Ch3 beat.
- Lines 336–337 (c1_0244–0245): Nanoha's "What did you think of her?" Outline 3.3 (line 77) has her asking lightly about the new girl and steering away.

**Fix:** no change to Ch1. Ch3 should play the "hovering" line as a callback and take the window question from a new angle, not repeat it. (Item 1 covers the back joke.)

### 9. LOW: Names the real Tanzawa range (Open: exact map; [P])
**Where:** line 146 (c1_0092): "fat with spring rain off the Tanzawa."

**Why:** canon §3 (line 103) gives the fictional town "a Tanzawa-style mountain backdrop," and line 108 says the exact map is Open. Naming the real range pins the town to real geography. Swapping the pilot's "snowmelt" for spring rain is good: it keeps snow out of Ch1, per decision 10.

**Fix:** "fat with spring rain off the mountains." Or keep it and record it as [P].

### 10. LOW (inherited, not the draft's to fix): the date card quietly fixes the year
**Where:** line 41, `@card Monday, April 7`.

**Why:**
- April 7 falls on a Monday in 2008, 2014, 2025 and 2031.
- Canon's era (line 109) is "smartphones and messaging apps everywhere, but before generative AI." Only 2014 fits that.
- Canon also says "The exact year is Open."
- The weekday comes from the chapter map and the pilot's timeline, not from this draft.

**Fix:** a note for Story. Either accept 2014 as Working, or drop the weekday from the card.

### 11. LOW: Akane leaves with them, then vanishes (staging)
**Where:** line 97 (c1_0048), "Mom, we're heading out," then the river walk is just the two of them (outline 1.2).

**Fix:** after line 100, add a half-line: "> Akane peels off at the corner toward the middle school."

### 12. LOW: Karaoke and the tour might be the same afternoon (staging)
**Where:** line 244 (c1_0162). By lunch Natsuki has "agreed to go to karaoke with a group of girls." She then spends the afternoon on Nanoha's tour and is walked home after dark.

**Fix:** give the karaoke a day: "agreed to go to karaoke on Friday with a group of girls…"

### 13. LOW: The dream woman's Japanese slips out of polite speech (style guide §3b–§3c)
**Where:** line 374 (p_0010): また怪我して。……手、見せてください。じっとして。

**Why:** §3b (line 189) and §3c (line 212) give her polite desu/masu, and じっとして is plain form.

**Fix:** じっとしていてください. It costs nothing, because decision 4 is re-voicing this line anyway.

### 14. LOW: Natsuki's "drawer" line hits Kōhei's actual drawer (clue ledger; Ch4 overlap)
**Where:** line 305 (c1_0217): "Someone who knows which drawer sticks in your kitchen."

**Why:**
- It names exactly the thing Nanoha does in Kōhei's kitchen (line 86).
- It can read as uncanny domestic knowledge (a wife's), which is a Natsuki clue the ledger doesn't list.
- It also anticipates Ch4's scene bank 3 discovery (outline 4.2, line 100).
- It's a protected line (decision 8), so keep it.

**Fix:** add it to the ledger's Ch1 Natsuki column. Make sure Ch4's discovery stays on the cups and the window, not the drawer.

### 15. LOW: The pilot-notes record overstates the script (record, not script)
**Where:** pilot-notes line 215 says "Saturday afternoons are his only free time." The script (line 144) says only "Saturday afternoons are free," and outline 4.2 has him free on Sunday after his lunch shift.

**Fix:** change the record to "Saturday afternoons are free (this week he gives his to the shrine sweep)."

### 16. LOW: The cold open's "sheathed sword" assumes a real heirloom blade (Open, recorded as [P])
**Where:** lines 26–33 (`cg_cold_hand`); described in pilot-notes line 206 as "the grip of a sheathed sword."

**Why:**
- Canon §2 (line 56) says only "a sword grip."
- "Sheathed" commits Ch40 to a real blade.
- Canon §6 (line 422) keeps the heirloom weapons as provisional, with their condition and practicality Open.
- The navy zip-up jacket also fixes Kōhei's Ch40 outfit.

**Fix:** keep both as [P], and note them on the Ch40 row so the climax art matches or the cold open gets re-cut.

---

## Checks I couldn't make from the text (verify before handover)
1. **`cg_dream`:**
   - No face, and **no hair**: canon §5 (line 207, Oct 18) hides her hair until the bloom.
   - A simple everyday kimono sleeve (fix 12).
   - The past-life palette: cool and desaturated, but never grayscale.
2. **The dream voice:** the two dream lines are re-voiced with the author's pick, a voice unlike either girl's (decision 4; canon revision Oct 18).
3. **`cg_collar`:** two-figure framing with no close-up of her hands (decision 7).
4. **Cold-open CGs:**
   - No face, mask or wolf shape.
   - No visible breath or snow, which would give away winter.
   - The same mirror passes twice. The script does repeat `cg_cold_mirror`.
5. **`bg_houses_night_lit`:** the facing windows are on the side walls inside the 3-foot gap. Seen from the street, the light should spill into the gap, not show in a window facing the street (line 353).
6. **`cg_natsuki_intro`, both variants:** shoulder-length restyle (fix 16).

---

## What is fine (checked and consistent)
- **Calendar:**
  - Mon Apr 7 matches the chapter map and the pilot timeline.
  - "Second year starts today" matches canon's hard start (Natsuki at the start of April).
  - The cherry trees in full bloom on Apr 7 and still dropping petals by Apr 12 is plausible for the foothills.
- **Schedule:** the whiteboard (line 52) and Kōhei's recital (line 140) match canon §8 exactly: kendo Mon, Wed, Fri and Saturday morning; shifts Tue, Thu and Sun. That lines up with the next chapters:
  - The first-week Wednesday start fits Ch2's first practice.
  - Saturday practice, then the sweep, fits Ch3.
  - The Sunday shift fits Ch4 4.2.
  - Monday practice fits 4.5.
- **Family:**
  - Dad's line "from last spring" (fix 11), followed by the pickup change last fall, is a coherent order.
  - The closed fusuma, the knock, no answer and the creak are kept (fix 21).
  - Akane is unwell, with no diagnosis named.
  - The food "for about a year" (line 84) and "never a knock" (line 73) line up with FB6: her first walk-in without knocking was after the funeral, when they were about 15. "Never" reads as "these days."
  - Akane's offer to make her own lunch fits canon: she isn't helpless and his help is partly unnecessary.
- **Heights and looks:**
  - Nanoha's height jokes fit 4′11″ against 5′9″, and §3c's "he shot past her in middle school."
  - Natsuki's hair is shoulder-length and tucked behind one ear, per the restyle. Copper is described plainly and no one remarks on it.
  - Imperial units only: ten feet between the doors, and a gap you could pass a book across. No metric anywhere.
- **Houses:** windows close enough to pass a book (canon §3), nothing between the houses, and the back door is the kitchen entry (FB6).
- **Address and pronouns (§3c), checked line by line:**
  - **Kōhei:**
    - He never says "Nanoha" aloud; his first time is Ch25.
    - He uses お前 with Nanoha and Akane.
    - His one "Night, Chibi" / おやすみ、チビ answers her "Good night, Kō-chan" exactly as planned, with "short-person direction" planted the same morning.
    - He uses 母さん with Mom and おばさん for Emi.
    - He uses a bare "Fujisawa"/"Mizuno" with Natsuki and never お前 to her.
  - **Nanoha:**
    - She uses "Kō-chan" only in private (the collar, good night) and "Kōhei" in public.
    - With Natsuki she goes "Mizuno-san" → "Natsuki-san" ("I'm working up to it"), stays on "-san" that night, and uses polite desu/masu while they're strangers.
  - **Natsuki:**
    - She uses きみ with Kōhei and a bare surname.
    - She calls Nanoha "Nanoha" from day one.
    - She asks Nanoha to call her Natsuki with Kōhei sitting right there, and never asks him.
  - **Everyone else:**
    - Akane: "Onii-chan," "Nanoha-chan."
    - Rika: "Nano-chan," "Fujisawa-kun," あたし.
    - Ōno: "Sensei" for himself and bare surnames for students.
    - Kōhei's narration says "Mizuno" and "Tokiwa," and Nanoha is always "Nanoha."
    - The interlude follows Nanoha.
- **Open items handled correctly:**
  - Name kanji stay in kana.
  - Natsuki's father's job is never named.
  - Her rank is dodged ("We'll find out on the floor").
  - No fairy in Ch1 (fix 2).
  - No shrine architecture.
  - No commute times.
  - The town and restaurant names are already recorded [P]s ("Shirasawa," "Hoshino Kitchen").
  - POV follows the pilot's convention.
- **Outline decisions 1–11 all applied:**
  - The cold open: wordless, no music, the mirror twice, then straight to the chapter card.
  - 水 written plainly on the inside of her left wrist.
  - The Sendai "seen him before" hook, without "This is going to sound weird."
  - The dream closes the chapter.
  - The Ōzakura sentence comes before Nanoha speaks.
  - "I don't remember when we decided that" is cut.
  - The collar CG is kept, and the text only notices her hands.
  - Natsuki's smaller smile and her "never stayed anywhere long enough" line are protected.
  - "Stubborn crease" is cut.
  - The snow simile is cut.
  - Taiyaki replaces hot dogs.
- **Fixes held:** no manga self-reference, no name-tag intros, no maternity ward, no flash at Natsuki's entrance, Kōhei is warm, and Akane is sweet.
- **Staging:**
  - Everyone is in school uniform all day. Akane stays in hers all of Ch1, per the Oct 17 change, and Nanoha's braid shows.
  - Time of day runs cleanly: 5:40, then 7:50, homeroom, lunch, evening sun, night.
  - Props carry over: two lunches lead to "I made it myself"; his left hand goes up because his right is clenched on the pen, so she sees the callus, which comes back in bed.
  - Seating holds: Natsuki behind him, last row by the window. She leans on "the desk in front of her own," his.
  - Kōhei is never on stage, only in face windows, per the outline's totals.

---

## Reader-knowledge target for Ch1 (outline lines 142–159)
- **Know: delivered.**
  - Danger comes from the cold open only.
  - Kōhei carrying the house, with Dad's death inferred (item 6).
  - Nanoha's hidden feelings, in the collar, the class list and the interlude's last line.
  - The dream: swordsman, bound wrist, "You're late," branch, petals, river.
  - The Ōzakura.
  - The mutual reaction on sight, left unexplained.
- **Not yet: held.**
  - Nothing is in the mist.
  - Neither girl remembers anything: Natsuki's "seen him before" stays ordinary, per decision 3.
  - Nothing about how that life ended.
  - No snow or winter.
- **Dream-woman balance: probably even to slightly Nanoha as drafted, against an outline that asked for no Nanoha tilt.**
  - **Toward Natsuki:**
    - Her falter and his pen grip.
    - 水 on the inside of her wrist, which rhymes with the cut on the inside of his.
    - The Sendai hook.
    - The callus she reads, with his thumb on it in bed just before the dream.
  - **Toward Nanoha:**
    - The collar (planned).
    - The shrine-family link (unplanned, item 1).
  - **Softer echoes to watch in cold reads, with no fix needed unless readers flag them:**
    - "You're taking out the trash on the wrong day" (line 330) is a scolding about timing just before "You're late."
    - Her lit window is the last image before bed.
    - The dream's "waiting a very long time" resonates with her sixteen years.
    - The dream's river is "close by" (line 367). Canon's layout puts the river *below* the tree, and the line could point at the embankment where the collar scene happened.
  - Cutting item 1 is the cheapest rebalance.
- **Both girls as love interests:**
  - Nanoha's is clear.
  - Kōhei's pull toward Natsuki reads mostly as rivalry, and Nanoha even names his smile "Somebody wants to fight me." The flustered "I—" (line 259) is the one romantic tell.
  - The map lists Ch2 as the first visible pull, so this isn't a Ch1 failure. Watch it in the window reads.

---

## New [P] details the draft invents (not yet in pilot-notes §3)
1. The river runs "fat with spring rain off the Tanzawa." It names the real range and replaces the pilot's snowmelt (line 146).
2. There's no kendo practice in the first week until Wednesday, Apr 9; Monday's session is skipped (lines 138, 263).
3. Rika is in 2-B, so all five friends share the class (line 163).
4. Rika eats taiyaki tail first ("save the best part for last"). The argument is due to resume at lunch with Ryōsuke's diagram (lines 175, 178).
5. Mom's room opens off the kitchen behind the fusuma, and Kōhei's room is upstairs (lines 46, 54).
6. Every morning Kōhei leaves Mom rice in the cooker and miso on the stove, and knocks twice (lines 96–97).
7. The rice goes on the timer the night before. Today's lunch: tamagoyaki, leftover spinach, the last of the frozen karaage (lines 50, 67).
8. Akane says she could make her own lunch, and he doesn't hand it over (lines 68–70).
9. Akane's bad-day tells: leaning on the doorframe, holding her head when the room tilts (line 63).
10. Nanoha walks on the river side. This is from the shipped pilot but was never recorded (line 109).
11. Kōhei and Nanoha walk to school together, and Rika treats it as worth remarking on (line 166).
12. The school has sticky shoe lockers, a vending machine that eats coins, and music rooms. The tour covered the library and the gym (lines 272, 319).
13. Natsuki has been the transfer student "six times" (see item 7) (line 214).
14. Natsuki wonders whether Kōhei has competed in Tōhoku. As far as Nanoha knows, he hasn't (lines 307–308).
15. Kōhei is right-handed, implied: the pen is in his right hand and he raises his left (lines 225, 228).
16. In the dream he held the cut closed "the whole way home," and the river is "close by" (lines 367–368).

**Already recorded, and the script matches:** the 5:40 alarm, two lunches, the whiteboard (Dad's line and the pickup change), the kitchen layout, the year of food, ten feet between the doors, the corner garbage point, the Ōzakura from the bridge, four years in one class and the 1-C exchange, about 200 second-years, arriving at 7:50, Fukuda in 2-E, the seating, the timetable handed out on day one, horror movies, the club invitations and karaoke, "the girl by the door," the pipes, Natsuki by the station, "Sendai, most recently," 水 on her wrist, taiyaki head first, the shrine sweep, and the cold-open details.

**Records to correct while filing:**
- "Only free time" (item 15).
- Rika's "a different novelty clip every day" (line 229). The script shows the style guide's fixed three clips ("The frog is new"), and her sprite is reused in Ch2–4. Record it as "occasionally a new clip," or plan for clip variants.
- The dream's "inside of his left wrist" (line 200). The script doesn't say which wrist, so the CG decides. Keep the record and the CG in agreement.

---

*Outside continuity, for the dialogue pass only:*
- The dream has three "She says it like…" lines in a row (lines 372–373), and §3b allows that construction once a chapter. They come from the prologue the author kept.
- Natsuki's "He's got kind of a normal one, right?" (line 312) brushes against §3b's no-verdicts rule.
