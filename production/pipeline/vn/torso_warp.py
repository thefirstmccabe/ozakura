#!/usr/bin/env python3
"""Lengthen (or shorten) a sprite's torso with a smooth vertical-only warp, keeping its head and its overall height.

  torso_warp.py IN OUT --keep-above Y0 --move Y_FROM Y_TO   (rows as fractions of the image height)

Rows above Y0 (the head, the bow) are untouched; the row at Y_FROM (the skirt's waistband) moves to Y_TO; everything below
is compressed to fit, so the bottom edge stays put. The mapping is a monotone cubic through (0,0), (Y0,Y0), (Y_TO,Y_FROM),
(1,1), so there are no visible kinks. Works on RGBA, so a sprite's cutout moves with it. Oct 24: Natsuki's waist sat
about 2 inches too high for her height (her torso drawn short), which put the two girls' waists far apart in two-shots.
"""
import argparse
import numpy as np
from PIL import Image
from scipy.interpolate import PchipInterpolator

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--keep-above", type=float, required=True)
ap.add_argument("--move", nargs=2, type=float, required=True)
a = ap.parse_args()
im = Image.open(a.inp); mode = im.mode
arr = np.array(im.convert("RGBA")).astype(np.float32); H = arr.shape[0]
y0, yf, yt = a.keep_above, a.move[0], a.move[1]
f = PchipInterpolator([0, y0, yt, 1], [0, y0, yf, 1])   # output row fraction -> source row fraction
src = f((np.arange(H) + 0.5) / H) * H - 0.5
i0 = np.clip(np.floor(src).astype(int), 0, H - 1); i1 = np.clip(i0 + 1, 0, H - 1); w = (src - np.floor(src))[:, None, None]
out = arr[i0] * (1 - w) + arr[i1] * w
res = Image.fromarray(out.round().clip(0, 255).astype(np.uint8), "RGBA")
(res if mode == "RGBA" else res.convert("RGB")).save(a.out)
print(f"rows < {y0:.3f} kept; waist {yf:.3f} -> {yt:.3f} ({(yt - yf) * H:.0f} px)")
