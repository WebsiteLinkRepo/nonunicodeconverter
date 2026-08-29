from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
glyph = glyf[cmap.get(0xF04B)]
coords = glyph.getCoordinates(glyf)[0]
for x, y in coords:
    if y < -50:
        print(f"Tail coords: ({x}, {y})")
