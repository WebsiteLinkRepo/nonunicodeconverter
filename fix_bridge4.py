with open('src/utils/anuNeoConverter.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the lookahead to remove \uF0E7 and \uF079
old_line = "const bridgeRegex = new RegExp(`([\\uF04E\\uF0A2][${narrowMatras}]*)(?![\\uF0E7\\uF079\\uF07E\\uF0FE])`, 'g');"
new_line = "const bridgeRegex = new RegExp(`([\\uF04E\\uF0A2][${narrowMatras}]*)(?![\\uF07E\\uF0FE])`, 'g');"

if old_line in content:
    content = content.replace(old_line, new_line)
else:
    print("Could not find old_line!")

with open('src/utils/anuNeoConverter.ts', 'w', encoding='utf-8') as f:
    f.write(content)
