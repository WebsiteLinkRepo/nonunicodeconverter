from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen

# Dump ALL glyphs and their paths, looking for any 'म' variant
font = TTFont("/home/samuelvictor/Downloads/Shreelipi_4642.TTF")
glyph_set = font.getGlyphSet()
cmap = font["cmap"].getBestCmap()

# Iterate over all glyphs in cmap
ma_variants = []
for code, name in cmap.items():
    g = glyph_set[name]
    pen = RecordingPen()
    g.draw(pen)

    # Check if width is approx 500-530 (standard ma width)
    # Check if Y-bounds are near 420-500
    ys = []
    for op, points in pen.value:
        for pt in points:
            if len(pt) == 2:
                ys.append(pt[1])

    if g.width > 480 and g.width < 550 and any(y >= 490 for y in ys):
        ma_variants.append((chr(code) if code < 256 else hex(code), name, g.width))

print(f"Found {len(ma_variants)} 'ma'-like candidates:")
for v in ma_variants:
    print(v)
