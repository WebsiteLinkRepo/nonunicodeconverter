with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'य': '{get_char(175)}'", "'य': '{get_char(174)}'")
# also replace half ya if needed, let's map half ya to 175
content = content.replace("'य्': 174", "'य्': 175")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
