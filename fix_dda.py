with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace 'द्' with 'द्द' for byte \uF0F1 (241)
content = content.replace("'द्': '\\uF0F1',", "'द्द': '\\uF0F1',")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
