#!/usr/bin/env python3
"""One-off: apply the author's Nov 25-26 review to story/scene-list.md (Pass 1).
Run from the repo root. The record of what he decided is
production/scene-list/review-notes-nov25.md."""
import pathlib
import re
import sys

p = pathlib.Path("story/scene-list.md")
lines = p.read_text(encoding="utf-8").split("\n")

HEAD = '''# Ōzakura scene list, Pass 1 (revised)

**Lede:** The whole story at one line per scene, revised from your review of Nov 25–26. Scenes that changed or are new carry a "changed" mark. Nothing here is approved yet.

**Status (Nov 26):** Pass 1, revised by the scene-list thread (Story role) from the author's review of every scene (the record: `production/scene-list/review-notes-nov25.md`). He looks over this revision next. **No production past Ch4 starts until the author approves this.** Pass 2 then writes each Part in full (when, where, who, what happens, what changes, threads, on screen as) and runs it past outline readers before it goes to him.

## How to read this
- **IDs never renumber.** A scene added later gets a letter (12.3a) or a zero (20.0, before 20.1); a cut scene leaves a gap; a scene that moves chapters is cut where it was and added where it lands. `P.0` is Chapter 0 and `P.1` the opening credits, `V1` and `V3` are short past-life glimpses, `R.1`–`R.8` are the recall interlude, `E.0` is the end credits and `E.1` the epilogue.
- **The italic line under each chapter:** when it happens; whose chapter it is (Nanoha's, Natsuki's, shared or neither); how much present-day closeness Natsuki and Kōhei get (none, light, strong); who is in it (K Kōhei, Na Nanoha, Nt Natsuki, T Takatsuki, A Akane, then side cast); and any uncanny or dread beat with its owner.
- **Tags at the end of a scene,** in this order: whose scene (Nanoha or Natsuki; none means neither); how it's shown if not plain sprites (CG, CG×2, insert = manga, gag = gag manga in a different art style, still = living still, anim = a short animation attempt, imagined = an imagined scene, ink = the old life's brush-and-ink manga, song = a music sequence); threads (comic, dread, A+T = Akane and Takatsuki, family, kendo, uncanny); the source; and Rev on anything changed or added in this revision.
- **Sources:** Built (in the built Ch1–3), D (decided by the author or in canon as Decided), SB and a number (canon's scene bank), Map (the chapter map's proposal), **P (invented by this thread)**. D and P together means he decided the beat and the staging is this thread's.
- **"Your call"** under a scene is a question only the author can answer. Open items in canon are proposed here, never settled.
- **What manga is used for** (from the review): fights and matches; the old life; a few long wordless or near-wordless sequences (the kiss night, Nanoha's kitchen table, her answer at the festival); childhood memories; and silent physical comedy sprites can't do (the umbrella).
- **The fairy** is in the story at three levels: fully drawn in Nanoha's childhood memories; a light that lives in Nanoha's room and window scenes from Ch9 until the bloom; whole and talking after it.
- The review page and the tables at the end are generated from this file by `production/scene-list/build_page.py`. Keep the line shapes.
'''

PART_INTRO = {
    "Part 1": "It opens in the winter to come (Chapter 0), then the opening credits, then April. Natsuki arrives, and from the first week both girls are plainly the love interests. Spring is the romcom at its lightest: Nanoha is already part of Kōhei's house, Natsuki gets him to put the load down, Akane starts at their school and wedges herself into the kendo club, the two boys are plainly best friends, and the five become a group. Under it, the dream, a split second of snow at the tree, the light at Nanoha's window and the first bad dream promise the other story.",
    "Part 3": "One night undoes the summer. After a tournament he knows he should have done better in, Kōhei beats a man who harassed Nanoha, knocks her down by accident and frightens her; he ends up at Natsuki's door, and the kiss breaks the girls' pact. September is everyone owning their part: Kōhei tells Kazuo and Emi, Natsuki tells Nanoha, Takatsuki walks him to the adviser, Emi goes through the closed door, and the family starts to come back.",
    "Part 5": "It opens with the old life, whole, dreamed by both of them the night of the bloom. Then the past is settled before the danger arrives: Kōhei and Natsuki grieve that life and say goodbye to it; he goes to Nanoha in real doubt and comes back to her by choice; the girls have it out. Then a body is found, the road closes on Akane and Takatsuki, and the five learn what the wolf is and what Nanoha can do about it. The plan is gone in seconds. They live because nobody fights alone, and every one of them pays.",
}
PART_SUB = {
    "Part 4": [("Kōhei learns form from Takatsuki and learns to let his mother carry things",
                "Kōhei learns form from Takatsuki, hears from Kazuo what his father regretted and what he has to become, and learns to let his mother carry things")],
}

