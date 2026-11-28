# Scene list: handover after the Nov 27 round

Written Nov 27 by the scene-list thread (Story role), for a fresh Story-role thread. The author asked for this handover so a new thread can apply the day's decisions; the old thread was long enough that its early part had been compressed.

## Where things stand
- **Pass 1 has been reviewed twice.** Round one (Nov 25–26) was applied on Nov 26. Round two (Nov 27) is **settled but not applied**: nothing from it is in `story/scene-list.md`, canon, the chapter map or the outline yet.
- **The source of truth for round two** is `production/scene-list/review-notes-nov25.md`, from "## Second review round (Nov 27)" to the end. Read all of it before touching the list. Where this handover and those notes differ, the notes win.
- **The author has approved applying it.** He was asked "Shall I write the handover so a fresh thread applies today's decisions, renumbers, marks all of this and rebuilds the page?" and said "Please."
- **Still nothing past Ch4 is built until he approves the scene list.**

## Read first
1. `CLAUDE.md` and the status board (`story/production-log.md` §0).
2. `production/scene-list/README.md` (the brief and its Status section).
3. `production/scene-list/review-notes-nov25.md`, the Nov 27 sections in full; skim the earlier ones.
4. `story/scene-list.md` as it stands (the Nov 26 revision).
5. The canon sections you will edit (list under step 6), each in full before changing it.

