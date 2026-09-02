import json
from fontTools.ttLib import TTFont

font = TTFont("/home/samuelvictor/Downloads/Shreelipi_4642.TTF")
cmap = font["cmap"].getBestCmap()

glyphs = {}
for code, name in sorted(cmap.items()):
    char = chr(code) if code < 65536 else f"\\U{code:08x}"
    glyphs[code] = {
        "hex": f"0x{code:04x}",
        "char": chr(code) if code < 65536 else "",
        "name": name
    }

with open("scratch/font_cmap.json", "w", encoding="utf-8") as f:
    json.dump(glyphs, f, indent=2, ensure_ascii=False)

print(f"Total mapped characters in font: {len(glyphs)}")