# chapter label -> (new title or None, new meta or None, new changes or None)
CH = {
    "Ch 1": (None,
             "*When: Mon Apr 7 · Whose: shared · Closeness: light · Cast: K, Na, Nt, T, A, Rika · Uncanny: Natsuki: her falter and his grip on the pen; Kōhei: the dream of her*",
             None),
    "Ch 3": (None,
             "*When: Thu Apr 10 – Sat Apr 12 · Whose: shared · Closeness: strong · Cast: K, Na, Nt, T, A, Kirishima, Genji, Emi, Mio · Uncanny: Kōhei: the tree in snow, for a split second; Town: the saying on the shrine steps, and the tree's legend*",
             "**Changes:** Nanoha is shown as the person who already shares his load, Natsuki as the one who gets him to put it down, and the tree gets its legend."),
    "Ch 4": ("The Light at Her Window",
             "*When: Sun Apr 13 – Mon Apr 14 · Whose: Nanoha · Closeness: light · Cast: K, Na, Nt, T, A, Mio, Genji, Chie, Fairy · Uncanny: Nanoha: the light at her window, and who it was; Town: thanking the path home*",
             "**Changes:** Mio asks the question nobody else will, Nanoha is stung by how fast he answers, and we see when Nanoha fell for him."),
    "Ch 7": (None,
             "*When: May · Whose: Nanoha · Closeness: none · Cast: K, Na, Nt, T, A, Mio, Fairy · Uncanny: Nanoha: a plushie that moved by itself*",
             None),
    "Ch 8": ("The New Hire",
             "*When: late May – early June · Whose: neither · Closeness: none · Cast: K, T, Yuzu · Uncanny: Kōhei: the first dream of the eyes*",
             "**Changes:** A new hire starts keeping score, his best friend is no help at all, and the first of the bad dreams arrives."),
    "Ch 11": (None,
              "*When: late June – July · Whose: shared · Closeness: strong · Cast: K, Na, Nt, T, A, Rika, Emi · Uncanny: Natsuki: she feels what Nanoha only imagined; Kōhei: the first dream of the path that won't end*",
              None),
    "Ch 13": (None, None,
              "**Changes:** With the pact made, the girls can be rivals and friends in one room and allies against a third party, and Nanoha nearly says it by accident."),
    "Ch 17": (None,
              "*When: mid-August, Obon · Whose: Natsuki · Closeness: light · Cast: K, Na, Nt, A, Genji · Uncanny: Natsuki: a stone on the old path that she can't photograph; Kōhei: his hands know a sword*",
              "**Changes:** The dead are welcomed home, Natsuki finds a stone no one visits, Kōhei is handed a sword his hands already know, and the summer ends."),
    "Ch 18": (None,
              "*When: late August · Whose: Nanoha · Closeness: light · Cast: K, Na, Nt, T, A, Emi, Kazuo · Uncanny: Kōhei: the other fight, as he hits a man who is already down*",
              "**Changes:** Nanoha sees the frightening version of him and backs away from his hand, and Kazuo sits down at the gate to wait."),
    "Ch 19": (None, None,
              "**Changes:** Natsuki kisses him, backs away and sends him home; by morning she has asked to be the one who tells Nanoha, and he has said yes to Kazuo because he has nothing left."),
    "Ch 20": (None,
              "*When: late August – early September · Whose: Nanoha · Closeness: none · Cast: K, Na, Nt, T, A, Emi, Kazuo, Fairy · Uncanny: Nanoha: the slap she only imagines, which Natsuki feels and names, and a rabbit put back on her pillow; Kōhei: the dream of her hands, and she is crying*",
              "**Changes:** He tells Kazuo and Emi, the pact is broken out loud on the roof, Nanoha goes cold, and Kōhei owns his half to her and to the club."),
    "Ch 21": (None, None,
              "**Changes:** Emi goes through the closed door because he lets her, we see what Dad asked of him, and we see the night Nanoha didn't hold him."),
    "Ch 25": (None,
              "*When: October · Whose: Nanoha · Closeness: none · Cast: K, Na, A, Mio, Emi, Kazuo, Fairy · Uncanny: none*",
              "**Changes:** Nanoha, still hurt, lets him back into the ordinary life they share, and Kazuo tells him what his father regretted and what he has to become."),
    "Ch 26": (None,
              "*When: late October, Kyoto and Nara · Whose: shared · Closeness: strong · Cast: K, Na, Nt, T, A, Rika, Ryōsuke, Mom, Fairy · Uncanny: Natsuki: she ties his sash like someone who has done it for years; Nanoha: she can sense what Natsuki is holding back; Kōhei: a dream of a wedding, the bride's face hidden*",
              "**Changes:** Away from shifts and family he gets the whole trip, an hour with each girl and a dream of a wedding, and goes home knowing he has to choose."),
    "Ch 29": ("Asking",
              "*When: November · Whose: neither · Closeness: none · Cast: K, Na, T, A, Emi, Kazuo, Mom · Uncanny: Kōhei: a walk home he keeps counting, and nothing happens*",
              "**Changes:** He tells her parents properly, starts asking people for things, and stops treating help as a debt."),
    "Ch 32": (None,
              "*When: New Year · Whose: shared · Closeness: light · Cast: K, Na, Nt, T, A, Emi, Kazuo, Mio, Genji, Mom, Fairy · Uncanny: Town: the tree blooms in the snow, and nothing else happens there; Nanoha: that night her friend is back*",
              "**Changes:** The tree blooms out of season in front of the whole town, and that night Nanoha gets her friend back while the other two go to sleep."),
    "Ch 33": (None,
              "*When: New Year's morning and early January · Whose: Natsuki · Closeness: strong · Cast: K, Nt · Uncanny: none new: they wake knowing*",
              "**Changes:** They wake knowing all of it, mourn that life together and let it be over, at her insistence."),
    "Ch 34": (None,
              "*When: early January · Whose: Nanoha · Closeness: none · Cast: K, Na, A, Fairy · Uncanny: Nanoha: her friend, whole and talking*",
              None),
    "Ch 37": (None,
              "*When: late January · Whose: neither · Closeness: none · Cast: K, Na, Nt, T, A, Mio, Fairy · Uncanny: The wolf, met awake for the first time; Nanoha: she finds a road that isn't there and opens it*",
              None),
    "Ch 38": (None,
              "*When: late January – February · Whose: neither · Closeness: light · Cast: K, Na, Nt, T, A, Genji, Fairy · Uncanny: Town: two more deaths; Nanoha: what her family used to do*",
              "**Changes:** They learn what they can about the wolf and about the caretaker family's old job, and decide it has to be them."),
    "Ch 39": (None,
              "*When: February · Whose: shared · Closeness: light · Cast: K, Na, Nt, T, A, Mom, Fairy · Uncanny: Nanoha: holding its road to one stretch, and what that takes out of her*",
              None),
    "Ch 40": (None, None,
              "**Changes:** They make a plan that needs every one of them, built on a wolf nobody has actually fought."),
    "Ch 42": (None, None,
              "**Changes:** The plan goes in whole and is gone in seconds."),
    "Ch 43": (None, None,
              "**Changes:** Natsuki stops the death she once watched, the wolf ends, and every one of them pays."),
    "Epilogue": ("At the Old Grave", None,
                 "**Changes:** Both of her lives end the same way: full, and grateful."),
}

CH0 = '''### Ch 0 — The Walk Home
*When: a January dusk to come · Whose: neither · Closeness: none · Cast: T, A · Uncanny: Reader: the road turns to woods, and the eyes*
**Changes:** The reader sees where winter is going before the story starts, and the credits promise both stories.
- **P.0 Chapter 0.** A January evening to come: Takatsuki walking Akane home, the two of them talking. Then the same mirror comes round again, the road is woods, his shinai is out and there are eyes in the mist. Her legs give out. Voices, flashlights, cut to black. Most likely a color manga sequence with sound. *(insert · anim · dread · D · P · Rev)*
- **P.1 Opening credits.** A song over stills and short clips, cut fast: all five, both girls at equal weight, nothing that shows who the woman in the dream is. It ends on new title art (all five, with some dread in it) and holds there with one button to begin. First visit: a bare start screen, Chapter 0, the credits, the title. Later visits open on the title. *(anim · song · D · Rev)*
'''.split("\n")

