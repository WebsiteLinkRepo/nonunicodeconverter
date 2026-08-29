from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF079, 0xF0EB]:
    glyph = glyf[cmap.get(c)]
    print(f"Char {hex(c)}: yMax {getattr(glyph, 'yMax', '?')}")
