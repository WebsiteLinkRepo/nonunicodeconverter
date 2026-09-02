from PIL import Image

img = Image.open('scratch/shree_telugu_all_combinations.png')
# Slice the big image into smaller vertical chunks for inspection
h = img.height
num_slices = 5
slice_h = h // num_slices

for i in range(num_slices):
    box = (0, i * slice_h, img.width, (i + 1) * slice_h if i < num_slices - 1 else h)
    sliced = img.crop(box)
    sliced.save(f'scratch/shreelipi_telugu/combo_slice_{i}.png')

print("Saved all combo slices!")
