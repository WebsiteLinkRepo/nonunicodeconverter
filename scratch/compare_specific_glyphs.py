from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 100)

chars_to_inspect = [
    (0x60, "`", "60_grave"),
    (0xb6, chr(0xb6), "b6_ya_alt"),
    (0x67, "g", "67_sa"),
    (0xf1, chr(0xf1), "f1_half_sa_alt"),
    (0xf1, chr(0xf1) + "_", "f1_plus_ma"),
    (0xf1, "ñ_", "ñ_half_sa_original"),
    (0x60, "`wJ", "60_yug"),
    (0xb6, chr(0xb6) + "wJ", "b6_yug"),
]

for code, txt, label in chars_to_inspect:
    img = Image.new('RGB', (400, 250), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), txt, font=font, fill=(0, 0, 0))
    img.save(f"scratch/inspect_{label}.png")

print("Generated inspection images")
