with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("with open"):
        new_lines.append('content += "  \'ैं\': \'{get_char(248)}\',\\n"\n')
        new_lines.append('content += "};\\n"\n')
        new_lines.append(line)
    elif line.startswith("content +="):
        if "};\\n" in line and "}" not in line.split("=")[0]:
            continue
        elif "  'ैं':" in line:
            continue
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('generate_neo_final3.py', 'w') as f:
    f.writelines(new_lines)
