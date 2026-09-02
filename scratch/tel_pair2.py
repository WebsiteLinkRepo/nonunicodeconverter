#!/usr/bin/env python3
import sys, importlib.util
spec = importlib.util.spec_from_file_location("m", "scratch/tel_match.py")
# reuse helpers without running main: inline instead
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
SH = ImageFont.truetype("public/SHREE-TEL.ttf", 120)
RF = ImageFont.truetype("/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf", 120)
H, CANVAS = 56, (150, 110)
def ink(font, t):
    img = Image.new("L", (600,400), 255)
    ImageDraw.Draw(img).text((80,90), t, font=font, fill=0)
    bb = Image.eval(img, lambda p:255-p).getbbox()
    if not bb: return None
    cr = img.crop(bb); w,h = cr.size
    if h==0: return None
    cr = cr.resize((max(1,int(round(w*H/h))), H), Image.LANCZOS)
    px = cr.load()
    return [(x,y) for y in range(H) for x in range(cr.size[0]) if px[x,y]<150] or None
def dmap(pts):
    W,Hh = CANVAS; BIG=10**6
    d=[[BIG]*W for _ in range(Hh)]
    for x,y in pts:
        if 0<=x<W and 0<=y<Hh: d[y][x]=0
    for y in range(Hh):
        for x in range(W):
            b=d[y][x]
            if y: b=min(b,d[y-1][x]+3)
            if x: b=min(b,d[y][x-1]+3)
            if y and x: b=min(b,d[y-1][x-1]+4)
            if y and x+1<W: b=min(b,d[y-1][x+1]+4)
            d[y][x]=b
    for y in range(Hh-1,-1,-1):
        for x in range(W-1,-1,-1):
            b=d[y][x]
            if y+1<Hh: b=min(b,d[y+1][x]+3)
            if x+1<W: b=min(b,d[y][x+1]+3)
            if y+1<Hh and x+1<W: b=min(b,d[y+1][x+1]+4)
            if y+1<Hh and x: b=min(b,d[y+1][x-1]+4)
            d[y][x]=b
    return d
def cost(a,bd,b,ad,dx):
    W,Hh=CANVAS; s1=n1=0
    for x,y in a:
        xx=x+dx
        if 0<=xx<W and 0<=y<Hh: s1+=bd[y][xx]; n1+=1
    s2=n2=0
    for x,y in b:
        xx=x-dx
        if 0<=xx<W and 0<=y<Hh: s2+=ad[y][xx]; n2+=1
    return 10**6 if not n1 or not n2 else 0.5*(s1/n1+s2/n2)

codes = sorted(TTFont("public/SHREE-TEL.ttf").getBestCmap())
target = sys.argv[1]
bases = [int(x,16) for x in sys.argv[2].split(',')]
rp = ink(RF, target); rd = dmap(rp)
out=[]
for b in bases:
    for c in codes:
        for combo in (chr(b)+chr(c), chr(b)+chr(c)+chr(0xe6)):
            p = ink(SH, combo)
            if not p: continue
            sc = min(cost(rp, dmap(p), p, rd, dx) for dx in (-4,0,4))
            lbl = "+".join(f"{ord(ch):x}" for ch in combo)
            out.append((sc,lbl))
out.sort()
print(target, " ".join(f"{l}({s:.1f})" for s,l in out[:10]))
