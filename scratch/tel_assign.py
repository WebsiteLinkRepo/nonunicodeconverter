#!/usr/bin/env python3
"""Globally consistent 1-to-1 assignment of the 36 Telugu consonants to SHREE-TEL forms.
Confusable pairs (మ/య, న/స, ప/వ, ఖ/ఘ, జ/ఙ) get resolved by elimination rather than
by independent nearest-neighbour, which is what made per-letter matching unreliable."""
import sys
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

SHP = "public/SHREE-TEL.ttf"
SH = ImageFont.truetype(SHP, 110)
REFS = ["/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"]
try:
    import subprocess
    for name in ("NotoSerifTelugu", "Gautami", "Pothana", "Ramabhadra", "Suranna"):
        o = subprocess.run(["fc-match","-f","%{file}",name], capture_output=True, text=True).stdout.strip()
        if o and o not in REFS and "Telugu" in o: REFS.append(o)
except Exception: pass
print("refs:", REFS, file=sys.stderr)
RFONTS = [ImageFont.truetype(p, 110) for p in REFS]

CONS = list("కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ") + ["క్ష"]

f = TTFont(SHP); cmap=f.getBestCmap(); gs=f.getGlyphSet(); hm=f['hmtx']
noncomb=[]
for c in sorted(cmap):
    g=cmap[c]; bp=BoundsPen(gs); gs[g].draw(bp); b=bp.bounds
    if b is None: continue
    if hm[g][0] <= 60 and b[0] < 0: continue
    noncomb.append(c)

H, CV = 60, (170, 120)
def ink(font, t):
    img = Image.new("L",(760,480),255)
    ImageDraw.Draw(img).text((120,120), t, font=font, fill=0)
    bb = Image.eval(img, lambda p:255-p).getbbox()
    if not bb: return None
    cr = img.crop(bb); w,h = cr.size
    if h==0: return None
    cr = cr.resize((max(1,int(round(w*H/h))), H), Image.LANCZOS)
    px=cr.load()
    return [(x,y) for y in range(H) for x in range(cr.size[0]) if px[x,y]<150] or None
def dmap(pts):
    W,Hh=CV; BIG=10**6
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

# candidate forms
forms=[]
for c in noncomb:
    for suf,tag in ((None,""),(0xe6,"+e6")):
        t = chr(c) + (chr(suf) if suf else "")
        p = ink(SH, t)
        if p: forms.append((f"{c:x}{tag}", p, dmap(p)))
print(len(forms), "forms", file=sys.stderr)

# reference points (average cost across available reference fonts)
refs=[]
for ch in CONS:
    rs=[]
    for rf in RFONTS:
        p = ink(rf, ch)
        if p: rs.append((p, dmap(p)))
    refs.append((ch, rs))

M={}
for ci,(ch,rs) in enumerate(refs):
    row=[]
    for fi,(lbl,p,d) in enumerate(forms):
        best=[]
        for rp,rd in rs:
            best.append(min(cost(rp,d,p,rd,dx) for dx in (-5,0,5)))
        row.append(sum(best)/len(best))
    M[ci]=row
    print("row done", ch, file=sys.stderr)

# greedy assignment then improve by pairwise swaps
import itertools
order = sorted(range(len(CONS)), key=lambda i: min(M[i]))
assign={}; used=set()
for ci in order:
    b=min((v,fi) for fi,v in enumerate(M[ci]) if fi not in used)
    assign[ci]=b[1]; used.add(b[1])
improved=True
while improved:
    improved=False
    for a,b in itertools.combinations(range(len(CONS)),2):
        fa,fb=assign[a],assign[b]
        if M[a][fa]+M[b][fb] > M[a][fb]+M[b][fa] + 1e-9:
            assign[a],assign[b]=fb,fa; improved=True
for ci in range(len(CONS)):
    fi=assign[ci]
    print(f"{CONS[ci]}\t{forms[fi][0]}\t{M[ci][fi]:.2f}")
