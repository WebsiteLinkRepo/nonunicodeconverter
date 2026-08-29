with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add \u095C and \u095D explicitly
content = content.replace("'ड़': '\\uF0E4\\uF067',", "'ड़': '\\uF0E4\\uF067',\n  '\\u095C': '\\uF0E4\\uF067',")
content = content.replace("'ढ़': '\\uF0E4\\uF06A',", "'ढ़': '\\uF0E4\\uF06A',\n  '\\u095D': '\\uF0E4\\uF06A',")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