INTERLUDE = '''### Interlude — The Old Life
*When: the night of the bloom, and long ago · Whose: shared · Closeness: strong · Cast: K, Nt · Uncanny: The past life, in full, dreamed by both of them*
**Changes:** The reader gets the whole old life and exactly how it ended, so everything after is dread, not mystery.
- **R.1 Before.** Brush and ink, for the whole chapter. Two people who have known each other since they were small. He comes back from a lost war with no lord and no name to offer. *(insert · ink · D · P · Rev)*
  - *Your call:* The recall is a full chapter of its own, between Ch32 and Ch33, so nothing renumbers. You set the direction (a dream that night, the death in full, Vagabond style); these eight lines are my first cut of what's in it. Right shape?
- **R.2 The wedding.** The bride in the white hood, now with her face: a marriage arranged for an heir, between two people already in love. *(Natsuki · insert · ink · D · Rev)*
- **R.3 The year.** About a year of it, and no children: her teasing, his late returns, the cut on his wrist, her counting his habits from the veranda. *(Natsuki · insert · ink · D · Rev)*
- **R.4 The walk.** A winter morning. She laughs at him for going armed on a walk, and he ties the cord anyway. The same landmark comes round again. *(insert · ink · D · Rev)*
- **R.5 The slow fight.** It comes straight at him. He cuts it, again and again, and it doesn't stop. He is losing, and behind him she can't run for help. *(insert · ink · dread · D · Rev)*
- **R.6 The trade.** The only move left: he gives it his throat to get inside its reach, and kills it. *(insert · ink · D · Rev)*
- **R.7 The promise.** Her kneeling in the snow with him. The promise. His last word, which we don't hear. The tree blooms over them. *(Natsuki · insert · ink · D · P · Rev)*
  - *Your call:* Hold back his last word here and give it at the end of the wolf fight (43.6)? It's the one thing I'd keep from the reader.
- **R.8 After.** Her long life as his widow, with no heir for the house; the stone she raises for him; her own name added to it when she dies old. *(Natsuki · insert · ink · P · Rev)*
'''.split("\n")

