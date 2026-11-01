# Phone layout pass, Nov 1 (handoff step 2)

What changed on phones, with before (Oct 31 layout, after the Nov 1 renames and name tags) and after shots at 844×345 (iPhone Safari with its bars showing). All changes are in `v2/index.html` (commit `b41a525`). No phone-only art and no separate layout: everything sits inside the existing short-landscape rule (`max-height: 500px`), except one line that applies everywhere and does nothing on iPad or desktop.

| # | Change | Why | Shot |
|---|---|---|---|
| 1 | `text-size-adjust: 100%` on the page | iPhone Safari enlarges some blocks of text on its own in landscape ("text autosizing"), which is the likely cause of the Oct 31 report that a few lines in 1.3 and the kendo lesson showed at the old iPad size. A desktop browser can't reproduce Safari's autosizing, so **please check those lines on your phone** (1.3 the class lists; Ch2 "Kendo, explained") | — |
| 2 | Taller tap areas on the control row (AUTO … MENU): an invisible strip above and below each button | The buttons were about 23 points tall, under half the 44-point touch guideline; now about 39, with no visual change. Red boxes show the tappable area | `1-tap-areas.jpg` |
| 3 | CGs (and their living stills) crop a little higher on phones | The text box covers the bottom fifth of the screen on a phone, so faces sat close to it; the CG now shows a little more of the upper middle | `2-cg-crop-collar.jpg`, `3-cg-crop-catch.jpg` |
| 4 | Menus are opaque on phones | The text box showed through the menu panels | `4-menu-panel.jpg`, `6-settings.jpg` |
| 5 | Three save slots across instead of two | Less scrolling on a short screen | `5-save-screen.jpg` |

## How it was checked
- **Every line of Ch1 and Ch2 at five phone setups** (844×345 notch left and right, 844×390, 812×330 and 812×375 with the notch on either side), with a measuring script (`production/pipeline/vn/qa_phone.py`) that records every element's box on every line and flags text smaller or larger than the phone size, anything off screen or under the notch, overlaps between the text box, name tag, face window and controls, text that overflows its box, a box taller than 42% of the screen, and controls smaller than 36 points. It also opens each translator's note, the menus, settings, the save and load screens, the backlog, the notes page, chapter select and the rotate screen. **Before: 550 small-tap flags per run. After: none, at all five setups.** The inserts' panel view and the text-message panel were in the run.
- **Name tags:** the widest full-name tag ("Tachibana Nanoha", 159 points) fits with no overflow on any line at any of the five setups.
- **iPad and desktop:** every line of Ch1 and Ch2 shot at 1180×820 and 1440×900 before and after, compared pixel by pixel (`snapshot_diff.py`). Result: see the handover (it should be zero changed frames apart from living stills).
- **Ch3** was built on this layout and checked the same way.

## Not changed
The Oct 31 values in style guide §3a (box size, notch margins, control row on the box's top edge) held up in the measurements, so they stay.
