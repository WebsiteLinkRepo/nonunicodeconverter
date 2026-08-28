with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'{get_char(78)}{get_char(237)}'", f"'{chr(0xF000 + 78)}{chr(0xF000 + 237)}'")
content = content.replace("'{get_char(78)}{get_char(239)}'", f"'{chr(0xF000 + 78)}{chr(0xF000 + 239)}'")
content = content.replace("'{get_char(162)}{get_char(237)}'", f"'{chr(0xF000 + 162)}{chr(0xF000 + 237)}'")
content = content.replace("'{get_char(162)}{get_char(239)}'", f"'{chr(0xF000 + 162)}{chr(0xF000 + 239)}'")

# Wait, the literal string was: "  'कु': '{get_char(78)}{get_char(237)}',\n"
# So replace is fine.

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
