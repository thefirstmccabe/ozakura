# Continuity check: Ch3 "Windows" draft (§9 step 3a)

**Draft:** `production/pilot-v2/script/ch03.ozs` (Nov 2 build). **Checked against:** `story/canon.md`, `story/chapter-map.md` (Ch1–3 rows, running threads), `story/pilot-notes.md` §3, `story/style-guide.md` §1a–§2 and §3b–§3c, `ch01.ozs`, `ch02.ozs`, and `production/pilot-v2/scene-outline.md` (Ch3 scenes and targets).

**Summary:** the draft is in good shape. Dates, the weekly schedule, address forms, the "Chibi" plant, the okuri-ōkami rule and every outline beat check out. I found **15 problems**. Two need a decision before handover: Nov 2 facts about Akane and Dad that canon hasn't absorbed (one of them touches an Open item). There are four medium staging and reader-target issues, and the rest are small. Problems are listed most important first, followed by what's fine, the reader-target check, and the new [P] details.

---

## Problems, most important first

### 1. Akane's diagnosis: canon still says Open, and the draft settles part of it (HIGH)
- **ch03.ozs 24–25** (c3_0065–0066): "Did she take her—" / "She ate. She took them." (薬も飲んだ)
- **ch03.ozs 92–96** (c3_0432–0436): "I called the clinic from your kitchen. They said it's the usual…" / "They've checked everything. Twice. They couldn't find anything wrong. It isn't dangerous." / "And they still don't know what it is." / "No. But they know what it isn't."
- **Canon:** §8 Akane (canon.md 576): "**Diagnosis Open;** symptoms must eventually be consistent." §11 (770) lists "Akane's diagnosis" as an open question. pilot-notes 266 says these lines were "added Nov 2, after the author's decisions on Dad and Akane", but canon was never updated. As written, canon governs and the draft contradicts it. The draft doesn't name a condition, but it does rule things out: two rounds of tests found nothing and it isn't dangerous. Any later diagnosis has to fit that, and it needs to fit FB4 (canon 362: little Akane "rushed to the hospital") too.
- **Internal wrinkle:** she takes regular medication ("She took them"), yet the doctors "couldn't find anything wrong." That can work (treatment for symptoms only), but no line says so, and a cold reader may stumble on it.
- **Fix:** if the author did decide this on Nov 2, hand it to the Story thread. It should fold the decision into canon §8 and §11, add a canon-revisions line, and log it. Until then, don't treat the build as canon-clean. If the author decided less than the draft says, soften the lines and keep the Open item vague: cut "They couldn't find anything wrong. It isn't dangerous." and keep "It's the usual" / "And they still don't know what it is." Either way, record the medication as [P], or make it "her pills for the dizziness" so it reads as treating symptoms.

### 2. Dad's cause of death (pancreatic cancer) is a new family fact that canon doesn't have (HIGH, procedural)
- **ch03.ozs 97** (c3_0437): "Dad's was cancer. In his pancreas. By the time anyone found it, we were counting in months."
- **Canon:** §8 Kōhei (484) has only "His father died after several months of illness around Kōhei's entry into high school." Nothing contradicts it ("counting in months" fits "several months of illness", and "last spring" fits the timing), but the illness isn't named anywhere in canon. pilot-notes 266 attributes it to a Nov 2 author decision.
- **Fix:** the Story thread should add it to canon §8 (and to the Ch21 flashback notes in §6) with a revision line. If the author didn't name the illness, mark it [P] in pilot-notes. It's already listed in the Nov 1 entry, but not as provisional.

