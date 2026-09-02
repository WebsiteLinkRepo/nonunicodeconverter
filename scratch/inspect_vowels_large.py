from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = "public/SHREE-TEL.ttf"
ttfont = TTFont(font_path)
cmap = ttfont.getBestCmap()
font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 14)

# Let's inspect codes:
# 0x41 to 0x4F (A to O)
# 0x60 to 0x7F
# 0xA0 to 0xFF
# 0x0100 to 0x2219

ranges = [
    ("0x40-0x4F", range(0x40, 0x50)),
    ("0x6D-0x7F", range(0x6D, 0x80)),
    ("0xA0-0xAF", range(0xA0, 0xB0)),
    ("0xB0-0xBF", range(0xB0, 0xC0)),
    ("0xC0-0xCF", range(0xC0, 0xD0)),
    ("0xD0-0xDF", range(0xD0, 0xE0)),
    ("0xE0-0xEF", range(0xE0, 0xF0)),
    ("0xF0-0xFF", range(0xF0, 0x100)),
    ("0x0152-0x2219", [0x152, 0x153, 0x160, 0x161, 0x178, 0x192, 0x2C6, 0x2DC, 0x2013, 0x2014, 0x2018, 0x2019, 0x201A, 0x201C, 0x201D, 0x2020, 0x2021, 0x2022, 0x2026, 0x2030, 0x2039, 0x203A, 0x2122, 0x2219])
]

img = Image.new('RGB', (1200, len(ranges) * 100 + 50), 'white')
draw = ImageDraw.Draw(img)

for r_idx, (title, codelist) in enumerate(ranges):
    y = r_idx * 100 + 20
    draw.text((10, y), title, fill='red', font=label_font)
    
    x = 120
    for code in codelist:
        if code in cmap:
            char_str = chr(code)
            hex_str = f"0x{code:02X}" if code <= 0xFF else f"0x{code:04X}"
            draw.text((x, y - 5), hex_str, fill='gray', font=label_font)
            draw.text((x, y + 18), char_str, fill='black', font=font)
            x += 65

img.save("scratch/inspect_vowels_large.png")
print("Saved to scratch/inspect_vowels_large.png")
