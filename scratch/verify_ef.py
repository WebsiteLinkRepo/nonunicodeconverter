from PIL import Image, ImageDraw, ImageFont
font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 40)
img = Image.new('RGB', (200, 100), 'white')
draw = ImageDraw.Draw(img)
draw.text((20, 20), "E F", fill='black', font=font)
draw.text((100, 20), chr(0x45) + chr(0x46), fill='black', font=font)
img.save("scratch/verify_ef.png")