# scene id -> new full line, or None to cut
R = {
    "P.0": None,
    "1.1": '- **1.1 Morning.** The 5:40 alarm, two lunches, Mom\'s closed door; Nanoha walks in with her mother\'s food; Akane, in their school\'s uniform now, sends the two of them on ahead. Emi goes to Akane\'s entrance ceremony in Mom\'s place. *(Nanoha · family · Built · D · Rev)*',
    "1.3": '- **1.3 Class lists.** 2-B again. Rika\'s tackle and one line of gossip; Takatsuki arrives mid-argument about which end of a taiyaki you eat first. *(comic · Built · D)*',
    "3.2": '- **3.2 The window talk.** Across the three-foot gap: Usagi-san\'s time-out, "You\'re not the only person who loves her," and Nanoha simply tells him Natsuki is coming on Saturday. *(Nanoha · CG · Built · D · Rev)*',
    "3.3": '- **3.3 Saturday practice and the walk up.** She reads him in sparring and he can\'t read her, and she takes a clean point off him; on the shrine steps she catches him mid-laugh on camera. *(Natsuki · CG · kendo · Built · D · Rev)*',
    "3.4": '- **3.4 The Great Cherry.** Under the tree, for a split second, it stands in snow. He definitely sees it. It isn\'t clear whether the girls do, and nobody says anything. *(CG · uncanny · Built · D · Rev)*',
    "3.5": '- **3.5 Tea and the steps.** Over tea Genji tells the new girl the tree\'s legend: it bloomed once in winter, the year something came down from the hills, and the town says it blooms when it needs protecting. On the steps he stumbles and says "Just stopping for a rest," Nanoha says it with him, and nobody explains. She asks Natsuki to lunch. *(dread · Built · D · Rev)*',
    "3.6": '- **3.6 Lunch at the Tachibanas\'.** The whole table over Emi\'s mountain of food; Mio orders Kōhei around and loses to Natsuki at Street Brawlers. *(CG×2 · comic · family · Built · D · Rev)*',
    "4.1": '- **4.1 Group study.** Natsuki\'s first time in his house: Nanoha knows where the cups go; Takatsuki grades everyone\'s study method. Akane, who has had a crush on him for years, argues her grade like the old friend she is and then loses her words when he praises it. "You worked a shift. Sit." *(Natsuki · comic · A+T · D · Rev)*',
    "4.2": '- **4.2 Mio asks.** Mio, tagging along: "Kō-nii, when are you marrying Onee-chan?" His "We\'re not" comes too fast. Natsuki already knew they weren\'t dating; what she learns is how fast he says it and what it does to Nanoha, which only she sees. *(Nanoha · comic · D · Rev)*',
    "4.3": '- **4.3 Interlude: Natsuki.** Leaving at dusk she photographs the two lit windows. Her text to Chie isn\'t about whether he\'s taken. It\'s about how fast he said it. *(Natsuki · CG · D · Rev)*',
    "4.4": '- **4.4 Interlude: Nanoha, and the light.** Usagi-san faces the wall. A point of light is at her window: "…You came back." Then the memory, as manga: a small Nanoha and her friend playing at the shrine, the friend fully drawn and talking; at seven the friend is gone, and only Kōhei believes her and leaves cookies out with her for weeks. *(Nanoha · insert · CG · uncanny · D · Rev)*',
    "5.1": '- **5.1 The form.** Future-plans forms go round the class. Kōhei writes "work" without thinking; class president Ishida collects them. *(family · D · P)*',
    "5.2": '- **5.2 The confessions.** At lunch Rika brings up the three first-years he turned down last year, which Nanoha knows all about, to make her point: Natsuki is a bigger problem than all three. *(Nanoha · comic · Map · D · Rev)*',
    "5.3": '- **5.3 The manager.** Akane turns up at practice with a clipboard and a signed form: the kendo club\'s new manager. Kōhei objects. Takatsuki finds the form in order. Kirishima approves. *(comic · A+T · kendo · family · D · P)*',
    "5.5": '- **5.5 Backyard.** Kazuo holds the mitts for him behind the Tachibana house, an old motorcycle half apart under a tarp; Mio referees. Kazuo says he only has to ask. Kōhei says he\'s fine. *(family · Map · D · P · Rev)*',
    "5.7": '- **5.7 The city.** Arcades and crane games. Kōhei and Takatsuki go at each other on a cabinet, loudly. He wins one crane-game prize that both Nanoha and Natsuki had their eye on. Akane asleep on Nanoha\'s shoulder on the train home. *(CG · comic · D · P · Rev)*',
    "7.3": '- **7.3 Usagi-san.** Why that rabbit, as manga: at seven, after her friend was gone, Kōhei saved up and bought it for her. *(Nanoha · insert · D · Rev)*',
    "7.4": '- **7.4 Game night.** All five at Takatsuki\'s. He plays the fighting game the way he does kendo, flawless and by the book. Kōhei can\'t beat him and gets ridiculously angry. *(gag · comic · Map · P · Rev)*',
    "8.2": None,
    "8.3": None,
    "8.4": None,
    "V1": '- **V1 She watches him train.** Long ago, in brush and ink: a woman with her hair covered counts a swordsman\'s habits from the veranda, day after day. She never picks up a blade. *(insert · ink · D · P · Rev)*',
    "9.2": '- **9.2 Interlude: Natsuki.** Walking behind them with her own umbrella, she hides it and soaks herself on purpose, asking herself why the whole way. One manga sequence with 9.3. *(Natsuki · insert · comic · SB13 · D · Rev)*',
    "9.3": '- **9.3 Three under one.** She runs up drenched and laughing and takes the umbrella\'s edge. He notices her more than he means to. *(Natsuki · insert · Map · D · Rev)*',
    "9.6": '- **9.6 On the sill.** After he\'s asleep, a point of light sits on her windowsill through the storm. She lets it stay. From here it lives in her room and window scenes, and she says to it what she won\'t say to people. *(Nanoha · uncanny · D · P · Rev)*',
    "11.4": '- **11.4 What she\'d like to do.** Nanoha imagines upending Natsuki\'s bentō over her head. Cut back to her complimenting the rolled omelet, and Natsuki, mid-bite, feels something and looks over her shoulder. It\'s real. *(Nanoha · imagined · comic · uncanny · D · Rev)*',
    "11.7": '- **11.7 The path.** That night he dreams a path that keeps bringing the same bend around. *(uncanny · dread · Map · D · Rev)*',
    "12.7": '- **12.7 The new captain.** Kirishima hands the club to Takatsuki. The manager comes with it. *(comic · A+T · kendo · D · P)*',
    "14.2": '- **14.2 Yukata.** All the girls in yukata. Stalls and goldfish; Takatsuki\'s by-the-book ring toss, with Akane coaching; Natsuki photographs everything. *(CG×2 · comic · A+T · Map · D · Rev)*',
    "14.6": '- **14.6 Chie\'s verdict.** On the platform Chie tells her what she saw: he can\'t stop looking at you, and his life is with her. *(Natsuki · P · Rev)*',
    "17.4": '- **17.4 The stone.** On an old path away from the shrine she finds a weathered marker nobody tends, clears the weeds without knowing why, and can\'t make herself take the picture. It is a memorial to both of them, and nothing on it says so. *(Natsuki · CG · uncanny · SB12 · D · Rev)*',
    "17.6": '- **17.6 Last quiet night.** The tournament is Saturday and he hasn\'t practiced in two weeks. He does his swings alone in the dark yard with the real sword, and his body does things with it that kendo never taught him. He\'ll keep doing this all autumn. *(kendo · uncanny · D · P · Rev)*',
    "V2": None,
    "18.1": '- **18.1 The tournament.** As manga: he loses a match he knows he should have won. Takatsuki places. He says all the right things. *(insert · kendo · D · Rev)*',
    "18.2": '- **18.2 Karaoke.** The five celebrate Takatsuki. Kōhei sings and laughs. The girls know how he\'s really doing, he knows they know, and their pity makes it worse: underneath, in plain words, he is furious at his whole life. Natsuki takes a tired Akane home early. *(CG · comic · D · P · Rev)*',
    "18.3": '- **18.3 The way back.** A man outside a bar starts on Nanoha: words, then a hand on her arm. Kōhei steps in faster than he needs to, does nothing to calm it down, and lets the man swing first. He\'s a little glad of the excuse. *(D · Rev)*',
    "18.6": '- **18.6 His hand.** Blood on his face, his shirt and his hands, he offers her one. She backs away. *(Nanoha · CG · D · Rev)*',
    "18.7": '- **18.7 Go.** Takatsuki runs up as it\'s ending, takes it in, and tells him to get the hell away from there. Then he takes Nanoha home. Kōhei goes, alone. *(D · Rev)*',
    "19.5": '- **19.5 She stops it.** She backs away, shaken, and asks him to go. Nobody has said a word all night. *(Natsuki · D · Rev)*',
    "19.6": '- **19.6 Unsent.** Later she types to Chie, "I wouldn\'t have run," and deletes it. None of it feels in her control. *(Natsuki · D · Rev)*',
    "19.7": '- **19.7 Dawn.** Kazuo is at the gate, where he has been all night. He sees that someone else tied the bandages, and doesn\'t ask. "Are you ready to accept my help now?" / "Yes." / "Then first thing, go get some sleep." The only words spoken in the chapter. *(CG · family · D · Rev)*',
    "20.1": '- **20.1 The first day.** School starts. His face is a mess, so everyone can see he fought and nobody needs the details. He and Natsuki are both acting strangely from the first bell, and Nanoha knows something is up. Natsuki asks her up to the roof that same day, before she\'s cornered. *(Natsuki · D · Rev)*',
    "20.2": '- **20.2 Interlude: Nanoha, on the roof.** Natsuki tells her. Nanoha imagines the slap, and "He was mine." She hasn\'t moved; she\'s still smiling; and Natsuki\'s hand goes to her cheek. "Did you just imagine slapping me?" It frightens Nanoha more than anything else that day. *(Nanoha · imagined · CG · uncanny · D · Rev)*',
    "20.3": '- **20.3 We said fairly.** "You could have any boy in the school. Why does it have to be him?" What hurts is the promise. Natsuki: "I don\'t want to win by default." Nanoha has no answer, and it\'s "Natsuki-san" again. *(Nanoha · D · Rev)*',
    "20.6": '- **20.6 The adviser.** A few weeks\' suspension from the club, and no outside matches until April. Next time it\'s expulsion from the school; only his family situation and Takatsuki\'s word are saving him. *(kendo · D · Rev)*',
    "20.7": '- **20.7 At the door.** Suspended from the club, he still gets Takatsuki, who turns up at the house with his gear to train in the yard anyway. Akane answers, and thanks him for getting Nanoha home. *(A+T · family · D · P · Rev)*',
    "20.8": '- **20.8 Crying.** He dreams of her hands again. This time she isn\'t scolding him. She\'s crying. *(uncanny · Map · P · Rev)*',
    "21.1": '- **21.1 Emi.** His yes at dawn cost nothing. This does: he steps aside and lets her through his mother\'s door, the thing he has been hiding. "I know you\'re hurting, but your son is falling apart." *(family · D · P · Rev)*',
    "21.3": '- **21.3 Interlude: Nanoha, at the funeral.** One manga sequence through 21.5, in her words. His mother doesn\'t come. People murmur. A fifteen-year-old stands as chief mourner, and Nanoha watches from the second row. *(Nanoha · insert · family · D · Rev)*',
    "21.4": '- **21.4 The bills.** That night he sits at the kitchen table working out how many shifts it takes. She walks in without knocking, for the first time, and does her homework across from him. *(Nanoha · insert · family · D · Rev)*',
    "21.5": '- **21.5 What she didn\'t do.** She imagines holding him and telling him everything: I would do anything. Cut back to her pencil, not moving. Now she knows who did hold him. *(Nanoha · insert · imagined · D · Rev)*',
    "21.6": None,
    "V3": '- **V3 The arrangement.** Long ago, in brush and ink: a swordsman with no name to offer kneels across from a man with no son. Behind the screen, her sleeve. They already know each other. *(insert · ink · P · Rev)*',
    "23.1": '- **23.1 Back.** First practice after the suspension. In front of the whole club he tells Takatsuki he was right. Only the five know about what. *(kendo · D · Rev)*',
    "25.5": '- **25.5 Her window.** That night she opens hers first, and the light is on her sill. They talk about nothing until one. *(Nanoha · CG · still · D · Rev)*',
    "26.2": '- **26.2 Kimono day.** In rented kimono they pass a real shrine wedding, the bride in a white hood. Natsuki reties his sash without thinking, quick and right. "My grandma," she says. Nanoha watches her hands. *(Natsuki · CG · uncanny · Map · D · Rev)*',
    "26.5": '- **26.5 Interlude: Nanoha, lights out.** Two rivals in the dark who each know the other knows. Nanoha finally says it to her face: she\'s angriest at herself, because Natsuki can act and she can\'t. Natsuki is kind, and holding something back, and Nanoha can sense it. *(Nanoha · uncanny · D · Rev)*',
    "26.6": '- **26.6 Interlude: Akane.** The house without him. She waters Dad\'s plants, and her mother comes out onto the balcony and asks which one is which. *(CG · family · D · P)*',
    "26.7": '- **26.7 Souvenir.** Takatsuki brings the club\'s manager a charm for health from the correct shrine, with his reasoning. She is beside herself, and ties it to her bag. *(comic · A+T · P · Rev)*',
    "27.4": '- **27.4 Now.** She freezes again, finds him in the crowd, and goes off script, deadpan: she has lived next door to someone her whole life and never told him what that\'s meant, and she\'s going to, today. Then she walks off the stage by herself. *(Nanoha · CG · D · Rev)*',
    "27.5": '- **27.5 Natsuki first.** He finds Natsuki on the roof and tells her before anyone. She knew. She says the kind thing, and asks him to go. *(Natsuki · CG · D · P)*',
    "27.6": '- **27.6 Nanoha.** That evening he reaches her before she has to come to him, and tells her, using her name for the first time in years. She imagines answering, composed: "This is the happiest moment of my life." What she actually does is fall apart and run into his arms. *(Nanoha · imagined · insert · CG · D · Rev)*',
    "28.2": '- **28.2 Not an announcement.** Nobody at school is told. Akane knows from how he says "I\'m heading out." Mio demands tribute. Her parents are another matter (29.0). *(comic · family · P · Rev)*',
    "29.1": None,
    "29.2": None,
    "29.3": None,
    "32.3": '- **32.3 The bloom.** The great cherry opens, all of it at once, in the snow. The crowd cheers. Genji doesn\'t. Nothing else happens. *(CG×2 · anim · still · uncanny · D · Rev)*',
    "32.4": None,
    "32.5": None,
    "32.6": '- **32.6 Back.** Nanoha comes home from the shrine and her friend is on the windowsill, whole and talking, as if ten years were an afternoon. She never left. Nanoha just stopped being able to see her. *(Nanoha · CG · uncanny · D · Rev)*',
    "33.1": None,
    "33.2": None,
    "34.6": '- **34.6 What it costs.** The dream of her hands doesn\'t come that night, and never comes again. *(D · P)*',
    "36.2": '- **36.2 What the fairy knows.** She tells the three of them what she can: its road is its strength, and on a road that never ends it never tires. Something like it was here long ago. The tree can shelter but not hunt, and she doesn\'t know how to kill it. *(CG · dread · D · Rev)*',
    "36.5": '- **36.5 The favor.** Kōhei has shifts he can\'t drop. He asks Takatsuki to walk Akane home on those nights. Takatsuki accepts as if sworn in. *(A+T · family · D · P)*',
    "37.3": '- **37.3 Not like the story.** It doesn\'t do what the story says. It follows, stops, stares, starts toward them and stops again. His shinai is up and it\'s coming when the lights arrive. He never has to fight it. *(dread · D · Rev)*',
    "37.5": '- **37.5 The motorcycle.** Kazuo isn\'t home. She takes his keys, and Kōhei drives, objecting to all of it, at length. Mio sees everything and names her price. *(Nanoha · CG · anim · comic · D · Rev)*',
    "37.7": '- **37.7 Out.** Flashlights, voices. Takatsuki carries Akane himself. The eyes watch them leave, and don\'t follow. *(CG · dread · A+T · D · Rev)*',
    "37.8": '- **37.8 After.** Akane, wrapped in every blanket in the house, wants it noted that she was only resting; at home it goes down as one of her spells. Days later Kazuo asks whether somebody\'s been riding his motorcycle. Nobody answers. *(comic · family · D · Rev)*',
    "38.1": '- **38.1 Takatsuki\'s notes.** What he observed, in order: it followed, it stared, it started and stopped. All accurate, and all about a wolf that was only playing. The legend got the following right and the rest wrong. *(dread · D · Rev)*',
    "38.2": '- **38.2 Genji.** Asked about the old customs, and not told why, he has customs, not answers: the saying on the steps, thanking the road, the lamp. In bad winters a woman of this house took the lamp and went out to meet whoever was late. *(dread · D · P · Rev)*',
    "38.4": None,
    "38.5": '- **38.5 Why us.** The police are searching real roads and paths. Only Nanoha can find the other kind, only three of them can hold a sword, and he has had a real one in his room since August. The adults know nothing, and it stays that way. *(D · P · Rev)*',
    "39.3": '- **39.3 Obligation, obviously.** Akane gives Takatsuki "obligation chocolate, obviously." He takes obligations very seriously: he goes to Kōhei and formally asks his permission before saying a word to her. Kōhei has to be sat down, and says yes. She isn\'t told. *(gag · comic · A+T · D · P · Rev)*',
    "39.5": '- **39.5 Practice.** Nanoha holds its kind of road to one stretch for ten minutes while the others walk it, and can\'t stand up afterward. Takatsuki walks it in full kendo armor and takes the helmet off himself: in mist he can\'t see sideways or hear. *(Nanoha · CG · uncanny · D · P · Rev)*',
    "39.6": '- **39.6 What she doesn\'t say.** The fairy tells her plainly: the more of herself she puts in, the weaker it gets, and enough could kill her. Nanoha tells nobody yet. *(Nanoha · D · Rev)*',
    "40.1": '- **40.1 The plan.** Nanoha goes in with them, carrying the lamp, and holds it to one stretch, which weakens it. Takatsuki meets its charge and holds it. Kōhei, with the real sword, kills it. Natsuki guards Nanoha. *(D · P · Rev)*',
    "40.2": '- **40.2 Both styles.** Kōhei and Takatsuki drill it until the instinct and the form stop arguing. In passing, Takatsuki: "Let me do my part, keep your head, and don\'t die." *(CG · kendo · D · Rev)*',
    "40.3": '- **40.3 Akane\'s part.** She stays out. She\'ll wait at the tree, where the road lets out, with the first-aid kit, the phone and a story ready for the adults. She points out that sitting still through something awful is the one thing she has trained for. *(family · D · P · Rev)*',
    "40.4": '- **40.4 The cord.** No armor for him: the padded gloves ruin the grip on a real sword. Natsuki ties the sword\'s cord at his waist, fast and sure. The frame widens: "You guys, I\'m right here." *(Natsuki · CG · comic · SB25 · D · Rev)*',
    "40.5": None,
    "V4": None,
    "42.1": '- **42.1 Into it.** Dawn mist. Akane stays at the tree. Four walk in: the two boys in front, Nanoha with the lamp, Natsuki beside her. No helmets. *(CG · still · dread · D · P · Rev)*',
    "42.2": None,
    "42.3": '- **42.3 Seconds.** It comes at once. Takatsuki meets the charge with perfect form and it doesn\'t matter: it has him by the leg and throws him. The plan is gone. *(insert · dread · D · Rev)*',
    "42.4": '- **42.4 Interlude: Akane.** At the tree, where the road lets out, with the kit and the phone. She can see none of it. She stays where she said she would. *(CG · family · P · Rev)*',
    "42.5": '- **42.5 The same fight.** Kōhei is alone at the front with the girls behind him, the samurai\'s situation exactly. He cuts it and it doesn\'t stop. Nanoha puts more of herself in. *(insert · dread · D · Rev)*',
    "42.6": '- **42.6 Go.** Mist takes him and the wolf away from the lamp. Nanoha tells Natsuki to go, and says she\'ll hold it. Natsuki goes. Nanoha is alone, spending more than she can afford. *(Nanoha · insert · D · Rev)*',
    "43.1": '- **43.1 The opening.** Alone with it and losing the same slow fight, he starts the old answer: the guard drops, to let it come. The reader has seen exactly this. *(insert · D · Rev)*',
    "43.2": None,
    "43.4": '- **43.4 Inches.** She hits it off its line. The bite takes his shoulder instead of his neck, and it turns on her and opens her face. *(Natsuki · CG · anim · D · Rev)*',
    "43.5": '- **43.5 The strike.** It is fixed on him now, as in the trade. Takatsuki, crawling, grabs hold of it, the opposite of form, and Kōhei drives the sword in one-armed. It comes apart into mist. *(insert · CG · D · Rev)*',
    "43.6": '- **43.6 Live.** A flash of the old snow, and the one thing the recall held back: his last word to her. *(CG · D · P · Rev)*',
    "43.7": '- **43.7 The goodbye.** Nanoha has spent everything that let her see. The last thing it shows her is her friend, saying goodbye properly this time, and unbothered: she isn\'t going anywhere. *(Nanoha · CG · uncanny · D · Rev)*',
    "43.8": '- **43.8 Just resting.** They come out where the road lets out, and Akane is the only one standing. She gets under Nanoha\'s arm, "We\'re just stopping for a rest," and makes the call with the story ready. *(family · D · P · Rev)*',
    "44.1": '- **44.1 What it cost.** One hospital room with too many visitors. His shoulder: no kendo until summer. Takatsuki\'s leg, which will never fully heal. Natsuki\'s face, stitched. His mother signs the forms. *(CG · family · D · P · Rev)*',
    "44.2": '- **44.2 What she can\'t see.** Nanoha sweeping at the shrine; the light under the branch is just light. He finds out she knew it could kill her and told Natsuki, not him, and they have the argument: deciding alone is what he has done all year. *(Nanoha · CG · D · Rev)*',
    "44.3": '- **44.3 White Day.** Takatsuki returns Akane\'s chocolate threefold, as custom requires, and walks her to her gate at his new pace; she times his rehab with the stopwatch he gave her. She thanks the road for seeing them home. No confession. *(comic · A+T · D · P · Rev)*',
    "44.4": '- **44.4 Graduation.** Kirishima and the third-years leave. "Next Saturday?" Takatsuki asks, on crutches, and Kōhei, one-armed, says yes. *(kendo · D · Rev)*',
    "44.5": '- **44.5 Natsuki asks.** Her father\'s transfer comes, as it always does. For the first time she asks to stay, and they let her. The scar is proof she was there, and she doesn\'t hide it. *(Natsuki · CG · D · P · Rev)*',
    "44.6": '- **44.6 The form.** The future-plans form comes round again for third year. He writes something he wants. We see him write it, and not what. *(P)*',
    "E.1": '- **E.1 Natsuki, old.** Her grandson takes her to the old grave, the stone she weeded at sixteen. The scar is still on her face. She sits down, and the fairy comes out to her, as she does for the very young and for those at the end of a long life. A good death after a full one. *(Natsuki · CG×2 · still · D · Rev)*',
}

