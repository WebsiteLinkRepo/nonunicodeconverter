import re
with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix the gap_chars loop
content = content.replace("'{get_char(code)}{get_char(64)}'", "'{get_char(code)}{get_char(231)}'")
content = content.replace("'{get_char(code)}{get_char(64)}{get_char(122)}'", "'{get_char(code)}{get_char(231)}{get_char(122)}'")
content = content.replace("'{get_char(code)}{get_char(64)}{get_char(123)}'", "'{get_char(code)}{get_char(231)}{get_char(123)}'")
content = content.replace("'{get_char(code)}{get_char(64)}{get_char(125)}'", "'{get_char(code)}{get_char(231)}{get_char(125)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
