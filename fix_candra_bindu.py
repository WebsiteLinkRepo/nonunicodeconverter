with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# I will use 126 for candra-bindu for now. If it's wrong, we can try 127.
content = content.replace("'ँ': '{get_char(125)}{get_char(88)}'", "'ँ': '{get_char(126)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