# scene id -> lines to add right after it (after any Your call it gets)
AFTER = {
    "8.1": ['- **8.2a No help.** Takatsuki walks him to his shift and hears about the new hire. He asks three clarifying questions and has no advice at all. *(comic · D · P · Rev)*'],
    "13.1": ['- **13.1a Customers.** Nanoha and Natsuki come in for dinner and watch Yuzu work on him. They have a pact; she didn\'t sign it. For one evening they\'re allies. *(CG · comic · Map · D · Rev)*',
             '- **13.1b Point to Tachibana.** Nanoha orders, very politely, in a way that leaves Yuzu flustered. Natsuki awards the point. *(Nanoha · comic · D · P · Rev)*'],
    "17.2": ['- **17.2a The storehouse.** Airing out the Tachibana storehouse for the summer, he picks up a long wrapped bundle with his hands already in the right place. A sword, older than anyone can say. Genji tells him to take it home, and he does. *(CG · uncanny · D · P · Rev)*'],
    "18.7": ['- **18.7a Interlude: Kazuo.** At the Tachibanas\' door it\'s Takatsuki, not Kōhei, and Emi presses him. Their daughter is all right, he says, and the rest is Kōhei\'s to tell; if he doesn\'t, they won\'t have to ask twice. Kazuo accepts that, tells his wife he\'ll wait, and sits down at the gate. *(family · D · Rev)*'],
    "19.6": ['- **19.6a The river.** He can\'t go home to the two windows. He sits by the river until it\'s light, and her text reaches him there: "Let me be the one to tell her." *(still · D · P · Rev)*'],
    "20.3": ['- **20.3a Usagi-san.** That night the rabbit goes across her room and she cries the ugly way, angriest at herself: Natsuki can act and she can\'t. In the morning he\'s back on her pillow, and she didn\'t put him there. *(Nanoha · CG · uncanny · D · P · Rev)*'],
    "25.3": ['- **25.3a The shed.** After dinner Kazuo, rebuilding the motorcycle\'s carburetor, hands him a wrench and starts talking about the karate club he shamed at nineteen. *(family · D · P · Rev)*',
             '- **25.3b What he said.** "He told me he was afraid he\'d asked too much of you." Then Kazuo apologizes, for all the times he offered and didn\'t insist. *(CG · family · D · Rev)*',
             '- **25.3c The hospital, again.** The same room, the part he wasn\'t there for: Dad to Kazuo, already sorry. *(CG · family · D · Rev)*',
             '- **25.3d Worthy.** Kazuo, plainly: winning wasn\'t the job, getting her home was; he won, and she still ended up on the ground. Fight when it\'s right and it doesn\'t endanger the person you\'re protecting. He could take the sword back, and doesn\'t. *(family · D · P · Rev)*'],
    "26.1": ['- **26.1a Sights.** The trip in full, the way manga do it: the famous places shown and talked about, Ishida lecturing, Natsuki\'s camera on everything. *(CG×2 · comic · D · Rev)*',
             '- **26.1b The deer.** The Nara day. Takatsuki bows to the deer by the guidebook and they bow back only to him. Kōhei gets mugged for his crackers. *(CG · comic · D · Rev)*'],
    "26.5": ['- **26.5a The hood.** That night he dreams a wedding. The bride wears the white hood, and he can\'t see her face or her hair. *(CG · uncanny · D · P · Rev)*'],
    "26.7": ['- **26.7a Waiting.** The light couldn\'t follow her to Kyoto. It\'s on her sill when she gets home. *(Nanoha · D · P · Rev)*'],
    "32.6": ['- **32.6a Asleep.** Next door Kōhei falls asleep with the snow still coming down. Across town, so does Natsuki. *(D · P · Rev)*'],
    "34.1": ['- **34.1a The reunion.** Those three days Nanoha has her friend back: ten years of hurt on one side, and on the other someone very old, fond and a little vague about how long it\'s been. It\'s funny, and it stings. *(Nanoha · CG · uncanny · D · P · Rev)*'],
}
# scene id -> lines to add right before it
BEFORE = {
    "20.1": ['- **20.0 The next day.** He sleeps until afternoon, goes next door, and tells Kazuo and Emi all of it, including that he isn\'t sure he\'d have stopped. Upstairs, Nanoha\'s window stays shut. *(family · D · P · Rev)*'],
    "29.4": ['- **29.0 Properly.** At the table he has eaten at for sixteen years, he bows and tells Kazuo and Emi he is dating their daughter. Emi has known for a decade. Kazuo lets him sweat for ten seconds. *(comic · family · D · P · Rev)*'],
    "33.3": ['- **33.0 Waking.** They wake knowing all of it. Natsuki has watched him die. She breaks, and she is not surprised. *(Natsuki · CG · D · Rev)*'],
    "42.1": ['- **42.0 Preparing.** A music sequence before the walk: each of them getting ready alone, in the rain before dawn. Your idea, after the rain lead-in to the church scene in Cowboy Bebop; you\'ll come back to it. *(anim · song · D · Rev)*'],
    "E.1": ['- **E.0 End credits.** A song over stills of their later lives. *(still · song · D · Rev)*'],
}
CALLS = {
    "5.5": "You said this one might be manga. Yes or no?",
    "26.1a": "Kyoto is now a long chapter (eleven scenes). Keep it as one, or split it into two halves in Pass 2?",
    "42.4": "Akane's second stretch in her own head, now waiting at the tree. You left this open until you'd read Ch42. Keep it?",
    "44.6": "Still open: what he writes. My proposal stands (university, to teach, with kendo) and so does the fallback (we don't see it).",
    "E.0": "Credits before the epilogue or after it? I've put them before, so the stills carry us across the years to her.",
}

