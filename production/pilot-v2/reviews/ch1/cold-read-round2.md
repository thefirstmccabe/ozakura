# Ch1 cold read, round 2 (§9 step 3e), Oct 18

Three new fresh readers (same personas and prompt), on the script after the round-1 fixes and their diff check, with the round-1 art fixes (falter seed 171, new classmate, petal, mist grade). The split is the same.

## The three numbers at each checkpoint
Ends up with / wants / dream woman (leading answer, %).

| Reader | After 1.2 | After 1.4 | After 1.6 | After 1.8 (end) |
|---|---|---|---|---|
| 1 casual | Nanoha 55 / **Nanoha 75** / — | Nanoha 50 / Nanoha 65 / — | Natsuki 50 / Nanoha 60 / — | Nanoha 50 / Nanoha 65 / Natsuki 45 (Nanoha 35) |
| 2 manga | **Nanoha 75** / **Nanoha 70** / — | Nanoha 55 / Nanoha 65 / — | Natsuki 55 / **Nanoha 70** / — | Nanoha 55 / **Nanoha 70** / Nanoha 50 (Natsuki 40) |
| 3 genre | Nanoha 50 / **Nanoha 75** / — | Natsuki 55 / Nanoha 65 / — | Natsuki 60 / Nanoha 65 / — | Nanoha 50 / Nanoha 65 / Nanoha 45 (Natsuki 40) |

## Against the target, both rounds
- **Ending:** on target in both rounds. It swings and finishes at 50–55. The one exception is reader 2's 75 Nanoha at the first checkpoint, before Natsuki appears.
- **Dream woman:** on target in both rounds. No reader went above 50. Averaged over the six final reads it is Natsuki 43, Nanoha 41. All six readers split the clues the same way: the wrist and callus point to Natsuki, while the scolding voice, "waited a very long time" and the hands-on-him rhyme with the collar point to Nanoha. Round 2 leans a hair toward Nanoha (two of three readers), so it is even rather than leaning Natsuki.
- **Wanting: off target, and the fixes didn't move it.** It leaned Nanoha about 63 in round 1 and about 67 in round 2. At the first checkpoint it is 70–75 for four of six readers. Natsuki's line fixes got praised (the callus read, "Big talk…", "I'm doing it anyway", the smaller smile), but every reader still called her "the thinner heroine" or a "type." The readers' own explanation is structural:
  - The first third of the chapter has only Nanoha.
  - Nanoha gets the interlude's inner life and the night scene.
  - Natsuki's appeal leans on "destiny."
  - Line-level dialogue passes won't close that. It needs Story-thread structure, for example more Natsuki on screen in Ch1 or her own interiority earlier than the Ch2 interlude. The outline treats Ch1 as direction, not a gate (the window is Ch1–4), so Ch2 may also carry it.
- **The 70% rule** is broken at the first checkpoint by four of six readers on wanting, and by one reader on the ending. All of these come before Natsuki has appeared. Moving the first checkpoint after 1.4 would hide this, not fix it, so the split was left as it is.

## Round-2 flags and what was done
| Flag (readers) | Done |
|---|---|
| **Falter gaze** reads as going to frame right, away from Kōhei's window seat (all 3). Reader 1 also found it too big a shock for "just for a second" | Redone: seed 192, irises pushed into the left corners and a softer face. A blind check reads it as looking toward the window side |
| Natsuki's tour small talk is generic: "This school's nice… lived in," "Baby pictures," "one of those faces" (readers 2 and 3) | c1_0206: "Okay, real question. Is this building haunted? Something in the music room was knocking." Nanoha's "The heating sounds like a ghost" and Natsuki's "Perfect." now answer it. c1_0224: "Ha— okay. Then he's just got a very ordinary face. Don't tell him I said that." (a poke, closing with a laugh). "Baby pictures" kept |
| "Please take care of me." is stiff in English (readers 1 and 2; one reader in round 1) | c1_0148: "Looking forward to this year." (English only; よろしくお願いします is unchanged) |
| "She lives by the station" reads as Nanoha (readers 2 and 3) | c1_0236: "Mizuno lives by the station." |
| Collar CG: no visible stretch (all 6 readers across both rounds) | c1_0075: "She's had to reach up for it since middle school." "Up on her toes" stays: her feet are out of frame, and the on-model check measured her height as consistent with being on her toes |
| Image file names gave away the falter (reader 3 saw `cg_natsuki_intro_falter.jpg` in the folder) | `reader_view.py` now names images `image_01.jpg`, `image_02.jpg` and so on; the key is written outside the readers' folder |
| "Someone who knows which drawer sticks in your kitchen" is too exact a callback (all 3) | **Kept**: the brief protects it |
| "I feel like I've met him somewhere before" is the genre's stock line (all 6) | **Kept**: Story-thread decision 3 |
| "Takes one to know one" is a cliché (2 readers across the rounds) | **Kept**: the brief protects it |
| The dream's closing couplet is generic or heavy (all 6) | **Kept**: the author's keep-as-is scene. Reported |
| The cold-open mirror and mist get no echo in the chapter; no image of the Ōzakura (5 of 6) | Offered to the Story thread (a new staging fact or a new CG) |
| Akane reads as stock apart from "…You always are" (readers 1 and 3) | Noted |

Not re-read by a third round: the round-2 fixes are small, and they got a diff check (below).

## Diff check of the round-2 fixes (fresh agent)
| ID | Finding | Done |
|---|---|---|
| c1_0224 | "a very ordinary face" brings back the "very X" tic and is a verdict; the Japanese ふじさわがよくある顔 is slightly off | "Ha— okay. Then it's his face. He's got kind of a normal one, right? Don't tell him I said that." あはは、そっか。じゃあ、顔のせいだ。ふじさわって、わりとふつうの顔してるよね？ 本人には内緒ね。 |
| c1_0206 | Too many "okay"s in the scene; 真面目な質問 sounds translated | "Serious question. Is this building haunted? Something in the music room was knocking." 真面目に聞くけど。…コンコン音がしてたんだけど。 |
| c1_0207 | School heating is off by April 7 in Kanagawa, so "the heating" leaves the knocking unexplained | "It's old. The pipes sound like a ghost." 配管の音が、おばけみたいなの。 |
| c1_0236 | "Mizuno" twice in a row | "…back from walking Mizuno home to her place by the station." |
| c1_0075 | Repeats the "since… reach" frame of c1_0039 | "She's needed the extra inches since middle school." |

Fine: c1_0148 ("Looking forward to this year."), and the tone of c1_0206, which gets a mundane answer straight away and reads as a horror fan's wish.
