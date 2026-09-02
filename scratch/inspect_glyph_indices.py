from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font = TTFont(font_path)
glyf = font['glyf']
cmap = font.getBestCmap()

# Print glyph names and their cmap codepoints
for code, name in sorted(cmap.items()):
    if any(k in name.lower() for k in ['grave', 'acute', 'circumflex', 'tilde', 'dieresis', 'ring', 'cedilla', 'slash', 'thorn', 'eth', 'oe', 'scaron', 'dagger', 'quote', 'bullet', 'period', 'minus', 'plus', 'equal', 'asciicircum', 'underscore', 'lozenge', 'cent', 'sterling', 'currency', 'yen', 'brokenbar', 'section', 'copyright', 'ordfeminine', 'guillemot', 'logicalnot', 'registered', 'macron', 'degree', 'plusminus', 'twosuperior', 'threesuperior', 'mu', 'paragraph', 'periodcentered', 'onesuperior', 'ordmasculine', 'onequarter', 'onehalf', 'threequarters', 'questiondown', 'multiply', 'divide', 'germandbls']):
        print(f"0x{code:04X} ({code:4d}) -> {name:20s} ({repr(chr(code))})")
