from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF04E, 0xF04B]:
    glyph = glyf[cmap.get(c)]
    print(f"Char {hex(c)}: yMin {getattr(glyph, 'yMin', '?')}, yMax {getattr(glyph, 'yMax', '?')}")
