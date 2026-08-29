from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF07A, 0xF07B, 0xF0F5, 0xF0F8, 0xF0E5]:
    glyph = glyf[cmap.get(c)]
    print(f"Char {hex(c)}: contours {glyph.numberOfContours}, xMin {getattr(glyph, 'xMin', '?')}, xMax {getattr(glyph, 'xMax', '?')}")
