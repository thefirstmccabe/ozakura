# Continuity check: Ch2 "Kendo" (pilot v2, Oct 25 checkout)

§9 step 3a. Files read (under ROOT): `story/canon.md`, `story/chapter-map.md` (Ch1–2 rows, running threads, windows, clue ledger), `story/pilot-notes.md` (§1 fix list, §3), `story/style-guide.md` §1a–§2 and §3b–§3c, `production/pilot-v2/script/ch01.ozs`, `production/pilot-v2/script/ch02.ozs`, `production/pilot-v2/scene-outline.md` (Ch2 scenes and reader targets, plus the Ch3–4 rows where Ch2 hands off). Nothing was edited.

**Bottom line:** the draft is clean on the big things. Canon facts, the calendar, the practice and shift schedule, address forms, kendo accuracy, the hair-color and imperial-units rules, the fix-list cuts and the outline's "not yet" list all hold. I found **8 problems, none severe.** Fix 1 and 2 before cold reads. The rest are one-line fixes or record-keeping.

---

## Problems, most important first

### 1. Chie's timeline contradicts the recorded [P] (medium)
- `ch02.ozs:373` (c2_0280): "Chie had been her best friend in fourth grade, and again last year, when her dad's work had swung them back through Sendai like a pendulum."
- `pilot-notes.md:197`: "Close to her in 4th and 8th grade."
- **Why it matters:** Chie recurs (Ch4's texts, the Ch29 call, the Ch33 unsent drafts).
- **The draft's version is the more coherent one.** The move order is Sapporo → Sendai → Shirasawa (`pilot-notes.md:157`, and the boxes at `ch02.ozs:347`), and she answers "Sendai, most recently" (`ch01.ozs:246`). Put those together and "8th grade" means three-plus years in Sendai, which works against the six-moves premise.
- **Fix:** keep "last year" and change `pilot-notes.md:197` to "4th grade and last year (her first year of high school)" [P]. If the author wants 8th grade, change the draft to "and again in eighth grade."

### 2. Two unoutlined Nanoha closers in Natsuki's chapter (medium; reader-knowledge, judgment call)
- **End of 2.1,** `ch02.ozs:84` (c2_0299): "There's a plastic container on the kitchen table when I get in, with a sticky note on the lid in Nanoha's handwriting. It says 'Again.'"
- **End of 2.7,** `ch02.ozs:337–338` (c2_0301, c2_0251): "When I get to the house, the light's on in Nanoha's window across the gap." / "It's only trash bags."
- **What the outline says:** neither beat is in it (`scene-outline.md:51`, `:63`). The outline calls Ch2 "Natsuki's chapter" (`:49`). It gives the chapter one window job: pull the wanting back from Ch1's ~65 Nanoha toward even (`:170`). It blames Ch1's lean on structure: Nanoha had the first third, the interlude and the night scene (`:49`).
- **The effect:** these two lines put Nanoha back in the closing beat of two Ch2 scenes. 2.1 was meant to land on him realizing he talked for an hour to someone he met yesterday. Now it lands on Nanoha.
- **The bridge closer earns its place.** It's his avoidance on screen (canon §6, Oct 18; chapter map `:19`, "avoided rather than missed"), and it protects the outline's check that no reader concludes Natsuki wins.
- **The container doesn't earn its place.** Ch1 already established the food habit (`ch01.ozs:85`).
- **Fix:**
  - Cut c2_0299, so 2.1 ends on c2_0057 ("…to someone I met yesterday").
  - Keep c2_0301/c2_0251 as [P] and have cold readers report the wanting with it in.
  - If the wanting still reads 60+ Nanoha, cut the bridge closer too and end 2.7 on c2_0250 ("something's been decided, and I wasn't the one who decided it").

### 3. "Three nights a week" (low–medium)
- `ch02.ozs:38` (c2_0017): `kohei(neutral): "Three nights a week." || 週に三日な。`
- **The conflict:** the Sunday shift is a day shift, not a night. Canon gives "a 4–5 hour Sunday shift" (`canon.md:490`), and Ch4 has "Sunday, after his lunch shift" (`scene-outline.md:102`).
- The voiced Japanese already says "three days," and line 70 gets it right ("three shifts a week").
- **Fix:** "Three days a week."

### 4. An ambiguous "she" makes Rika look like the one wiping the board (low–medium; staging)
- `ch02.ozs:129` (c2_0090): "Two minutes later she's wiped the practice schedule off the whiteboard by the door, borrowed a pair of glasses from the lost-and-found box, and picked up a shinai to point with."
- **The problem:** the previous subject and speaker are both Rika (`:127–128`), and Natsuki's sprite only appears on the next line (`:130`). A reader pictures Rika in the glasses until Kōhei's "Whose glasses are those?" Kirishima's later "Mizuno. The practice schedule was on that board." (`:175`) confirms who it was, but only after the fact.
- **Fix:** "Two minutes later Mizuno has wiped…", or move `@show natsuki teach_smile c` above the line.

### 5. Two different staff aprons at Hoshino Kitchen (low; carry forward to Ch8)
- **Kōhei:** a brown bib apron with a cartoon chef on the pocket (`ch02.ozs:36`; `style-guide.md:89`, marked [P] Ch2 Oct 24).
- **Yuzu, at the same restaurant:** a "burgundy waist apron" (`style-guide.md:96`; the author approved her look Oct 8).
- A kitchen/floor split doesn't explain it, because Kōhei also works the floor (register, tables; `ch02.ozs:24–25`).
- **Fix:** settle it before Ch8 (style guide §2 is Production's). Either Yuzu wears the brown chef apron, or the floor staff wear burgundy waist aprons and Kōhei's bib is for dish duty. Note the choice as [P] in the handover.

### 6. Narration moves home while the background stays put (low; staging)
- **Tuesday,** `ch02.ozs:82–84`: the walk home and the container on the kitchen table all play over `bg_restaurant_night`.
- **Wednesday,** `ch02.ozs:335–338`: "Halfway up the hill… When I get to the house, the light's on in Nanoha's window…" plays over `bg_bridge_dusk`.
- Ch1 cuts to the houses plate for the same kind of beat (`ch01.ozs:330`, `:357`).
- **Fix:**
  - Tuesday: `@bg black slow` before c2_0056. Line 84 doesn't matter if fix 2 cuts it.
  - Wednesday: cut to the houses plate before c2_0301. Ch4 already needs the dusk plate with both windows lit (`scene-outline.md:115`); Ch1's night lit plate also works.

### 7. Natsuki's signature technique edges into an Open item (low)
- `ch02.ozs:155` (c2_0112): "Debana… It's my favorite." Her point on Kōhei is debana-kote (`:232`).
- `canon.md:480`: "Particular strengths and ranks are Open."
- **The choice is a good one.** Debana is canon's one-sided recognition passed off as ordinary skill. But it's a new fact about her kendo.
- **Fix:** no text change. Record "Natsuki's favorite waza is debana" as [P] so later chapters don't treat it as settled.

### 8. The practice order doesn't match the pilot-notes record (low; record-keeping)
- **The draft's order** (`ch02.ozs:110`, `:122`, `:183–184`): warm-ups and suburi → water break (the lesson) → bogu → an hour of kirikaeshi and waza → shiai-geiko → kneeling debrief.
- `pilot-notes.md:252` records "warm-ups, kirikaeshi, waza, break, shiai-geiko."
- **Fix:** correct `pilot-notes.md:252` to the draft's order. The lesson scene needs this order, because nobody is in bogu at the break.

---

## Address and pronouns (style guide §3c)
Clean. Line by line:
- **Kōhei ↔ Natsuki:** "Mizuno" / "Fujisawa" throughout. No *omae* in any Kōhei line, and her *kimi* appears at `:318` (きみが楽しくてやってること).
- **The planned change for Ch2:** classmates and Rika call her "Nacchan" by Tuesday, on screen as the outline asks (`:34`, `:124`).
- **Natsuki** → "Rika", "Takatsuki-kun". She doesn't ask Kōhei to use her given name.
- **Takatsuki:** *boku* (`:113`, `:233`), surnames, no "you" in his Japanese, few contractions.
- **Kirishima:** bare surnames, and "Captain" (主将) at practice.
- **The manager** → "Fujisawa-kun", and Kōhei answers him politely. **Kōhei** → "Hoshikawa".
- **Narration and interlude:** Kōhei's narration says "Mizuno" throughout. Natsuki's interlude follows her POV ("Nanoha"). Chie's capitals "NATSUKI" match §3c.
- **Kanji:** none in the Japanese name lines (fix 14 holds), and the Ōzakura is おおざくら.
- **No "Chibi" in Ch2.** That's correct: Nanoha is off stage, and the Ch1–3 planting resumes at the Ch3 windows.
- **Nits (not counted):** Rika's chant "Fu-ji-sa-wa!" drops her usual "-kun", which is natural in a chant. Kōhei's English "Captain." is voiced as a plain はい (`:221`). Both are fine.

## Staging (beyond problems 4 and 6)
- **Outfits track.**
  - Tuesday: uniform in class and at the restaurant, and `@wear kohei work` at the restaurant.
  - Wednesday: kendo from the dojo through the mop race, then `@wear kohei school` for the bridge.
  - Natsuki: keikogi and a long ponytail until the bridge, then uniform.
- **Props carry over.**
  - The paper flag goes from her blazer pocket Tuesday, to "still in her blazer pocket from last night", to the pen cup.
  - The wiped schedule gets restored "from memory."
  - The borrowed glasses are never returned, which is harmless.
- **Time of day works** for April 9 in western Kanagawa (sunset around 6:05 pm).
  - Wednesday: a two-hour practice after school, long orange light at the mop race, streetlights coming on at the bridge, a night interlude.
  - Tuesday: she arrives at 8:00, the girls leave at 8:40, the restaurant closes at 9:00, and they talk for about an hour. That fits Ch3's "home after ten."
- **Who's on stage is consistent.** Present-day Kōhei is face-window only. Kirishima speaks from off stage at `:125` and `:175` through face windows (§3a). No more than three sprites are up at once.

## Reader-knowledge target (`scene-outline.md:165–170`)
- **Know: every item lands.**
  - He talks and laughs more than he has in months (`:52`, `:77`, `:83`).
  - She never handles him carefully (`:70`).
  - The reader gets enough kendo to follow the insert: the lesson covers every term and call the match uses.
  - "She was there before I moved" (`:199`), and Takatsuki's "I have never once been there first" (`:233`).
  - The tear she can't explain (`:270–279`).
  - Her loneliness and unease, at full interlude depth.
  - The romantic pull is visible and unnamed: the red ears, "exactly where my hand is on her back," watching her go. "It's only trash bags" denies the pull rather than naming it.
- **Not yet: held.**
  - No past-life content beyond the Ch1 dream.
  - No fragments of her own. The interlude tries ordinary explanations and finds them thin, which reads as unease, not memory.
  - Nothing supernatural on screen.
  - The fix-2 cuts stay cut: no flash at the catch, no "put down something heavy," no "promise I don't remember making."
  - The replacement line "something's been decided, and I wasn't the one who decided it" (`:336`) has a true, ordinary reading (she decided she's coming Saturday). Fine.
- **Dream woman (≤60% Natsuki): watch in the cold reads.**
  - The draft stacks more Natsuki pointers than the clue ledger lists for Ch2 (`chapter-map.md:126`): the neck prickle (`:20`, approved as P5), the lesson's "How do you know when they're starting? / Mostly you don't. That's why it's hard." (`:156–157`), which she then does to him in front of Takatsuki, and the memory cue at the catch.
  - The text has counterweights. She'd "watched him all through the drills" (`:371`), and she texts "except the last one. didn't see that one at all" (`:360`).
  - The wrist rhyme stays loose: her kote hits his right wrist, and the dream's cut is on the inside of his left (`pilot-notes.md:199`). Leave it that way.
  - If any reader goes past 60%, trim `:157` to "That's why it's hard."
- **Acceptable wrong guess (comrade or rival):** left open, and the lesson's framing, if anything, invites it.
- **Wanting:** see problem 2.

## Open items
No story-level Open item gets settled.
- The town name ("SHIRASAWA" on the boxes, `:347`) and Hoshino Kitchen are existing pilot [P] names.
- Natsuki's father's job stays unnamed ("Yokohama until Friday," "her dad's work").
- Chie is still a [P] confidant.
- Natsuki's photography ambition isn't touched: "That's my project, then" is about getting him to have fun.
- No fairy, no Akane diagnosis, no ranks, no build.
- The only edge is debana (problem 7).

## Fine as written
- **Calendar and schedule:**
  - Calendar: Tuesday Apr 8 and Wednesday Apr 9, with the club starting on the first Wednesday (`ch01.ozs:139`).
  - Practice: four days a week, two hours a session (`canon.md:490`).
  - Shifts: Tuesday runs 5:30 to the 9:00 close, which is canon's 3.5 hours, and "three shifts a week" is right.
  - "Saturday afternoons are free," spent carrying trash bags at the shrine, echoes Ch1 and matches pilot-notes ("his only free time").
  - The bridge invitation still makes sense even though she just joined the club: he turns her extra-practice offer into the practice that already exists. That line is kept by fix 5.
- **Map:**
  - Her apartment is by the station.
  - The river and the bridge are where their routes split.
  - His walk home from the station-side restaurant crosses the bridge.
  - Her balcony faces a cherry-lined street along the river.
  - All consistent with Ch1 and pilot-notes §5.
- **Natsuki:**
  - "Kendo since I was seven" matches "nine years."
  - "Six schools," "Sendai, most recently," and the Sapporo → Sendai → Shirasawa boxes.
  - Nanoha walking her home Monday, and the vending-machine tour.
  - Her long ponytail.
  - Hair color is never mentioned.
- **House rules:**
  - Imperial units only ("an inch," "more than two hundred miles," which is right for Sendai).
  - No manga self-reference, no name-tag intros.
- **Kendo accuracy:**
  - Kote is usually the right wrist.
  - Tsuki is allowed only from high school.
  - "Men ari," ki-ken-tai-itchi, and zanshin, with laughing inside the men as the lapse.
  - Shiai-geiko with calls (P3), "Nihonme," and time called at 1–1.
- **Fix list:**
  - Takatsuki is precise and never mocks missed practices (fix 7). His "Captain, I could take her" is plainly about a new opponent, Kirishima's joke closes it, and nothing points toward romance.
  - Kirishima is male and deadpan (fix 28).
  - P1, P2, P4 and P5 are done.
  - Fix 32: every term is glossed.

## Forward note (not counted)
Ch2 already says three times that Kōhei's kendo is wrong but works:
- "gets away with it" (`:169`);
- the left foot forward on the dō (`:238`);
- "It scored." / "Yes." (`:239–240`).

The pilot ends in Ch4 on Takatsuki's "That shouldn't have worked" (`scene-outline.md:110`). When Ch4 is drafted, give that line a specific new impossible thing so it doesn't land as a fourth repeat.

---

## New [P] details the draft invents (one line each)

**Not yet in pilot-notes §3 (add them):**
1. Nanoha leaves Emi's food on the Fujisawa kitchen table with a sticky note in her handwriting: "Again." (`:84`; drop it if problem 2's cut is taken.)
2. Kōhei closes out his shift: he finishes the floor and counts out the register (`:82`).
3. Hoshino Kitchen takes orders on an order tablet (`:43`).
4. Tuesday timing: Natsuki arrives about 8:00, the girls leave about 8:40, and she talks with him for about an hour after the 9:00 close (`:33`, `:55`, `:83`).
5. A minute after the empty-container photo, Akane sends a second, closer one (`:29`).
6. Kōhei knows where the mountain wind blows strongest, for petal photos (`:69`).
7. Kirishima will put Takatsuki in charge of the first-years when they join ("someone with patience") (`:114`).
8. Visitors take off their indoor shoes in the dojo (Kirishima's "Shoes off") (`:125`).
9. Natsuki has to rewrite the wiped practice schedule from memory (`:175–178`).
10. Natsuki's favorite waza is debana, and her point on Kōhei is debana-kote (`:155`, `:232`).
11. Kōhei opens the match with a men feint, which she ignores (`:191`, `:233`).
12. Takatsuki: laughing inside the men after a point is the part of zanshin she left out (`:237`).
13. Practice ends with a bow and a kneeling line, and Kirishima says one sentence to each member (`:215`).
14. The session order is warm-ups and suburi → water break → bogu → an hour of kirikaeshi and waza → shiai-geiko → debrief (corrects `pilot-notes.md:252`).
15. The floor is cleaned "the old way," by hand with wet zōkin (`:251`).
16. On the bridge Natsuki shoots with her phone: the river, the railing, a crow on a lamppost (`:298`).
17. Natsuki's moving rule: never buy anything that won't fit in a box (`:349`).
18. Chie was her best friend in fourth grade and again last year, during the second Sendai stint. This replaces "4th and 8th grade" (`:373`; problem 1).
19. Chie is "more than two hundred miles away," so she's still in Sendai (`:374`).
20. Natsuki watched Kōhei all through the drills before the match (`:371`).
21. Natsuki's text to Chie: she read every move but the last one, the dō (`:360`).
22. When Kōhei gets home Wednesday at dusk, Nanoha's window is lit (`:337`; staging).

**Already in pilot-notes §3 (`pilot-notes.md:248–256`) and consistent with the draft:**
- **Hoshino Kitchen:** closes at 9; the Tuesday shift starts at 5:30; dish pit, drink bar and register; numbered tables, the window booth, the noisy dishwasher, the automatic door; the brown chef apron tied like a hakama; "Lifesaver" ×9; the manager mistaking Natsuki for staff.
- **The restaurant visit:** Akane's dinner note and the seven o'clock photo; the five karaoke girls and the parfait; the kids' plate isn't ID-checked, has a flag, gets photographed from three angles.
- **Town:** the mountain that looks walkable; the taiyaki stand at the north exit; the freezing drink fridge; the June flood and the herons; the bridge with its streetlights and trains; the Ōzakura at dusk.
- **Club:** two-hour practices; Takatsuki's solo suburi; the off-center hakama and their year of training; Kirishima's quiet; the whiteboard and the lost-and-found box; first-years mop and Kōhei stays.
- **Kendo:** both sets of form faults; the 1–1 match.
- **Rika:** her "People in motion" assignment.
- **Natsuki:** "mostly vending machines"; wanting the Ōzakura since Monday; "mornings, weekends"; her mother's first-week notes; her father in Yokohama; the SAPPORO→SENDAI→SHIRASAWA boxes; the flag in the pen cup; Chie's pinned chat and their birthday calls; the balcony; eleven photos, one sent.
