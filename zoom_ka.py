from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('public/AnuSM/ttf/NEOGANBO.TTF', 100)
img = Image.new('RGB', (600, 200), 'white')
d = ImageDraw.Draw(img)

d.text((20, 20), chr(0xF04D), fill='black', font=font) # Half Ka
d.text((150, 20), chr(0xF04E), fill='black', font=font) # Ka without bridge?
d.text((300, 20), chr(0xF04E) + chr(0xF0FE), fill='black', font=font) # Ka with bridge?
d.text((450, 20), chr(0xF081), fill='black', font=font) # 0xF081?

img.save('zoom_ka.png')
