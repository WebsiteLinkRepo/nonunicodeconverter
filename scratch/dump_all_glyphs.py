from fontTools.ttLib import TTFont
import json

font = TTFont('/home/samuelvictor/Downloads/Shreelipi_4642.TTF')
cmap = font['cmap'].getBestCmap()
glyf = font['glyf']
hmtx = font['hmtx']

entries = []
for code, name in sorted(cmap.items()):
    try:
        g = glyf[name]
        adv, lsb = hmtx[name]
        ch = chr(code) if code < 256 else hex(code)
        entries.append({
            "code": code,
            "hex": hex(code),
            "char": ch,
            "name": name,
            "adv": adv,
            "lsb": lsb,
            "xMin": g.xMin,
            "xMax": g.xMax,
            "yMin": g.yMin,
            "yMax": g.yMax
        })
    except Exception as e:
        pass

with open('scratch/all_font_glyphs.json', 'w') as f:
    json.dump(entries, f, indent=2)

print(f"Dumped {len(entries)} glyphs to scratch/all_font_glyphs.json")
