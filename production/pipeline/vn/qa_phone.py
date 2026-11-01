"""Phone-layout QA (Nov 1): play a VN build through at a phone size, shoot every line, and measure the layout on each one.

qa_play.py checks that the build plays; this checks that it fits. On every line (and every text message and insert step)
it records where the text box, name tag, face window, control row, interlude label, text-message panel and tap hint sit,
the rendered size of every piece of text in the box, and whether anything overflows, clips, overlaps, leaves the screen
or sits under a simulated notch. It then tours the menus (backlog, save, load, settings, notes, chapters), opens one
translator's note per term, and shoots the title and the rotate-your-device screen.

Notch: Chromium has no safe areas, so the page's env(safe-area-inset-*) values are rewritten as the build loads
(iPhone 12 Pro in landscape: 47 points on the notch side, 21 at the bottom). --notch left|right|none.

Flags (report.json "flags", also printed):
  text-size     a text run in the box renders above the phone size (the Oct 31 "old iPad size" lines)
  offscreen     an element leaves the viewport;  notch  an element starts inside the notch inset
  overlap       name tag / control row / face window / text overlap each other; phone panel vs interlude label
  overflow      the text, the name tag or a panel body overflows its box (clipped)
  tall-box      the text box covers more than --max-box of the screen height (default 0.42)
  small-tap     a control smaller than 28 points on either side
Usage: python3 qa_phone.py URL OUT [--size 844x345] [--notch left] [--every] [--dsf 2] [--no-tour] [--from SCENE]
"""
import argparse, json, re
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("out")
ap.add_argument("--size", default="844x345"); ap.add_argument("--notch", default="left", choices=["left", "right", "none"])
ap.add_argument("--inset", type=int, default=47); ap.add_argument("--bottom", type=int, default=21)
ap.add_argument("--every", action="store_true"); ap.add_argument("--dsf", type=float, default=2)
ap.add_argument("--no-tour", action="store_true"); ap.add_argument("--max-box", type=float, default=0.42)
ap.add_argument("--phone-text", type=float, default=16.5, help="largest allowed rendered text size in the box, points")
ap.add_argument("--fonts", default="", help="URL of a local stylesheet for the game fonts (this sandbox can't reach Google Fonts)")
ap.add_argument("--limit", type=int, default=0, help="stop after this many lines (smoke tests)")
ap.add_argument("--desktop", action="store_true", help="no touch, no phone user agent, no notch (iPad/desktop geometry dumps)")
a = ap.parse_args()
W, H = map(int, a.size.split("x"))
L = a.inset if a.notch == "left" else 0
R = a.inset if a.notch == "right" else 0
B = a.bottom if a.notch != "none" else 0
if a.desktop:
    L = R = B = 0

MEASURE = r"""() => {
  const q = s => document.querySelector(s), W = innerWidth, H = innerHeight;
  const vis = e => { if (!e) return false; const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return false;
    let x = e; while (x && x !== document.body) { const s = getComputedStyle(x); if (s.display === 'none' || parseFloat(s.opacity) < 0.05) return false; x = x.parentElement; } return true; };
  const r = e => { const b = e.getBoundingClientRect(); return [Math.round(b.left*10)/10, Math.round(b.top*10)/10, Math.round(b.right*10)/10, Math.round(b.bottom*10)/10]; };
  const out = {W, H, el: {}};
  for (const [k, s] of Object.entries({box:'#box', text:'#text', name:'#name', face:'#face', ctrl:'#ctrl', ilabel:'#ilabel', phone:'#phone', hint:'#tapHint', note:'#note'})) {
    const e = q(s); if (vis(e) && !(k === 'name' && !e.textContent.trim())) out.el[k] = r(e);
  }
  const box = q('#box');
  if (vis(box)) {
    const t = q('#text'); let mx = 0, mn = 99;
    const walker = document.createTreeWalker(t, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) { const n = walker.currentNode; if (!n.textContent.trim()) continue; const fs = parseFloat(getComputedStyle(n.parentElement).fontSize); mx = Math.max(mx, fs); mn = Math.min(mn, fs); }
    out.textSize = mx; out.textMin = mn === 99 ? 0 : mn;
    out.textOverflow = t.scrollHeight - t.clientHeight;
    const nm = q('#name'); if (vis(nm) && nm.textContent.trim()) { out.nameText = nm.textContent; out.nameOverflow = nm.scrollWidth - nm.clientWidth; out.nameSize = parseFloat(getComputedStyle(nm).fontSize); }
    out.cb = [...document.querySelectorAll('#ctrl .cb')].map(b => r(b));
    out.textLines = Math.round(t.getBoundingClientRect().height / parseFloat(getComputedStyle(t).lineHeight || '24'));
  }
  const ph = q('#phone'); if (vis(ph) && ph.classList.contains('on')) out.phoneOverflow = ph.scrollHeight - ph.clientHeight;
  return out;
}"""


