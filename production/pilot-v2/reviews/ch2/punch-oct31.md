# Ch2 punch list, Oct 31 (author; for Production)

Two items, both approved by the author on Oct 31 (about 2:53 pm: "I'm going to want this change and a change to both chapters to work better on phones"). Written in a review chat; nothing in `v2/` or the scripts has been touched. Spend: none expected.

| # | Item | Source |
|---|---|---|
| 1 | Natsuki's interlude (c2_interlude): trim and reorder the interior narration | A fresh read of Ch2 in a review chat (Oct 31); every change below approved by the author |
| 2 | Phone layout, Ch1 and Ch2 (engine; iPad and desktop must not change) | The "Visual novel phone layout" chat (Oct 31); its last plan, below |

---

## 1. Natsuki's interlude

**Why:** the four paragraphs between "Natsuki looked at that last message for a long time." and her "yeah i'm good!!" reply re-explained what the chat had just shown (the read, already in her text and in Takatsuki's debrief) and parked Chie's backstory inside the held beat, so the dodge read as considered instead of reflexive. "and didn't quite believe herself" named the subtext that Nanoha's Ch1 interlude ("She did not let herself think about why it had needed deciding at all") leaves unsaid. "Six schools" was the third use of the number (Ch1's intro and lunch).

**Edits:**
- c2_0257: cut "Six schools." The line starts "You learned names fast."
- c2_0282–c2_0283 (Nanoha) move up, to after c2_0260. c2_0283 ends at "none of her business." ("and didn't quite believe herself" cut.)
- c2_0280–c2_0281 (Chie's backstory) move up, to after c2_0261 (she opens the pinned chat) and before the first text.
- c2_0277 and c2_0278 are replaced by one line: "She didn't know why she'd cried. She didn't know how she'd known where he would move, either." Production's choice whether it keeps the c2_0277 ID (suggested) or takes a new one; c2_0278 goes. "The fall, probably. First-week nerves." and the nine-years paragraph ("That should have covered it.") are cut.
- Nothing else changes: the texts, the balcony and "The other ten she kept." stay as they are.

**The scene as it should read** (source syntax; unchanged lines keep their IDs):

```
== c2_interlude | Natsuki: the apartment
@mode interlude Interlude: Natsuki
@bg bg_natsuki_apartment_night
@bgm night
> The apartment was dark when Natsuki let herself in. It usually was.  #c2_0252
> There was a note on the counter in her mother's handwriting: curry in the fridge, back late, proud of you. Her mother wrote "proud of you" every first week. Natsuki had never asked what for.  #c2_0253
> Her father was in Yokohama until Friday.  #c2_0254
> She ate the curry standing up. Then she sat on the floor between the boxes that hadn't been unpacked yet. They said SAPPORO in marker, crossed out, and SENDAI, crossed out, and SHIRASAWA underneath in newer marker.  #c2_0255
> The little paper flag was still in her blazer pocket from last night. She stood it up in the pen cup on the low table.  #c2_0256
> You learned names fast. You laughed first. You said yes to karaoke. You didn't buy anything that wouldn't fit in a box.  #c2_0257
> She had a line for it, for when people asked about the moves. She tried it out loud, to see if it still worked.  #c2_0258
natsuki(smile): "I'm amazing at first days. It's the second semesters I never get to." || 転校初日なら、誰にも負けないよ。二学期まで、いられたことがないだけで。  #c2_0259
> It still worked. It always got a laugh. It just didn't get one from her.  #c2_0260
> And there was Nanoha, who had walked her all the way home on Monday without being asked. Natsuki liked her, and not the first-week way, where you like everyone.  #c2_0282
> Nanoha lived next door to Fujisawa. Natsuki decided that was none of her business.  #c2_0283
> She took out her phone and opened the chat at the top, the one pinned so long it had its own little gray tab. Chie.  #c2_0261
> Chie had been her best friend in fourth grade, and again last year, when her dad's work had swung them back through Sendai like a pendulum. Chie was the only person she'd ever managed to keep. Birthday calls. A box of {zunda mochi|sweet green soybean rice cakes} every New Year.  #c2_0280
> Chie was also more than two hundred miles away.  #c2_0281
@phone me first official kendo practice at the new school 🥋✨🔥  #c2_0262
@phone chie AND??? 👀  #c2_0263
@phone me there's a guy  #c2_0264
@phone chie oh no  #c2_0265
@phone me not like that!!! 😤😤 he's good. like scary good 😱⚔️  #c2_0266
@phone me i knew what he was going to do before he did it. every time  #c2_0267
@phone me except the last one. didn't see that one at all 🫠  #c2_0302
@phone chie ok that's actually kind of hot  #c2_0268
@phone me CHIE 😤😤😤  #c2_0269
@phone me also i cried on him 🙈🙈  #c2_0270
@phone chie NATSUKI  #c2_0271
@phone me pollen!!!!! 🤧🤧🌸  #c2_0272
@phone chie it's april  #c2_0273
@phone me why does everyone keep saying that 😩  #c2_0274
@phone chie are you ok tho. for real  #c2_0275
> Natsuki looked at that last message for a long time.  #c2_0276
> She didn't know why she'd cried. She didn't know how she'd known where he would move, either.  #c2_0277
@phone me yeah i'm good!! made a friend 🥹 a real one i think. she gave me the tour on monday and showed me the vending machine that eats coins 😂🪙  #c2_0284
@phone chie that's my girl  #c2_0285
@phone chie go to sleep. send me pics of the cherry trees 🌸  #c2_0286
@phone me ok ok. night!! 🌙✨  #c2_0287
@phone me sticker:😴💤  #c2_0326
> Natsuki put the phone down and went out onto the little balcony.  #c2_0288
> The street outside ran along the river under a row of cherry trees, white under the streetlights.  #c2_0289
> She took eleven pictures. She sent Chie the best one.  #c2_0290
> The other ten she kept.  #c2_0291
@mode normal
@bgm -
@bg black slow
@wait 1.0
@endchapter 2
```

**Notes:**
- Narration only: no re-voicing, no Japanese pass. The one voiced line (c2_0259) is unchanged.
- Reader targets (outline 2.8): she still can't explain the tear or the read, and it unsettles her more than she lets Chie see; the flip from "every time" to "yeah i'm good!!" is now tighter; she likes Nanoha, and "none of her business" (now right before "there's a guy") carries the small worry. The read is still in the text, in her own texts.
- Placement of the Nanoha pair (before the phone, not after the long look) is a judgment call [P]; the author saw it and approved. Easy to move back after c2_0277 if it plays wrong.
- Saves on c2_0278 should resume sensibly (the Oct 30 check noted a save on cut c2_0279 resumes at the interlude's start; same behavior is fine).

---

## 2. Phone layout (Ch1 and Ch2)

**Target:** a casual visitor on an iPhone in Safari with its bars showing; no setup. Reference size iPhone 12 Pro: about 844×345 points in Safari, 844×390 from the Home Screen. Nothing older than the iPhone X needs to work. Landscape only, as always (canon §2). iPad and desktop must stay pixel-identical.

**Changes** (all in `v2/index.html`, roughly 25 lines; values provisional, judged by playing):
1. **Notch margins (a bug, not polish).** The build uses `env(safe-area-inset-top/bottom)` but never left/right, so in landscape the box's left edge and the face window sit partly under the notch, and with the phone turned the other way MENU can end up under it. Add `safe-area-inset-left/right` to the dialogue box, face window, control row, texting panel and translator's-note pop-up. (`viewport-fit=cover` is already set.) The inset is zero on iPad and desktop.
2. **One phone-only rule** for landscape screens under about 500 points tall: text 17 → 16 points, name tag a little smaller, tighter padding and line spacing, no forced minimum box height. In the mockup the box drops from about a third of the screen to about a fifth.
3. **Control row moved, not hidden:** on phones, AUTO … MENU shrinks to a small row along the box's top edge, beside the name tag, freeing the bottom strip the row reserves (most of the box's dead space). No new UI. (Folding the row into MENU was dropped: MENU opens Settings, so it would have meant a new pop-up.)
4. **Android full-screen on tap-to-start** [P]: Android phones only (Chrome allows it; iPhone Safari doesn't). Not on iPad or desktop.
5. **Backlog item folded in:** on phones the text-message panel covers the interlude label (c2_0262 on).

**Dropped (author):** any "Add to Home Screen" hint; the scroll-to-collapse-Safari's-bars trick; phone-specific art or a separate phone layout.

**Checks:**
- Render at 844×345 and 844×390 with the notch on each side: title, dialogue with and without a face window, the texting panel and its interlude label, a translator's note, save/load, log, chapters, settings, and a manga insert page.
- Snapshot diff proving iPad and desktop are unchanged.
- **Ch1 is approved** (baseline `approved/v2-ch1`, commit `05a993b`): run the regression against it (style guide §9 step 10); only phone-size frames should differ.
- Full playthroughs at iPad, phone and desktop sizes.
- The author looks at it on his phone for a couple of minutes.

**Approval note:** this changes the approved Ch1 build at phone size. Proposed (not yet confirmed by the author): re-approve Ch1 together with Ch2, rather than a separate Ch1 round, with a new Ch1 baseline after.

---

## Done (Production, Oct 31; branch `ch2-punch-oct31`)
**Approval note, answered (author, 3:06 pm):** Ch1 needs re-approval **for the phone layout only**; the rest of Ch1 stays approved as it was.

**1. Interlude:** applied exactly as the block above (copied from it): c2_0257, c2_0277 and c2_0283 reworded, c2_0278 cut, the Nanoha pair and Chie's backstory moved. Lint clean; no voiced line changed.

**2. Phone layout** (`v2/index.html`):
- Notch margins: the box (and with it the face window, name tag and controls), the translator's note, the text-message panel and the menus keep clear of a notch on either side. Written so that with no notch (iPad, desktop) every value computes as before.
- Phones in landscape under 500 points tall: box padding 16/18/10, no minimum height; text 16 points at line height 1.45; name tag 13 points; face window 76 points; the AUTO … MENU row as a small strip on the box's top edge (10-point labels). The box is about 73 points tall at 844×345 (about a fifth of the screen; it was about a third).
- The interlude label moves to the left on phones, clear of the text-message panel.
- Android phones: tap-to-start goes full-screen [P]. Tested with Android, iPhone, iPad and desktop browsers: only Android goes full-screen.

**Checks:**
- Phone renders at 844×345 and 844×390 with a simulated notch on each side (the page's safe-area values set to the iPhone 12 Pro's 47 points): tap-to-start, title, chapters, dialogue with and without a face window, a long line, the texts with the interlude label, a translator's note, save, log, settings, a manga panel. One fix from them: the face window first kept its iPad size on phones and covered the start of the line; it now takes the phone size.
- iPad (1180×820) and desktop (1440×900), a shot of every line before and after the change: the only differences are the "Tap to continue" pulse and fades caught at a different moment (timing; the frames match once settled). Layout identical.
- Full playthroughs at 844×345 and 844×390: 555 lines, none missed, all 329 voiced lines, 10 insert steps, no failed requests or errors. (iPad and desktop runs above: the same.)
- **For the author:** a couple of minutes on his phone; this is the Ch1 phone-layout re-approval too.
