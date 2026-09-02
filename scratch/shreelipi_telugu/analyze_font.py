import os
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()
glyf = tt['glyf']

print(f"Total cmap entries: {len(cmap)}")

entries = []
for code, name in sorted(cmap.items()):
    char = chr(code)
    g = glyf[name]
    num_contours = g.numberOfContours
    entries.append({
        'code': code,
        'hex': f"0x{code:02X}",
        'char': repr(char),
        'name': name,
        'contours': num_contours
    })

for e in entries:
    print(f"{e['hex']} ({e['code']:3d}) | {e['char']:6s} | {e['name']:25s} | contours: {e['contours']}")
