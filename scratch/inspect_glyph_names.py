from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font = TTFont(font_path)
cmap = font.getBestCmap()

for code, name in sorted(cmap.items()):
    # print code, name, and char representation
    print(f"0x{code:04X} ({code:4d}) : {name:20s}")
