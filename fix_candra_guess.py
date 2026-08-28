with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Guess Candrabindu is a single byte 127
content = content.replace("get_char(125)}{get_char(230)}", "get_char(127)")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
