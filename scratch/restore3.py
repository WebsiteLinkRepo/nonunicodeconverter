with open('src/utils/mappings/neo.ts', 'r') as f:
    content = f.read()

content = content.replace("};", """  'हृ': '\\uF0D3',
  'ह्ण': '\\uF0D4',
  'ह्न': '\\uF0D5',
  'ह्म': '\\uF0D6',
  'ह्य': '\\uF0D8',
  'ह्र': '\\uF0D9',
  'ह्ल': '\\uF0DA',
  'ह्व': '\\uF0DB',
};""")

with open('src/utils/mappings/neo.ts', 'w') as f:
    f.write(content)
