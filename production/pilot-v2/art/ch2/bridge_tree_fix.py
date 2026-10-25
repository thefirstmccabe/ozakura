"""Oct 24 on-model fix for bg_bridge_dusk: the distant Ozakura was too big and too crisp (wider than a nearer cherry tree).
Removes it from the NB plate (difference against the pilot plate, which has no tree, colour-matched), pastes it back at
SCALE (0.6) anchored at its base with lower contrast and a light blur, then redraws the three power lines in front of it
as straight fits of the wires either side.

  python3 bridge_tree_fix.py BEFORE_MASTER.webp OUT.png [SCALE]
BEFORE_MASTER is the 93ee18c master:  git show 93ee18c:production/pilot-v2/art/masters/bg_bridge_dusk.webp > before.webp
Run from the repo root (it reads the pilot plate img/bg/bg_bridge_dusk.webp)."""
from PIL import Image
import numpy as np, cv2, sys
M=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(np.float32)
P=np.asarray(Image.open('img/bg/bg_bridge_dusk.webp').convert('RGB').resize((2752,1536),Image.LANCZOS)).astype(np.float32)
x0,y0,x1,y1=1680,330,2000,560
a=M[y0:y1,x0:x1].copy(); b=P[y0:y1,x0:x1].copy()
g=cv2.cvtColor(a.astype(np.uint8),cv2.COLOR_RGB2GRAY)
wire=cv2.morphologyEx(g,cv2.MORPH_BLACKHAT,np.ones((9,9),np.uint8))>18
# color-match pilot to master on the area away from the tree box
far=np.ones(a.shape[:2],bool); far[40:200,60:270]=False; far&=~wire
gain=a[far].mean(0)/np.maximum(b[far].mean(0),1); bm=np.clip(b*gain,0,255)
d=np.abs(cv2.GaussianBlur(a,(0,0),1.5)-cv2.GaussianBlur(bm,(0,0),1.5)).sum(2)
tree=(d>45); tree[:, :40]=False; tree[:, 280:]=False; tree[:30]=False; tree[200:]=False
tree=cv2.morphologyEx(tree.astype(np.uint8),cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(tree); k=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); tree=(lab==k).astype(np.uint8)
# fill holes
ff=tree.copy(); h,w=ff.shape; m2=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,m2,(0,0),1); tree=(tree|(1-ff)).astype(bool)
ys,xs=np.where(tree); print('tree bbox',xs.min()+x0,xs.max()+x0,ys.min()+y0,ys.max()+y0)
treeD=cv2.dilate(tree.astype(np.uint8),np.ones((9,9),np.uint8)).astype(np.float32)
soft=cv2.GaussianBlur(treeD,(0,0),3)[...,None]
base=a*(1-soft)+bm*soft
# tree sprite from the master (pink pixels only), wires inpainted out
t_img=cv2.inpaint(a.astype(np.uint8),(wire&tree).astype(np.uint8)*255,3,cv2.INPAINT_TELEA).astype(np.float32)
lum=t_img.mean(2); pink=(lum>50)&tree
alpha=cv2.GaussianBlur(pink.astype(np.float32),(0,0),1.2)
bx0,bx1,by0,by1=xs.min(),xs.max()+1,ys.min(),ys.max()+1
spr=t_img[by0:by1,bx0:bx1]; al=alpha[by0:by1,bx0:bx1]
mean=spr[al>0.5].mean(0); spr=mean*0.85+(spr-mean)*0.85
sc=float(sys.argv[3]) if len(sys.argv)>3 else 0.6
nw,nh=int(round(spr.shape[1]*sc)),int(round(spr.shape[0]*sc))
spr=cv2.GaussianBlur(cv2.resize(spr,(nw,nh),interpolation=cv2.INTER_AREA),(0,0),0.6)
al=cv2.GaussianBlur(cv2.resize(al,(nw,nh),interpolation=cv2.INTER_AREA),(0,0),1.0)*0.9
cx=(bx0+bx1)/2; px0=int(round(cx-nw/2)); py0=by1-nh
out=base.copy(); r=out[py0:py0+nh,px0:px0+nw]; out[py0:py0+nh,px0:px0+nw]=r*(1-al[...,None])+spr*al[...,None]
lum0=a.mean(2)
zone=cv2.dilate(treeD.astype(np.uint8),np.ones((15,15),np.uint8)).astype(bool)
bh0=cv2.morphologyEx(g,cv2.MORPH_BLACKHAT,np.ones((9,9),np.uint8))
wr=(bh0>5)&~zone
yy,xx=np.where(wr); col=np.median(a[wr],0)
# candidate lines: slope -0.45..-0.05, scan intercepts at x=160; keep peaks with strong support
cands=[]
for k in np.arange(-0.40,-0.28,0.002):
    c=yy-k*(xx-160)
    h,e=np.histogram(c,bins=np.arange(0,231,1.0))
    for i in np.where(h>=60)[0]: cands.append((h[i],k,e[i]+0.5))
cands.sort(reverse=True); kept=[]
for n_,k,c in cands:
    sel=np.abs(yy-(k*(xx-160)+c))<1.5
    if (xx[sel]<60).sum()<15 or (xx[sel]>265).sum()<15: continue
    if all(abs(c-c2)>5 for _,k2,c2 in kept): kept.append((n_,k,c))
    if len(kept)>=3: break
draw=np.zeros(a.shape[:2],np.float32)
for n_,k,c in kept:
    sel=np.abs(yy-(k*(xx-160)+c))<1.5
    p=np.polyfit(xx[sel],yy[sel],1)
    print('wire',round(p[0],3),round(np.polyval(p,160),1),int(sel.sum()), 'x range',xx[sel].min(),xx[sel].max())
    xs_=np.arange(0,a.shape[1]); ys_=np.polyval(p,xs_)
    tmp=np.zeros(a.shape[:2],np.uint8)
    cv2.polylines(tmp,[np.stack([xs_*8,ys_*8],1).astype(np.int32)],False,255,1,lineType=cv2.LINE_AA,shift=3)
    draw=np.maximum(draw,cv2.GaussianBlur(tmp/255.,(0,0),0.5)*1.4)
draw=np.clip(draw,0,1)
zs=cv2.GaussianBlur(zone.astype(np.float32),(0,0),2)
wa=(draw*zs)[...,None]
out=out*(1-wa)+col*wa
R=M.copy(); R[y0:y1,x0:x1]=out
img=Image.fromarray(np.clip(R,0,255).astype(np.uint8)); img.save(sys.argv[2])
print('new w',nw,'build w',round(nw*2400/2752))
