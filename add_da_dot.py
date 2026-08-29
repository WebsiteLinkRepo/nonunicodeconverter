with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("'ड': '\\uF067',", "'ड़': '\\uF0E4\\uF067',\n  'ड': '\\uF067',")
content = content.replace("'ढ': '\\uF06A',", "'ढ़': '\\uF0E4\\uF06A',\n  'ढ': '\\uF06A',")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
