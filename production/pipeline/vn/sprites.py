"""Finish VN sprites from bria cutouts: one shared crop per character set (so expressions don't jump),
clean the alpha edge, scale to 1800 px tall, save .webp.
Usage: python3 sprites.py OUTDIR file1.png file2.png ...  (files of one set: same character + outfit)"""
import sys, numpy as np
from PIL import Image
out, files = sys.argv[1], sys.argv[2:]
ims = [Image.open(f).convert('RGBA') for f in files]
boxes = []
for im in ims:
    a = np.array(im)[..., 3]
    ys, xs = np.where(a > 24)
    boxes.append((xs.min(), ys.min(), xs.max(), ys.max()))
    print(f"{files[len(boxes)-1].split('/')[-1]:34s} bbox {boxes[-1]}")
x0 = min(b[0] for b in boxes); y0 = min(b[1] for b in boxes); x1 = max(b[2] for b in boxes); y1 = max(b[3] for b in boxes)
pad = 6
H = ims[0].height
box = (max(0, x0 - pad), max(0, y0 - pad), min(ims[0].width, x1 + pad), H)  # bottom edge stays the frame edge
for f, im in zip(files, ims):
    c = im.crop(box)
    arr = np.array(c); al = arr[..., 3].astype(float)
    al[al < 10] = 0                     # drop faint halo specks
    arr[..., 3] = al.astype(np.uint8)
    c = Image.fromarray(arr)
    s = 1800 / c.height
    c = c.resize((round(c.width * s), 1800), Image.LANCZOS)
    name = f.split('/')[-1].rsplit('.', 1)[0]
    c.save(f"{out}/{name}.webp", 'WEBP', quality=90, method=6)
print('crop', box)
