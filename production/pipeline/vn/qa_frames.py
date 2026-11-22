"""Screenshot chosen lines at several screen sizes, to check framing (a CG against the text box, a name tag, a face window).
Jumps straight to each line with the dev hook (no playthrough), waits for the CG and the text to settle, and saves
OUT/<size>_<line id>.png plus OUT/boxes.json (the text box's and name tag's top edge on each shot, in points).

Usage: python3 qa_frames.py URL OUT --sizes 1080x810,1180x820,844x390 --ids c3_0100,c3_0106 [--fonts URL] [--wait 2600]
Sizes under 500 points tall get touch and a phone-style context (the engine's phone layout keys off the height).
Made Nov 21 for the Ch3 window-CG lift."""
import argparse, json, os, re
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("url"); ap.add_argument("out")
ap.add_argument("--sizes", required=True); ap.add_argument("--ids", required=True)
ap.add_argument("--fonts", default=""); ap.add_argument("--wait", type=int, default=2600)
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
sizes = [tuple(map(int, s.split("x"))) for s in a.sizes.split(",")]
ids = [i for i in a.ids.split(",") if i]
boxes = {}
with sync_playwright() as p:
    b = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"], ignore_default_args=["--disable-dev-shm-usage"])
    for W, H in sizes:
        phone = H < 500
        ctx = b.new_context(viewport={"width": W, "height": H}, device_scale_factor=2 if not phone else 3, has_touch=True, is_mobile=phone)
        pg = ctx.new_page()
        if a.fonts:   # this sandbox can't reach Google Fonts; a local copy keeps the text metrics honest (as qa_phone.py does)
            def patch(route):
                resp = route.fetch(); body = re.sub(r'href="https://fonts\.googleapis\.com/css2[^"]*"', f'href="{a.fonts}"', resp.text())
                route.fulfill(response=resp, body=body, headers={**resp.headers, "content-type": "text/html; charset=utf-8"})
            ctx.route(re.compile(r".*/(index\.html)?(\?[^/]*)?$"), patch)
        pg.goto(a.url + "#qa&dev"); pg.wait_for_timeout(2500)
        pg.click("#tapStart"); pg.wait_for_timeout(300)
        pg.evaluate("window.__vn.audioInit()"); pg.evaluate("window.__vn.setDev(false)")
        for i in ids:
            j = pg.evaluate(f"window.__vn.S.findIndex(c=>c.id==='{i}')")
            if j < 0:
                print("not in this build:", i); continue
            pg.evaluate(f"window.__vn.devJump({j})"); pg.evaluate("window.__vn.setDev(false)")
            pg.wait_for_timeout(a.wait)
            # finish the typewriter without advancing: one advance() completes the line if it is still typing
            if pg.evaluate("document.querySelector('#text').classList.contains('typing')"):
                pg.evaluate("window.__vn.advance()"); pg.wait_for_timeout(300)
            r = pg.evaluate("""()=>{const q=s=>{const e=document.querySelector(s); if(!e||getComputedStyle(e).display==='none') return null; const r=e.getBoundingClientRect(); return r.width?{top:Math.round(r.top),bottom:Math.round(r.bottom),left:Math.round(r.left)}:null};
                return {box:q('#box'), name:q('#name'), face:q('#face.on'), nameText:(document.querySelector('#name')||{}).textContent||''}}""")
            boxes[f"{W}x{H}_{i}"] = r
            pg.screenshot(path=f"{a.out}/{W}x{H}_{i}.png")
        ctx.close()
    b.close()
json.dump(boxes, open(os.path.join(a.out, "boxes.json"), "w"), indent=1, ensure_ascii=False)
print(json.dumps(boxes, ensure_ascii=False)[:1500])
