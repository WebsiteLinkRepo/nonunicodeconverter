from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('/home/samuelvictor/Downloads/Shreelipi_4642.TTF', 34)
img = Image.new('RGB', (1000, 300), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

text1 = "AmO H$b H$m ~ƒm H§$ß`yQ>a grIVm h¡&"
text2 = "H$b Ho$ ~‹So> AmX_r ^r VH$ZrH$r kmZ aIVo h¢&"
text3 = "`h g_` H$r _m±J h¡ Am¡a h_o§ Bgo ñdrH$ma H$aZm Mm{hE&"

draw.text((20, 20), text1, font=font, fill=(0, 0, 0))
draw.text((20, 100), text2, font=font, fill=(0, 0, 0))
draw.text((20, 180), text3, font=font, fill=(0, 0, 0))

img.save('scratch/shree_perfect_render.png')
print('Successfully saved scratch/shree_perfect_render.png')
