import sys

content = "# The Ultimate Glyph Finder\n\n"
content += "Please paste this entire block into PageMaker (using Anu NeoGanesh font). It will print every single character in the font next to its number.\n\n"

# Generate 3 columns of numbers and chars
for i in range(33, 256):
    # skip standard numbers and letters if we want to save space, but let's just print all
    content += f"{i}: {chr(i)}   "
    if i % 10 == 0:
        content += "\n\n"

with open('/home/samuelvictor/.gemini/antigravity-cli/brain/389ae3e3-f32c-4819-8cd2-96656cafd1b0/ultimate_glyph_finder.md', 'w', encoding='utf-8') as f:
    f.write(content)
