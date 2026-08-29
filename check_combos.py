from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
cmap = font.getBestCmap()
# Print all glyphs that have advance width > 0
for c in range(0xF020, 0xF0FF):
    glyph_name = cmap.get(c)
    if glyph_name:
        print(f"{hex(c)}: {glyph_name}")
