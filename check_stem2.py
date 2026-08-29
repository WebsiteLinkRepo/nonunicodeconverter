from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF04E]:
    glyph = glyf[cmap.get(c)]
    coords = glyph.getCoordinates(glyf)[0]
    print(coords)
