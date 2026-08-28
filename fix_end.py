with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("  'ैं':"):
        continue
    if line.startswith("content +="):
        if "};\\n" in line and "}" not in line.split("=")[0]:
            continue
    new_lines.append(line)

new_lines.append('content += "  \'ैं\': \'{get_char(248)}\',\\n"\n')
new_lines.append('content += "};\\n"\n')

with open('generate_neo_final3.py', 'w') as f:
    f.writelines(new_lines)
