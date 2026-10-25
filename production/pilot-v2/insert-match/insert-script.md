# Ch2 manga insert: the practice match (`ins_match`, scene c2_match)

Three pages, ten panels, right to left [P] (the outline asked for about 9 panels on 2 pages; the beats needed a third page so the dō is a page-turn reveal, style guide §4a "surprises go on a new page"). The script lines live in `production/pilot-v2/script/ch02.ozs` between `@insert ins_match` and `@insert end`; this file is the art brief. Layout and lettering: `insert-spec.json` (1600 × 2272 page units). Built from the Oct 12 jigeiko test where its panels passed review (p1-1, p2-3, and p2-4 with the eyes recolored green).

| Panel | Box (shape) | Shot | Lettering |
|---|---|---|---|
| **Page 1** | | | |
| p1-1 | full width, 21:9 | Sonkyo at the line, tips crossed; Kirishima behind them, arm raised; the club kneeling along the wall. *(Oct 12 p1-1)* | KIRISHIMA (shout): "Hajime!" · gloss "(Begin!)" |
| p1-2 | full width, 16:9 | Over Natsuki's shoulder: Kōhei lifts his tip as if for men (the feint); her tip stays on his throat. | CAPTION: "I show her men. She doesn't even blink." |
| p1-3 | full width, 21:9 | Kōhei commits, arms going up for men; her sword already moving toward his wrist. | CAPTION: "Half a second, I stop to think. Then I go." |
| **Page 2** | | | |
| p2-1 | full width, 16:9 (large) | Her kote lands on his right wrist as his arms come up. | NATSUKI (shout): "Kote-e-e!" · SFX *PAN!* |
| p2-2 | right, 4:3 | Kirishima, arm raised toward her side. | KIRISHIMA (shout): "Kote ari!" · gloss "(Point: wrist!)" |
| p2-3 | left, 4:5 | Close on Kōhei's eyes behind his grille, a bead of sweat. *(Oct 12 p1-4)* | CAPTION: "She was there before I moved." |
| p2-4 | right, 1:1 | Close on Natsuki behind her grille, laughing, out of breath. *(Oct 12 p2-2, irises recolored jade green)* | CAPTION: "She's laughing behind her men." |
| p2-5 | left, 3:2 | Back at the line in kamae, tips crossed again. | KIRISHIMA (shout, off panel): "Nihonme!" · gloss "(Second point!)" · CAPTION: "This time I don't think." |
| **Page 3** | | | |
| p3-1 | full width, about 1:1 (most of the page) | She comes in for men; he drops under it, left foot forward (the wrong foot), and cuts across her dō as they pass. | KŌHEI (shout): "Dō-o-o!" · SFX *BASHI!* |
| p3-2 | full width, 21:9 | Turned to face each other again; Kirishima's arm raised toward Kōhei's side. | KIRISHIMA (shout): "Dō ari!" · gloss "(Point: body!)"; "Yame! …That's time." · gloss "(Stop!)" |

**Rules applied (§4a):** men on in every kendo panel; one beat per panel; every balloon inside its own panel; no tall panels except the 4:5 eye close-up; kendo calls paired with a small English gloss caption (§5).

**Build:** `python3 production/pipeline/manga/compose.py insert-spec.json panels ../../../v2/img/ins/ins_match --scale 2 --ins ../../../v2/img/ins/ins_match.json --src img/ins/ins_match/` (run from this folder) writes the three 3200 × 4544 pages and the engine's geometry file. A 1× proof: drop `--scale/--ins/--src` and give another output folder.

**Prompts and seeds:** `production/pilot-v2/art/prompts.md` (Ch2, manga insert); request IDs in `art/jobs-ch2.md`.
