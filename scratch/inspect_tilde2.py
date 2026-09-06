from fontTools.ttLib import TTFont
font = TTFont('public/SHREE-TEL-web.ttf')
cmap = font.getBestCmap()
print(f"Cmap for ˜ ({0x02DC}): {cmap.get(0x02DC)}")
