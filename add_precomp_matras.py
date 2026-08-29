with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Add precomposed matras right after 'ी'
content = content.replace("'ी': '\\uF079',", "'ी': '\\uF079',\n  'ीं': '\\uF0EB',")
content = content.replace("'े': '\\uF07A',", "'े': '\\uF07A',\n  'ें': '\\uF0F5',")
content = content.replace("'ै': '\\uF07B',", "'ै': '\\uF07B',\n  'ैं': '\\uF0F8',")
content = content.replace("'ो': '\\uF0E7\\uF07A',", "'ो': '\\uF0E7\\uF07A',\n  'ों': '\\uF0E7\\uF0F5',")
content = content.replace("'ौ': '\\uF0E7\\uF07B',", "'ौ': '\\uF0E7\\uF07B',\n  'ौं': '\\uF0E7\\uF0F8',")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
