with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix Candrabindu back to 125 + 88
content = content.replace("'ँ': '{get_char(126)}'", "'ँ': '{get_char(125)}{get_char(88)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
