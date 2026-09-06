from fontTools.ttLib import TTFont
import math
import sys

font = TTFont('public/SHREE-TEL-web.ttf')
cmap = font.getBestCmap()
# dump character to HTML
html = ["<html><head><meta charset='utf-8'><style>@font-face { font-family: 'Shree'; src: url('../public/SHREE-TEL-web.ttf') format('truetype'); } .shree { font-family: 'Shree'; font-size: 30px; border: 1px solid #ccc; display: inline-block; width: 50px; text-align: center; } .label { font-size: 10px; }</style></head><body>"]
for code, name in sorted(cmap.items()):
    c = chr(code)
    html.append(f"<div style='display:inline-block; margin: 2px;'><div class='shree'>&#x{code:x};</div><div class='label'>{hex(code)}</div></div>")
html.append("</body></html>")
with open('scratch/all_glyphs.html', 'w') as f:
    f.write("".join(html))