### 3. Natsuki's camera is aimed at the branch the moment before the light appears under it (MEDIUM)
- **ch03.ozs 221** (c3_0388): "Mizuno's a few steps off with the camera up, pointed at the branch, at me. She lowers it. She doesn't take the shot."
- **ch03.ozs 223–227**: Nanoha looks "at a spot just under" the low branch, and the light appears there.
- **Canon/outline:** in April–August only Nanoha notices the light (canon 642). The outline (99) replaced Natsuki's old excuse, "the light changed," precisely because it tied her to the fairy, and the Ch3 check (194) allows no new signals for Natsuki beyond the camera. With her lens on the branch one beat before the light shows up under it, a reader can conclude that she saw it too.
- **Fix:** aim the camera at Kōhei only, e.g. "Mizuno's a few steps off with the camera up, pointed at me." Keep the order as it is: she lowers the camera before the light appears.

### 4. "The first-years who bow to her in the hallway" on Thursday of the first week (MEDIUM)
- **ch03.ozs 86** (c3_0120): "Not Hoshikawa, not the first-years who bow to her in the hallway."
- **Calendar:** it's Thursday, April 10. Term started Monday (ch01 c1_0004), and the first-years haven't even joined clubs yet (ch02 134, 279). A habit of first-years bowing to her can't have formed by Thursday. v2 already fixed the same slip in Ch1: the class representative's assistant became "last year's job, since it's only the first day of the new year" (pilot-notes 146). Two cold readers asked about this line (pilot-notes 267).
- **Fix:** "Not Hoshikawa, not anyone at school. Just me, across three feet of night." Or move the bit to a later chapter.

### 5. Kōhei's face windows are still in school uniform after his shower (MEDIUM-LOW, staging)
- **ch03.ozs 11** sets `@wear kohei school`, and nothing changes it before **62** ("I take a shower."). Every Kōhei line at the window (69–109) shows the school-uniform face window.
- **Why it matters:** outfit-specific face windows exist (Ch2 switches between work, kendo and school), so a blazer and tie at a bedtime window is visible to the player.
- **Fix:** add a home or sleepwear variant of his face set and `@wear` it after line 62. If the crops are tight enough to hide his clothes, check it on screen and note it.

### 6. Nanoha at the shrine is in her `home` sprite (hair down?), not the outing state or the shrine sprite the outline lists (MEDIUM-LOW, staging)
- **ch03.ozs 195–196**: `@show nanoha home_smile l` / "Nanoha's on the stone path in her weekend clothes…". The same sprite is used down the steps and at lunch.
- **Canon/style guide:** canon §8 hair states (512–515): "School and outings: a loose side braid. At home: long and loose." The style guide §2 (90) says the same. The outline's Needs (111) say "Reused: Nanoha … at the shrine." The text also uses the same `home` outfit for Thursday's "house clothes" (line 20) and Saturday's "weekend clothes."
- **Fix:** use the shrine or outing sprite (braid) on the hill and keep `home` for lunch at her house. If loose hair at the shrine is wanted, record it as [P].

### 7. Genji's drawn height may put him shorter than Nanoha (LOW-MEDIUM, heights)
- **pilot-notes 273** (the Ch3 build record): "Genji is drawn at 58 inches, his 5′2″ with the stoop."
- **Style guide §1b (63):** "Genji 5′2″ (stooped)" [P], with Nanoha at 4′11″. If 5′2″ is already his stooped height, drawing him at 4′10″ makes him 4 inches short and an inch shorter than Nanoha on the steps and in the lunch CG. "58 inches" also breaks the feet-and-inches rule.
- **Fix:** decide which reading is meant. If 5′2″ is his stooped height, redraw at 5′2″. Write the record as "4′10″" or "5′2″", not "58 inches".

### 8. How Natsuki knew to ask Nanoha (LOW, who knows what)
- **ch03.ozs 200–202** (c3_0372–0374): "I asked Nanoha on Thursday, after you'd gone to work, if I could come up and take pictures." / "Grandpa said yes before I'd finished asking."
- **Outline 91** gave her a source: "Rika had told her it's Nanoha's grandfather's [P]." The draft drops it. Nothing in Ch1–2 tells Natsuki that the shrine is Nanoha's family's (Kōhei only said "a shrine" and "the Ōzakura"). It still works if she simply asked the girl next door, but a reader may wonder.
- **Fix (optional):** half a line, e.g. "Rika said it's your grandpa's shrine, so I asked Nanoha…". Or leave it and drop the Rika detail from the handover.

