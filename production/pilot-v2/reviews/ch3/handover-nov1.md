# Ch3 "Windows": handover (Nov 1)

**Play:** https://thefirstmccabe.github.io/ozakura/v2/ (Menu → Chapters → Chapter 3, or play on from Ch2). Build = branch `v2-ch3` (merged to `main` for the link). Ch1 and Ch2 play exactly as approved (build `b41a525`, branch `approved/v2-ch2`).

## What's in it
Thursday night (Kōhei home after his shift, Akane asleep under a blanket, Nanoha on the floor with his manga), the window talk (three CGs: Nanoha holding Usagi-san under her chin, her chin on her arms on the sill, and the rabbit's sentence reduced), Saturday practice (Takatsuki's tip about Natsuki's shoulder), the shrine steps with Natsuki and her camera, the Great Cherry with Genji and Nanoha (Natsuki photographing the tree, the moment under the low branch and its light, "…You came back."), tea and Genji's stumble on the way down, and lunch at the Tachibanas' (the "Itadakimasu!" CG, Mio's Street Brawlers rematch). Ends on "To be continued: Chapter 4, 'The Light at the Shrine,' comes next."

126 voiced lines and 98 lines of narration. New: sprite sets for Natsuki (track clothes and camera), Akane (home), Mio and Genji; Nanoha's and Emi's home sets brought into v2; Akane's home face windows; two backgrounds (the shrine steps, the Tachibanas' living room); five CGs plus the tree with its light; living stills on the window sill (curtains), the turned rabbit, Natsuki at the tree (petals) and lunch (steam). Genji, Emi and Mio voiced by Algenib, Achernar and Kore (+4 semitones), the §7 picks.

## Process (§9)
Writing gates before art: continuity check, lint, dialogue diagnosis → rewrite → overcorrection check, a Japanese pass, one cold-read round (three fresh readers, Ch1–3). Reports in this folder. Every image went through a fresh-agent on-model check (`onmodel-r1.md`). Voices transcript-checked (Wizper); 8 retakes (the cold-read rewrites and three mishearings). QA on every line at iPad (1180×820), desktop (1440×900) and two phone setups (844×345 notch left, 812×375 notch right) with `qa_play.py` and `qa_phone.py`; then an independent build review (`build-review.md`).

## Cold read (record `cold-read-round1.md`)
All three numbers inside the outline's targets at every checkpoint, nobody at 70%:
- **Who he ends up with:** back from Natsuki 58 at the end of Ch2 to Nanoha about 53.
- **Who he wants:** inside 40–60 for everyone, leaning Nanoha (about 55).
- **The dream woman:** Nanoha about 48 at the end (peak 55); two readers keep a third option, "a spirit tied to the tree."
- All three caught both Saturday secrets ("Thursday. After school. Before the window." was quoted by all three as the chapter's best sting), the look a second too long, the wrong moment under the branch, Natsuki lowering the camera and the stumble ritual. All three now think the Ōzakura is the dream's tree. Nobody named the childhood fairy.

## Provisional details [P] (judge by playing; Story folds them into canon)
The story details are listed in `story/pilot-notes.md` §3, "v2 Ch3 'Windows'" (Thursday, the window, Saturday practice, the steps, the tree, the stumble, lunch). From production:
- **Usagi-san faces the curtain after his sentence is reduced** (the outline said the corner). The image model would only turn him toward the curtain, so the text follows the art. Ch4's "rabbit facing the wall" still works as the next step.
- **The light under the branch** is drawn in code on the tree plate: a small cool-white point where the branch leaves the trunk, against dark bark. All three cold readers read the first version (warm, lower) as the sun on the horizon.
- **Genji is drawn at 58 inches.** The style guide gives him 5′2″ (stooped); at 62 inches his head came out about a quarter bigger than Natsuki's, so the stoop takes the 4 inches. One number in `v2/index.html`.
- **Nanoha's and Emi's home sprites** are cropped a little differently from their school sets, so the engine sizes each outfit on its own (`VSET`).
- **The night living room** is the day plate with a warm, dim tint.
- **The lunch CG** is from Kōhei's seat (his hands together at the bottom of the frame), Genji on his right; c3_0413 says so.

## Known compromises
{COMPROMISES}

## Spend
Ch3 about $9.10 (art $4.42; CGs and living stills $2.43; voices $2.25){ONMODEL_SPEND}; running total about $49.30 (going over $40 is approved; Story's guard for Ch3 was $15). Details in `production/pilot-v2/ledger.md`.

## Waiting on you
- **Play Ch3** and flag what doesn't work. Approving it starts Ch4.
- **On your iPhone:** check that 1.3 (the class lists) and Ch2's kendo lesson now show at the phone text size (the Nov 1 phone pass, `../phone-nov1/README.md`).
- **The rabbit facing the curtain** (above), if you'd rather have the corner.
- **For you and Story** (reader flags outside Production's lane, from the cold read): the prologue (fog, mirror, katana) gets no echo in three chapters; Dad, Mom and Akane's illness stay unnamed ("too coy," all three readers); the paired symmetry (two interludes, two "decided," two inexplicable moments, two cover stories) is starting to show; Kōhei reads as passive; the text never describes Akane (her lilac hair surprised readers in the lunch CG; in the game her sprite shows it earlier); two readers asked why the first-years bow to Nanoha (c3_0120; nobody explains). Ch1–2 lines flagged again (approved, so only listed): the drawer line in Natsuki's mouth, the kendo lesson's glossing, "Race you!", the collar CG's river side and collar-vs-tie.
- **Kept against one reader:** c3_0308, "I tell myself that all the way to the door" (another reader called it the turn from cozy to uncanny).
