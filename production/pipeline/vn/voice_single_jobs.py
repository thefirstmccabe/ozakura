"""Build one-line-per-take TTS jobs for a chapter (the Oct 24 method: each take's style instruction carries the
line's sprite expression or face, what the line means in English, and where it's said).

Usage: python3 voice_single_jobs.py VOICE_LINES.json SRC.ozs PREFIX OUT_JOBS.json
  VOICE_LINES.json: compile_script.py's voice list; only ids starting with PREFIX (e.g. c2_) are used.
  SRC.ozs: the chapter source, read for each line's <expr> / (face).
Writes a list of {key, ids, texts, input: {prompt, voice, style_instructions}} (the voice_jobs.py format).
Cast and base directions: style guide §7 (voice_jobs.VOICE plus the Ch2 cast below). Pitch shifts are applied later
by voice_pack.py."""
import json, re, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from voice_jobs import VOICE, PLACE
VOICE, PLACE = dict(VOICE), dict(PLACE)
VOICE.update({
 "kirishima": ("Charon", "A 17-year-old Japanese high-school boy, captain of the kendo club. Calm, low voice with quiet authority; deadpan, bone-dry humor; never raises his voice except to call a match."),
 "takatsuki": ("Fenrir", "A 16-year-old Japanese high-school boy in the kendo club. Precise, reserved and dry; speaks in complete, correct sentences; serious and formal, never sneering."),
 "manager": ("Enceladus", "The manager of a family restaurant, in his forties: harried and rushed but upbeat and kind, calling out to his part-time staff."),
 "classmate": ("Callirrhoe", "A 16-year-old Japanese high-school girl out with friends after school: friendly, bright and chatty, teasing a little. Must sound like a teenager."),   # [P] Oct 25, Production; for the Audio thread to confirm
})
PLACE.update({"c2_tuesday": "a busy family restaurant at night", "c2_dojo": "a school kendo dojo before practice",
              "c2_lesson": "a school kendo dojo during a water break", "c2_match": "a kendo practice match",
              "c2_debrief": "a school kendo dojo right after a practice match", "c2_mop": "an empty kendo dojo in the evening, wiping the floor",
              "c2_bridge": "a bridge over a river at dusk", "c2_morning": "a family kitchen early on a school morning", "c2_interlude": "a quiet apartment at night"})
MOOD = {"smile": "smiling", "grin": "grinning, cheeky", "laugh": "laughing", "smirk": "smug, teasing", "surprised": "surprised",
        "blush": "embarrassed, flustered", "curious": "curious", "wistful": "soft and a little wistful", "tears": "flustered and embarrassed, laughing it off",
        "point": "explaining brightly, like a teacher", "calm": "calm", "stern": "stern and level", "neutral": "even, neutral", "deadpan": "deadpan, dry",
        "annoyed": "mildly annoyed", "flustered": "flustered", "serious": "serious", "grin_": "", "scheme": "scheming, eager", "frown": "displeased",
        "sad": "sad", "stillness": "very quiet and still"}
EXTRA = {"c2_0259": " She says it aloud to herself, alone, trying out a practiced joke about always moving schools: bright on the surface, a little hollow underneath.",
         "c2_0185": " She is slipping on a wet floor: a short, startled gasp.",
         "c2_0133": " Sheepish, caught out by the captain.", "c2_0135": " A small, dismayed echo of what the captain just said.",
         "c2_0226": " Brushing it off quickly and lightly: a quick smile covering a little disappointment.",
         "c2_0307": " His voice is a little hoarse this morning from talking a lot last night.",
         "c2_0316": " She has just noticed something new in his face; quiet, matter-of-fact.",
         "c2_0322": " Gentle and matter-of-fact, setting a throat lozenge down for him."}
REF = " He is refereeing the match: a loud, clear, crisp call that carries across the dojo."
KIAI = {"めぇぇんっ！", "こてぇぇっ！", "どぉぉっ！"}
lines_path, src_path, prefix, out = sys.argv[1:5]
lines = [x for x in json.load(open(lines_path, encoding="utf-8")) if x["id"].startswith(prefix)]
SAY = re.compile(r'^(\w+)(?:<(\w+)>)?(?:\((\w+)\))?:.*#(\S+)\s*$')
mood_of, cur = {}, {}
for l in open(src_path, encoding="utf-8"):
    m = re.match(r'@show (\w+) \w+?_(\w+)', l)
    if m: cur[m.group(1)] = m.group(2)
    m = SAY.match(l.rstrip("\n"))
    if m:
        who, expr, face, lid = m.groups()
        if expr: cur[who] = expr
        mood_of[lid] = face or expr or cur.get(who)
jobs = []
for x in lines:
    voice, style = VOICE[x["who"]]
    mood = MOOD.get(mood_of.get(x["id"]) or "", "")
    en = re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", x["en"]).strip('"')
    s = f"{style} This line is said in {PLACE[x['scene']]}"
    s += f", {mood}." if mood else "."
    s += f' It means: "{en}"'
    s += EXTRA.get(x["id"], "")
    if x["who"] == "kirishima" and x["scene"] == "c2_match": s += REF
    if x["ja"] in KIAI: s += " It is a kendo kiai: a sharp, loud, full-voiced shout on the strike, held a little."
    jobs.append({"key": f"{x['scene']}.{x['who']}.{x['id']}", "ids": [x["id"]], "texts": [x["ja"]],
                 "input": {"prompt": x["ja"], "voice": voice, "style_instructions": s}})
json.dump(jobs, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(jobs), "jobs,", sum(len(j["input"]["prompt"]) + len(j["input"]["style_instructions"]) for j in jobs), "chars")
