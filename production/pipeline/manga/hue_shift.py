#!/usr/bin/env python3
"""Pull a hue band toward another hue on a panel (Ch2 insert: Natsuki's uniform drifting violet, 259-270 deg, back to
her reference's dusty blue, about 214-237 deg). Only saturated-enough pixels inside the band move; the shift fades out
over FEATHER degrees at both ends of the band, so lines, skin and the warm dojo are untouched.

  hue_shift.py IN OUT --band 248,292 --shift -32 [--feather 10] [--min-sat 0.10] [--box x0,y0,x1,y1]
"""
import argparse
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--band", default="248,292"); ap.add_argument("--shift", type=float, default=-32)
ap.add_argument("--feather", type=float, default=10); ap.add_argument("--min-sat", type=float, default=0.10)
ap.add_argument("--box", help="limit to x0,y0,x1,y1 (px)")
a = ap.parse_args()
im = Image.open(a.inp).convert("RGB")
hsv = np.asarray(im.convert("HSV")).astype(np.float32)
h, s, v = hsv[..., 0] * 360 / 255, hsv[..., 1] / 255, hsv[..., 2]
lo, hi = map(float, a.band.split(","))
w = np.clip((h - lo) / a.feather, 0, 1) * np.clip((hi - h) / a.feather, 0, 1) * np.clip((s - a.min_sat) / 0.05, 0, 1)
if a.box:
    x0, y0, x1, y1 = map(int, a.box.split(","))
    m = np.zeros_like(w); m[y0:y1, x0:x1] = 1; w *= m
h2 = (h + a.shift * w) % 360
out = np.stack([h2 * 255 / 360, s * 255, v], -1).clip(0, 255).astype(np.uint8)
Image.fromarray(out, "HSV").convert("RGB").save(a.out, quality=95)
print(f"moved {(w > 0.5).mean() * 100:.1f}% of pixels")
