# Continuity check: Pilot v2 Prologue + Ch1 (`production/pilot-v2/script/ch01.ozs`, Oct 17 build)

**Read:** `story/canon.md` (all), `story/chapter-map.md` (Ch1 row and running threads), `story/pilot-notes.md` (§1 fixes, §3–§6), `story/style-guide.md` §1a–§2 from this build, §3b–§3c from the Oct 18 style guide (this build doesn't have them yet), `production/pilot-v2/scene-outline.md`, and the draft. Line numbers below refer to `ch01.ozs`.

**About the reader-knowledge target:** the outline has no separate "reader-knowledge target" section. I took the target from outline 1.1–1.7 plus the fixes it cites (2, 3, 13, 26) and canon §1 ("keep the strangeness subtle"). By the end of Ch1 the reader should know: the household routine and its weight (Mom behind the fusuma, Dad gone by implication, Akane watched); Nanoha's familiarity, her private oddness and the feelings she's hiding; and that Natsuki arrives with **a physical reaction only** (no flash, no narrated certainty). Also: no fairy, no manga comparison, and no dream at the end.

**Summary:** 17 problems. Two are verify-only checks on assets or the compiler (#5, #6). The two that matter most: Natsuki says her déjà vu out loud to Nanoha on day one (#1), and the planned "Chibi" plant is missing (#2). Most of the rest is small.

---

## Problems, most important first

### 1. Natsuki says the recognition out loud on day one, and says it to Nanoha (reader knowledge over target; touches an Open item)
Lines 321–328:
> natsuki: "Hey. This is going to sound weird." … natsuki<wistful>: "Does he ever seem like… someone you've met before?" … nanoha<surprised>: "…" … "It's the jet lag talking." … "Very intense jet lag."

- Outline 1.4 says "physical reaction only," and fix 2 thins the week-one supernatural beats. This line is a spoken version of the cut "narrated certainty," and it comes from Natsuki's side.
- The outline gives Natsuki's side of the recognition to Ch2.8, and only privately: the Chie text "i knew what he was going to do before he did it." Saying it here uses that beat up a chapter early, and in public.
- It tells **Nanoha** on day one that Natsuki feels she's met him before. Canon (§4 Oct–Dec row; §6 "Dating") says Nanoha senses the past-life connection later, and that "how much she perceives, and when, is Open." Line 324 (`nanoha<surprised>: "…"`) has her register it, which starts settling that Open item in Ch1.
- It looks like a replacement for the cut "Like in manga" exchange (fix 26). The outline asked only that the manga line go, not that something take its place.

**Fix:** cut lines 321–328 and go straight from 320 to 331. The interlude still works: drawer, then "Thanks for today, Nanoha." If the scene needs a beat there, use an ordinary one with no recognition in it, such as Natsuki making a casual bid for company, which fits canon §8's "makes important invitations sound casual." (A side benefit: the cut also removes Nanoha's public deadpan at someone she just met, lines 325 and 327. §3b rules that out.)

### 2. The planned "Chibi" plant is missing (§3c planned shift 1)
Line 366:
> kohei(smile): "Night." || おやすみ。

§3c says plainly that the Ch1 revision plants it: "Night, Chibi," おやすみ、チビ, in answer to her "Good night, Kō-chan." Ch11's "the nickname that suddenly hurts" and Ch25's first "Nanoha" both depend on this plant. Line 95's "short-person direction" bit is already in place to set it up.

**Fix:** `kohei(smile): "Night, Chibi." || おやすみ、チビ。`

### 3. Natsuki uses *kimi* to Nanoha (§3c)
Line 282:
> natsuki<surprised>: "Oh—hi. You're…" || あ、どうも。えっと、きみは……

§3c: Natsuki uses "*kimi* to Kōhei (her signature); names for everyone else." Using it with Nanoha in the same scene, minutes after her two *kimi* lines to Kōhei (257, 272), weakens the signature.

**Fix:** `あ、どうも。えっと……` (the English can stay as it is).

### 4. Nanoha's Japanese turns casual with someone she's just met (§3c, Nanoha: "polite *desu/masu* with strangers")
Line 283 is polite (…です, …持ってます). Then it drops to plain form at once:
- 284 「案内しようか？…そういうの。」
- 287 「大したツアーじゃないよ。」
- 292 「段階を踏んでるの。…時間がいるから。」
- 294 「うん。いいよ。」

Her "I'm working up to it" (292) is about formality, so the Japanese should show her still being formal.

**Fix:** keep lunch polite: 「よかったら、放課後、校内をご案内しましょうか？」, 「大したツアーじゃないですよ。」, 「段階を踏んでいるんです。」, 「それは……はい。大丈夫です。」. Let her loosen during the tour interlude (308 onward), so the change is visible.

### 5. Prologue speaker label: check that it doesn't name Natsuki (verify only)
Lines 29 and 32 use the speaker ID `past_natsuki`. Pilot-notes §3 says the past-life girl's label is **"???"**, and fix 27 says "???" speakers get no face window. Name tags are drawn in the character's color.

**Check:** the compiler should map `past_natsuki` to "???", in a color that isn't Natsuki's copper and with no face window. If it doesn't, the name tag and the backlog tell the reader on the first screen who the dream woman is, though the outline keeps "her face … out of frame."

### 6. Night backgrounds: check they're the corrected houses plate (verify only)
Lines 342 and 369: `bg_houses_night`, `bg_houses_night_lit`. Outline 1.7 lists "street at night" as a **reused** background. The shipped street plate shows an alley and stairs between the houses, which fix 18 calls wrong and canon §3 rules out ("No alley, path or stairway runs between them").

**Check:** both plates should be built from `production/refs/locations/houses-street.png` (Oct 10). Line 370's "gap so narrow you could pass a book through it" depends on it.

### 7. Nanoha has no hair clip (design, style guide §2 and canon §8)
Line 129:
> One lands in her hair, right on the clip, and stays there.

Her school look is a loose side braid, with no clip in canon §8 or style guide §2. Clips belong to Akane (side clip) and Rika (novelty clips, line 169), and the line will make an artist or a reader look for one.

**Fix:** "One lands in her hair, right where her braid starts, and stays there."

### 8. Grandpa's "very convenient back" is used here and again in Ch3
Lines 152–153:
> kohei: "His back again?" / nanoha: "His back is a very convenient back. It only hurts on days with a lot of petals."

Outline 3.5 puts this beat at the Great Cherry: "Sweeping with Nanoha; her grandfather's 'very convenient back.'" Using it in Ch1 means Ch3 either repeats the joke or loses its beat. Outline 1.2 also keeps the river walk "just the two of them, easy," with private oddities saved for later scenes.

**Fix:** cut 152–153. Keep 151 (the Saturday sweep, which 3.5 needs) and go straight to 154: "I'll come after practice. Somebody has to carry the trash bags while you supervise."

### 9. The pilot's "second semesters" seed is dropped, and the replacement points the other way
Line 331:
> natsuki<smile>: "Thanks for today, Nanoha. Seriously. First days are usually…"

The pilot [P] line is "I'm amazing at first days. It's the second semesters I never get to." Pilot-notes lists it in §3, in §6 ("Seeds planted: … will she move again?"), and in §7 as one of the pilot's best lines. The draft doesn't use it, and "First days are usually…" trailing off suggests first days go badly, which works against both the seed and her "basically a professional" (221).

**Fix:** restore the line here (`natsuki<wistful>: "I'm good at first days. It's the second semesters I never get to."`), or change the trail-off to point past first days ("It's after the first day that it's usually…"), and note in the handover where the seed now lands.

### 10. Natsuki names the exact Fujisawa-kitchen detail that Ch4 is built on
Line 319:
> "Someone who knows which drawer sticks in your kitchen."

She has no way to know about the sticking drawer. Read with line 320 ("Nanoha didn't say that Kōhei's kitchen drawer stuck"), it plays either as coincidence or as intuition, which is another quiet recognition signal (see #1). It also uses up scene bank 3 / outline 4.2, where Natsuki *discovers* that Nanoha "knows where his cups go and which window sticks."

**Fix:** keep Natsuki's image general, e.g. "Someone who knows where everything is in your house." Leave line 320 as it is: the dramatic irony stays, carried by Nanoha's thoughts.

### 11. Where Mom's room is (staging)
- Line 49, heard from Kōhei's **upstairs** bedroom (canon §3): "Nothing from the room down the hall."
- Line 57, in the kitchen: "The fusuma to Mom's room is closed."
- Line 100: "I wrap the lunches. I knock twice on the fusuma." He knocks without going anywhere.
- Outline 4.2 has Natsuki notice "the closed fusuma" during group study at the Fujisawa house, so the room needs to be downstairs, off the kitchen or living room.

Line 49 puts it upstairs (unless it means Akane's room, which isn't clear).

**Fix:** line 49: "Nothing from Mom's room downstairs." Treat downstairs, off the kitchen and living room, as the [P] location.

### 12. A calendar showing this April can't hold Dad's handwriting from last spring (object continuity)
- Lines 54–56: Kōhei reads "the calendar on the wall" with "a red circle around the eighteenth" (a page for this month), and "the bottom line … still says 'Garbage: burnables, Mon/Thu' in Dad's. He wrote it last spring."
- A paper calendar for this year couldn't have last spring's writing on it.

**Fix:** make it a reusable board, "the whiteboard calendar by the fridge," or put Dad's line on a strip of tape along the bottom. Pilot-notes §3 ("Dad's handwriting is still on the kitchen calendar") still holds. (Fix 11's "from last spring" is applied correctly.)

### 13. "Monday, April 7" plus the era decision implies a year (calendar note for the handover)
- Line 44's card puts a weekday on the date. In 2005–2030, April 7 falls on a Monday only in **2008, 2014 and 2025**.
- Canon §3 (Oct 13) sets the era as "smartphones … everywhere, but before generative AI." That leaves **2014** as the only fit. Canon says the exact year is Open.

The draft doesn't state a year, so this is not an error. It is a constraint that later chapters will inherit. **Fix:** keep the card, and add one line to the handover and chapter map: weekdays follow the 2014 calendar (Apr 18, Akane's clinic day, is a **Friday**, a practice day; Christmas is a Thursday; Jan 1 is a Thursday). Also avoid anything that dates to a particular year. If the author doesn't want the year pinned even implicitly, drop the weekday from the cards.

### 14. Trash-walk staging: where they're standing and what he can see (staging)
- Line 344: he's "taking the burnables out to the corner."
- Line 364: Nanoha "walks the ten feet to her own front door," so they're right outside the houses, not at the corner.
- Line 370: from the street he sees her light "in the window that faces mine." The facing windows are on the side walls across the three-foot gap, so from the street he'd see the glow, not the window itself.

**Fix:**
- Line 344: "I've just left the burnables at the corner and I'm on my way back when Nanoha comes up the street…"
- Line 370: "her upstairs light comes on, spilling into the gap between our houses from the window that faces mine…"

### 15. A small tense slip at the reveal (staging)
Line 226: "Her eyes go along the rows while she says it." She has already finished her introduction (lines 218–223), and the CG has just been cleared. **Fix:** "Her eyes go along the rows while the laughter settles."

### 16. A slight drift toward "loner" (canon §8: "Socially: functional, not a loner")
Line 253: "…a group of girls whose names I don't think I've ever said out loud." Without context, this suggests he doesn't know his classmates after a year. **Fix:** "…a group of girls from the other end of the room," or make clear they're new to him because classes were reshuffled.

### 17. 大桜 is in kanji where the script's own rule says kana (voice pipeline)
Line 151: 「今年の大桜は」. The script header keeps proper names in kana until kanji are chosen (fix 14). 大桜 is the locals' name for the tree, and TTS may read it だいざくら or たいおう. **Fix:** 「今年のおおざくらは」.

---

## Checked and fine
- **Structure:** matches the chapter-map Ch1 row and outline 1.1–1.7: the 5:40 alarm, two lunches, kinpira and "It's a sickness," the one-beat food history (fix 20), the fusuma knock with no answer and then the creak (fix 21), Akane sweet in her sailor uniform saying "Onii-chan," the collar, Rika's tackle, Ryōsuke arriving mid-argument, the intro with the grin stutter and the pen grip, a beat of silence at the hitch, the lunch confessions and "I don't have time," the interlude ending on "shut a window against the wind," "You smiled," and no dream return.
- **Calendar and schedule:** Monday Apr 7 matches the pilot timeline and the chapter map. Kendo Mon/Wed/Fri/Sat morning and Hoshino Kitchen Tue/Thu/Sun match canon §8 and pilot-notes §3. "Club starts Wednesday" (141, 275) sets up Ch2's first practice on Apr 9. The Saturday sweep "after practice" sets up 3.4–3.5. "About a year" of food and "last spring" for Dad fit his death around Kōhei's entry into high school.
- **Heights and designs:** Rika's "taller than the vice-principal" works with Natsuki at 5′3″. Nanoha (4′11″) going up on her toes to reach a 5′9″ collar fits. Natsuki's hair is shoulder-length and tucked behind an ear (§2). Akane's red scarf, Kōhei's tie, and Rika's pigtails and clips all match. Hair color is described plainly and no one remarks on it (canon §2).
- **Presentation:** Kōhei is never on stage and has a face window on every spoken line. No fairy, no manga reference, no flash. "You're late" appears only in the prologue (fix 2).
- **Prologue:** the cut wrist comes "home from training" and gets bound while she scolds him (canon §5, fix 23). The CG keeps her face out of frame. Past-life Natsuki speaks politely and never says his name (§3b–§3c).
- **Open items left open:** kendo rank (Kōhei dodges "shodan?"), Akane's diagnosis, Natsuki's father's job, money details, Mom's name. Dad's death is implied rather than stated. Names in the Japanese lines are kana (except #17).
- **Address (§3c):**
  - Akane: "Onii-chan" and "Nanoha-chan."
  - Kōhei: *omae* to Akane and Nanoha, never to Natsuki, whom he calls "Mizuno" aloud and in narration. "Tokiwa" with Ryōsuke. Oba-san translated as "her" (88).
  - Nanoha: "Kōhei" in public (200, 312), "Kō-chan" only in private (131, 365). "Mizuno-san" then "Natsuki-san," and "Rika-chan." お母さん for Emi, おじいちゃん translated "Grandpa."
  - Natsuki: *kimi* to Kōhei, "Nanoha" from day one, and she asks Nanoha, not Kōhei, to use her given name, with him sitting right there.
  - Rika: "Nano-chan" and "Fujisawa-kun," *atashi*.
  - Ōno: bare surnames, refers to himself as 先生.
- **"There's never a knock" (76):** fine as present habit. It doesn't conflict with FB6, where the first no-knock entry came after the funeral.
- **Small details:** the Fukuda gag is correct in gojūon order (ふくだ before ふじさわ). The house gap (370) matches canon §3.

## New [P] details the draft invents (for the handover and pilot-notes)
**Home**
- Kōhei is usually awake before the 5:40 alarm and lies there the full ten seconds "as a matter of principle" (48).
- House sounds: the water heater ticks; a crow on the power line (49).
- Rice goes on the timer the night before. Today's lunches: tamagoyaki, leftover spinach, the last frozen karaage (53, 70).
- Everything on the kitchen calendar is in Kōhei's handwriting except Dad's line (55).
- Dad's line reads "Garbage: burnables, Mon/Thu"; Kōhei has never written over it (56).
- Burnables pickup has since moved to Tue/Fri; the collection point is at the street corner (344).
- Akane's bad-day signs: leaning on doorframes, holding her head when the room tilts (66).
- Akane offers to make her own lunch and straightens her own scarf before he can (71–74).
- Nanoha comes in by the Fujisawas' sliding back door (75–76).
- Kitchen layout: mugs in the cupboard left of the sink, glasses in the other; the sticking drawer is under the counter (hip-bump); the latch on the window over the sink needs a jiggle to vent steam (90).
- Kōhei stopped protesting the food "around last summer" (87).
- He leaves rice in the cooker and miso soup on the stove for Mom, and knocks twice (100–101).
- Mom's room: currently "down the hall" (49); proposed downstairs off the kitchen and living room (#11).
- Nanoha has known about the sticking drawer since she was six (320).

**River walk**
- The school route follows the river, then turns toward town (109).
- Nanoha always walks on the river side (112).
- Kōhei and Nanoha have been in the same class four years running (118).
- Last year Kōhei was put in 1-C for five days during an "exchange program" (122–123).
- The snowmelt comes "from the Tanzawa," naming the real range where canon says "Tanzawa-style" (150).
- Genji says the Ōzakura is the best it's been in years; Nanoha helps him sweep Saturday; Kōhei comes after practice to carry trash bags (151–154).

**School**
- 7:50 a.m. at the entrance (178).
- About 200 second-years; the lists are six sheets posted in the entrance hall (162).
- Opening day has a ceremony, then a first period and lunch (202, 247, 253).
- Rika is making matching keychains; the crowned-frog clip is new (167, 169).
- Rumor: the transfer student is "super tall" and "from somewhere far" (190).
- The vice-principal is 5′0″ in shoes (191). Add to the style-guide §1b heights list as [P].
- A boy named Fukuda, "very easy to find," was in their class before and isn't in 2-B (200–201).
- Kōhei's name is about halfway down the 2-B list (198).
- Seats look like free choice: Ryōsuke third row by the window, Kōhei second-to-last row by the window, Natsuki behind him, Nanoha two rows over (187, 208, 237).
- Natsuki's intro: "looking for a dojo that'll put up with me"; someone in the front row claps (222–223).
- Natsuki spots Kōhei's kendo from his tsuka callus (242). The callus itself is existing [P].
- By lunch Natsuki has half the class's names, two club invitations, and a karaoke date with a group of girls (date unstated) (253).
- A girl "by the door" told her about the three confessions before she'd put her shoes away (262).
- Nanoha's tour offer: library, music rooms, sticking shoe lockers, a coin-eating vending machine (284).
- A faded rectangle on the wall where a trophy case used to be (304).
- The building is old; the heating "sounds like a ghost" (308).
- Natsuki sits backward in Kōhei's chair (310).
- Sendai to the town is "barely three hours by train" (327). Canon keeps travel times Open.

**Night**
- Kōhei knows about the eleventh step too (350).
- Nanoha's front door is about ten feet from where they talk (364).

**Prologue**
- The cut is across the back of his wrist; he held it closed all the way home; she binds it with a strip of cloth; new line "Hurt again. Give me your hand… Hold still." (26, 32–33).

**Existing [P] reused, so no new entry is needed:** Shirasawa; Hoshino Kitchen on Tue/Thu/Sun; clinic day on the 18th; the 5:40 alarm and two lunches; the kinpira; Rika's clips; Ōno's cardigan; six second-year classes; the green pool; stairs squeaking on 4 and 11; the bathroom window facing the mountains; the clipboard; six moves and Sendai; the tsuka callus; the face catalogue (No. 1 and No. 4); Genji's back; "Kō-chan"; the score-keeping.

## Outside this check (for the dialogue pass, §3b; not counted above)
- **Natsuki's verdicts and self-labels,** which §3b names: "Okay, you're fun" (272), "People tell me I'm pushy" (289).
- **The "very" tic:** 71, 200, 270, 297, 308, 328.
- **"She says it like…" / "the way you…":** 30–31, 147, 277, 353, alongside the kept line 336.
- **Two girls reading Kōhei's face:** Akane at 67–69 and 96; Nanoha at 359–361.
- **Akane's mock-formal deadpan,** which §3b says she never does: "Medical science is baffled" (65).
- **Ryōsuke's hot-dog / "sub roll" argument (174–183):** it follows canon §1 and outline 1.3, but the later §3b replaces it with taiyaki head-or-tail. The documents conflict, so Story should settle it; the draft isn't wrong.