### 9. Kazuo is at work on a Saturday (LOW)
- **ch03.ozs 304** (c3_0413): "Uncle Kazuo is at work."
- **Background:** canon 523 leaves Nanoha's parents' jobs Open. pilot-notes 178 gives Kazuo [P] "an office job at the city water bureau," which normally doesn't work Saturdays. This isn't a contradiction (the outline marks "Kazuo is at work [P]"), but the two [P] details pull against each other.
- **Fix:** keep the line vague, which it is, and record "Kazuo works some Saturdays" as [P], or revisit the water-bureau detail when his job is decided.

### 10. The shrine stairway reads steeper than canon's "slightly uphill" (LOW)
- **ch03.ozs 151** (c3_0341): "a stone stairway through the cedars, steep enough that the old people in the neighborhood count the landings out loud."
- **Canon §3 (122):** the shrine "sits slightly uphill, an ordinary walk from the houses. Detailed architecture is Open." The pilot's stone stairs (pilot-notes §5) and the valley view are precedent, so this is a matter of degree.
- **Fix:** "steep in places", or keep it and have the Story thread note in canon that the approach is a stairway with landings ([P]). The counting habit may also read as a second folk rule waiting to pay off. That's fine if Ch38 wants it, but log it.

### 11. Two lines narrow canon's flashback ages (FB2, FB3) (LOW, for the Story thread)
- **ch03.ozs 77** (c3_0111): Usagi-san "in time-out on and off since you were ten." This means FB2 (Kōhei buying the rabbit, Ch7) has to fall before age 10. That fits canon 360 ("childhood, maybe after the fairy is gone").
- **ch03.ozs 64** (c3_0097): "when we were little we ran a string between our windows with two paper cups." FB3 is "the origin of the window conversations" (canon 361), and its age is Open (style guide §3c, 264). A childhood paper-cup telephone pushes FB3 toward childhood, or at least makes "the windows begin" read as the second start.
- **Fix:** no script change needed. Tell the Story thread so FB2 and FB3 are placed with these lines in mind. Or drop "when we were little" if FB3 should stay free to be early middle school.

### 12. pilot-notes lists a Ch3 detail that isn't in the draft (LOW, doc mismatch)
- **pilot-notes 270** (v2 Ch3, Great Cherry): "the hot-springs visitors who get lost". No such line exists in `ch03.ozs`.
- **Fix:** delete it from pilot-notes. Keep it out of the script too: people getting lost is the autumn beast thread (canon 410–411), and it mustn't sit beside a past-life fragment at the tree in spring (canon §2: beast threads stay separate from past-life clues).

### 13. "Down the lane" (LOW, nit)
- **ch03.ozs 98, 107**: "Somewhere down the lane, a cat yells at another cat." / "the cat down the lane".
- **Canon §3 (117):** "No alley, path or stairway runs between them." The house layout was fixed four times over an alley (fixes 10, 18, 31), and "lane" can call one up.
- **Fix:** "down the street" in both places.

### 14. Akane is left asleep on the sofa (LOW, staging)
- **ch03.ozs 51–62**: "She pulls the blanket up over her head. Conversation over." Then Kōhei showers, soaks the lunch boxes, sets the rice and goes upstairs. Nothing moves Akane, which is out of character for a brother who checks her forehead (line 26).
- **Fix:** add one line to c3_0095, e.g. "I get Akane up the stairs and into bed. I take a shower…"

### 15. A Japanese-only name in c3_0434 (NIT)
- **ch03.ozs 94**: the English starts "They've checked everything…", but the Japanese starts こうへい、検査は全部したでしょ。 Nanoha says his name only in the voiced line.
- **Fix:** drop こうへい、 or add "Kōhei." to the English. Either form is correct under §3c.

---

