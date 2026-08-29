with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix द्य from \uF0F6 (246) to \uF08D (141)
content = content.replace("'द्य': '\\uF0F6'", "'द्य': '\\uF08D'")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
