from fontTools.ttLib import TTFont
font = TTFont('public/SHREE-TEL-web.ttf')
if 'kern' in font:
    kern_table = font['kern']
    for subtable in kern_table.kernTables:
        print(f"Format: {subtable.format}")
        # let's just see if space is involved in kerning
        space_glyph = font.getBestCmap().get(ord(' '))
        for (left, right), val in subtable.kernTable.items():
            if left == space_glyph or right == space_glyph:
                print(f"Kern pairs involving space: {left} {right} -> {val}")
else:
    print("No kern table")