## What's fine (checked and consistent)
- **Dates and weekdays:** the "Thursday, April 10" and "Saturday, April 12" cards follow from Mon Apr 7 (map row 3). Dad "last spring," the food "about a year," and "sixteen years" all match Ch1.
- **Schedule:** Thursday is a shift (Tue/Thu/Sun). He gets home "after ten" from a 9 o'clock close. Saturday-morning practice comes before the afternoon sweep (canon 494; ch01 c1_0008, c1_0096). Akane's seven o'clock two-photo routine matches Ch2 c2_0009. "Lifesaver" eleven times as "a record" fits Ch2's "about nine." Takatsuki is on the floor first doing his practice swings (Ch2 bit). Free sparring is the last half hour.
- **Kendo:** Kōhei "takes most of what there is to take," Natsuki is always already there, and he can't read her (fixes 5 and 6: one-sided recognition). Her right-heel read and Takatsuki's "left shoulder… so that it is fair" match Kirishima's Ch2 note.
- **Address and pronouns (§3c):** all correct. Natsuki says "Fujisawa" with *kimi* (きみ). Nanoha → Natsuki "Natsuki-san". Natsuki → Nanoha "Nanoha". Akane → Natsuki "Natsuki-san" (her change waits until Ch15). Mio → Kōhei "Kō-nii" and → Natsuki "Natsuki-nee", with herself in the third person ("Mio is the best in this house"). Natsuki → Mio "Mio-chan" and → Takatsuki "Takatsuki-kun". Emi → Kōhei "Kōhei-kun". Genji → bare given names. Nanoha → Genji おじいちゃん. Kōhei uses *omae* to Nanoha and never to Natsuki, and never says Nanoha's name to her face ("What did you say?" has no name, outline 3.4). Takatsuki's Japanese avoids "you". Narration uses "Mizuno," "Hoshikawa," "Kirishima-senpai," "Nanoha," and the translated "Grandpa / Auntie Emi / Uncle Kazuo" per §3c. Names in the Japanese are in kana (fix 14).
- **Planned name changes:** Ch3's "Good night, Kō-chan." / "Night, {Chibi|shorty}." plants "Chibi" as the map asks (Ch1–3) and uses the Nov 1 gloss form. No change is due in Ch3, and none happens early.
- **Supernatural rules:** the light is a deniable point of light that only Nanoha reacts to, and Kōhei's narration never names it. The staging line for cold readers is present (line 226). The fragment under the branch (snow in April, the branch too low) is a sensory fragment, not an awake fight flash, so it stays within canon §6's rule that fight flashes come only with anger (keep mist, mask and grip out of it). The stumble on the steps follows the okuri-ōkami rule exactly: Genji says he's resting and sits down. Nobody explains, Genji turns to the weather (§3b "folk knowledge… as habit"), and "Kōhei has never asked." No dream appears in Ch3 (never two per chapter).
- **Houses and town:** three feet between the windows, reachable with fingertips, and ten feet between front doors (Ch1). The way up starts "a little past our houses," not between them (canon 117). The station lies the other way from the hill (Ch2). Natsuki's Niigata story fits the pilot's [P] move list (Sendai → Niigata → Okayama → Sapporo → Sendai → here) and canon's "Sapporo, Sendai, then here."
- **Story-text rules:** no hair color anywhere. No manga self-reference (Nanoha reading his manga is allowed). No "You're late" from Nanoha (fix 2). "Very" appears once, in Genji's "very convenient back." Ch3's face-reader is Natsuki only, and Nanoha's face catalogue stays out (§3b). Nanoha's height gets only "Chibi."
- **Outline beats:** all present. The two empty-container photos and the sleeve, "you're hovering again", the window (time-out, "You're not the only person who loves her," thanks answered through the rabbit, "it didn't come up"), the project and progress reports, the Niigata line, the photo on the landing and his second-too-long look, the second broom handed over without a word, "Thursday. After school. Before the window.", the fragment and the lowered camera, "…You came back" / "A petal," three cups of bitter tea, the steps, "It's a sickness," "Kōhei-kun, welcome home," the lunch CG seating, Kagero and "Natsuki-nee, again!", and the ordinary tree at the end. The rabbit's quarter turn instead of the corner is a recorded change (pilot-notes 267). "He knows what he did" and the wall stay saved for Ch4.
- **Staging otherwise:** time of day, backgrounds, who's on stage, and face windows against style guide §3a rules 2 and 4 are consistent throughout. Outfits are consistent apart from problems 5 and 6. Natsuki stays in track clothes from the steps to the gate ("I smell like a kendo glove"), and Akane is in her home outfit (outline: moved to Ch3). The props carry through: camera, brooms, trash bags, thermos, the manga reshelved between volumes five and seven.

