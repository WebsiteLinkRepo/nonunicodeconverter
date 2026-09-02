from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = "public/SHREE-TEL.ttf"
ttfont = TTFont(font_path)
cmap = ttfont.getBestCmap()
font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 14)

# Let's inspect potential Ru, Ruu, Anusvara, Visarga glyphs
# Look at 0x23, 0x24, 0x2B, 0x30..0x3F, 0x76, 0x77, 0x78, 0xC6, 0xC7, 0xC8, 0x0152, 0x0153, 0x0178, 0x0192, 0x02C6, 0x02DC, 0x2013, 0x2014, 0x2018, 0x2019, 0x201A, 0x201C, 0x201D, 0x2020, 0x2021, 0x2022, 0x2026, 0x2030, 0x2039, 0x203A, 0x2122, 0x2219

codes = [
    # Ru / Ruu candidates
    0x23, 0x2B, 0x76, 0x77, 0x78, 0x0178, 0x02DC, 0x2013, 0x2014, 0x2021, 0x2030,
    # Anusvara (Sunna / Full circle) candidates
    0x25, 0x30, 0x40, 0x75, 0x78, 0xB7, 0xC6, 0xC7, 0xCA, 0xCF, 0xE6, 0x2022, 0x2026, 0x2219,
    # Visarga candidates
    0x3A, 0x3B
]

img = Image.new('RGB', (1000, 600), 'white')
draw = ImageDraw.Draw(img)

x, y = 20, 20
for code in codes:
    if code in cmap:
        char_str = chr(code)
        hex_str = f"0x{code:02X}" if code <= 0xFF else f"0x{code:04X}"
        
        # Draw box
        draw.rectangle([x, y, x + 90, y + 80], outline='gray')
        draw.text((x + 5, y + 5), f"{hex_str}", fill='blue', font=label_font)
        draw.text((x + 20, y + 25), char_str, fill='black', font=font)
        
        x += 100
        if x > 900:
            x = 20
            y += 90

img.save("scratch/step1_candidates_detailed.png")
print("Saved to scratch/step1_candidates_detailed.png")
