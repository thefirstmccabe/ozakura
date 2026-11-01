"""Ch3 sprite sets for new characters (Mio, Genji): paste each head-crop expression edit back onto the base only where
it changed, then cut out with the base's alpha and finish with sprites.py (one shared crop, 1800 px tall).

  python3 build_sprites.py WORKDIR OUTDIR

WORKDIR holds the base renders (mio721.png, genji731.png), their bria cutouts (*_cut.png) and the 1K head edits
(mio_grin.png, …). Head crops (base px): Mio (440, 60, 1280, 900), Genji (650, 100, 1250, 700).
The paste mask is the thresholded difference between the edit and the base crop inside a central ellipse (every region over 250 px), closed,
dilated and feathered, so hair, collar and background outside the changed face stay the base's pixels exactly.
"""
import os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import cv2

W, OUT = sys.argv[1], sys.argv[2]
SETS = {
    "mio_home": ("mio721", (440, 60, 1280, 900), {"smug": None, "grin": "mio_grin", "pout": "mio_pout", "surprised": "mio_surprised"}),
    "genji_shrine": ("genji731", (650, 100, 1250, 700), {"smile": None, "grin": "genji_grin", "surprised": "genji_surprised"}),
    # Akane's home set: the expressions are pasted the same way, then framed like her school sprites by outfit_sprite.py
    # (fitted alignment, below), so her engine height and floor (v .733) still hold
    "akane_home": ("akane711", (531, 43, 1231, 743), {"smile": None, "sleepy": "akane_sleepy", "pout": "akane_pout", "tease": "akane_tease", "happy": "akane_happy"}),
}
ELLIPSE = {"akane_home": ((.47, .69), (.28, .18))}   # face only: her sweater-paw hands sit just under the chin in the crop
AKANE = dict(scale=1800 / 2528 * 1.35, align="0.77,-268.3,-56.6")   # hair-silhouette fit to v2/img/ch/akane_school_smile.webp
os.makedirs(OUT, exist_ok=True)
tmp = os.path.join(W, "exprs"); os.makedirs(tmp, exist_ok=True)
for name, (base, box, exprs) in SETS.items():
    rgb = Image.open(os.path.join(W, base + ".png")).convert("RGB")
    cut = Image.open(os.path.join(W, base + "_cut.png")).convert("RGBA")
    alpha = cut.split()[3]
    x0, y0, x1, y1 = box; side = x1 - x0
    crop = np.asarray(rgb.crop(box)).astype(np.int16)
    files = []
    for expr, src in exprs.items():
        out = rgb.copy()
        if src:
            ed = Image.open(os.path.join(W, src + ".png")).convert("RGB").resize((side, side), Image.LANCZOS)
            e = np.asarray(ed).astype(np.int16)
            diff = (np.abs(e - crop).max(2) > 22).astype(np.uint8) * 255
            (ecx, ecy), (erx, ery) = ELLIPSE.get(name, ((.5, .56), (.36, .40)))
            ell = np.zeros_like(diff); cv2.ellipse(ell, (int(side * ecx), int(side * ecy)), (int(side * erx), int(side * ery)), 0, 0, 360, 255, -1)
            m = cv2.bitwise_and(diff, ell)
            m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
            n, lab, stats, _ = cv2.connectedComponentsWithStats(m)
            if n > 1:   # keep every sizable changed region (eyes and mouth can be separate), drop specks
                keep = [k for k in range(1, n) if stats[k, cv2.CC_STAT_AREA] > 250]
                m = np.isin(lab, keep).astype(np.uint8) * 255
            m = cv2.dilate(m, np.ones((15, 15), np.uint8))
            mask = Image.fromarray(m).filter(ImageFilter.GaussianBlur(7))
            patch = Image.composite(ed, rgb.crop(box), mask)
            out.paste(patch, (x0, y0))
            print(f"{name}_{expr}: changed area {int((m > 0).sum())} px")
        rgba = out.convert("RGBA"); rgba.putalpha(alpha)
        f = os.path.join(tmp, f"{name}_{expr}.png"); rgba.save(f); files.append(f)
    vn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../pipeline/vn")
    if name != "akane_home":
        subprocess.run([sys.executable, os.path.join(vn, "sprites.py"), OUT] + files, check=True); continue
    repo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../..")
    for f in files:
        im = Image.open(f); im = im.resize((round(im.width * AKANE["scale"]), round(im.height * AKANE["scale"])), Image.LANCZOS)
        sf = f.replace(".png", "_S.png"); im.save(sf); expr = os.path.basename(f).rsplit(".", 1)[0].split("_")[-1]
        subprocess.run([sys.executable, os.path.join(vn, "outfit_sprite.py"),
                        "--master", os.path.join(repo, "production/pilot-v2/art/ch3/refs/akane-school-smile-white.png"),
                        "--ref-sprite", os.path.join(repo, "v2/img/ch/akane_school_smile.webp"), "--cutout", sf,
                        "--face-box", "372,345,290,260", "--align", AKANE["align"], "--oval", "372,340,128,118",
                        "--out", os.path.join(W, "akane_frame"), "--name", f"akane_home_{expr}"], check=True)
        os.replace(os.path.join(W, "akane_frame", f"akane_home_{expr}_base.webp"), os.path.join(OUT, f"akane_home_{expr}.webp"))
