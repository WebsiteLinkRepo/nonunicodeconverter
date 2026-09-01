from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen

font = TTFont("/home/samuelvictor/Downloads/Shreelipi_4642.TTF")
glyph_set = font.getGlyphSet()
cmap = font["cmap"].getBestCmap()

# Find all glyphs that look like 'म' or are related to 'म'
# Let's inspect 0x5f, 0xe5, 0x2018
for code in [0x5f, 0xe5, 0x2018]:
    name = cmap.get(code)
    print(f"Code: 0x{code:02x} ({chr(code) if code < 256 else '?'}) -> name: {name}")
    if name:
        g = glyph_set[name]
        pen = RecordingPen()
        g.draw(pen)
        # Check shirorekha coordinates
        ys = []
        for op, points in pen.value:
            for pt in points:
                if len(pt) == 2 and 400 <= pt[1] <= 550:
                    ys.append(pt[1])
        print(f"  Width: {g.width}, Y-values around top: {sorted(list(set(ys)))}")
