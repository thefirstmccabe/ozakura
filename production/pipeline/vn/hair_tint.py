"""Tint a sprite's hair (style guide §1: Takatsuki's deep slate blue, blue-black with steel-blue highlights [P], Oct 10).

The hair is found, not painted: in the top of the sprite, the largest connected region of dark, low-saturation pixels
(the hair mass and its line art), closed so its highlights join it; inside that region every low-saturation pixel
is recolored in Lab, keeping its lightness and setting its chroma to a blue that deepens with lightness
(b* = -(B0 + BK * L)), so the darkest lines stay near black and the highlights turn steel blue. Skin, eyes and the
keikogi are left alone (skin is saturated; the eyes and the gi are separate regions).
Usage: python3 hair_tint.py OUTDIR [--top 650] [--b0 8 --bk 0.27 --a -1] sprite1.webp sprite2.webp ...
Writes OUTDIR/<same name>.webp and OUTDIR/<name>_hairmask.png (for checking)."""
import argparse, os
import cv2, numpy as np
from PIL import Image
ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("files", nargs="+")
ap.add_argument("--top", type=int, default=650, help="search rows 0..TOP for the hair")
ap.add_argument("--b0", type=float, default=8); ap.add_argument("--bk", type=float, default=0.27); ap.add_argument("--a", type=float, default=-1)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
for f in a.files:
    s = np.asarray(Image.open(f).convert("RGBA")); rgb = s[..., :3]; al = s[..., 3]
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    dark = ((hsv[..., 2] < 130) & (hsv[..., 1] < 80) & (al > 128)).astype(np.uint8); dark[a.top:] = 0
    n, lab, st, _ = cv2.connectedComponentsWithStats(dark, 8)
    i = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    region = cv2.morphologyEx((lab == i).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    hair = (region > 0) & (hsv[..., 1] < 90) & (hsv[..., 2] < 215) & (al > 0)
    m = cv2.GaussianBlur(hair.astype(np.float32), (0, 0), 1.2)
    L, A, B = cv2.split(cv2.cvtColor(rgb.astype(np.float32) / 255, cv2.COLOR_RGB2LAB))
    A2 = np.full_like(A, a.a); B2 = -(a.b0 + a.bk * L)
    t = cv2.cvtColor(cv2.merge([L, A2, B2]), cv2.COLOR_LAB2RGB) * 255
    out = rgb * (1 - m[..., None]) + t * m[..., None]
    name = os.path.basename(f).rsplit(".", 1)[0]
    Image.fromarray(np.dstack([np.clip(out, 0, 255).astype(np.uint8), al]), "RGBA").save(os.path.join(a.out, name + ".webp"), "WEBP", quality=90, method=6)
    Image.fromarray((m * 255).astype(np.uint8)).save(os.path.join(a.out, name + "_hairmask.png"))
    print(name, "hair px", int(hair.sum()))
