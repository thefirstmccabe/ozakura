# Ch2: author's report, Oct 28 (Safari, tapping quickly)

**Outcome: not applied.** On replaying, the author found it working and said not to change anything (Oct 28, 7:51 pm: "maybe we shouldn't change anything"), then marked the edit unnecessary. The fix below stays on branch `ch2-tap-hold`, unmerged. Nothing in the live build changed.

**Report:** "I don't see the drawing CG, and the manga part is broken… after the first panel, the manga just ends and cuts to the next scene." In Safari, tapping quickly through lines he had read before (not in Skip mode). He asked whether it could be caching.

**Not caching:** the live site was at the same commit as the test build (`7fe9f22`; the Pages deploy succeeded), and GitHub Pages content goes stale in Safari for 10 minutes at most.

**Cause:** taps went straight through the art. Measured with a tap every 0.3 s (Chrome, iPad size):
- The whiteboard CG fades in over 1 s, and a tap during its arrival pause moved straight on to its one narration line and then off it: it was over 90% visible for about 0.3 s.
- In the match insert, every tap moved the camera to the next panel at once, so from panel 2 on the 0.55 s zoom never landed (each panel was up about 0.3 s, moving the whole time). Panel 1 held only because taps are ignored while the insert loads. That reads as the manga ending after its first panel. A line of text takes two quick taps (one finishes the typing), but a panel took one.

**Fix built, not merged (engine, would touch Ch1):** art that is still arriving holds the taps, as the animated catch already did.
- A CG that comes up where none was (not a swap while one is already up) waits for its image to load, and taps are dropped until it has faded in (1 s; 1.4 s for a slow fade, 0.5 s for a cut). Then a tap goes on as before.
- In a manga insert, taps are dropped for 0.8 s after each panel or page turn starts (0.9 s for the opening), so the zoom lands before the next tap counts.
- Same 0.3 s tapping afterwards: the whiteboard is over 90% visible for about 1 s and over 50% for about 1.5 s; each panel is up about 0.95 s and holds still for about 0.4 s. Read at a normal pace, nothing changes.
- Kept as is: the whiteboard comes down before Rika's "How do you get a point?" so her scheming look shows (holding the CG through her line would hide her sprite).

**Seen in the test WebKit, not reported:** at an insert page turn, the 0.6 s cross-fade held the old page for about 0.8 s and then snapped to the new one. It may be the sandbox's software rendering rather than Safari. Backlog: watch a page turn on the iPad.

**Checks:** the fast-tap measurements above in Chrome, and in WebKit (WebKitGTK through WebDriver, the engine Safari uses): the whiteboard stays up about 1.7 s and all 10 panels play. Normal-pace and Skip play unchanged. The full playthrough and Ch1 snapshot diff were stopped when the author paused.
