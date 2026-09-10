with open("src/components/TextConverter.astro", "r") as f:
    lines = f.readlines()

textarea_block = lines[280:289]
toolbar_block = lines[289:316]

# Fix border-t to border-b in toolbar
for i, line in enumerate(toolbar_block):
    if 'border-t' in line:
        toolbar_block[i] = line.replace('border-t', 'border-b')

new_lines = lines[:280] + toolbar_block + textarea_block + lines[316:]

with open("src/components/TextConverter.astro", "w") as f:
    f.writelines(new_lines)
