with open('src/utils/mappings/neo.ts', 'r') as f:
    content = f.read()

content = content.replace("};", """  'क्र': '\\uF0B2',
  'प्र': '\\uF09F',
};""")

with open('src/utils/mappings/neo.ts', 'w') as f:
    f.write(content)
