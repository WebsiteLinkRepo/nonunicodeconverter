with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "  'कु':" in line or "  'फु':" in line:
        continue # Remove the overrides for KU and FU since standard 236 is perfect!
    new_lines.append(line)

content = "".join(new_lines)
with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
