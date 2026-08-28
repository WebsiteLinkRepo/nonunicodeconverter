from PIL import Image

img1 = Image.open('original.png')
img2 = Image.open('see_here.png')

# Create a new image to hold both
combined = Image.new('RGB', (max(img1.width, img2.width), img1.height + img2.height))
combined.paste(img1, (0, 0))
combined.paste(img2, (0, img1.height))

combined.save('compare_koo.png')