def flags_for(m, where):
    f = []
    el = m["el"]; Wv, Hv = m["W"], m["H"]

    def off(k):
        x0, y0, x1, y1 = el[k]
        return x0 < -0.5 or y0 < -0.5 or x1 > Wv + 0.5 or y1 > Hv + 0.5

    def inter(p, q, pad=0):
        return not (p[2] <= q[0] + pad or q[2] <= p[0] + pad or p[3] <= q[1] + pad or q[3] <= p[1] + pad)
    for k in el:
        if k in ("name", "ctrl", "ilabel", "hint"):   # these sit on edges by design; still must be on screen
            pass
        if off(k) and k != "note":
            f.append(("offscreen", f"{k} {el[k]}"))
        if k in ("box", "face", "ctrl", "phone", "note", "ilabel", "name", "text") and (el[k][0] < L - 0.5 or el[k][2] > Wv - R + 0.5):
            f.append(("notch", f"{k} {el[k]} (insets L{L} R{R})"))
        if k in ("box", "face", "ctrl") and el[k][3] > Hv - B + 0.5:
            f.append(("notch", f"{k} bottom {el[k][3]} under the home-indicator inset {B}"))
    if "textSize" in m and m["textSize"] > a.phone_text and not a.desktop:
        f.append(("text-size", f"text renders at {m['textSize']} pt"))
    if m.get("textOverflow", 0) > 1:
        f.append(("overflow", f"text overflows by {m['textOverflow']} pt"))
    if m.get("nameOverflow", 0) > 1:
        f.append(("overflow", f"name tag '{m.get('nameText')}' clipped by {m['nameOverflow']} pt"))
    if m.get("phoneOverflow", 0) > 1:
        f.append(("overflow", f"phone panel overflows by {m['phoneOverflow']}"))
    if "name" in el and "ctrl" in el and inter(el["name"], el["ctrl"], 2 if False else 0):
        f.append(("overlap", f"name tag {el['name']} meets the control row {el['ctrl']}"))
    if "face" in el and "text" in el and inter(el["face"], el["text"]):
        f.append(("overlap", f"face {el['face']} over text {el['text']}"))
    if "face" in el and "name" in el and inter(el["face"], el["name"]):
        f.append(("overlap", f"face {el['face']} over name {el['name']}"))
    if "ctrl" in el and "text" in el and inter(el["ctrl"], el["text"]):
        f.append(("overlap", f"controls {el['ctrl']} over text {el['text']}"))
    if "phone" in el and "ilabel" in el and inter(el["phone"], el["ilabel"]):
        f.append(("overlap", f"phone panel {el['phone']} over interlude label {el['ilabel']}"))
    if "phone" in el and "hint" in el and inter(el["phone"], el["hint"]):
        f.append(("overlap", f"phone panel {el['phone']} over tap hint {el['hint']}"))
    if "box" in el and not a.desktop and (el["box"][3] - el["box"][1]) / Hv > a.max_box:
        f.append(("tall-box", f"box is {(el['box'][3]-el['box'][1])/Hv:.0%} of the screen"))
    for b in m.get("cb", []):
        if not a.desktop and (b[2] - b[0] < 28 or b[3] - b[1] < 28):
            f.append(("small-tap", f"control {b} is {b[2]-b[0]:.0f}x{b[3]-b[1]:.0f}")); break
    return [(k, f"{where}: {v}") for k, v in f]


