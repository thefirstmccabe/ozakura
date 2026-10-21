"""Paste an edit back over its original only where it changed inside a box: mask = |edit-orig| > T inside the box,
closed and dilated, holes filled, feathered. Usage: region_composite.py ORIG EDIT OUT x0 y0 x1 y1 [T] [GROW] [FEATHER]"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
orig, edit, out = sys.argv[1:4]; x0, y0, x1, y1 = map(float, sys.argv[4:8])
T = float(sys.argv[8]) if len(sys.argv) > 8 else 30; grow = int(sys.argv[9]) if len(sys.argv) > 9 else 24; fe = int(sys.argv[10]) if len(sys.argv) > 10 else 18
O = Image.open(orig).convert('RGB'); E = Image.open(edit).convert('RGB').resize(O.size, Image.LANCZOS)
o = np.array(O).astype(int); e = np.array(E).astype(int); H, W = o.shape[:2]
d = np.abs(e - o).max(2) > T
box = np.zeros_like(d); box[int(y0*H):int(y1*H), int(x0*W):int(x1*W)] = True
m = d & box
m = ndimage.binary_closing(m, iterations=6)
m = ndimage.binary_opening(m, iterations=2)
lab, n = ndimage.label(m)
if n:
    sizes = ndimage.sum(m, lab, range(1, n + 1)); keep = np.isin(lab, 1 + np.where(sizes > 400)[0]); m = keep
m = ndimage.binary_fill_holes(m)
m = ndimage.binary_dilation(m, iterations=grow) & box
a = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(fe))
res = Image.composite(E, O, a); res.save(out)
A = np.array(a) > 8; ys, xs = np.where(A)
print(f"changed area x {xs.min()/W:.3f}-{xs.max()/W:.3f}, y {ys.min()/H:.3f}-{ys.max()/H:.3f}; {A.mean()*100:.1f}% of the frame")
outside = np.abs(np.array(res).astype(int) - o).max(2)[~A]
print("max change outside the mask:", outside.max())
