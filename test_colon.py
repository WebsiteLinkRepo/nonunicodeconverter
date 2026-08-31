import fontTools.ttLib as ttLib

font = ttLib.TTFont('public/AnuSM main/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()

def print_glyph_info(cp):
    name = cmap.get(cp)
    if not name:
        return
    g = glyf[name]
    num_contours = g.numberOfContours
    print(f"Codepoint {hex(cp)} ({name}): {num_contours} contours")
    
for cp in [0x3a, 0xf03a, 0x2d, 0xf02d]:
    print_glyph_info(cp)
