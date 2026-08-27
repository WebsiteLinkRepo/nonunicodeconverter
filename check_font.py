import sys
from fontTools.ttLib import TTFont

font = TTFont('./dist/AnuSM main/ttf/PRIYAANK.TTF')
cmap = font.getBestCmap()
for k, v in cmap.items():
    print(f"Char: {chr(k)} (Code: {k}) -> Glyph: {v}")
