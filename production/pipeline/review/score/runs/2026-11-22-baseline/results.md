# Harness score against the author's punch lists

Run: `runs`. Ground truth: 46 scored items (67 in all). Strict = hit; lenient = hit or partial.

## Overall

| | Items | Caught (strict) | Caught (lenient) |
|---|---|---|---|
| All scored items | 46 | 13 (28%) | 31 (67%) |
| Catchable from the text | 32 | 11 (34%) | 23 (71%) |
| Catchable from the screen | 13 | 2 (15%) | 8 (61%) |
| Catchable from the script | 1 | 0 (0%) | 0 (0%) |

## By build

| | Items | Caught (strict) | Caught (lenient) |
|---|---|---|---|
| b0-ch1-oct17 | 6 | 1 (16%) | 4 (66%) |
| b1-ch1-oct18 | 7 | 2 (28%) | 5 (71%) |
| b2-ch2-oct25 | 22 | 7 (31%) | 14 (63%) |
| b3-ch3-nov2 | 11 | 3 (27%) | 8 (72%) |

## By kind

| | Items | Caught (strict) | Caught (lenient) |
|---|---|---|---|
| staging (staging or art against text) | 8 | 1 (12%) | 4 (50%) |
| unclear (unclear referent or meaning) | 8 | 2 (25%) | 7 (87%) |
| explains (explains itself, on the nose, clue-heavy) | 6 | 4 (66%) | 6 (100%) |
| engine (engine or layout) | 6 | 1 (16%) | 3 (50%) |
| term (untranslated term) | 4 | 3 (75%) | 4 (100%) |
| flat (flat, or doesn't land) | 3 | 0 (0%) | 1 (33%) |
| tone (tone: edgy, brooding, quippy, trying too hard) | 2 | 0 (0%) | 2 (100%) |
| overplayed (overplayed or repeated beat) | 2 | 0 (0%) | 1 (50%) |
| story (story decision or content request) | 2 | 1 (50%) | 1 (50%) |
| look-voice (character look or voice (design, casting, pitch)) | 2 | 0 (0%) | 1 (50%) |
| callback (callback that needs memory) | 2 | 0 (0%) | 0 (0%) |
| continuity (fact against canon) | 1 | 1 (100%) | 1 (100%) |

## By check

Items each check raised (strict / lenient), and how many findings it made.

| Check | Strict | Lenient | Findings | Matched an item |
|---|---|---|---|---|
| continuity | 1 | 6 | 71 | 7 |
| diagnosis | 5 | 14 | 176 | 16 |
| lint | 1 | 2 | 15 | 6 |
| reader1 | 4 | 11 | 101 | 11 |
| reader2 | 3 | 9 | 110 | 11 |
| reader3 | 4 | 10 | 119 | 9 |
| onmodel | 0 | 1 | 38 | 1 |
| build | 2 | 9 | 59 | 11 |

**Findings:** 689 in all; 72 matched an author item, 617 didn't (89% unmatched).

## Item by item

| Item | Build | Kind | Catchable | Verdict | Raised by |
|---|---|---|---|---|---|
| A02 An interlude's POV character uses face windows, not a sprite (Nanoha s | b0 | staging | screen | partial | build (partial), lint (partial) |
| A03 Ōno-sensei should be shown on screen (he speaks with no sprite) | b0 | staging | screen | miss | — |
| A04 Natsuki's arrival should stay on the front-of-class CG through the hit | b0 | staging | screen | partial | build (partial), onmodel (partial), continuity (partial) |
| A05 Natsuki isn't tall any more, so cut the 'taller than the vice-principa | b0 | continuity | text | hit | reader3 (hit), reader1 (partial), reader2 (partial), diagnosis (partial) |
| A06 The cut is on the inside of the wrist, matching the CG | b0 | staging | text | miss | — |
| A07 Rephrase 'Which I'm also fast at' | b0 | tone | text | partial | diagnosis (partial) |
| A10 Doesn't know what some of the Japanese foods are; wants a little more  | b1 | term | text | hit | reader2 (hit), reader3 (partial) |
| A11 Cut 'The moment closed up, and it was fine.' and 'It was fine.' | b1 | explains | text | partial | diagnosis (partial) |
| A12 Too much is made of the height difference; change some lines | b1 | overplayed | text | partial | reader1 (partial), reader2 (partial), reader3 (partial) |
| A19 The line about the jacket being ironed like someone meant it doesn't r | b1 | flat | text | miss | — |
| A20 Classroom murmuring about how pretty she is when she's introduced | b1 | story | text | miss | — |
| A21 The class-assignment banter doesn't really land | b1 | flat | text | partial | diagnosis (partial), reader2 (partial), reader3 (partial) |
| A23 The smirk and deadpan are used too much; non-tense talk reads that way | b1 | staging | screen | hit | lint (hit) |
| A24 The container line at the end of the restaurant part is confusing | b2 | unclear | text | partial | continuity (partial), diagnosis (partial), build (partial) |
| A25 Needs glosses (suburi, bogu) | b2 | term | text | hit | diagnosis (hit) |
| A26 'she' read as Rika | b2 | unclear | text | hit | continuity (hit), diagnosis (hit), build (hit), reader1 (hit), reader2 (hit), reader3 (hit) |
| A28 Glosses on every use of a Japanese term, not just the first | b2 | term | text | partial | diagnosis (partial), reader1 (partial), reader2 (partial), reader3 (partial) |
| A29 Don't show the full page before panel by panel | b2 | engine | screen | miss | — |
| A30 'The floor belongs to whoever stays after practice' is confusing | b2 | unclear | text | miss | — |
| A31 Switch the music after practice (the practice cue is battle music) | b2 | staging | script | miss | — |
| A32 The catch animation doesn't show her falling and being caught (flagged | b2 | staging | screen | partial | build (partial) |
| A33 His face flashed embarrassed, then normal (first time only) | b2 | engine | screen | miss | — |
| A34 'Mostly vending machines' doesn't work | b2 | flat | text | miss | — |
| A35 The same face flash (Kōhei's face before Natsuki's) | b2 | engine | screen | miss | — |
| A36 Texts need a 'tap to continue' note | b2 | engine | screen | partial | build (partial) |
| A37 Cryptic | b2 | unclear | text | partial | reader1 (partial), reader3 (partial) |
| A38 A little Nanoha in Ch2 | b2 | story | text | hit | reader3 (hit), continuity (partial), diagnosis (partial) |
| A40 Texts: the girls use more emoji and stickers, each in her own style | b2 | look-voice | text | miss | — |
| A42 Full name on a character's first line in each chapter | b2 | unclear | text | hit | reader1 (hit), reader3 (hit) |
| A45 Too many things untranslated in the kendo scenes | b2 | term | text | hit | diagnosis (hit), reader2 (hit), reader1 (partial), reader3 (partial) |
| A48 Is c2_0278 too on the nose? (c2_0279 cut) | b2 | explains | text | hit | reader1 (hit) |
| A49 The interlude re-explains what the chat just showed ('The fall, probab | b2 | explains | text | hit | reader1 (hit) |
| A51 'Six schools' is the third use of the number | b2 | overplayed | text | miss | — |
| A52 Chie's backstory parked inside the held beat, so the dodge reads as co | b2 | explains | text | partial | continuity (partial) |
| A53 Phone layout: the box takes a third of the screen; notch overlap | b2 | engine | screen | partial | build (partial) |
| A54 Akane's empty-container photo reads as Kōhei controlling her | b3 | unclear | text | partial | diagnosis (partial) |
| A55 The tree scene: cut Natsuki's camera beat (too much) | b3 | explains | text | hit | diagnosis (hit), continuity (partial) |
| A56 'It lands somewhere I wasn't guarding.' is too on the nose | b3 | explains | text | hit | diagnosis (hit) |
| A57 The text box covers part of Nanoha's face | b3 | engine | screen | hit | build (hit) |
| A58 'Trash bags.' leans on a Ch1–2 running bit he didn't remember | b3 | callback | text | miss | — |
| A59 The bridge callback needs Ch2 fresh in mind | b3 | callback | text | miss | — |
| A61 'I laugh before I can decide not to.' is too edgy | b3 | tone | text | partial | reader1 (partial), reader2 (partial) |
| A62 'lifts the camera before I can get a hand up' is unclear | b3 | unclear | text | partial | build (partial) |
| A64 The rain dodge reads oddly ('it' reads as the rain) | b3 | unclear | text | partial | diagnosis (partial), reader1 (partial) |
| A65 Three cream cardigans (Akane's too much like Nanoha's) | b3 | look-voice | screen | partial | reader2 (partial) |
| A66 Grandpa at the head of the table | b3 | staging | screen | miss | — |

**Liked items flagged as problems:** 2 of 2
- L01 (b3-ch3-nov2): diagnosis: "c3_0367 "I don't notice I've stopped being tired until we reach the top." FLAT (states the feeling). It tells the reader"; continuity: "The shrine stairway reads steeper than canon's "slightly uphill" (LOW)"; build: "c3_0359 and c3_0365: "She lifts the camera" and "pulled the camera back against her chest with both hands". The sprite h"; reader1: "Kōhei only laughs out loud with Natsuki (the chair at the restaurant, "I laugh before I can decide not to," "this time I"; reader2: "Slightly obvious: the "a second longer" device is used for Nanoha's hands (part 1) and then Kōhei's look at Natsuki (par"
- L02 (b3-ch3-nov2): reader1: "Genji: "And you're the young lady with the camera. Take as many as you like. The tree doesn't mind." A stock wise grandp"
