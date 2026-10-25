"""Automated playthrough of a VN build in Chromium at iPad sizes.
Steps through every line (and lists any line it never saw on screen), screenshots each scene start and every line listed in --shots, checks that every
voiced line decodes, that every image/video/audio request succeeds, and that no script errors occur.
Usage: python3 qa_play.py URL OUTDIR [--size 1180x820] [--every] [--shots id1,id2]"""
import sys, json, time, argparse
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("out")
ap.add_argument("--size", default="1180x820"); ap.add_argument("--every", action="store_true")
ap.add_argument("--shots", default="")
a = ap.parse_args()
W, H = map(int, a.size.split("x"))
shots = set(filter(None, a.shots.split(",")))
report = {"errors": [], "bad_requests": [], "voice_missing": [], "shots": [], "missed_lines": []}
seen = []
where = {"at": "start"}   # the last line or insert step reached, so a failed request says where it happened
with sync_playwright() as p:
    b = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
    ctx = b.new_context(viewport={"width": W, "height": H}, device_scale_factor=2, has_touch=True)
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: report["errors"].append(str(e)))
    pg.on("console", lambda m: report["errors"].append(m.text) if m.type == "error" else None)
    pg.on("response", lambda r: report["bad_requests"].append(f"{r.status} {r.url} (at {where['at']})") if r.status >= 400 else None)
    pg.goto(a.url + "#qa&dev"); pg.wait_for_timeout(3500)
    pg.screenshot(path=f"{a.out}/00_title.png"); report["shots"].append("00_title")
    pg.click("#tapStart"); pg.wait_for_timeout(400)
    pg.evaluate("window.__vn.audioInit()")
    # voice check
    # spoken lines, including those inside manga inserts (Ch2 on)
    ids = pg.evaluate("window.__vn.S.flatMap(c=>c.t==='insert'?c.panels.flatMap(p=>p.lines):[c]).filter(c=>c.t==='say').map(c=>c.id)")
    for i in ids:
        d = pg.evaluate(f"window.__vn.vprobe('{i}')")
        if not d and pg.evaluate(f"!!(window.__vn.vIndex||{{}})['{i}']"):
            report["voice_missing"].append(i)
    report["voiced"] = sum(1 for i in ids if pg.evaluate(f"!!(window.__vn.vIndex||{{}})['{i}']"))
    report["say_lines"] = len(ids)
    pg.evaluate("window.__vn.setDev(false)")   # hide the dev strip for clean screenshots
    pg.click("#mStart"); pg.wait_for_timeout(1500)
    last_scene, n, guard = None, 0, 0
    while guard < 2000:
        guard += 1
        st = pg.evaluate("window.__vn.check()")
        if "endCard" in st["cards"]:
            pg.wait_for_timeout(900); pg.screenshot(path=f"{a.out}/99_end.png"); report["shots"].append("99_end"); break
        cur = st.get("id")
        scene = pg.evaluate("window.__vn.state.scene")
        where["at"] = f"{scene}/{cur}"
        if st.get("cur") == "insert" and st.get("ins"):
            # a manga insert: one stop per step (the whole page, then each panel); its lines count as seen when shown
            k = st["ins"]["k"]
            if not seen or seen[-1] != f"ins:{st['ins']['name']}:{k}":
                seen.append(f"ins:{st['ins']['name']}:{k}")
                if scene != last_scene or a.every:
                    tag = f"{n:03d}_{st['ins']['name']}_{k:02d}" if scene == last_scene else f"{n:03d}_{scene}_start"
                    last_scene = scene
                    pg.wait_for_timeout(900); pg.screenshot(path=f"{a.out}/{tag}.png"); report["shots"].append(tag)
                pg.evaluate("window.__vn.advance()"); pg.wait_for_timeout(120)
            else:
                pg.wait_for_timeout(150)
            continue
        if st.get("cur") == "phone":
            n += 1
            if cur and (not seen or seen[-1] != cur): seen.append(cur)
            if scene != last_scene or a.every or cur in shots:
                tag = f"{n:03d}_{scene}_start" if scene != last_scene else f"{n:03d}_{cur}"
                last_scene = scene
                pg.wait_for_timeout(500); pg.screenshot(path=f"{a.out}/{tag}.png"); report["shots"].append(tag)
            pg.evaluate("window.__vn.advance()"); pg.wait_for_timeout(60)
            continue
        if st.get("cur") in ("say", "nar") and not st["typing"]:
            n += 1
            if cur and (not seen or seen[-1] != cur): seen.append(cur)
            tag = None
            if scene != last_scene:
                tag = f"{n:03d}_{scene}_start"; last_scene = scene
            elif a.every or cur in shots:
                tag = f"{n:03d}_{cur}"
            if tag:
                pg.wait_for_timeout(1300)          # let fades and live stills settle
                pg.screenshot(path=f"{a.out}/{tag}.png"); report["shots"].append(tag)
            pg.evaluate("window.__vn.advance()")
            pg.wait_for_timeout(60)
        elif st.get("typing"):
            # check and tap in one step: a short line can finish typing in between, and a plain tap would skip it
            pg.evaluate("(()=>{ if(window.__vn.check().typing) window.__vn.advance(); })()"); pg.wait_for_timeout(30)
        else:
            pg.wait_for_timeout(250)
            if st["cards"]:
                pg.evaluate("window.__vn.advance()")
    report["lines_seen"] = n
    all_ids = pg.evaluate("window.__vn.S.filter(c=>c.t==='say'||c.t==='nar'||c.t==='phone').map(c=>c.id)")
    report["missed_lines"] = [i for i in all_ids if i not in set(seen)]
    # every step of every insert should have been shown
    ins = pg.evaluate("window.__vn.S.filter(c=>c.t==='insert').map(c=>c.name)")
    report["insert_steps_seen"] = {nm: sum(1 for x in seen if x.startswith(f"ins:{nm}:")) for nm in ins}
    b.close()
json.dump(report, open(f"{a.out}/report.json", "w"), indent=1)
print(json.dumps({k: (v if not isinstance(v, list) else (len(v) if k == "shots" else v[:12])) for k, v in report.items()}, indent=1, ensure_ascii=False))
