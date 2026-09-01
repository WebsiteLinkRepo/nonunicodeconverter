from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"

# Test at small sizes like 16, 20, 24
for size in [16, 20, 24, 32]:
    font = ImageFont.truetype(font_path, size)
    img = Image.new('RGB', (100, 60), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), "`wJ", font=font, fill=(0, 0, 0))
    # resize using nearest neighbor to make pixels visible
    img_zoomed = img.resize((500, 300), Image.NEAREST)
    img_zoomed.save(f"scratch/small_render_{size}.png")

print("Rendered small sizes")
