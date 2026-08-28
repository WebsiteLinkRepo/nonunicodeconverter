from PIL import Image

img1 = Image.open('original.png')
# Crop 'का' and 'कु' from original.png
# It's manual trial and error, I'll just save it to view
img1.save('original_view.png')