## The job, in order
1. **Reset the change marks.** Strip every `Rev` tag and `*Changed:*` line left from the Nov 26 revision. Tag only what changes now, with a short `*Changed:*` note under each (he asked for those in line; they made review easier).
2. **Apply the Nov 27 decisions to `story/scene-list.md`** (summary below; details in the notes).
3. **Renumber once** (approved). Ch1–4 keep their numbers. Write the old-to-new table for every chapter and scene ID to `production/scene-list/id-map-nov27.md`, so both rounds of his page notes still resolve. After this, "scene IDs never renumber" holds again: later additions get letters.
4. **Mark point of view on every scene** by the rules in the notes ("### Point of view"). Two marks per scene: how it is shown, and whose head we are in (which can be nobody's). Run the rule-8 audit as you go and flag any scene whose point is something physically happening but that has no CG or manga. Show him the new manga and CG totals; he has said cost is not the worry ("Let's just do this right").
5. **Extend `build_page.py` and `page-template.html`** for the new mark: a head tag (suggested syntax `head:K`, `head:Na`, `head:Nt`, `head:T`, `head:A`, `head:Kz`, `head:none`), a filter for non-Kōhei scenes, a count per chapter, and a chip for flagged scenes. The existing "whose" tag (whom a scene favors) stays; the balance tables use it.
6. **Canon and the other docs**, edited in place in `story/`, each with a line in `canon-revisions.md`, then uploaded to the Project (`project_read` first; `project_write` refuses otherwise). What changes is listed under "Canon edits" below. The chapter map gets a dated pending block as on Nov 26 (its rows are rewritten Part by Part when the long version is approved). `production/pilot-v2/scene-outline.md` gets its pending note extended (Chapter 0 is now a December evening on the hill road; 4.2, 4.4 and 4.5 change).
7. **Sweep chapter numbers.** The renumber shifts about half the chapters (table below), and canon, the chapter map, the style guide, the pilot notes and the log cite chapters by number. List every "ChN" mention with a script, check each against the table, and leave historical mentions alone ("Ch19–24 in the Oct 12 map"). If it won't fit in your thread, put it on the status board as pending and say so to him plainly; do not leave canon half swept without a note at its top.
8. **Rebuild and publish a new private review page** with a clean notes store (a new artifact; declare `{"db": {}}`; a new `--key`). The earlier pages stay as his record: round one `bf6df7b9-6b56-4e39-b8ee-b72539360df8`, round two `e32a7dfd-96e1-4220-98a2-dca69044c1ea`. The page stays private: he has not said the whole plot may go on the public site.
9. **Tell him in a few lines** what was applied, what you decided yourself, and what he needs to look at (the point-of-view marks, the flagged scenes, anything below marked unanswered).
10. **Then Pass 2**, Part by Part, each through fresh outline readers (brief §5), reviewed on a page. No outline readers have been run on any revision so far. He likes independent agent checks but ask before spawning agents.

## Chapter numbers, old to new
| Old | New | Note |
|---|---|---|
| Ch0–Ch7 | same | Chapter 0 now flashes forward to new Ch31, a December evening |
| Ch8 The New Hire | folded | Yuzu's first day and Takatsuki's "no help" open new Ch12; the first eyes dream goes to new Ch8 |
| Ch9–Ch25 | Ch8–Ch24 | each drops by one (Umbrella is Ch8, Summer Break is Ch12, Karaoke is Ch17, Second Semester is Ch19, Autumn Tournament is Ch23) |
| Ch26 School Trip | Ch25 and Ch26 | split: the trip as a trip; the choice closing in |
| Ch27–Ch30 | same | the escort starts in Ch29 (November), the walks are in Ch30 |
| new | Ch31 | the loop, mid-December (old 37.1–37.8 without Natsuki) |
| Ch31 Christmas | Ch32 | the almost-kiss |
| Ch32 The Bloom | Ch33 | Part 4 now ends here |
| Interlude | Interlude | ends on the promise and the bloom; R.8 is cut |
| Ch33 What We Were | Ch34 | |
| Ch34 Doubt | Ch35 | the real first kiss |
| Ch36 Found | Ch36 | the body, the fairy's telling, Takatsuki and Akane told the rest, Mom at the station |
| Ch35 Since Summer | Ch37 | the girls' talk, now after the body |
| Ch37 The Loop | gone | moved to Ch31 |
| Ch38–Ch44, Epilogue | same | Ch43 needs a new title ("Live" is dropped) |

This is the plan at chapter level. Check the count (44) and every Part boundary when you build the scene-level table.

## The Nov 27 decisions, in brief
Details, his words and the reasons are in the notes under the same headings.

**The old life**
- "Live" is dropped. She says she'll wait for him (find me); his last words are the promise; then the bloom. Nothing is held back from the recall. 43.6 goes.
- Her life after his death stays out of the story. R.8 is cut. The dream ends at the bloom for both of them. The stone stays both of theirs, unexplained.
- When the beast dies, in both lives: a strike to the head; for a breath it is only a wolf, odd, very large and old; then it is gone, and the mist with it. No corpse in either era.
- The dream is manga with no single point of view; the wedding is through his eyes, because we want to see the bride. Brush and ink, with full color for the wedding and the death. In R.2 she is interested, not yet in love.

**The wolf's first appearance moves to December**
- Escort from November; the loop in mid-December as a scare (no attack, nobody hurt); Nanoha follows her light into the trees; the adults hear it was one of Akane's spells.
- Natsuki misses the rescue only because she is across town and is told everything the next day.
- Afterward Kōhei tells the group his dread dreams (the eyes, the road) and keeps the romance dreams to himself.
- The dream on Jan 1 explains December. Early January: grief, he tells Nanoha, the fairy tells them what she can, he chooses. Mid-January: the body, then the girls' talk. Late January on, unchanged.
- The hiker moves to October. Mom's walk becomes her coming to the station for Akane in January. The fairy is visible to all five from January.

**Kōhei**
- He looks forward to the late-summer tournament from Golden Week on. It is the qualifier for regionals; the autumn tournament Natsuki does well in is regionals. One want, no tournament arc.
- First kiss: an almost-kiss on Christmas Eve, broken by the bride in the white hood; the real one when he chooses Nanoha again after the dream.
- He tells Kazuo alone the day after the fight, and Kazuo apologizes then. September shows the help. The October talk gets shorter.
- At the fireworks he looks. On the night of the fight he misses and punches a brick wall. He admits he is scared (22.2).

**Natsuki**
- The transfer news comes in November, right after she isn't chosen; she tells only Chie. Show it from outside (boxes, Chie's question): canon's working rule keeps her interludes on what she does until the girls' talk.
- The night before the fight Nanoha tells her to stay. In 44.5 she asks her parents and stays for herself. Last image: Nanoha takes the camera and puts her in the frame under the ordinary spring bloom. She gives Nanoha the Kyoto photo.
- 38.6: the two of them work out together what the old fight looked like.
- Her mother is a nurse, planted early. On the roof the slap is not named aloud. No new boy.

