import re

with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

def repl(match):
    char = match.group(0)
    code = ord(char)
    if 0xF000 <= code <= 0xF0FF:
        return f"\\u{code:04X}"
    return char

new_content = re.sub(r'[\uF000-\uF0FF]', repl, content)

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed neo.ts!")
