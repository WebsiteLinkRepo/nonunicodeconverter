from fontTools.ttLib import TTFont

font = TTFont('/home/samuelvictor/Downloads/Shreelipi_4642.TTF')
cmap = font['cmap'].getBestCmap()
glyf = font['glyf']
hmtx = font['hmtx']

# Check glyph 0x9D (shirorekha extension)
ext_code = 0x9D
gname_ext = cmap[ext_code]
g_ext = glyf[gname_ext]
adv_ext, lsb_ext = hmtx[gname_ext]
print(f'Extension glyph 0x9D: {gname_ext}, adv={adv_ext}, lsb={lsb_ext}, xMin={g_ext.xMin}, xMax={g_ext.xMax}, yMin={g_ext.yMin}, yMax={g_ext.yMax}')

# Check ALL glyphs that have yMax=500 and narrow widths (potential shirorekha helpers)
print("\nAll narrow glyphs with yMax near 500:")
for code, gname in sorted(cmap.items()):
    try:
        g = glyf[gname]
        adv, lsb = hmtx[gname]
        if g.yMax >= 490 and adv < 150:
            ch = chr(code) if code < 256 else hex(code)
            print(f'  code={hex(code)} char={repr(ch)} name={gname} adv={adv}, lsb={lsb}, xMin={g.xMin}, xMax={g.xMax}, yMin={g.yMin}, yMax={g.yMax}')
    except:
        pass

# Check all glyphs with the shirorekha line (where glyph has y contours near 420-500 range)
# and their advance widths, focusing on gap patterns
print("\nGlyphs sorted by advance width:")
for code, gname in sorted(cmap.items()):
    try:
        g = glyf[gname]
        adv, lsb = hmtx[gname]
        if g.yMax >= 490 and g.yMax <= 510:
            ch = chr(code) if code < 256 else hex(code)
            gap = adv - g.xMax
            print(f'  code={hex(code)} char={repr(ch)} name={gname} adv={adv} xMax={g.xMax} gap={gap}')
    except:
        pass
