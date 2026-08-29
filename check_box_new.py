from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF04E, 0xF079, 0xF0E7, 0xF0AA]:
    glyph = glyf[cmap.get(c)]
    print(f"{hex(c)}: xMin {getattr(glyph, 'xMin', '?')}, xMax {getattr(glyph, 'xMax', '?')}")
