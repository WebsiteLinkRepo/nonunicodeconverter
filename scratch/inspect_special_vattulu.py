from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

# Let's inspect what glyph is rendered by these codes when following 'a'
codes_to_test = [
    (0xA7, '§', '0xA7 section (da base?)'),
    (0xAA, 'ª', '0xAA ordfeminine (ta/da vattu?)'),
    (0xA6, '¦', '0xA6 brokenbar (tha vattu?)'),
    (0xDD, 'Ý', '0xDD Yacute (na vattu?)'),
    (0xDE, 'Þ', '0xDE Thorn (sa vattu?)'),
    (0xE5, 'å', '0xE5 aring (ha/La vattu?)'),
    (0xC3, 'Ã', '0xC3 Atilde (La base/vattu?)'),
    (0x160, 'Š', '0x160 Scaron (Na vattu?)'),
    (0x161, 'š', '0x161 scaron (ma vattu?)'),
    (0x178, 'Ÿ', '0x178 Ydieresis (ya vattu?)'),
    (0x2013, '–', '0x2013 endash (ra vattu?)'),
    (0x2018, '‘', '0x2018 quoteleft (?)'),
    (0x2019, '’', '0x2019 quoteright (?)'),
    (0x201C, '“', '0x201C quotedblleft (?)'),
    (0x201D, '”', '0x201D quotedblright (?)'),
    (0x2020, '†', '0x2020 dagger (ti combo)'),
    (0x2021, '‡', '0x2021 daggerdbl (?)'),
    (0x2022, '•', '0x2022 bullet (?)'),
    (0x2026, '…', '0x2026 ellipsis (?)'),
    (0x2039, '‹', '0x2039 guilsinglleft (?)'),
    (0x203A, '›', '0x203A guilsinglright (?)'),
    (0x00A8, '¨', '0x00A8 dieresis (di combo)'),
    (0x00A9, '©', '0x00A9 copyright (dee combo)'),
    (0x00A4, '¤', '0x00A4 currency (dhi combo)'),
    (0x00A5, '¥', '0x00A5 yen (dhee combo)')
]

img = Image.new('RGB', (800, len(codes_to_test) * 45 + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for code, ch, desc in codes_to_test:
    draw.text((10, y), desc, fill=(0,0,120), font=label_font)
    try:
        # Standalone
        draw.text((350, y-5), f"standalone: {ch}", fill=(0,0,0), font=shree_font)
        # With 'a' prefix
        draw.text((550, y-5), f"with 'a': a{ch}", fill=(180,0,0), font=shree_font)
    except:
        pass
    y += 45

img.save('scratch/inspect_codes.png')
print("Saved scratch/inspect_codes.png")
