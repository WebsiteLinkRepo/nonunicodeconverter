from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
hmtx = font['hmtx']
cmap = font.getBestCmap()

# Find all glyphs that look like reph or top matras
for c, name in sorted(cmap.items()):
    if name in glyf:
        glyph = glyf[name]
        if hasattr(glyph, 'yMax') and glyph.yMax > 650:
            width = hmtx[name][0]
            print(f"Char {hex(c)} ({name}): width={width}, xMin={getattr(glyph, 'xMin', 0)}, xMax={getattr(glyph, 'xMax', 0)}, yMin={getattr(glyph, 'yMin', 0)}, yMax={getattr(glyph, 'yMax', 0)}")
