from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF0D1, 0xF0D2, 0xF0F3, 0xF0F7]:
    glyph = glyf[cmap.get(c)]
    print(f"Char {hex(c)}: yMin {getattr(glyph, 'yMin', '?')}, yMax {getattr(glyph, 'yMax', '?')}, xMin {getattr(glyph, 'xMin', '?')}, xMax {getattr(glyph, 'xMax', '?')}")
