from PIL import Image, ImageDraw, ImageFont

font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 14)

# Let's test combinations:
# Independent vowels:
# అ = 'A'
# ఆ = 'B'
# ఇ = 'C'
# ఈ = 'D'
# ఉ = 'E'
# ఊ = 'F'
# ఋ = ?
# ౠ = ?
# ఎ = 'G'
# ఏ = 'H'
# ఐ = 'I'
# ఒ = 'J'
# ఓ = 'K'
# ఔ = 'L'
# అం = 'A' + Sunna
# అః = 'A' + Visarga

anusvara_options = [
    ("0x30 ('0')", "0"),
    ("0xC6", chr(0xC6)),
    ("0x2026", chr(0x2026)),
    ("space + 0xC6", " " + chr(0xC6)),
    ("0x78", chr(0x78)),
]

ru_options = [
    ("0x76, 0x77", chr(0x76), chr(0x77)),
    ("0xC7, 0xC8", chr(0xC7), chr(0xC8)),
    ("0x2030, 0x2021", chr(0x2030), chr(0x2021)),
    ("0x02DC, 0x02DC + ~", chr(0x02DC), chr(0x02DC) + "~"),
    ("0x6D (m)", "m", "m" + chr(0xE9)),
]

visarga_options = [
    ("':' (0x3A)", ":"),
    ("0x40", chr(0x40)),
]

img = Image.new('RGB', (1100, 700), 'white')
draw = ImageDraw.Draw(img)

y = 20
for r_name, r_char, rr_char in ru_options:
    for a_name, a_char in anusvara_options[:3]:
        for v_name, v_char in visarga_options[:1]:
            line = f"A B C D E F {r_char} {rr_char} G H I J K L A{a_char} A{v_char}"
            desc = f"Ru: {r_name} | Anusvara: {a_name}"
            draw.text((20, y), desc, fill='blue', font=label_font)
            draw.text((20, y + 20), line, fill='black', font=font)
            y += 65

img.save("scratch/vowels_exact_test.png")
print("Saved to scratch/vowels_exact_test.png")
