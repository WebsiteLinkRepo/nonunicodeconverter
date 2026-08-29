with open('src/utils/mappings/neo.ts', 'r') as f:
    content = f.read()

content = content.replace("'़': '',", "'़': '\uF024',")

with open('src/utils/mappings/neo.ts', 'w') as f:
    f.write(content)
