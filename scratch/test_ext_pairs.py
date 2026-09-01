from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"

# Test at small size where user is viewing (e.g. 24px) and large size
for size in [24, 48]:
    font = ImageFont.truetype(font_path, size)
    img = Image.new('RGB', (800, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    ext = chr(0x9d)

    # Compare WITHOUT extension vs WITH extension
    # 1. भस्म: '^ñ_' vs '^ñ' + ext + '_'
    # 2. महा: '_hm' vs '_' + ext + 'hm' or '_h' + ext + 'm'
    # 3. हमारे: 'h_mao' vs 'h' + ext + '_mao'
    # 4. मात्रा: '_mÌm' vs '_' + ext + 'mÌm'
    # 5. विमूढ़: '{d_y‹T>' vs '{d_' + ext + 'y‹T>'

    pairs = [
        ("भस्म without ext", "^ñ_"),
        ("भस्म with ext", "^ñ" + ext + "_"),
        ("महा without ext", "_hm"),
        ("महा with ext", "_" + ext + "hm"),
        ("हमारे without ext", "h_mao"),
        ("हमारे with ext", "h" + ext + "_mao"),
    ]

    y = 20
    for label, txt in pairs:
        draw.text((20, y), f"{label}: ", fill=(100, 100, 100))
        draw.text((300, y), txt, font=font, fill=(0, 0, 0))
        y += size + 15

    img.save(f"scratch/compare_ext_{size}.png")
    print(f"Saved compare_ext_{size}.png")
