#!/usr/bin/env python3
"""One-off: apply the author's second review round (Nov 27) to story/scene-list.md.

    python3 production/scene-list/archive/revise_nov27.py <the Nov 26 scene list> story/scene-list.md production/scene-list/id-map-nov27.md

The input is the Nov 26 revision (commit 52b167d: `git show 52b167d:story/scene-list.md`).
The record of what he decided is production/scene-list/review-notes-nov25.md, from
"Second review round (Nov 27)"; the job is production/scene-list/handover-nov27.md.

What it does: drops the Nov 26 change marks; applies the Nov 27 decisions; renumbers once
(Ch1-4 keep their numbers and scene IDs); puts a head tag on every scene; flags scenes whose
point is something physical but which have no CG or manga; writes the old-to-new ID table.
Scenes that don't change keep their Nov 26 wording, taken from the input, not retyped.
Then run build_page.py --tables to regenerate the tables.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build_page as bp  # noqa: E402

SRC, DST, MAP = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
old_text = SRC.read_text(encoding="utf-8")
old, problems = bp.parse(old_text)
assert not problems, problems
OLD = {s["id"]: s for p in old["parts"] for c in p["chapters"] for s in c["scenes"]}
OLDCH = {c["label"]: c for p in old["parts"] for c in p["chapters"]}
OLDMETA = {}
lab = None
for line in old_text.split("\n"):
    m = bp.CHAP.match(line)
    if m:
        lab = m.group(1)
    elif lab and bp.META.match(line):
        OLDMETA[lab] = line
        lab = None

WHOSE = ("Nanoha", "Natsuki")
SCREEN = ("CG", "insert", "gag", "still", "anim", "imagined", "ink", "song")
THREAD = ("comic", "dread", "A+T", "family", "kendo", "uncanny")


def cls(t):
    if t in WHOSE:
        return 0
    if t in SCREEN or t.startswith("CG×"):
        return 1
    if t in THREAD:
        return 2
    return 3  # sources


def k(old_id, head, **kw):
    """Keep a Nov 26 scene. kw: title, line, add, drop, changed, call ('' removes), flag, also (old IDs merged in), id, sub (old, new: an ID reference to update)."""
    return dict(kind="keep", old=old_id, head=head, **kw)


def n(title, line, tags, head, changed, **kw):
    """A new scene. kw: call, flag, also (old IDs it replaces), id."""
    return dict(kind="new", title=title, line=line, tags=tags, head=head, changed=changed, **kw)


MOVED_LOOP = "Moved to December with the rest of the loop (it was {})."

# ---------------------------------------------------------------- the new list
PARTS = [
 dict(title="Part 1 — Spring (April–May)",
      intro="It opens in the winter to come (Chapter 0), then the opening credits, then April. Natsuki arrives, and from the first week both girls are plainly the love interests. Spring is the romcom at its lightest: Nanoha is already part of Kōhei's house, Natsuki gets him to put the load down, Akane starts at their school and wedges herself into the kendo club, the two boys are plainly best friends, and the five become a group. Kōhei says out loud the one thing he wants this year. Under it, the dream, a split second of snow at the tree and the light at Nanoha's window promise the other story.",
      chapters=[
  dict(label="Ch 0", fixed=True, old="Ch 0",
       meta="*When: a December dusk to come · Whose: neither · Closeness: none · Cast: T, A · Uncanny: Reader: the road turns to woods, and the eyes*",
       scenes=[
    k("P.0", "none",
      line="A December evening to come: Takatsuki walking Akane home up the one-lane road that climbs the hill to her house, the two of them talking. Then the same curve mirror comes round again, the road is gone into woods, his shinai is out and there are eyes in the mist. Her legs give out. Voices, flashlights, cut to black. Most likely a color manga sequence with sound.",
      changed="Now a December evening on the one-lane road up the hill, which disappears. It flashes forward to Ch31. Shown from outside, as manga."),
    k("P.1", "none"),
  ]),
  dict(label="Ch 1", fixed=True, old="Ch 1", scenes=[
    k("1.1", "K"), k("1.2", "K"), k("1.3", "K"), k("1.4", "K"), k("1.5", "K"), k("1.6", "Na"), k("1.7", "K"), k("1.8", "K"),
  ]),
  dict(label="Ch 2", fixed=True, old="Ch 2", scenes=[
    k("2.1", "K"), k("2.1b", "K"), k("2.2", "K"), k("2.3", "K"), k("2.4", "K"), k("2.5", "K"), k("2.6", "K"), k("2.7", "K"), k("2.8", "Nt"),
  ]),
  dict(label="Ch 3", fixed=True, old="Ch 3", scenes=[
    k("3.1", "K"), k("3.2", "K"), k("3.3", "K"), k("3.4", "K"), k("3.5", "K"), k("3.6", "K"),
  ]),
  dict(label="Ch 4", fixed=True, old="Ch 4",
       meta="*When: Sun Apr 13 · Whose: Nanoha · Closeness: light · Cast: K, Na, Nt, T, A, Mio, Genji, Chie, Fairy · Uncanny: Nanoha: the light at her window, and who it was; Town: thanking the path home*",
       scenes=[
    k("4.1", "K"),
    k("4.2", "K", drop=["comic"], add=["CG"],
      line="Mio, tagging along: \"Kō-nii, when are you marrying Onee-chan?\" His \"We're not\" comes too fast. Natsuki already knew they weren't dating; what she learns is how fast he says it and what it does to Nanoha, which only she sees. Played straight, not for laughs: the CG is Nanoha's look, and Natsuki seeing it.",
      changed="Played straight, because it's sad. Added a CG of her look, with Natsuki seeing it."),
    k("4.3", "Nt"),
    k("4.4", "Na",
      line="Usagi-san faces the wall. A point of light is at her window: \"…You came back.\" Then the memory, as manga: a small Nanoha and her friend playing at the shrine, the friend drawn and talking but her face kept from us; at seven the friend is gone, and only Kōhei believes her and leaves cookies out with her for weeks. It ends on a full page of her hugging him, and her eyes.",
      changed="The manga ends on a full-page hug and her eyes, and now ends the chapter. The friend's face is held back until the night of the bloom."),
  ]),
  dict(label="Ch 5", old="Ch 5",
       meta="*When: mid-April – early May · Whose: Natsuki · Closeness: strong · Cast: K, Na, Nt, T, A, Rika, Ryōsuke, Kirishima, Kazuo, Mio · Uncanny: Kōhei: a practice he takes too far*",
       changes="Akane takes a place in the kendo club over her brother's objections, Kōhei says out loud the one thing he wants this year, and the five go out together for the first time.",
       scenes=[
    k("4.5", "K", changed="Moved here from the end of Ch4 (it was 4.5), so Ch4 ends on her memory.",
      flag="A strike is the whole point and there's nothing to show it. I'd give it one CG."),
    k("5.1", "K"),
    k("5.2", "Na"),
    k("5.3", "K"),
    k("5.4", "K", add=["P"],
      line="A practice where he doesn't stop when he should. Kirishima ends the drill; Natsuki is the one who says something. Asked what the hurry is, he says it out loud for once: the late-summer tournament, the qualifier for regionals. He wants it.",
      changed="Added: he says he wants the late-summer tournament, the qualifier for regionals.",
      call="The tournament gets three small beats before he loses it: said aloud here, sharpened after the summer meet (11.5), and a shift costing him practice in July (12.2). Right places?",
      flag="A practice taken too far, with nothing to show it. I'd give it one CG."),
    k("5.5", "K", add=["CG"], call="", changed="Now a CG, as you said. Plain sprites won't carry it."),
    k("5.6", "K"),
    k("5.7", "K"),
  ]),
  dict(label="Ch 6", old="Ch 6", scenes=[
    k("6.1", "K", add=["P"],
      line="A week of an early prep shift before school on top of his evening one, for Akane's birthday present. Nanoha counts them and says nothing.",
      changed="School is in session in May, so the second shift is an early one before school."),
    k("6.2", "K"), k("6.3", "K"),
    k("6.4", "none", add=["D", "P"],
      line="Nanoha is already cooking in his kitchen when Natsuki arrives with her own and can't find a bowl. Her mother is a nurse, she points out; Nanoha points out whose kitchen it is. Akane referees.",
      changed="Added: Natsuki's mother is a nurse, planted here and in 9.1."),
    k("6.5", "K"), k("6.6", "K"),
  ]),
  dict(label="Ch 7", old="Ch 7", scenes=[
    k("7.1", "Nt"), k("7.2", "Nt"), k("7.3", "Na"), k("7.4", "K"), k("7.5", "K"),
  ]),
 ]),
 dict(title="Part 2 — Rain and summer (June–August)",
      intro="The rivalry comes into the open and stays friendly: an umbrella each girl cheats for, a pact made over a fever, two lunches on one desk. The first of the bad dreams comes with the first storm. Summer is the cast at its happiest and the triangle at full tilt, with Kōhei feeling the pull toward Natsuki and, at the fireworks, looking. The one thing he wants for himself, the late-summer qualifier, is being eaten by his shifts. Akane's place in the club costs her a bad day at the summer meet, where his anger first shows. The season ends quietly, at Obon, before the night that breaks it.",
      chapters=[
  dict(label="Ch 8", old="Ch 9",
       meta="*When: June · Whose: shared · Closeness: strong · Cast: K, Na, Nt, Fairy · Uncanny: Nanoha: a light on her sill in the storm; Kōhei: the first dream of the eyes*",
       changes="Each girl now knows the other knows, and the first of the bad dreams arrives.",
       scenes=[
    k("V1", "none", id="V1"),
    k("9.1", "K"), k("9.2", "Nt", sub=("with 9.3", "with 8.3")), k("9.3", "K"),
    k("9.4", "Na", flag="A sight gag (the umbrella slipping out, the zip) with nothing to show it. I'd make it the last page of the umbrella manga."),
    k("9.5", "K"), k("9.6", "Na"),
    k("8.5", "K",
      line="That night, while her light sits on the sill next door: mist, and eyes in it, and a fear he doesn't recognize. He tells no one.",
      changed="Moved here from the folded Ch8 (it was 8.5), onto the storm night."),
  ]),
  dict(label="Ch 9", old="Ch 10", scenes=[
    k("10.1", "Na", add=["D", "P"],
      line="Natsuki's seat is empty. Kōhei has a shift, so it's Nanoha who works out she's alone: her father is away, and her mother, a nurse, is on nights.",
      changed="Her mother is a nurse, on nights, which is why the apartment is so quiet."),
    k("10.2", "Na"), k("10.3", "Na"), k("10.4", "Na"), k("10.5", "Na"), k("10.6", "Nt"),
  ]),
  dict(label="Ch 10", old="Ch 11", scenes=[
    k("11.1", "Na"), k("11.2", "K"), k("11.3", "none"), k("11.4", "Na"), k("11.5", "K"), k("11.6", "Na"), k("11.7", "K"),
  ]),
  dict(label="Ch 11", old="Ch 12", scenes=[
    k("12.1", "K"),
    k("12.2", "K", flag="She goes down on the gym floor and a boy laughs; nothing shows it. I'd give it one CG."),
    k("12.3", "Na"), k("12.4", "K"),
    k("12.5", "K", add=["P"],
      line="He wins on points and nobody cheers. Takatsuki says it to his face. What Kōhei takes from it is the qualifier: he wants to win that one clean.",
      changed="Added: he wants to fight the qualifier clean."),
    k("12.6", "K"), k("12.7", "K"),
  ]),
  dict(label="Ch 12", old="Ch 13",
       meta="*When: late July · Whose: Nanoha · Closeness: none · Cast: K, Na, Nt, T, A, Rika, Yuzu, Fairy · Uncanny: Nanoha: someone keeps pardoning the rabbit*",
       changes="A summer hire starts keeping score and his best friend is no help; with the pact made, the girls can be rivals and friends in one room and allies against a third party, and Nanoha nearly says it by accident.",
       scenes=[
    k("8.1", "K", title="The summer hire", add=["family", "D"], also=["13.1"],
      line="Summer break means shifts nearly every day, and Kitchen Komugi takes on a summer hire, Shiina Yuzu. He trains her; she flirts out loud and keeps score. The girls see him mostly across a counter.",
      changed="Yuzu arrives here now, as a summer hire (it was 8.1, with 13.1 folded in)."),
    k("8.2a", "K", add=["kendo"],
      line="Takatsuki walks him from the practice he's leaving early to the shift that's costing him it, with the qualifier a month off, and hears about the new hire. He asks three clarifying questions and has no advice at all.",
      changed="Moved here with Yuzu (it was 8.2a). Added: a shift is costing him practice before the qualifier."),
    k("13.1a", "Na"), k("13.1b", "Na"), k("13.2", "Na"), k("13.3", "Na"), k("13.4", "Na"), k("13.5", "K"), k("13.6", "Na"),
  ]),
  dict(label="Ch 13", old="Ch 14",
       changes="An outsider sees what the reader sees, and for one burst of fireworks he lets himself look at Natsuki.",
       scenes=[
    k("14.1", "K"), k("14.2", "K"), k("14.3", "K"), k("14.4", "K"),
    k("14.5", "K", add=["D"],
      line="Separated from the others for one burst, he and Natsuki watch it side by side, and he looks at her.",
      changed="He looks."),
    k("14.6", "Nt"),
  ]),
  dict(label="Ch 14", old="Ch 15", scenes=[
    k("15.1", "Nt"), k("15.2", "none"), k("15.3", "Nt"), k("15.4", "Nt"),
    k("15.5", "Nt", flag="The joke is something seen (her sandals by the door, the note). I'd give it one CG."),
  ]),
  dict(label="Ch 15", old="Ch 16", scenes=[
    k("16.1", "K"), k("16.2", "K"), k("16.3", "K"),
    k("16.4", "K", flag="Physical comedy (Nanoha watching through her fingers) with nothing to show it. I'd give it one CG."),
    k("16.5", "K"), k("16.6", "K"),
  ]),
  dict(label="Ch 16", old="Ch 17", scenes=[
    k("17.1", "K"),
    k("17.2", "K", flag="The lamp going up to the tree is the picture the last walk repeats. I'd give it one CG."),
    k("17.2a", "K"), k("17.3", "Nt"), k("17.4", "Nt"), k("17.5", "Na"),
    k("17.6", "K",
      line="The qualifier is Saturday, the one he has wanted since Golden Week, and he hasn't practiced properly in two weeks. He does his swings alone in the dark yard with the real sword, and his body does things with it that kendo never taught him. He'll keep doing this all autumn.",
      changed="The tournament is now the qualifier he has wanted since Golden Week.",
      flag="His body doing things with a real sword, and nothing to show it. I'd give it one CG, or a wordless manga page."),
  ]),
 ]),
 dict(title="Part 3 — The fight and September (late August–September)",
      intro="One night undoes the summer. After he loses the qualifier he has wanted since spring, Kōhei beats a man who harassed Nanoha, knocks her down by accident and frightens her; he ends up at Natsuki's door, and the kiss breaks the girls' pact. September is everyone owning their part: Kōhei tells Kazuo, who apologizes and starts helping in earnest; Natsuki tells Nanoha; Takatsuki walks him to the adviser; Emi goes through the closed door; and the family starts to come back.",
      chapters=[
  dict(label="Ch 17", old="Ch 18", scenes=[
    k("18.1", "K", add=["P"],
      line="As manga: the qualifier for regionals. He loses a match he knows he should have won. Takatsuki goes through, and so does Natsuki. He says all the right things.",
      changed="It's the qualifier for regionals now. Natsuki goes through too, since she fights at regionals in October [P]."),
    k("18.2", "K",
      line="The five celebrate the two who went through. Kōhei sings and laughs. The girls know how he's really doing, he knows they know, and their pity makes it worse: underneath, in plain words, he is furious at his whole life. Natsuki takes a tired Akane home early.",
      changed="They celebrate both who qualified."),
    k("18.3", "K", flag="A hand on her arm and a man swinging first, with nothing to show it. I'd start the fight manga here."),
    k("18.4", "K",
      line="Kōhei takes a hit and then wins it, ugly. One swing misses outright and goes into a brick wall. With the man down he keeps hold of his collar and draws back again.",
      changed="Added: he misses and punches a brick wall."),
    k("18.5", "K"),
    k("18.6", "K",
      line="Blood on his face and his shirt, and the hand he put into the wall is a mess, though nothing is broken. He offers it to her. She backs away.",
      changed="His hand is a mess from the wall, nothing broken."),
    k("18.7", "K", flag="Takatsuki running up and sending him off is action with nothing to show it. I'd end the fight manga here."),
    k("18.7a", "Kz"),
  ]),
  dict(label="Ch 18", old="Ch 19", scenes=[
    k("19.1", "none"),
    k("19.2", "none", add=["P"],
      line="At the sink she washes the blood off his hands and binds them, out of a nurse's daughter's cabinet.",
      changed="Her mother being a nurse explains the supplies and the skill."),
    k("19.3", "none"), k("19.4", "none"),
    k("19.5", "none", flag="This is the middle of the wordless kiss night and isn't marked as manga. I'd make it part of that sequence."),
    k("19.6", "none"), k("19.6a", "K"), k("19.7", "K"),
  ]),
  dict(label="Ch 19", old="Ch 20",
       meta="*When: late August – early September · Whose: Nanoha · Closeness: none · Cast: K, Na, Nt, T, A, Kazuo, Fairy · Uncanny: Nanoha: the slap she only imagines, which Natsuki feels, and a rabbit put back on her pillow; Kōhei: the dream of her hands, and she is crying*",
       changes="He tells Kazuo, who owns his part of it; the pact is broken out loud on the roof, Nanoha goes cold, and Kōhei owns his half to her and to the club.",
       scenes=[
    k("20.0", "K",
      line="He sleeps until afternoon, goes next door, and tells Kazuo alone, all of it, including that he isn't sure he'd have stopped. Kazuo hears it and apologizes for his own part: he offered for a year and a half and never insisted. He tells Emi that night. Upstairs, Nanoha's window stays shut.",
      changed="He tells Kazuo alone, and Kazuo's apology comes here, not in October."),
    k("20.1", "K"),
    k("20.2", "Na",
      line="Natsuki tells her. Nanoha imagines the slap, and \"He was mine.\" She hasn't moved; she's still smiling; and Natsuki's hand goes to her cheek. Neither of them says a word about it, and they both know. It frightens Nanoha more than anything else that day.",
      changed="The slap is not named aloud. Her hand goes to her cheek and they both know."),
    k("20.3", "Na"), k("20.3a", "Na"), k("20.4", "K"), k("20.5", "K"), k("20.6", "K"),
    k("20.7", "K",
      line="Suspended from the club, he still gets Takatsuki, who turns up with his gear: they train in Kazuo's yard, at Kazuo's invitation. Akane answers the door, and thanks him for getting Nanoha home.",
      changed="They train in Kazuo's yard: his help has started."),
    k("20.8", "K"),
  ]),
  dict(label="Ch 20", old="Ch 21",
       changes="Emi goes through the closed door because he lets her, Kazuo's help turns practical, we see what Dad asked of him, and we see the night Nanoha didn't hold him.",
       scenes=[
    k("21.1", "K"),
    n("The books", "Within the month Kazuo has found Mom bookkeeping she can do from the back room, and Kōhei hands back two shifts a week.",
      ["family", "D", "P"], "K", "New: September shows Kazuo's help, and he can work a bit less.",
      call="Kazuo finding Mom the bookkeeping work is my proposal, not yours. Yes?"),
    k("21.2", "K"), k("21.3", "Na", sub=("through 21.5", "through 20.6")), k("21.4", "Na"), k("21.5", "Na"),
  ]),
  dict(label="Ch 21", old="Ch 22", scenes=[
    k("22.1", "K"),
    k("22.2", "K",
      line="She tells him plainly that Nanoha is in love with him. He does see it, and admits why he hasn't let himself: he's scared of anything between them changing.",
      changed="He admits he does see it, and that he's scared."),
    k("22.3", "K"), k("22.4", "K"), k("22.5", "Na"), k("22.6", "K"),
  ]),
 ]),
 dict(title="Part 4 — Autumn (October–December)",
      intro="The in-between. Banned from matches, Kōhei learns form from Takatsuki, hears from Kazuo what his father regretted and what he has to become, and learns to let his mother carry things, and for five weeks he has real feelings for both girls: Natsuki at her best at the regionals he didn't reach, Nanoha at the windows, both of them in Kyoto. At the cultural festival Nanoha stops waiting and he chooses her. Natsuki learns she is meant to leave in April and tells no one here. Then they date, visibly and happily, while bad news comes down from the hills and the dreams close in. In mid-December the hill road closes on Akane and Takatsuki, and Nanoha follows her light into the trees and gets them out: a scare nobody can explain, two weeks before the tree blooms in the snow.",
      chapters=[
  dict(label="Ch 22", old="Ch 23", scenes=[
    k("V3", "none", id="V3"),
    k("23.1", "K"),
    k("23.2", "K", flag="Physical comedy (drilled like a first-year, Akane timing) with nothing to show it. I'd give it one CG."),
    k("23.3", "K", flag="Physical comedy, and it sets up his grab in the wolf fight. I'd make it a short gag manga."),
    k("23.4", "K", add=["P"],
      line="Mom, a few weeks into the bookkeeping, asks for the household accounts back. He hands them over, and checks them at midnight anyway.",
      changed="She has had the bookkeeping work since September (20.2)."),
    k("23.5", "K"), k("23.6", "K"),
    k("23.7", "K", add=["D"],
      line="The road dream: the same bend, and this time something walking behind him that stops when he stops. Then a growl.",
      changed="Added a growl."),
  ]),
  dict(label="Ch 23", old="Ch 24",
       changes="He sees Natsuki at her best from the stands, at the regionals he didn't reach, and how easy it is to be beside her.",
       scenes=[
    k("24.1", "K",
      line="These are the regionals he lost his place at, and he's banned besides, so he becomes her preparation: every evening after practice, the two of them and the empty dojo.",
      changed="The autumn tournament is regionals, which he failed to qualify for."),
    k("24.2", "K"), k("24.3", "K"), k("24.4", "Na"), k("24.5", "K"), k("24.6", "K"),
  ]),
  dict(label="Ch 24", old="Ch 25",
       meta="*When: October · Whose: Nanoha · Closeness: none · Cast: K, Na, A, Mio, Emi, Kazuo, Fairy · Uncanny: Town: a hiker lost on a trail he knew*",
       scenes=[
    k("25.1", "K"), k("25.2", "K"), k("25.3", "K"), k("25.3a", "K"),
    k("25.3b", "K", also=["25.3c"],
      line="The same hospital room, the part he wasn't there for: Dad to Kazuo, already sorry. \"He told me he was afraid he'd asked too much of you.\"",
      changed="Shorter: the apology moved to the day after the fight (19.1), and the two hospital beats are one scene (it was 25.3b and 25.3c)."),
    k("25.3d", "K"), k("25.4", "K"), k("25.5", "K"), k("25.6", "K"),
    k("28.5", "K",
      line="On the news the night before he leaves: a man who has walked the same trail for thirty years is found a day later, a mile off it, unable to say where he was.",
      changed="Moved here from November (it was 28.5), before Kyoto."),
  ]),
  dict(label="Ch 25", old="Ch 26", title="School Trip",
       meta="*When: late October, Kyoto and Nara · Whose: shared · Closeness: light · Cast: K, Na, Nt, T, A, Rika, Ryōsuke, Mom · Uncanny: Natsuki: she ties his sash like someone who has done it for years*",
       changes="Away from shifts and family he gets the whole trip, and Nanoha starts watching Natsuki's hands.",
       scenes=[
    k("26.1", "K"),
    k("26.1a", "K", call=""),
    k("26.1b", "K",
      line="The Nara day. Takatsuki bows to the deer by the guidebook and they bow back only to him. Kōhei, who is irrationally afraid of deer, gets mugged for his crackers.",
      changed="Added: he's irrationally afraid of them."),
    k("26.6", "A"),
    k("26.2", "K"),
  ]),
  dict(label="Ch 26", new_title="Lights Out",
       meta="*When: late October, Kyoto, then home · Whose: shared · Closeness: strong · Cast: K, Na, Nt, T, A, Fairy · Uncanny: Nanoha: she can sense what Natsuki is holding back; Kōhei: a dream of a wedding, the bride's face hidden*",
       changes="He gets an hour with each girl and a dream of a wedding, and goes home knowing he has to choose.",
       scenes=[
    k("26.3", "K"), k("26.4", "K"), k("26.5", "Na"), k("26.5a", "K"), k("26.7", "K"), k("26.7a", "Na"),
  ]),
  dict(label="Ch 27", old="Ch 27", scenes=[
    k("27.1", "K"), k("27.2", "K"), k("27.3", "K"),
    k("27.4", "K",
      line="She freezes again, finds him in the crowd, and goes off script, deadpan: she has lived next door to someone her whole life and never told him what that's meant, and she's going to, today. Then she walks off the stage by herself. The gym murmurs and turns to stare at him. Natsuki, in the crowd, is sad.",
      changed="Added: the murmuring and staring at him, and Natsuki is sad."),
    k("27.5", "K"), k("27.6", "Na"),
  ]),
  dict(label="Ch 28", old="Ch 28",
       meta="*When: November · Whose: Nanoha · Closeness: none · Cast: K, Na, Nt, A, Yuzu, Chie, Mio, Fairy · Uncanny: Nanoha: her light, upset and turned toward the hills; Kōhei: the dream of the eyes, nearer*",
       changes="They're a couple in front of everyone, Natsuki finds her feet as their friend while packing boxes nobody here knows about, and Nanoha's light turns toward the hills.",
       scenes=[
    k("28.1", "K"), k("28.2", "K", sub=("(29.0)", "(29.1)")),
    k("28.3", "K", add=["P"],
      line="Yuzu, kept on for weekends after the summer, tries one \"Senpai~\" too many, and he tells her, kindly, that he has a girlfriend.",
      changed="She was a summer hire, so she has stayed on for weekends [P]."),
    n("The posting", "From outside: flattened moving boxes come back out from behind her wardrobe, and on the phone Chie asks where to this time. Her father's next posting starts in April. She tells nobody here.",
      ["Natsuki", "D", "P"], "none", "New: the transfer news, right after she isn't chosen, shown from outside."),
    k("28.4", "Na"), k("28.6", "Na"), k("28.7", "K"),
  ]),
  dict(label="Ch 29", old="Ch 29",
       changes="He tells her parents properly, starts asking people for things, and asks his best friend to see his sister home.",
       scenes=[
    k("29.0", "K", flag="The bow, and Kazuo making him sweat, is a picture. I'd give it one CG."),
    k("29.4", "K"), k("29.5", "K"), k("29.6", "K"),
    k("36.5", "K",
      line="School wants no one walking alone, Akane has her spells, and he has shifts he can't drop. He asks Takatsuki to walk her home on those nights. Takatsuki accepts as if sworn in.",
      changed="Moved here from January (it was 36.5): the escort starts in November, before anyone has met anything."),
  ]),
  dict(label="Ch 30", old="Ch 30",
       meta="*When: late November – early December · Whose: neither · Closeness: light · Cast: K, Na, Nt, T, A, Fairy · Uncanny: Nanoha: something in Natsuki's photograph of him; Town: a woman missing, a wound nobody can explain; Kōhei: the dream of the eyes, closest*",
       changes="Someone is missing, Takatsuki is walking Akane home, and Nanoha starts to see that whatever is strange about Kōhei is strange about Natsuki too.",
       scenes=[
    k("30.1", "K"),
    k("30.2", "K", flag="A wound nobody can explain should be seen. I'd give it one CG."),
    k("36.6", "none",
      line="Their walks: he keeps to the traffic side and texts arrival times to her brother. She is having the best December of her life.",
      changed="Moved here from January (it was 36.6)."),
    k("30.3", "Na"), k("30.4", "Na"), k("30.5", "K"), k("30.6", "K"),
  ]),
  dict(label="Ch 31", new_title="The Loop",
       meta="*When: mid-December · Whose: neither · Closeness: none · Cast: K, Na, Nt, T, A, Mio, Fairy · Uncanny: The wolf, met awake for the first time, and it only follows and stares; Nanoha: she follows her light to a road that isn't there*",
       changes="Something is on the hill road, nobody is hurt and nobody can explain it, and Nanoha can do the one thing nobody else can.",
       scenes=[
    k("37.1", "T",
      line="Takatsuki's side: the walk home up the hill road, the same mirror coming around a third time, then trees.",
      changed="The whole loop is now a mid-December scare, before the bloom (it was Ch37, in late January)."),
    k("37.2", "T", changed=MOVED_LOOP.format("37.2")),
    k("37.3", "T",
      line="It doesn't do what the story says. It follows, stops, stares, starts toward them and stops again. It never comes. His shinai stays up the whole time, and he never has to use it.",
      changed="It never attacks and nobody is hurt: December is a scare (it was 37.3).",
      flag="The wolf itself, and it isn't marked as manga. I'd carry the manga through from 31.1."),
    k("37.4", "K",
      line="At home Nanoha stops mid-sentence: her light has gone frantic, and this time she feels it herself. She tells Kōhei they have to go to them this minute.",
      changed="Nanoha feels it too. It's her light, since the fairy can't speak until the bloom (it was 37.4)."),
    k("37.5", "K",
      line="Kazuo isn't home. She takes his keys, and Kōhei drives, objecting to all of it for the first half of the ride. Mio sees everything and names her price.",
      changed="He objects, but not the whole ride (it was 37.5)."),
    k("37.6", "K", add=["D"],
      line="Where the road goes wrong she gets off and follows her light into the trees as if there were a path, and there is. Natsuki is across town and knows nothing until tomorrow.",
      changed="Natsuki isn't there. Nanoha follows her light in (it was 37.6)."),
    k("37.7", "K", changed=MOVED_LOOP.format("37.7")),
    k("37.8", "K", changed="Moved with the loop (it was 37.8). The motorcycle's payoff is now the last end-credit still (E.0)."),
    n("The next day", "Natsuki is told all of it; nothing is kept from her. Then Kōhei tells the five what he has been dreaming since June: the eyes, and the road that won't end. The dreams of her he keeps to himself.",
      ["dread", "D"], "K", "New: Natsuki is told everything, and he tells them his dread dreams."),
  ]),
  dict(label="Ch 32", old="Ch 31",
       meta="*When: late December · Whose: Nanoha · Closeness: none · Cast: K, Na, Nt, T, A, Chie, Mio, Mom · Uncanny: Kōhei: a bride in a white hood, while he's awake*",
       changes="Their first Christmas is everything she wanted, two weeks after a scare, until the past reaches into the middle of their first kiss.",
       scenes=[
    k("31.1", "K"), k("31.2", "K"),
    k("31.3", "K",
      line="Snow starts, or petals; he can't tell. They lean in for their first kiss, and in that breath there is a bride beside him in a white hood, her face hidden. He flinches, and it doesn't happen. She doesn't know why.",
      changed="Now an almost-kiss, broken by the bride in the hood."),
    k("31.4", "none"),
    k("31.5", "Na",
      line="Past midnight Nanoha asks what happened. \"Snow,\" he says. He told her about the eyes last week; this he keeps. She knows his faces, and this one is new.",
      changed="She asks why he flinched. It's the one kind of dream he still keeps back."),
  ]),
  dict(label="Ch 33", old="Ch 32", scenes=[
    k("32.1", "K"), k("32.2", "K"), k("32.3", "K"),
    k("32.6", "Na",
      line="Nanoha comes home from the shrine and her friend is on the windowsill, whole and talking, as if ten years were an afternoon. It is the first time we see her face. She never left. Nanoha just stopped being able to see her.",
      changed="Her face is shown here for the first time."),
    k("32.6a", "none"),
  ]),
 ]),
 dict(title="Part 5 — Winter (January–March)",
      intro="It opens with the old life, whole, dreamed by both of them the night of the bloom, and the dream explains what was on the hill road in December. The past is settled first: Kōhei and Natsuki grieve that life and say goodbye to it; he goes to Nanoha in real doubt, the fairy tells them what she can, and he comes back to Nanoha by choice, with their first real kiss. Then the missing woman is found dead, Takatsuki and Akane are told the rest, and the girls have it out. For about eight weeks the five know what is out there while the adults search real roads: two more deaths, the caretaker family's old job, what Nanoha can do and what it may cost her. The plan is gone in seconds. They live because nobody fights alone, and every one of them pays.",
      chapters=[
  dict(label="Interlude", fixed=True, old="Interlude",
       changes="The reader gets the whole old life and exactly how it ended, and December is explained; everything after is dread, not mystery.",
       scenes=[
    k("R.1", "none", call="",
      line="Brush and ink for the whole chapter, with full color for the wedding and the death. Two people who have known each other since they were small. He comes back from a lost war with no lord and no name to offer.",
      changed="Full color for the wedding and the death."),
    k("R.2", "none",
      line="Through his eyes, in color: the bride in the white hood, now with her face. A marriage arranged for an heir, between two people who are interested in each other and not yet in love.",
      changed="Through his eyes, because we want to see the bride. Interested, not yet in love."),
    k("R.3", "none",
      line="About a year of it, and no children. This is where they fall in love: her teasing, his late returns, the cut on his wrist, her counting his habits from the veranda.",
      changed="They fall in love here, after the wedding."),
    k("R.4", "none",
      line="A winter morning. People have been lost on paths they knew, so he goes armed; she laughs at him for it, and he ties the cord anyway. The same landmark comes round again.",
      changed="Added why he goes armed: people lost on paths they knew."),
    k("R.5", "none"),
    k("R.6", "none",
      line="The only move left: he gives it his throat to get inside its reach, and strikes it in the head. For a breath it is only a wolf, odd, very large and old. Then it is gone like something long dead, and the mist with it.",
      changed="The strike is to the head; for a breath it is only a wolf, then gone. The same thing happens in Ch43."),
    k("R.7", "none",
      line="Her kneeling in the snow with him. He is dying, so she does most of the talking: she'll wait for him, and he is to find her. \"I'll wait. Don't be late.\" His last words are the promise. The tree blooms over them, and the dream ends there, for both of them.",
      changed="\"Live\" is gone. She says she'll wait; his last words are the promise; nothing is held back; and the dream ends at the bloom, so her life afterward stays out of the story (R.8 is cut).",
      call="Two of mine to confirm. Her line: \"I'll wait. Don't be late.\" And the vow's form: the old saying that husband and wife are bound for two lives, so the promise is spent in this one and nothing hangs over Nanoha. Yes to each?"),
  ]),
  dict(label="Ch 34", old="Ch 33",
       changes="They wake knowing all of it, including what was on the road in December, mourn that life together and let it be over, at her insistence.",
       scenes=[
    k("33.0", "K"),
    k("33.3", "K",
      line="At the boulder they lay out what each of them has. He has all of it now. She has known who she was since summer, and doesn't say so; he doesn't ask. They both know what was on the hill road in December, and that maybe it was never really killed.",
      changed="Added: the dream explains December, and maybe they never killed it."),
    k("33.4", "K", add=["P"],
      line="She cries for a man who died on this spot. He lets himself be the one who's still here. \"You're late,\" she says, for the last time: he found her, and the promise is kept.",
      changed="Added: \"You're late,\" for the last time, which closes the promise [P].",
      call="\"You're late\" gets its last use here, and that closes the promise. Mine, not yours. Yes?"),
    k("33.5", "K"), k("33.6", "K"),
  ]),
  dict(label="Ch 35", old="Ch 34",
       meta="*When: early January · Whose: Nanoha · Closeness: none · Cast: K, Na, A, Fairy · Uncanny: Nanoha: her friend, whole and talking, and what she knows*",
       changes="He tells Nanoha everything, admits he doesn't know what it means, and then chooses her again knowing what he gives up. It is their first real kiss.",
       scenes=[
    k("34.1", "K"), k("34.1a", "Na"),
    k("34.2", "K",
      line="All of it: a wife, a death, the tree, and what December was. She listens with her hands flat on the table.",
      changed="Added: what December was."),
    k("36.2", "K",
      line="Nanoha's friend tells the two of them what she can: its road is its strength, and on a road that never ends it never tires. Something like it was here long ago. The tree can shelter but not hunt, and she doesn't know how to kill it.",
      changed="Moved here from after the body (it was 36.2): she tells Kōhei and Nanoha first, before he chooses.",
      call="The notes have her telling them before he chooses; the handover had it after the body. I followed the notes, and she says it again to all five in 36.2. Right place?"),
    k("34.3", "K"), k("34.4", "K"),
    k("34.5", "K",
      line="He works a shift, walks home, and knows: that life was whole and it's finished, and this one he gets to choose. He chooses her, and this time nothing stops the kiss.",
      changed="Added: their first real kiss."),
    k("34.6", "K"),
  ]),
  dict(label="Ch 36", old="Ch 36",
       meta="*When: mid-January · Whose: neither · Closeness: none · Cast: K, Na, Nt, T, A, Mom, Fairy · Uncanny: Town: the missing woman is found dead*",
       changes="The danger becomes real and local, all five now know all of it, and Mom walks to the station to bring her daughter home.",
       scenes=[
    k("36.1", "K"),
    k("36.3", "K", add=["D"],
      line="Takatsuki and Akane, who met it in December, get the rest: the old life, and Nanoha's friend, whom all five can see now and who tells it again herself. Takatsuki asks, politely, for evidence anyway.",
      changed="They have already met the wolf, and all five can see the fairy from January."),
    k("36.4", "K",
      line="School ends club early and sends everyone home in groups.",
      changed="The station moved to the next scene."),
    k("39.4", "K", title="Mom at the station",
      line="At dusk the station fills with parents, and one of them is Mom, who walked there by herself to bring Akane home.",
      changed="Mom's walk moves here from February (it was 39.4): she comes to the station for Akane.",
      flag="A crowd, and the picture of her in it is the point. I'd give it one CG."),
  ]),
  dict(label="Ch 37", old="Ch 35", scenes=[
    k("35.1", "Na"), k("35.2", "Na"), k("35.3", "Nt"),
    k("35.4", "Na",
      line="She could have told him in October. She didn't want him to start dating her for the old life's sake and only then work out it should have been Nanoha. Nanoha, who won, understands exactly.",
      changed="Her reason, as you put it. This chapter now comes after the body is found."),
    k("35.5", "Na"),
  ]),
  dict(label="Ch 38", old="Ch 38", scenes=[
    k("38.1", "K",
      line="What he observed in December, in order: it followed, it stared, it started and stopped. All accurate, and all about a wolf that never came at him. The legend got the following right and the rest wrong.",
      changed="\"Only playing\" is gone: his notes are about a wolf that never came at him, and they're from December."),
    k("38.2", "K"), k("38.3", "K"), k("38.5", "K"),
    k("38.6", "K", add=["D"],
      line="With the real sword on the floor between them, the two of them work out what the old fight looked like, him from inside it and her from where she knelt. Neither is the expert. She can't look at the blade for long.",
      changed="They work it out together; neither is the expert."),
  ]),
  dict(label="Ch 39", old="Ch 39",
       meta="*When: February · Whose: shared · Closeness: light · Cast: K, Na, Nt, T, A, Fairy · Uncanny: Nanoha: holding its road to one stretch, and what that takes out of her*",
       scenes=[
    k("39.1", "K"), k("39.2", "K"),
    k("39.3", "T",
      line="From Takatsuki's side. Akane gives him \"obligation chocolate, obviously.\" He takes obligations very seriously, and he is more nervous about this than about the wolf: he goes to Kōhei to ask permission, formally, before he says a word to her. Kōhei says yes before he can ask. She isn't told.",
      changed="From Takatsuki's side. He's more nervous about this than the wolf, and Kōhei says yes before he can ask."),
    k("39.5", "K"), k("39.6", "Na"),
  ]),
  dict(label="Ch 40", old="Ch 40", scenes=[
    k("40.1", "K"), k("40.2", "K"), k("40.3", "K"), k("40.4", "K"),
  ]),
  dict(label="Ch 41", old="Ch 41",
       changes="Nanoha tells Natsuki what her part may cost, asks her to look after him, and tells her to stay. Then he tells Nanoha he loves her.",
       scenes=[
    k("41.1", "Nt",
      line="Nanoha tells her: she can make sure they all come out, and it may not leave her alive. If so, she wants Natsuki to look after him. With that promised, she says, she can face tomorrow.",
      changed="Added: with Natsuki's promise she can face it."),
    k("41.2", "Nt", add=["P"],
      line="Natsuki says what it is to be asked to be the fallback, by someone who doesn't know she is meant to be gone by April. So she says that too. Nanoha tells her to stay; nobody has ever asked her to. Then she promises.",
      changed="Added: the transfer comes out, and Nanoha tells her to stay."),
    k("41.3", "K"), k("41.4", "K"), k("41.5", "K"), k("41.6", "K"),
  ]),
  dict(label="Ch 42", old="Ch 42", scenes=[
    k("42.0", "none"),
    k("42.1", "K"),
    k("42.4", "A", call="", changed="Moved up to right after they walk in, so the fight runs unbroken."),
    k("42.3", "K"), k("42.5", "K"), k("42.6", "Na"),
  ]),
  dict(label="Ch 43", old="Ch 43", title="Inches", scenes=[
    k("43.1", "K"), k("43.3", "Nt"), k("43.4", "Nt"),
    k("43.5", "K",
      line="It is fixed on him now, as in the trade. Takatsuki, crawling, grabs hold of it, the opposite of form, and Kōhei brings the sword down on its head, one-armed. For a breath it is only a wolf, odd, very large and old. Then it is gone like something long dead, and the mist with it.",
      changed="The strike is to the head, and for a breath it is only a wolf before it's gone, as in the old life."),
    k("43.7", "Na"),
    k("43.8", "A",
      line="They come out where the road lets out, and Akane is the only one standing. She hides the sword, gets under Nanoha's arm, \"We're just stopping for a rest,\" and makes the call with the story ready: a huge stray dog went for them on an early club run, and ran off.",
      changed="The story they tell is a stray dog on an early club run, and Akane hides the sword first [P]. From her side, as the end of her wait.",
      call="The story the five tell, and Akane hiding the sword before she calls, are mine. Yes?",
      flag="The last picture of the fight, and nothing shows it. I'd give it one CG."),
  ]),
 ]),
 dict(title="Part 6 — Aftermath (March–April)",
      intro="Spring. Everyone is alive and nobody is unchanged: a shoulder in a sling, a leg that won't fully heal, a scar, a girl who can no longer see what she used to, a town that will never know. The loose ends are small and human. He asks again. Natsuki, asked to stay by the last person she expected, asks for something for herself for the first time, and ends up in a photograph. The tree blooms on time.",
      chapters=[
  dict(label="Ch 44", old="Ch 44", scenes=[
    k("44.1", "K",
      line="One hospital room with too many visitors, and a stray-dog story the police can't disprove. His shoulder: no kendo until summer. Takatsuki's leg, which will never fully heal. Natsuki's face, stitched. His mother signs the forms.",
      changed="Added: the story they tell holds."),
    k("44.2", "K"),
    k("44.3", "none", flag="His new pace, and her timing it, is something to see. I'd give it one CG."),
    k("44.4", "K", flag="A ceremony, with one of them on crutches and one in a sling. I'd give it one CG."),
    k("44.5", "Nt",
      line="Her father's posting is weeks away. Nanoha lived, so the promise is void, and she asks anyway: for the first time she asks her parents to let her stay, and they do. The scar is proof she was there, and she doesn't hide it.",
      changed="She asks for herself: Nanoha lived, so the promise isn't what keeps her here."),
    k("44.6", "K", call="Still open, by your choice: what he writes. My proposal stands (university, to teach, with kendo) and so does the fallback (we don't see it)."),
    n("In the frame", "Under the tree, in ordinary bloom, with everyone there. Natsuki has never been in one of her own photographs. She gives Nanoha the print from Kyoto, the one of him she never showed anyone, and Nanoha takes the camera and puts her in the frame.",
      ["Natsuki", "CG", "D", "P"], "Nt", "New: her last image. She gives Nanoha the Kyoto photo, and Nanoha puts her in a picture."),
    k("44.7", "K"),
  ]),
  dict(label="Epilogue", fixed=True, old="Epilogue", scenes=[
    k("E.0", "none", call="", add=["comic"],
      line="A song over stills of their later lives. The last still is a wedding day, years on: Mio finally tells Kazuo who took the motorcycle, and the day it is is the only reason Kōhei lives.",
      changed="Added the last still: Kazuo finds out about the motorcycle at their wedding."),
    k("E.1", "Nt"),
  ]),
 ]),
]

CUT = {  # Nov 26 IDs that are gone, with where their content went
    "13.1": "folded into 12.1 (the summer hire)",
    "25.3c": "folded into 24.5 (what he said)",
    "R.8": "cut: her life after his death stays out of the story",
    "43.6": "cut: \"Live\" is dropped; the promise is whole in R.7",
}

HEAD_TEXT = '''# Ōzakura scene list, Pass 1 (second revision)

**Lede:** The whole story at one line per scene, revised from your second review (Nov 27) and renumbered once. Every scene now says how it is shown and whose head we are in. Scenes that changed carry a "changed" mark. Nothing here is approved yet.

**Status (Nov 27):** Pass 1, revised twice: from the author's review of every scene (Nov 25–26) and from his second round (Nov 27). The record of both is `production/scene-list/review-notes-nov25.md`. He reviews this revision next, point of view included. **No production past Ch4 starts until the author approves this.** Pass 2 then writes each Part in full (when, where, who, what happens, what changes, threads, on screen as) and runs it past outline readers before it goes to him.

## How to read this
- **Renumbered once, on Nov 27.** Ch1–4 kept their numbers; from Ch5 on the chapters and scenes are numbered cleanly, and the old-to-new table for every ID is `production/scene-list/id-map-nov27.md`, so notes from both earlier rounds still resolve. **From here IDs never renumber again:** a scene added later gets a letter (12.3a), a cut scene leaves a gap. `P.0` is Chapter 0 and `P.1` the opening credits, `V1` and `V3` are short past-life glimpses, `R.1`–`R.7` are the recall interlude, `E.0` is the end credits and `E.1` the epilogue.
- **The italic line under each chapter:** when it happens; whose chapter it is (Nanoha's, Natsuki's, shared or neither); how much present-day closeness Natsuki and Kōhei get (none, light, strong); who is in it (K Kōhei, Na Nanoha, Nt Natsuki, T Takatsuki, A Akane, then side cast); and any uncanny or dread beat with its owner.
- **Tags at the end of a scene,** in this order: whose head we are in (`head:K` Kōhei, `head:Na` Nanoha, `head:Nt` Natsuki, `head:T` Takatsuki, `head:A` Akane, `head:Kz` Kazuo, `head:none` nobody's: the camera is outside); whom the scene favors in the triangle (Nanoha or Natsuki; none means neither); how it's shown if not plain sprites (CG, CG×2, insert = manga, gag = gag manga in a different art style, still = living still, anim = a short animation attempt, imagined = an imagined scene, ink = the old life's brush-and-ink manga, song = a music sequence); threads (comic, dread, A+T = Akane and Takatsuki, family, kendo, uncanny); the source; Rev on anything changed or added in this revision; and flag (below).
- **Point of view, by the rules agreed Nov 27:** (1) the default is Kōhei, first person, present tense; (2) Nanoha and Natsuki get third-person interludes when he isn't there or the point is what she thinks; (3) from the kiss night (Ch18) until the girls' talk (Ch37) Natsuki is shown from outside only, what she does and not what she thinks, so that talk isn't a cheat, and those scenes are marked nobody's head; (4) the rare others are Takatsuki (Chapter 0's road in Ch31; the permission scene, 39.3), Akane (the week he is in Kyoto, 25.4; the wait at the tree, 42.3, and its end, 43.6) and Kazuo (the night of the fight, 17.8); (5) imagined scenes are always Nanoha's; (6) the old life is manga and has no single point of view (the camera is on the bride at the wedding, his view; on him training, hers; outside both for the fight and the promise); (7) manga is free to move between people, so a manga scene is marked with a head only where the words over it are one person's.
- **flag** marks a scene whose point is something physically happening (a fight, a crowd, physical comedy, a group all doing something) but which has neither a CG nor manga. The "Flag" line under it says what I'd give it. Built scenes in Ch1–3 weren't audited; they get it when you re-review those chapters in the game.
- **Sources:** Built (in the built Ch1–3), D (decided by the author or in canon as Decided), SB and a number (canon's scene bank), Map (the chapter map's proposal), **P (invented by this thread)**. D and P together means he decided the beat and the staging is this thread's.
- **"Changed"** under a scene says in a few words what changed in this revision.
- **"Your call"** under a scene is a question only the author can answer. Open items in canon are proposed here, never settled.
- **What manga is used for** (from the review): fights and matches; the old life; a few long wordless or near-wordless sequences (the kiss night, Nanoha's kitchen table, her answer at the festival); childhood memories; and silent physical comedy sprites can't do (the umbrella).
- **The fairy** is in the story at three levels: drawn and talking, but with her face held back, in Nanoha's childhood memories; a light that lives in Nanoha's room and window scenes from Ch8 until the bloom; whole and talking after it, and visible to all five from January.
- The review page and the tables at the end are generated from this file by `production/scene-list/build_page.py`. Keep the line shapes.
'''

TAIL_TEXT = '''## Whole-story questions
- **Q10.** In December, should Takatsuki report a big stray dog to the police box after the night on the hill road? It would seed the story the five tell in March (43.6). *(What I'd do: yes, as one line in 31.8.)*
- **Q11.** Point of view: you said Natsuki is outside-only "from summer." Canon's line is from the days after the wound care, so I closed her head at the kiss night (Ch18) and left it open before that (the umbrella, the pact, Chie's verdict, the stone at Obon). Right place? *(What I'd do: keep it at the kiss night. Before it she knows nothing, so nothing is hidden.)*
- **Q12.** Two chapter titles are mine: Ch26 "Lights Out" (the second Kyoto chapter) and Ch43 "Inches" (it was "Live"). Keep them or rename? *(What I'd do: keep both for now; titles are cheap to change.)*
- **Q13.** Twenty scenes are flagged because something physical happens and there is no CG or manga (the Flagged filter shows them, each with what I'd give it). Go one by one, or take all my suggestions? *(What I'd do: take them all; it adds fourteen CGs and puts six more scenes into manga.)*

## What changed in this revision
- **Renumbered once:** Ch1–4 keep their numbers. Ch8 (The New Hire) folds, so old Ch9–25 are now Ch8–24. Kyoto splits into Ch25 and Ch26. The loop is the new Ch31, in mid-December, so Christmas is Ch32 and the bloom Ch33. In Part 5: What We Were is Ch34, Doubt Ch35, Found Ch36, Since Summer Ch37. Ch38–44 keep their numbers. The count stays 44. Every old ID is in `production/scene-list/id-map-nov27.md`.
- **Point of view:** every scene is marked with how it is shown and whose head we are in; the tables at the end count them.
- **New:** Kazuo's help in September (20.2); the transfer news (28.4); the day after the loop (31.9); Natsuki in the frame (44.7).
- **Moved:** Monday practice, from the end of Ch4 to the start of Ch5 (5.1); the first dream of the eyes, to the storm night (8.7); Yuzu's arrival and Takatsuki's "no help," to summer (12.1, 12.2); the hiker, to October (24.10); Akane's week at home, to the middle of the trip (25.4); asking Takatsuki to walk her home, to November (29.5), and the walks to December (30.3); the whole loop, from late January to mid-December (Ch31); what the fairy knows, to before he chooses (35.4); Mom's walk, to the station in January (36.4); the girls' talk, to after the body (Ch37); Akane's wait at the tree, to right after they walk in (42.3).
- **Cut:** "Live" and the scene that carried it (43.6); her life after his death (R.8); the "Full time" scene and one hospital beat, folded into their neighbors (13.1, 25.3c).
- **Rewritten from your decisions:** Chapter 0 (a December evening on the hill road); the promise (R.7) and what the wolf is for a breath when it dies (R.6, 43.4); the almost-kiss at Christmas (32.3) and the real one when he chooses again (35.7); the tournament he wants (5.5, 11.5, 12.2, 16.7, 17.1, 23.1); telling Kazuo alone, and the apology (19.1); the roof, where the slap isn't named (19.3); Kazuo's shorter talk (24.5); the loop as a scare (Ch31); Natsuki's ending (41.2, 44.5, 44.7); the two of them working out the old fight together (38.5); the permission scene from Takatsuki's side (39.3); the wedding-day gag as the last credit still (E.0).
- **Your page notes, applied:** 4.2, 4.4, 5.6, 13.5, 17.4, 17.6, 18.2, 21.2, 22.7, 25.3, 27.4, R.1, R.2, 37.4, 31.4, 31.5, 38.1, 41.1.
- **Mine, waiting on a yes from you** (each has a "Your call"): where the tournament beats land (5.5); Kazuo finding Mom the bookkeeping (20.2); her line and the vow's form (R.7); "You're late," for the last time (34.3); where the fairy's telling goes (35.4); the stray-dog story and the hidden sword (43.6).
- **Still open by your choice:** what he writes on the form (44.6); the preparing sequence (42.1); how long the recall runs and exactly what is in it.

## Changes from the chapter map (for other threads)
The chapter map stays the chapter-level summary until the author approves this list, **and it still uses the old chapter numbers** (its header has the table). Where this list differs, on purpose:
- **Numbers:** see "Renumbered once," above, and `production/scene-list/id-map-nov27.md`.
- **Chapter 0 and the opening credits** come before Ch1; the recall is **an unnumbered interlude chapter** between Ch33 and Ch34. Chapter 0 is a December evening and flashes forward to Ch31.
- **Akane** is a first-year at their school and one of the five: the kendo club's manager from Ch5 (approved), with a crush on Takatsuki that predates the story. She stays out of the wolf fight and is the one standing at the end. **Akane and Takatsuki** end with no confession; he asks Kōhei's permission in Ch39 and she isn't told.
- **The two boys** are shown as friends in Part 1 (5.8, 7.4). The New Hire chapter is gone: Yuzu is a summer hire (Ch12).
- **The fairy** never left: Nanoha stopped being able to see her at seven. Her face is held back in the childhood manga. A light lives in Nanoha's room from Ch8; she is whole and talking from the night of the bloom (33.4), has a reunion scene in Ch35, and all five can see her from January.
- **Ch3 (built) changes:** no unspoken Saturday; a split-second CG of the tree in snow; the light moves to Ch4; Genji tells the tree's legend at tea; two new CGs. **Ch4:** 4.2 is played straight with a CG; the memory manga ends on a full-page hug; Monday practice opens Ch5.
- **The tournament:** from Golden Week Kōhei wants the late-summer tournament, the qualifier for regionals. He loses it in Ch17; the autumn tournament (Ch23) is regionals. Three competitions in all, against canon's "one or two at most" (the author was told and left it).
- **The sword** is his from Ch16. There is no armor for him and no storehouse scene in winter.
- **The night of the fight:** he misses once and punches a brick wall; Takatsuki arrives as it ends and sends him away; a Kazuo interlude closes Ch17; Ch18 is wordless until the gate. The next day he tells Kazuo alone, and Kazuo apologizes then.
- **Kazuo's help** starts in September (the yard, the bookkeeping work [P]). His talk about Dad's regret and being worthy is in Ch24, before the choice, and is shorter. Ch29 is him telling her parents, and asking Takatsuki to walk Akane home.
- **The first kiss** is an almost-kiss at Christmas (Ch32) and a real one when he chooses Nanoha again (Ch35).
- **Natsuki** learns in November that her father's next posting starts in April, and tells only Chie; the night before the fight Nanoha tells her to stay; in Ch44 she asks her parents and stays, and Nanoha puts her in a photograph. The epilogue is at the old grave, not the tree.
- **The wolf's first appearance is mid-December (Ch31),** as a scare: it follows and stares, nobody is hurt, and the adults hear it was one of Akane's spells. Natsuki isn't there and is told the next day; Kōhei then tells the five his dread dreams. The escort starts in November. The hiker is in October.
- **The bloom:** nothing happens at the shrine but the tree. The recall is a dream that night and shows the death in full. It ends on the promise and the bloom: "Live" is dropped, and her life after his death stays out of the story.
- **January:** grief; he tells Nanoha; the fairy tells them what she can; he chooses; then the body is found, Takatsuki and Akane are told the rest, and the girls talk (Ch37, after Ch36).
- **The wolf** attacks; it isn't a careful hunter. In Ch42 it takes Takatsuki out in the first seconds. Nanoha goes in and weakens it at her own cost. When it dies, in both lives, the strike is to the head, and for a breath it is only a wolf before it is gone. Costs: Takatsuki's leg, Natsuki's face, Kōhei's shoulder, Nanoha's gift.
- **The adults know nothing,** before or after. The story the five tell is a stray dog [P].
- **Dreams** now fall in Ch1, 6, 8, 10, 15, 19, 22, 26, 28 and 30; he tells the five the dread ones after Ch31.
- **One uncanny owner per chapter** holds through Part 3 and may bend after it (the author, Nov 25).
- **Takatsuki is captain from Ch11** (approved); Kirishima graduates in Ch44.

## Tables
Generated from the chapters above by `production/scene-list/build_page.py --tables`. Don't edit by hand.

<!-- tables:start -->
<!-- tables:end -->
'''


# ---------------------------------------------------------------- build
def tag_string(spec, base_tags, rev, flag):
    tags = [t for t in base_tags if t not in ("Rev", "flag") and not t.startswith("head:")]
    tags = [t for t in tags if t not in spec.get("drop", [])]
    for t in spec.get("add", []):
        if t not in tags:
            tags.append(t)
    def src(t):  # sources read Built or SB or Map, then D, then P
        return {"D": 2, "P": 3}.get(t, 1)
    ordered = sorted(tags, key=lambda t: (cls(t), src(t) if cls(t) == 3 else 0))  # stable: keeps the old order inside each class
    out = ["head:" + spec["head"]] + ordered
    if rev:
        out.append("Rev")
    if flag:
        out.append("flag")
    return " · ".join(out)


out = [HEAD_TEXT]
idmap = {}        # old id -> new id
new_ids = []
chap_rows = []
for part in PARTS:
    out.append("## " + part["title"])
    out.append(part["intro"])
    out.append("")
    for ch in part["chapters"]:
        label = ch["label"]
        oc = OLDCH.get(ch.get("old"))
        title = ch.get("new_title") or ch.get("title") or oc["title"]
        meta = ch.get("meta") or OLDMETA[ch["old"]]
        changes = ch.get("changes") or oc["changes"]
        out.append(f"### {label} — {title}")
        out.append(meta)
        out.append(f"**Changes:** {changes}")
        num = label.split()[1] if label.startswith("Ch ") else None
        i = 0
        for sc in ch["scenes"]:
            if sc["kind"] == "keep":
                o = OLD[sc["old"]]
                stitle = sc.get("title", o["title"])
                line = sc.get("line", o["line"])
                if sc.get("sub"):  # a cross-reference to another scene's ID, updated; not a change to the scene
                    assert sc["sub"][0] in line, sc["sub"]
                    line = line.replace(*sc["sub"])
                base = o["tags"]
                call = o["call"] if sc.get("call") is None else sc["call"]
            else:
                stitle, line, base, call = sc["title"], sc["line"], sc["tags"], sc.get("call", "")
            if sc.get("id"):
                sid = sc["id"]
            elif ch.get("fixed"):
                sid = sc["old"]
            else:
                i += 1
                sid = f"{num}.{i}"
            changed = sc.get("changed", "")
            flag = sc.get("flag", "")
            assert sid not in new_ids, sid
            new_ids.append(sid)
            if sc["kind"] == "keep":
                assert sc["old"] not in idmap, sc["old"]
                idmap[sc["old"]] = sid
            for a in sc.get("also", []):
                idmap[a] = sid
            out.append(f"- **{sid} {stitle}.** {line} *({tag_string(sc, base, bool(changed), bool(flag))})*")
            if changed:
                out.append(f"  - *Changed:* {changed}")
            if flag:
                out.append(f"  - *Flag:* {flag}")
            if call:
                out.append(f"  - *Your call:* {call}")
        out.append("")
out.append(TAIL_TEXT)
DST.write_text("\n".join(out), encoding="utf-8")

missing = [i for i in OLD if i not in idmap and i not in CUT]
assert not missing, missing

# ---------------------------------------------------------------- the ID map
CHAPTER_ROWS = [
    ("Ch 0 The Walk Home", "Ch 0", "now a December evening; flashes forward to Ch 31"),
    ("Ch 1–Ch 4", "same", "4.5 moved to open Ch 5"),
    ("Ch 5–Ch 7", "same", "scenes in Ch 5 shift by one"),
    ("Ch 8 The New Hire", "folded", "8.1 and 8.2a open Ch 12; 8.5 closes Ch 8"),
    ("Ch 9 Umbrella", "Ch 8", ""), ("Ch 10 Fever", "Ch 9", ""), ("Ch 11 Two Bentō", "Ch 10", ""),
    ("Ch 12 That Wasn't Kendo", "Ch 11", ""), ("Ch 13 Summer Break", "Ch 12", "gains Yuzu's arrival"),
    ("Ch 14 Summer Festival", "Ch 13", ""), ("Ch 15 Team Nanoha", "Ch 14", ""), ("Ch 16 Watermelon", "Ch 15", ""),
    ("Ch 17 Proof I Was There", "Ch 16", ""), ("Ch 18 Karaoke", "Ch 17", ""), ("Ch 19 Wound Care", "Ch 18", ""),
    ("Ch 20 Second Semester", "Ch 19", ""), ("Ch 21 The Kitchen Table", "Ch 20", ""), ("Ch 22 Nikujaga", "Ch 21", ""),
    ("Ch 23 Form", "Ch 22", ""), ("Ch 24 Autumn Tournament", "Ch 23", ""), ("Ch 25 The Window Latch", "Ch 24", "gains the hiker"),
    ("Ch 26 School Trip", "Ch 25 and Ch 26", "split: School Trip, then Lights Out"),
    ("Ch 27 Cultural Festival", "Ch 27", ""), ("Ch 28 Dating", "Ch 28", "loses the hiker; gains the posting"),
    ("Ch 29 Asking", "Ch 29", "gains the favor"), ("Ch 30 Posters at the Station", "Ch 30", "gains the escort"),
    ("(new)", "Ch 31 The Loop", "old Ch 37, in mid-December, without Natsuki"),
    ("Ch 31 Christmas", "Ch 32", ""), ("Ch 32 The Bloom", "Ch 33", "Part 4 ends here"),
    ("Interlude The Old Life", "Interlude", "R.8 cut"),
    ("Ch 33 What We Were", "Ch 34", ""), ("Ch 34 Doubt", "Ch 35", "gains what the fairy knows"),
    ("Ch 35 Since Summer", "Ch 37", "now after the body"), ("Ch 36 Found", "Ch 36", "loses the favor and the escort; gains Mom at the station"),
    ("Ch 37 The Loop", "Ch 31", "moved to December"),
    ("Ch 38–Ch 42", "same", "39.4 moved to 36.4; scenes in Ch 42 reordered"),
    ("Ch 43 Live", "Ch 43 Inches", "43.6 cut"), ("Ch 44 Spring, Epilogue", "same", "44.7 is new, so Again is 44.8"),
]
ROUND1 = [  # IDs on the first page (Nov 25) that the Nov 26 revision moved or cut
    ("8.2", "cut Nov 26 (the inventory); replaced by 8.2a", "8.2a"),
    ("8.3", "moved Nov 26 to 13.1a", "13.1a"), ("8.4", "moved Nov 26 to 13.1b", "13.1b"),
    ("V2", "cut Nov 26", None), ("V4", "cut Nov 26; shown in the recall", None),
    ("21.6", "cut Nov 26 (the yes moved to the gate, 19.7)", "19.7"),
    ("29.1", "moved Nov 26 to 25.3a", "25.3a"), ("29.2", "moved Nov 26 to 25.3b", "25.3b"), ("29.3", "moved Nov 26 to 25.3c", "25.3c"),
    ("32.4", "cut Nov 26 (the fugue at the shrine)", None), ("32.5", "cut Nov 26 (\"You two, again\")", None),
    ("33.1", "moved Nov 26 to R.2", "R.2"), ("33.2", "moved Nov 26 to R.3", "R.3"),
    ("38.4", "cut Nov 26 (the storehouse in winter)", None), ("40.5", "cut Nov 26 (the trust exchange; one line kept in 40.2)", "40.2"),
    ("42.2", "moved Nov 26 to R.4", "R.4"), ("43.2", "moved Nov 26 to R.6", "R.6"),
]


def sort_key(i):
    import re
    m = re.match(r"^(\d+)\.(\d+)([a-z]?)$", i)
    if m:
        return (1, int(m.group(1)), int(m.group(2)), m.group(3))
    order = ["P.0", "P.1", "V1", "V3", "R.1", "R.2", "R.3", "R.4", "R.5", "R.6", "R.7", "R.8", "E.0", "E.1"]
    return (0 if i.startswith("P") else 2, order.index(i), 0, "")


def resolve(i):
    if i in idmap:
        return idmap[i]
    return None


m = ["# Scene list: old-to-new IDs (the Nov 27 renumber)", "",
     "Written by `production/scene-list/archive/revise_nov27.py` when the scene list was renumbered once, on Nov 27 (approved by the author). "
     "\"Old\" is the Nov 26 revision, the one the second review page (`e32a7dfd-96e1-4220-98a2-dca69044c1ea`) was built from. "
     "Use this to read his notes from either earlier page against today's `story/scene-list.md`. After this, scene IDs never renumber: later additions get letters.", "",
     "## Chapters", "", "| Old (Nov 26) | New | Note |", "|---|---|---|"]
for a, b, c in CHAPTER_ROWS:
    m.append(f"| {a} | {b} | {c} |")
m += ["", "Page-note IDs for chapters follow the same table (`ch13` on the old pages is `ch12` now). Old `ch8` has no successor; old `ch26` is `ch25` and `ch26`; old `ch37` is `ch31`.", "",
      "## Scenes", "", "| Old (Nov 26) | New | Title now, or what happened to it |", "|---|---|---|"]
newtitle = {}
for line in "\n".join(out).split("\n"):
    mm = bp.SCENE.match(line)
    if mm:
        newtitle[mm.group(1)] = mm.group(2)
for i in sorted(OLD, key=sort_key):
    if i in CUT:
        m.append(f"| {i} | {idmap.get(i, '—')} | {CUT[i]} |")
    else:
        new = idmap[i]
        note = newtitle[new]
        if OLD[i]["title"] != note:
            note += f" (was \"{OLD[i]['title']}\")"
        m.append(f"| {i} | {new} | {note} |")
m += ["", "## New on Nov 27 (no old ID)", "", "| New | Title |", "|---|---|"]
olds = set(idmap.values())
for i in new_ids:
    if i not in olds:
        m.append(f"| {i} | {newtitle[i]} |")
m += ["", "## First-page IDs (Nov 25) that the Nov 26 revision had already moved or cut", "",
      "| First page (Nov 25) | What happened on Nov 26 | Now |", "|---|---|---|"]
for a, what, via in ROUND1:
    now = resolve(via) if via else None
    m.append(f"| {a} | {what} | {now or '—'} |")
m += ["", "Every other first-page ID is the same as its Nov 26 ID, so read it through the Scenes table. "
      "Two Nov 26 scenes reused a first-page ID for new content and are easy to misread: first-page 42.6 (the old life's slow fight, now R.5) is not Nov 26's 42.6 (\"Go,\" still 42.6); "
      "first-page 43.6 (the promise, now R.7) is not Nov 26's 43.6 (\"Live,\" cut).", ""]
MAP.write_text("\n".join(m), encoding="utf-8")
print(f"{len(new_ids)} scenes written; {len(idmap)} old IDs mapped, {len(CUT)} cut or folded")
