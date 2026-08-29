from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF0EE]:
    glyph_name = cmap.get(c)
    glyph = glyf[glyph_name]
    print(f"yMin {glyph.yMin}, yMax {glyph.yMax}")