report = {"size": a.size, "notch": a.notch, "lines": {}, "flags": [], "errors": [], "bad": [], "tour": []}
with sync_playwright() as p:
    b = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"], ignore_default_args=["--disable-dev-shm-usage"])
    kw = dict(viewport={"width": W, "height": H}, device_scale_factor=a.dsf)
    if not a.desktop:
        kw.update(has_touch=True, is_mobile=True, user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1")
    ctx = b.new_context(**kw)

    def patch(route):
        resp = route.fetch(); body = resp.text()
        body = re.sub(r"env\(safe-area-inset-left(?:,\s*0px)?\)", f"{L}px", body)
        body = re.sub(r"env\(safe-area-inset-right(?:,\s*0px)?\)", f"{R}px", body)
        body = re.sub(r"env\(safe-area-inset-bottom(?:,\s*0px)?\)", f"{B}px", body)
        body = re.sub(r"env\(safe-area-inset-top(?:,\s*0px)?\)", "0px", body)
        if a.fonts:
            body = re.sub(r'href="https://fonts\.googleapis\.com/css2[^"]*"', f'href="{a.fonts}"', body)
        route.fulfill(response=resp, body=body, headers={**resp.headers, "content-type": "text/html; charset=utf-8"})
    ctx.route(re.compile(r".*/(index\.html)?(\?[^/]*)?$"), patch)
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: report["errors"].append(str(e)))
    pg.on("console", lambda m: report["errors"].append(m.text) if m.type == "error" else None)
    pg.on("response", lambda r: report["bad"].append(f"{r.status} {r.url}") if r.status >= 400 else None)
    pg.goto(a.url + "#qa&dev"); pg.wait_for_timeout(3000)
    pg.screenshot(path=f"{a.out}/000_tapstart.png")
    pg.click("#tapStart"); pg.wait_for_timeout(900)
    pg.evaluate("window.__vn.setDev(false)"); pg.wait_for_timeout(300)
    pg.screenshot(path=f"{a.out}/000_title.png")
    pg.evaluate("window.__vn.audioInit()")
    pg.click("#mStart"); pg.wait_for_timeout(1500)
    n, last, seen_terms, guard = 0, None, set(), 0
    while guard < 4000:
        guard += 1
        st = pg.evaluate("window.__vn.check()")
        if "endCard" in st["cards"] or (a.limit and n >= a.limit):
            pg.wait_for_timeout(900); pg.screenshot(path=f"{a.out}/999_end.png"); break
        scene = pg.evaluate("window.__vn.state.scene")
        cur = st.get("id")
        key = None
        if st.get("cur") == "insert" and st.get("ins"):
            key = f"ins:{st['ins']['name']}:{st['ins']['k']}"
        elif st.get("cur") == "phone" or (st.get("cur") in ("say", "nar") and not st["typing"]):
            key = cur
        if key and key != last:
            last = key; n += 1
            pg.wait_for_timeout(1100 if st.get("cur") != "phone" else 450)
            m = pg.evaluate(MEASURE)
            tag = f"{n:03d}_{key.replace(':', '-')}"
            report["lines"][key] = {"scene": scene, **m}
            report["flags"] += flags_for(m, f"{scene}/{key}")
            if a.every or scene not in {v["scene"] for k, v in list(report["lines"].items())[:-1]}:
                pg.screenshot(path=f"{a.out}/{tag}.png")
            # one translator's note per term: open it, measure, shoot, close
            if not a.no_tour and st.get("cur") in ("say", "nar"):
                terms = pg.evaluate("[...document.querySelectorAll('#text .tn')].map(e=>e.dataset.n||e.textContent)")
                for i, t in enumerate(terms):
                    if t in seen_terms: continue
                    seen_terms.add(t)
                    pg.evaluate(f"document.querySelectorAll('#text .tn')[{i}].click()"); pg.wait_for_timeout(450)
                    mm = pg.evaluate(MEASURE)
                    report["tour"].append({"what": f"note {t} at {key}", **mm})
                    report["flags"] += flags_for(mm, f"note {t} at {key}")
                    pg.screenshot(path=f"{a.out}/{tag}_note-{re.sub(r'[^a-z0-9]+', '', t.lower())}.png")
                    pg.evaluate("window.__vn.closeNote()"); pg.wait_for_timeout(250)
            pg.evaluate("window.__vn.advance()"); pg.wait_for_timeout(60)
            continue
        if st.get("typing"):
            pg.evaluate("(()=>{ if(window.__vn.check().typing) window.__vn.advance(); })()"); pg.wait_for_timeout(30)
        else:
            pg.wait_for_timeout(200)
            if st["cards"]: pg.evaluate("window.__vn.advance()")
    report["count"] = n
    if not a.no_tour:
        # menus, from a line mid-Ch2 so the backlog and save slots have content
        def shot(name, fn, wait=600):
            try:
                pg.evaluate(fn); pg.wait_for_timeout(wait)
                info = pg.evaluate("""() => { const p=[...document.querySelectorAll('.panel.on')][0]; if(!p) return null;
                    const b=p.querySelector('.body'), h=p.querySelector('header'); const r=e=>{const x=e.getBoundingClientRect(); return [x.left,x.top,x.right,x.bottom]};
                    const wide=[...p.querySelectorAll('*')].filter(e=>{const x=e.getBoundingClientRect(); return x.width>0 && (x.right>innerWidth+0.5||x.left<-0.5)}).length;
                    return {panel:p.id, header:r(h), body:r(b), overflowX:b.scrollWidth-b.clientWidth, wide}; }""")
                report["tour"].append({"what": name, "panel": info})
                if info and (info["overflowX"] > 1 or info["wide"]):
                    report["flags"].append(("overflow", f"menu {name}: {info}"))
                if info and (info["header"][0] < L - 0.5 or info["header"][2] > W - R + 0.5):
                    report["flags"].append(("notch", f"menu {name}: header {info['header']}"))
                pg.screenshot(path=f"{a.out}/tour_{name}.png")
            except Exception as e:
                report["errors"].append(f"tour {name}: {e}")
        pg.evaluate("window.__vn.startAt && window.__vn.devJump && 0")
        pg.goto(a.url + "?tour#qa"); pg.wait_for_timeout(2500); pg.click("#tapStart"); pg.wait_for_timeout(600)
        pg.click("#mChap"); pg.wait_for_timeout(700); shot("chapters", "0")
        pg.evaluate("document.querySelector('#chapP [data-close]').click()"); pg.wait_for_timeout(300)
        pg.click("#mSet"); pg.wait_for_timeout(700); shot("settings", "0")
        pg.evaluate("document.querySelector('#setP .body').scrollTop=9999"); pg.wait_for_timeout(300); pg.screenshot(path=f"{a.out}/tour_settings_bottom.png")
        pg.evaluate("document.querySelector('#setNotes').click()"); pg.wait_for_timeout(600); shot("notes", "0")
        pg.evaluate("document.querySelectorAll('.panel.on [data-close]').forEach(x=>x.click())"); pg.wait_for_timeout(300)
        pg.click("#mStart"); pg.wait_for_timeout(1200)
        for _ in range(60):
            pg.evaluate("window.__vn.advance()"); pg.wait_for_timeout(120)
        pg.wait_for_timeout(800)
        pg.evaluate("document.querySelector('#bLog').click()"); pg.wait_for_timeout(700); shot("backlog", "0")
        pg.evaluate("document.querySelector('#logP [data-close]').click()"); pg.wait_for_timeout(300)
        pg.evaluate("document.querySelector('#bSave').click()"); pg.wait_for_timeout(700); shot("save", "0")
        pg.evaluate("document.querySelector('#slots .slot') && document.querySelector('#slots .slot').click()"); pg.wait_for_timeout(700); shot("save_after", "0")
        pg.evaluate("document.querySelectorAll('.panel.on [data-close]').forEach(x=>x.click())"); pg.wait_for_timeout(300)
        pg.evaluate("document.querySelector('#bLoad').click()"); pg.wait_for_timeout(700); shot("load", "0")
        pg.evaluate("document.querySelectorAll('.panel.on [data-close]').forEach(x=>x.click())"); pg.wait_for_timeout(300)
        pg.evaluate("document.querySelector('#bMenu').click()"); pg.wait_for_timeout(700); shot("menu", "0")
        pg.evaluate("document.querySelectorAll('.panel.on [data-close]').forEach(x=>x.click())"); pg.wait_for_timeout(300)
        # portrait: the rotate screen
        pg.set_viewport_size({"width": H, "height": W}); pg.wait_for_timeout(700)
        pg.screenshot(path=f"{a.out}/tour_rotate.png")
        rot = pg.evaluate("getComputedStyle(document.querySelector('#rotate')).display")
        report["tour"].append({"what": "rotate", "display": rot})
        if rot != "flex" and not a.desktop:
            report["flags"].append(("rotate", f"portrait shows no rotate screen ({rot})"))
    b.close()
json.dump(report, open(f"{a.out}/report.json", "w"), indent=1, ensure_ascii=False)
kinds = {}
for k, v in report["flags"]:
    kinds.setdefault(k, []).append(v)
print(json.dumps({"size": a.size, "notch": a.notch, "items": n, "errors": report["errors"][:8], "bad": report["bad"][:8],
                  "flags": {k: {"n": len(v), "first": v[:6]} for k, v in kinds.items()}}, indent=1, ensure_ascii=False))
