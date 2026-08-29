with open('src/utils/mappings/neo.ts', 'r') as f:
    content = f.read()

content = content.replace("};", """  'रु': '\\uF0BB',
  'रू': '\\uF0BF',
  'क्ष': '\\uF071',
  'ज्ञ': '\\uF072',
  'त्र': '\\uF0DE',
  'श्र': '\\uF0C8',
  'द्र': '\\uF0FC',
  'द्य': '\\uF08D',
  'द्व': '\\uF0FB',
  'त्त': '\\uF0F0',
  'ट्ट': '\\uF063',
  'द': '\\uF074',
  'द्द': '\\uF0F1',
  'र्': '\\uF07C',
  'क्र': '\\uF0B2',
  'प्र': '\\uF09F',
};""")

with open('src/utils/mappings/neo.ts', 'w') as f:
    f.write(content)
