from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen

font = TTFont("/home/samuelvictor/Downloads/Shreelipi_4642.TTF")
glyph_set = font.getGlyphSet()
cmap = font['cmap'].getBestCmap()

def get_shirorekha_y(char_str):
    res = []
    for c in char_str:
        glyph_name = cmap.get(ord(c))
        if not glyph_name:
            res.append((c, "NO_GLYPH"))
            continue
        g = glyph_set[glyph_name]
        pen = RecordingPen()
        g.draw(pen)
        # Find maximum y coords in the path
        max_y = -99999
        min_y = 99999
        top_y_points = []
        for op, points in pen.value:
            for pt in points:
                if len(pt) == 2:
                    if pt[1] > max_y:
                        max_y = pt[1]
                    if pt[1] > 400: # points in the top bar region
                        top_y_points.append(pt[1])
        res.append((c, ord(c), glyph_name, max_y, sorted(list(set(top_y_points)))))
    return res

chars = "_hmÌñg`1234567890H$Ijklmnop"
for r in get_shirorekha_y(chars):
    print(r)
