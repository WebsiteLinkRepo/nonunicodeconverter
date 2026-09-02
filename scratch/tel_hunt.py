#!/usr/bin/env python3
"""Exhaustive search: single glyphs + base+combining pairs, IoU prefilter then chamfer."""
import sys
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

SHP = "public/SHREE-TEL.ttf"
SH = ImageFont.truetype(SHP, 110)
RF = ImageFont.truetype("/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf", 110)
f = TTFont(SHP); cmap = f.getBestCmap(); gs = f.getGlyphSet(); hmtx = f['hmtx']
codes = sorted(cmap)
comb, base = [], []
for c in codes:
    g = cmap[c]; bp = BoundsPen(gs); gs[g].draw(bp)
    adv = hmtx[g][0]; b = bp.bounds
    if b is None: continue
    if adv <= 60 and b[0] < 0: comb.append(c)
    else: base.append(c)

N = 40
def bmp(font, t):
    img = Image.new("L", (700, 460), 255)
    ImageDraw.Draw(img).text((110, 110), t, font=font, fill=0)
    bb = Image.eval(img, lambda p: 255-p).getbbox()
    if not bb: return None
    cr = img.crop(bb); w, h = cr.size
    s = N / max(w, h)
    nw, nh = max(1,int(w*s)), max(1,int(h*s))
    cr = cr.resize((nw, nh), Image.LANCZOS)
    can = Image.new("L", (N, N), 255)
    can.paste(cr, ((N-nw)//2, (N-nh)//2))
    px = can.load()
    return frozenset((x,y) for y in range(N) for x in range(N) if px[x,y] < 150)

def iou(a, b):
    return len(a & b) / len(a | b) if (a or b) else 0.0

cands = {}
for b in base:
    s = chr(b)
    m = bmp(SH, s)
    if m: cands["%x" % b] = (s, m)
    for c in comb:
        s2 = chr(b) + chr(c)
        m2 = bmp(SH, s2)
        if m2: cands["%x+%x" % (b, c)] = (s2, m2)
print(f"{len(cands)} candidates", file=sys.stderr)

# chamfer refine (reuse tel_match style, smaller canvas)
H, CV = 56, (150, 110)
def ink(font, t):
    img = Image.new("L",(700,460),255)
    ImageDraw.Draw(img).text((110,110), t, font=font, fill=0)
    bb = Image.eval(img, lambda p:255-p).getbbox()
    if not bb: return None
    cr = img.crop(bb); w,h = cr.size
    if h == 0: return None
    cr = cr.resize((max(1,int(round(w*H/h))), H), Image.LANCZOS)
    px = cr.load()
    return [(x,y) for y in range(H) for x in range(cr.size[0]) if px[x,y]<150] or None
def dmap(pts):
    W,Hh = CV; BIG=10**6
    d=[[BIG]*W for _ in range(Hh)]
    for x,y in pts:
        if 0<=x<W and 0<=y<Hh: d[y][x]=0
    for y in range(Hh):
        for x in range(W):
            v=d[y][x]
            if y: v=min(v,d[y-1][x]+3)
            if x: v=min(v,d[y][x-1]+3)
            if y and x: v=min(v,d[y-1][x-1]+4)
            if y and x+1<W: v=min(v,d[y-1][x+1]+4)
            d[y][x]=v
    for y in range(Hh-1,-1,-1):
        for x in range(W-1,-1,-1):
            v=d[y][x]
            if y+1<Hh: v=min(v,d[y+1][x]+3)
            if x+1<W: v=min(v,d[y][x+1]+3)
            if y+1<Hh and x+1<W: v=min(v,d[y+1][x+1]+4)
            if y+1<Hh and x: v=min(v,d[y+1][x-1]+4)
            d[y][x]=v
    return d
def cost(a,bd,b,ad,dx):
    W,Hh=CV; s1=n1=0
    for x,y in a:
        xx=x+dx
        if 0<=xx<W and 0<=y<Hh: s1+=bd[y][xx]; n1+=1
    s2=n2=0
    for x,y in b:
        xx=x-dx
        if 0<=xx<W and 0<=y<Hh: s2+=ad[y][xx]; n2+=1
    return 10**6 if not n1 or not n2 else 0.5*(s1/n1+s2/n2)

for target in sys.argv[1:]:
    rm = bmp(RF, target); rp = ink(RF, target); rd = dmap(rp)
    pre = sorted(((iou(rm, m), k) for k,(s,m) in cands.items()), reverse=True)[:60]
    out=[]
    for _, k in pre:
        p = ink(SH, cands[k][0])
        if not p: continue
        out.append((min(cost(rp, dmap(p), p, rd, dx) for dx in (-4,0,4)), k))
    out.sort()
    print(target, " ".join(f"{k}({s:.1f})" for s,k in out[:8]))
