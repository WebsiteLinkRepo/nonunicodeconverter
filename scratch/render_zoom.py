from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 150)

# Render ` (ya) and ñ (half sa)
img = Image.new('RGB', (400, 300), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
draw.text((100, 50), "`", font=font, fill=(0, 0, 0))
img.save("scratch/zoom_ya.png")

img2 = Image.new('RGB', (400, 300), color=(255, 255, 255))
draw2 = ImageDraw.Draw(img2)
draw2.text((100, 50), "ñ", font=font, fill=(0, 0, 0))
img2.save("scratch/zoom_half_sa.png")

print("Rendered zoom images")
