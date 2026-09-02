from PIL import Image, ImageDraw, ImageFont

font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 40)

with open('scratch/step1_out.txt', 'r', encoding='utf-8') as f:
    text = f.read().strip()

img = Image.new('RGB', (800, 100), 'white')
draw = ImageDraw.Draw(img)
draw.text((20, 20), text, fill='black', font=font)
img.save("scratch/step1_out.png")
