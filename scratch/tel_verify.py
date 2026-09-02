#!/usr/bin/env python3
"""Telugu Shree-Lipi verification renders.

Writes two sheets into scratch/:
  tel_compare.png  - input Unicode syllable (reference font) vs. current
                     converter output (SHREE-TEL), side by side, large.
  tel_allglyphs.png - every cmap code in SHREE-TEL, large, for identifying
                     which code actually holds ఋ / ౠ / sunna / visarga.
"""
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

SHREE = "public/SHREE-TEL.ttf"
SIZE = 60

# ---- find a Unicode Telugu reference font -------------------------------
REF_CANDIDATES = [
    "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf",
    "/usr/share/fonts/TTF/NotoSansTelugu-Regular.ttf",
    "/usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf",
    "/usr/share/fonts/noto/NotoSerifTelugu-Regular.ttf",
    "/usr/share/fonts/gsfonts/Gargi.ttf",
]
ref_path = next((p for p in REF_CANDIDATES if os.path.exists(p)), None)
if ref_path is None:
    try:
        out = subprocess.run(["fc-match", "-f", "%{file}", "Telugu"],
                             capture_output=True, text=True, timeout=10).stdout.strip()
        if out and os.path.exists(out):
            ref_path = out
    except Exception:
        pass
print("reference font:", ref_path)

shree = ImageFont.truetype(SHREE, SIZE)
ref = ImageFont.truetype(ref_path, SIZE) if ref_path else None
label = ImageFont.load_default(15)

# ---- sheet 1: input vs current converter output -------------------------
# (converter output strings are produced by the node one-liner in
#  scratch/tel_convert.mjs and passed in via scratch/tel_pairs.txt)
PAIRS_FILE = "scratch/tel_pairs.txt"
if os.path.exists(PAIRS_FILE):
    pairs = []
    with open(PAIRS_FILE, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or "\t" not in line:
                continue
            uni, legacy = line.split("\t", 1)
            pairs.append((uni, legacy))

    CW, CH = 460, 110
    img = Image.new("RGB", (CW, CH * len(pairs) + 40), "white")
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Unicode input   ->   SHREE-TEL output", fill="blue", font=label)
    for i, (uni, legacy) in enumerate(pairs):
        y = 40 + i * CH
        d.line([(0, y), (CW, y)], fill="#ddd")
        d.text((10, y + 6), f"U+{ord(uni[0]):04X}", fill="blue", font=label)
        if ref:
            d.text((90, y + 20), uni, fill="black", font=ref)
        d.text((215, y + 40), "->", fill="blue", font=label)
        d.text((260, y + 20), legacy, fill="black", font=shree)
        d.text((260, y + 88), " ".join(hex(ord(c)) for c in legacy), fill="green", font=label)
    img.save("scratch/tel_compare.png")
    print("wrote scratch/tel_compare.png", len(pairs), "pairs")
else:
    print("skip tel_compare.png (no", PAIRS_FILE + ")")

# ---- sheet 2: every cmap code, large -----------------------------------
from fontTools.ttLib import TTFont
codes = sorted(TTFont(SHREE).getBestCmap())
COLS, CW, CH = 10, 130, 130
rows = (len(codes) + COLS - 1) // COLS
img = Image.new("RGB", (COLS * CW, rows * CH), "white")
d = ImageDraw.Draw(img)
for i, c in enumerate(codes):
    x, y = (i % COLS) * CW, (i // COLS) * CH
    d.rectangle([x, y, x + CW - 1, y + CH - 1], outline="#ccc")
    d.text((x + 5, y + 4), f"{c:#04x} {chr(c)!r}", fill="blue", font=label)
    d.text((x + 18, y + 30), chr(c), fill="black", font=shree)
img.save("scratch/tel_allglyphs.png")
print("wrote scratch/tel_allglyphs.png", len(codes), "glyphs")
