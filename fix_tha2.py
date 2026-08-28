with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'थ': '{get_char(115)}{get_char(64)}'", "'थ': '{get_char(115)}'")
content = content.replace("'य': '{get_char(174)}{get_char(64)}'", "'य': '{get_char(175)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