TAIL = '''## Whole-story questions
- **Q7.** Ch8 is down to three scenes (the new hire, the two boys, the first dream of the eyes). Leave it short, or fold it into Ch7? *(What I'd do: leave it, and decide once Part 1 is written in full.)*
- **Q8.** The recall interlude is a whole chapter of brush-and-ink manga, the most expensive stretch in the story. Roughly how long should it run? *(What I'd do: about as long as two ordinary inserts put together, mostly wordless, and settle the page count in Pass 2.)*
- **Q9.** The old-life scenes are now told once, in the recall, and the wolf fight only flashes back to panels the reader has seen. That leaves two short glimpses before the bloom (V1 in Ch9 and V3 in Ch23). Keep both? *(What I'd do: keep both. They're the only taste of the brush-and-ink look before Ch32.)*

## What changed in this revision
- **New:** Chapter 0 as a real scene and the opening credits (P.0, P.1); the two boys in Ch8 (8.2a); the sword at Obon (17.2a); Kazuo at the door (18.7a); the river (19.6a); telling Kazuo and Emi (20.0); Usagi-san thrown (20.3a); Kazuo's point about being worthy (25.3d); Kyoto in full and the deer (26.1a, 26.1b); the wedding dream (26.5a); the light waiting (26.7a); telling her parents (29.0); the night of the bloom (32.6a); the recall interlude (R.1–R.8); waking (33.0); the reunion with the fairy (34.1a); the preparing sequence (42.0); the end credits (E.0).
- **Moved:** the dinner with Yuzu, from Ch8 to Ch13 (8.3, 8.4 became 13.1a, 13.1b); the big Kazuo talk, from Ch29 to Ch25 (29.1–29.3 became 25.3a–25.3c); the light and "…You came back," from the tree in Ch3 to her window in Ch4; the "yes" to Kazuo, from Ch21 to the gate at dawn (19.7), with its cost in 21.1; his last word, out of the recall to 43.6 if you agree.
- **Cut:** the inventory (8.2); two of the four past-life glimpses (V2, V4); "Yes" as its own scene (21.6); the fugue at the shrine and "You two, again" (32.4, 32.5, and 32.6 as it was); Ch33's two inserts, now in the recall (33.1, 33.2); the storehouse in winter and the old armor (38.4); the "trust" exchange (40.5); the old-life scenes inside the wolf fight (42.2, 43.2).
- **Rewritten from your decisions:** the night of the fight and the kiss (Ch18–19); the roof (20.2, 20.3); Nanoha's kitchen table as manga in her words (21.3–21.5); what she says on the stage and how she answers (27.4, 27.6); the bloom (Ch32); Ch37, where Takatsuki never has to fight it; the plan and the whole wolf fight (Ch40, Ch42, Ch43); what each of them pays (44.1); the epilogue at the old grave.
- **Settled without a text change** (the questions under them are gone): 1.3, 5.1, 5.3, 12.7, 26.6, 27.5, 34.6, 36.5, and the six whole-story questions from the first pass (keep 44 chapters; Ch37 is the first time anyone meets the wolf awake; the deaths are strangers; point of view as drafted; the seven gag inserts; try each animation once).

## Changes from the chapter map (for other threads)
The chapter map stays the chapter-level summary until the author approves this list. Where this list differs, on purpose:
- **Chapter 0 and the opening credits** come before Ch1; the recall is **an unnumbered interlude chapter** between Ch32 and Ch33.
- **Akane** is a first-year at their school and one of the five: the kendo club's manager from Ch5 (approved), with a crush on Takatsuki that predates the story. She stays out of the wolf fight and is the one standing at the end. **Akane and Takatsuki** end with no confession; he asks Kōhei's permission in Ch39 and she isn't told.
- **The two boys** are shown as friends in Part 1 (5.7, 7.4, 8.2a); Ch8 no longer has the girls in it.
- **The fairy** never left: Nanoha stopped being able to see her at seven. A light lives in Nanoha's room from Ch9; she is whole and talking from the night of the bloom (32.6) and has a reunion scene in Ch34.
- **Ch3 (built) changes:** no unspoken Saturday; a split-second CG of the tree in snow; the light moves to Ch4; Genji tells the tree's legend at tea; two new CGs.
- **The sword** is his from Ch17. There is no armor for him and no storehouse scene in winter.
- **The night of the fight:** Takatsuki arrives as it ends and sends him away; a Kazuo interlude closes Ch18; Ch19 is wordless until the gate; Kōhei tells Kazuo and Emi the next day.
- **Kazuo's talk and Dad's regret** move from Ch29 to Ch25, before the choice. Ch29 is now him telling her parents.
- **The bloom:** nothing happens at the shrine but the tree. The recall is a dream that night and shows the death in full.
- **The wolf** attacks; it isn't a careful hunter. Takatsuki never fights it in Ch37. In Ch42 it takes him out in the first seconds. Nanoha goes in and weakens it at her own cost. Costs: Takatsuki's leg, Natsuki's face, Kōhei's shoulder, Nanoha's gift.
- **The adults know nothing,** before or after.
- **Dreams** now fall in Ch1, 6, 8, 11, 16, 20, 23, 26, 28 and 30; Ch26's is new (the wedding, her face hidden).
- **One uncanny owner per chapter** holds through Part 3 and may bend after it (the author, Nov 25): Ch26 has three.
- **Takatsuki is captain from Ch12** (approved); Kirishima graduates in Ch44.
- **Natsuki stays** for third year; the epilogue is at the old grave, not the tree.

## Tables
Generated from the chapters above by `production/scene-list/build_page.py --tables`. Don't edit by hand.
'''

