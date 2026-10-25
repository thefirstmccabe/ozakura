"""Build batched TTS jobs (one speaker, one scene, up to 10 lines each) from a compiled voice line list.
Usage: python3 voice_jobs.py lines.json jobs.json"""
import json, sys, collections
VOICE = {  # style guide §7 (author-picked cast); pitch shifts are applied afterwards
 "kohei": ("Puck", "A 16-year-old Japanese high-school boy. Calm and grounded with dry humor; warm underneath, often with an easy smile in his voice; never gruff."),
 "nanoha": ("Erinome", "A 16-year-old Japanese high-school girl. Young, light, clear voice; soft and relaxed, quiet deadpan with a hidden smile; playful. Must sound like a teenager, never a grown woman."),
 "natsuki": ("Zephyr", "A 16-year-old Japanese high-school girl with a young, light, clear anime-heroine voice. Bright, sunny and quietly confident; playful and teasing, a smile in every line, never loud. Must sound like a teenager, never a grown woman."),  # Oct 24, Audio thread pick: brighter direction, +1 semitone (voice_pack.py)
 "akane": ("Aoede", "A 14-year-old Japanese middle-school girl, the sweet little sister. Young, soft, a little higher pitched, playful and teasing, slightly frail. Must sound 14, never a grown woman."),
 "rika": ("Laomedeia", "A 16-year-old high-school girl. Genki, loud, bubbly, no indoor voice. Young and bright."),
 "ryosuke": ("Achird", "A 16-year-old male high-school student. Precise, a little smug, dry and amused know-it-all."),
 "teacher": ("Schedar", "A tired male homeroom teacher in his 40s, droopy, mild and long-suffering, speaking to his class."),
 "past_natsuki": ("Despina", "A young married woman in Edo-era Japan, in her mid-twenties, heard in a dream. A grown woman, not a teenager: warm, gentle, a little lower and slower; scolding with love while half laughing, as if she has waited a very long time."),  # recast Oct 18 (style guide §7; audition oct18-dream, candidate 2)
}
PLACE = {"prologue": "a dream", "c1_dream": "a dream", "c1_morning": "a morning scene at home", "c1_river": "a walk to school along the river",
         "c1_entrance": "a busy school entrance", "c1_intro": "a classroom", "c1_lunch": "lunch in the classroom",
         "c1_interlude": "an empty classroom after school", "c1_night": "a quiet street at night"}
if __name__ == "__main__":
    lines = json.load(open(sys.argv[1]))
    groups = collections.OrderedDict()
    for x in lines:
        groups.setdefault((x["scene"], x["who"]), []).append(x)
    jobs = []
    for (scene, who), xs in groups.items():
        k = max(1, -(-len(xs) // 10)); size = -(-len(xs) // k)
        for c in range(k):
            chunk = xs[c * size:(c + 1) * size]
            voice, style = VOICE[who]
            tail = (f" These are separate lines of dialogue from {PLACE[scene]}: give each line its own natural emotion, "
                    "and leave a clear pause between lines.") if len(chunk) > 1 else f" A line of dialogue from {PLACE[scene]}."
            jobs.append({"key": f"{scene}.{who}.{c + 1}", "ids": [x["id"] for x in chunk], "texts": [x["ja"] for x in chunk],
                         "input": {"prompt": "\n\n".join(x["ja"] for x in chunk), "voice": voice, "style_instructions": style + tail}})
    json.dump(jobs, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
    print(len(jobs), "jobs,", sum(len(j["input"]["prompt"]) + len(j["input"]["style_instructions"]) for j in jobs), "chars")