**Structure and small notes**
- Fold Ch8; Yuzu arrives in Ch13 (old numbering) as a summer hire; split Kyoto; the count stays 44.
- 4.5 opens Ch5. Akane's wait at the tree moves up to right after the four walk in. The wedding-day gag is the last end-credit still, before the epilogue.
- The rest of his page notes are listed in the notes ("### His page notes from the second round").

## Canon edits this implies
Read each section in full first; never turn an Open item into a fact; add a line to `canon-revisions.md` for each.
- **§1:** the cold open is a December evening on the one-lane road up his hill, flashing forward to the new loop chapter; the genre note that says the Ch20 roof "names it aloud"; kendo's "tournament arcs dropped" gains its one exception.
- **§2:** the point-of-view line (Decided Nov 26) gains the rules.
- **§5:** the promise (the "two halves" proposal replaced); the optional coda retired; the stone unexplained; "she finds him" in the three beats reworded; the third beat reworded (her full life is her own choice).
- **§6:** the imagined slap (the Nov 25 "says it aloud" reversed); the recall (ends at the bloom; nothing held back); Kazuo's first talk (alone; the apology); the first kiss; the tournament; the threat's timeline (the first encounter in December; the body in January stands); "no corpse" gains the moment of the plain wolf.
- **§7:** Natsuki's ending (the transfer, the photograph).
- **§8:** Kōhei ("how active he is": one want in the first half); Natsuki (her mother; the transfer); Nanoha's ability ladder (she finds a road in December, before her friend can talk; the Ch20 rung without the line); the fairy's stages (a light at the December rescue).
- **§10 (scene bank):** item 22 (the farewell); the optional coda at item 24 retired; 24a, the night before the battle (the "Live" clause goes); 24b (Nanoha tells her to stay).
- **§11:** close "whether his last word is held back"; keep the form, the preparing sequence and the recall's length open.

Section numbers were checked against canon's headings on Nov 27; line-level placement is yours to confirm by reading each section.

## Proposed by Story and not answered: do not treat as decided
Mark these [P] in the list and ask him on the page.
- Her line at the promise: "I'll wait. Don't be late."
- "You're late" gets its last use in the grief chapter, and that closes the promise.
- The vow's form: the old saying that husband and wife are bound for two lives, so nothing hangs over Nanoha afterward.
- Kazuo finds Mom the bookkeeping work.
- "Double shifts" in May is an early prep shift before school plus the evening one. (He said "Rest I'm fine"; treat as accepted, still [P].)
- The story the five tell: a huge stray dog on an early club run. Akane hides the sword before she calls.
- Where each tournament beat lands (5.4, 12.5, early August).

## Still open by his choice
- What he writes on the form (44.6).
- The preparing sequence before the fight (42.0, his Cowboy Bebop rain lead-in).
- The recall interlude's length and exact contents (he expects it and the kiss night to run near full manga-chapter length).

## Watch for these
- **December has to stay a scare.** If it reads as a wolf attack, five teenagers sit on it for ten weeks.
- **They know for about eight weeks before the fight.** January needs the deaths and the failed adults' search to carry that.
- **Three competitions** now (the summer meet, the qualifier, regionals) against canon's "one or two at most." He was told; left as is.
- **Ch13 (old numbering) grows to nine short scenes.**
- **Akane was missing from old Ch8 and Ch9 in a row;** the fold fixes one of them.
- **Not raised with him:** Takatsuki reporting a big stray dog to the police box in December would seed the story they tell in March. Ask before using it.

## Working with him
- Phone app: lead with the answer, short lists, one topic at a time. Direct, no flattery, plain pushback; say so when an idea of yours was wrong.
- Propose and discuss first; change nothing until he says to. He asks for critique of his own ideas and means it.
- Imperial units. Hours and the decide-or-ask rules are in the Project instructions and `CLAUDE.md`.
