with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert प्र from \uF09B\uF0DD to \uF09F
content = content.replace("'प्र': '\\uF09B\\uF0DD'", "'प्र': '\\uF09F'")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