CHAP = re.compile(r"^### (Ch \d+|Epilogue) — (.+)$")
SCENE = re.compile(r"^- \*\*(\S+) ")

# cut the old head (everything before Part 1) and the old tail sections
i_part1 = next(i for i, l in enumerate(lines) if l.startswith("## Part 1"))
i_q = next(i for i, l in enumerate(lines) if l == "## Whole-story questions")
i_tables = next(i for i, l in enumerate(lines) if l.startswith("<!-- tables:start -->"))
body = lines[i_part1:i_q]
tables = lines[i_tables:]

out, used, used_after, used_before, used_ch = [], set(), set(), set(), set()
label = None
pending_meta = pending_changes = None
k = 0
while k < len(body):
    line = body[k]
    if re.match(r"^\s+- \*Your call:\*", line):
        k += 1
        continue
    m = re.match(r"^## (Part \d+) — ", line)
    if m:
        out.append(line)
        part = m.group(1)
        # the paragraph is the next non-empty line
        k += 1
        para = body[k]
        if part in PART_INTRO:
            para = PART_INTRO[part]
        for a, b in PART_SUB.get(part, []):
            if a not in para:
                sys.exit(f"{part}: intro text to replace not found")
            para = para.replace(a, b)
        out.append(para)
        k += 1
        continue
    m = CHAP.match(line)
    if m:
        label = m.group(1)
        if label == "Ch 1":
            out.extend(CH0)
        if label == "Ch 33":
            out.extend(INTERLUDE)
        title, meta, changes = CH.get(label, (None, None, None))
        if label in CH:
            used_ch.add(label)
        out.append(f"### {label} — {title}" if title else line)
        pending_meta, pending_changes = meta, changes
        k += 1
        continue
    if line.startswith("*When: ") and pending_meta:
        out.append(pending_meta)
        pending_meta = None
        k += 1
        continue
    if line.startswith("**Changes:**") and pending_changes:
        out.append(pending_changes)
        pending_changes = None
        k += 1
        continue
    m = SCENE.match(line)
    if m:
        sid = m.group(1)
        for extra in BEFORE.get(sid, []):
            out.append(extra)
            eid = SCENE.match(extra).group(1)
            if eid in CALLS:
                out.append(f"  - *Your call:* {CALLS[eid]}")
        if sid in BEFORE:
            used_before.add(sid)
        if sid in R:
            used.add(sid)
            if R[sid] is not None:
                out.append(R[sid])
        else:
            out.append(line)
        if sid in CALLS and R.get(sid, line) is not None:
            out.append(f"  - *Your call:* {CALLS[sid]}")
        for extra in AFTER.get(sid, []):
            out.append(extra)
            eid = SCENE.match(extra).group(1)
            if eid in CALLS:
                out.append(f"  - *Your call:* {CALLS[eid]}")
        if sid in AFTER:
            used_after.add(sid)
        k += 1
        continue
    out.append(line)
    k += 1

missing = (set(R) - used) | (set(AFTER) - used_after) | (set(BEFORE) - used_before) | (set(CH) - used_ch)
if missing:
    sys.exit("not found in the scene list: " + ", ".join(sorted(missing)))

text = HEAD + "\n" + "\n".join(out).rstrip("\n") + "\n\n" + TAIL + "\n" + "\n".join(tables)
p.write_text(text, encoding="utf-8")
print("written:", len(text.split("\n")), "lines")
