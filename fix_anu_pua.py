import re
import ast

def to_pua(match):
    original_string = match.group(1)
    
    try:
        decoded = ast.literal_eval(f'"{original_string}"')
    except:
        decoded = original_string
    
    pua_escaped = ""
    for char in decoded:
        try:
            byte = char.encode('cp1252')[0]
            pua_escaped += f"\\u{0xF000 + byte:04X}"
        except UnicodeEncodeError:
            if ord(char) < 256:
                pua_escaped += f"\\u{0xF000 + ord(char):04X}"
            else:
                pua_escaped += char
    return f'to: "{pua_escaped}"'

for filename in ['src/utils/mappings/anu7.ts', 'src/utils/mappings/anu6.ts']:
    # Checkout fresh copies
    import os
    os.system(f"git checkout {filename}")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace 'to: "..."'
    new_content = re.sub(r'to:\s*"([^"\\]*(?:\\.[^"\\]*)*)"', to_pua, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed {filename}")

