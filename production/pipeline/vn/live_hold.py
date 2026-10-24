#!/usr/bin/env python3
"""Hold parts of a living-still loop still: inside the given boxes every frame shows the loop's first frame, so people
can't morph mid-loop (Kling redrew a bag on Natsuki and opened Nanoha's eyes in the Oct 20 title loop), while petals,
branches and sky keep moving. Boxes are x0,y0,x1,y1 fractions of the frame; edges are feathered.

  live_hold.py IN.mp4 OUT.mp4 --size 1920x1072 --box 0.22,0.53,0.31,1 --box ... [--oval cx,cy,rx,ry] [--feather 28] [--crf 20]
               [--still NEW.png]

--oval adds an elliptical held region (center and radii as fractions of the frame). --still shows that image (scaled to the
frame) in the held regions instead of the loop's first frame: for a small fix to the still after the loop was made (Oct 24:
Natsuki's face in the title loop, an already-held loop, with just an oval on her face).
"""
import argparse, subprocess
import numpy as np
from PIL import Image, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--size", default="1920x1072"); ap.add_argument("--box", action="append", default=[])
ap.add_argument("--oval", action="append", default=[])
ap.add_argument("--feather", type=float, default=28); ap.add_argument("--crf", default="20")
ap.add_argument("--still", default=None)
a = ap.parse_args()
W, H = map(int, a.size.split("x"))
m = Image.new("L", (W, H), 0)
px = np.zeros((H, W), np.uint8)
for b in a.box:
    x0, y0, x1, y1 = map(float, b.split(","))
    px[int(y0 * H):int(y1 * H), int(x0 * W):int(x1 * W)] = 255
yy, xx = np.mgrid[0:H, 0:W]
for o in a.oval:
    cx, cy, rx, ry = map(float, o.split(","))
    px[((xx - cx * W) / (rx * W)) ** 2 + ((yy - cy * H) / (ry * H)) ** 2 <= 1] = 255
mask = np.array(Image.fromarray(px).filter(ImageFilter.GaussianBlur(a.feather))).astype(np.float32)[..., None] / 255
still = np.asarray(Image.open(a.still).convert("RGB").resize((W, H), Image.LANCZOS), np.float32) if a.still else None
dec = subprocess.Popen(["ffmpeg", "-nostdin", "-v", "error", "-i", a.inp, "-vf", f"scale={W}:{H}:flags=lanczos", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "24", "-i", "-",
                        "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", a.crf, "-preset", "slow", "-movflags", "+faststart", "-an", a.out], stdin=subprocess.PIPE)
first, n = None, 0
while True:
    buf = dec.stdout.read(W * H * 3)
    if len(buf) < W * H * 3:
        break
    f = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
    if first is None:
        first = f if still is None else still
    enc.stdin.write((mask * first + (1 - mask) * f).round().astype(np.uint8).tobytes()); n += 1
enc.stdin.close(); enc.wait(); dec.wait()
print(f"{n} frames -> {a.out}")