## Reader-knowledge target for Ch3 (outline 190–194)
- **Know: all hit.** Akane texted Nanoha, and Nanoha came and stayed. At the window Nanoha shares the load and hides in the bit. Each of them kept Saturday from the other, and Nanoha's unease shows only in what she does (she knew, the broom, the lunch invitation). Kōhei usually has the edge, but Natsuki reads him and he can't read her. With her he forgets to be tired, the project is him having fun, and he looks a second too long. The snow and the low branch come with the camera lowered. Nanoha speaks to something. The odd line on the steps goes unexplained. The Tachibanas take him and Natsuki in.
- **Suspect: supported.** The tree and the branch point at the dream's tree, and "You came back" points to something older than Natsuki's arrival.
- **Not yet: held, with two watch items.** (a) The light appears right after Kōhei's fragment under the same branch. That juxtaposition invites a link to the past life, which the target says to withhold. It's approved staging, so ask cold readers whether they link the two. (b) The snow fragment is the approved hint and shouldn't read as "it ended in winter."
- **More than intended:** the Nov 2 window lines add Akane's test history and Dad's cancer (problems 1 and 2). The targets don't forbid them, but they're told backstory (canon §1, "save backstory for real scenes," with Dad's illness due in Ch21). They also give the window more weight on Akane and Dad than on Nanoha. Cold readers should say whether the window still reads as Nanoha sharing the load.
- **Balance:** Natsuki's new signals are within the allowance: her reads of him in sparring and on the steps (things anyone could see), plus the camera. Problem 3 is the one risk. Her Kagero win "by waiting" makes her anticipation look like a general skill, which helps keep the dream-woman number near even. The weight on each side (window, broom, lunch for Nanoha; the walk up, the photo, Mio for Natsuki) matches the outline's plan.

## Forward notes for Ch4 (not counted as problems)
- Genji's "Looks like rain tomorrow" (line 257) falls on Sunday, which is Ch4. Decide Sunday's weather on purpose: rain makes the dodge come true, and a clear sky keeps it a dodge.
- Ch2 has Kōhei say "Three nights a week" (c2_0017), but the Ch4 outline has a Sunday *lunch* shift. Reword one of them when Ch4 is built.

---

## 6. New [P] details in the draft

### 6a. Not yet in pilot-notes §3 (add to pilot-notes and the handover)
- Akane takes regular medication ("Did she take her—" / "She took them", c3_0065–0066). This touches the Open diagnosis (problem 1).
- Nanoha's sleeve shows in the corner of Akane's second empty-container photo (c3_0310, c3_0311).
- Nanoha's light is normally on at ten at night ("isn't like her at ten o'clock", c3_0059).
- Akane falls asleep on the Fujisawa sofa under a fleece blanket, with the TV paused on the hospital drama (c3_0060).
- Nanoha's bit: "'Welcome home' is customarily answered with 'I'm home'" (c3_0064).
- "It's always two against one in this house" (Akane and Nanoha against Kōhei, c3_0085).
- Kōhei's routine after a shift: shower, lunch boxes put to soak, rice set for the morning (c3_0095).
- Kōhei owns a bike (c3_0342).
- Seen from school, the shrine is the opposite direction from the station; Natsuki "takes the long way" (c3_0339–0340).
- In free sparring, Natsuki gives ground when Kōhei comes in hard (c3_0327).
- The boulder is where Kōhei and Nanoha climbed as kids (c3_0184).
- The Ōzakura's trunk is "split in places like old stone," and its branches roof the whole hilltop (c3_0182).
- A stone lantern stands by the stone path, with the second broom leaning on it (c3_0185). Shrine architecture is Open in canon.
- Genji sits on the shrine-office step during the sweep and tells Natsuki "The tree doesn't mind" (c3_0376, c3_0380).
- The tea comes up in Genji's thermos (c3_0259).
- Natsuki's cover for the untaken shot: "It wasn't a good one! Too many petals." (c3_0393).
- After his stumble, Genji sits down on the step for a moment "as if that had been the plan all along" (c3_0398).
- Kōhei has heard the "rest" line on these steps all his life (c3_0402).
- Natsuki carries her practice bag to the shrine (c3_0405).
- Emi seems to expect them and has cooked "enough for twelve" (c3_0282, c3_0411).
- Akane is at the Tachibanas' before the others come down for lunch (c3_0285).
- Kōhei answers Mio's order with "Yes, ma'am" (c3_0407).
- Kōhei told Akane he had "a bad Wednesday"; per Nanoha, "the whole class knows" Natsuki took a point off him (c3_0419).
- Natsuki promises Mio a rematch (c3_0428).
- Akane's route home from school passes the station stairs (c3_0075; outline [P], unrecorded as a logistics fact).

### 6b. Already in pilot-notes §3 "v2 Ch3" (Nov 1–2) and confirmed in the draft
- Thursday: "Lifesaver" eleven times; Akane dizzy on the station stairs, sitting for ten minutes; Nanoha phoning the clinic ("the usual"); the tests done twice; Dad's pancreatic cancer ("counting in months"; see problem 2).
- Three episodes of a hospital drama at the Fujisawas' (bigger TV, the handsome surgeon who's a terrible doctor, "should be arrested").
- Nanoha reshelves the manga between volumes five and seven; "Window?" / "…Window."
- The window: about three feet; the childhood paper-cup telephone; books passed across; the scrunchie she's had since middle school.
- Usagi-san: bought by Kōhei, "in time-out on and off since you were ten," "repeat offender," "We don't discuss it," the quarter-turn reduced sentence, "halfway out of trouble."
- The first-years bowing to her (see problem 4).
- Saturday: Takatsuki first on the floor; free sparring in the last half hour; the right-heel tell; Takatsuki's "so that it is fair."
- The steps: they start a little past the houses, through cedars, the old people count the landings (see problem 10), and there's a rope rail.
- Natsuki: navy track shirt and dark sweats; a real camera with a lens that "probably cost more than my bike"; the Niigata rice-planting day; the photo "like somebody's little brother"; "Nope. It's a good one."
- Kōhei slept four and a half hours and shakes out his left hand every ten steps and in third period.
- The tree: three adults can't link arms around it; the near-level branch "offering you its arm"; the big flat boulder; the valley view.
- Natsuki asked Nanoha on Thursday after his shift began; Genji said yes before she finished asking.
- Natsuki photographs moss on a lantern, Nanoha's drifts and her sneakers; Nanoha tells the tree "Rude."
- Bitter tea, three cups, "This one'll do"; the shrine office keeps the tea.
- "Just stopping for a rest" twice, Nanoha's echo, "Looks like rain tomorrow."
- Lunch: Emi's "You're saving me"; the menu (two plates of tamagoyaki, kinpira as the source of Monday mornings); the seating; Kazuo at work (see problem 9); Mio leads "Itadakimasu"; Kagero "for cowards"; three wins by waiting; "Natsuki-nee"; "I smell like a kendo glove"; Emi thanked three times; Natsuki leaves at three.
- Production: the light drawn in code; her window going dark; the five new CGs; Genji at 58 inches (see problem 7).

### 6c. pilot-notes entries that don't match the draft
- "the hot-springs visitors who get lost" (pilot-notes 270): not in the draft. Delete it (problem 12).
