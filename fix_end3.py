with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith("  'कु':"):
        continue
    if line.startswith("  'कू':"):
        continue
    if line.startswith("  'फु':"):
        continue
    if line.startswith("  'फू':"):
        continue
    if line.startswith("};"):
        continue
    
    if line.startswith("content += \"  'ैं':"):
        new_lines.append(line)
        new_lines.append("content += \"  'कु': '{get_char(78)}{get_char(237)}',\\n\"\n")
        new_lines.append("content += \"  'कू': '{get_char(78)}{get_char(239)}',\\n\"\n")
        new_lines.append("content += \"  'फु': '{get_char(162)}{get_char(237)}',\\n\"\n")
        new_lines.append("content += \"  'फू': '{get_char(162)}{get_char(239)}',\\n\"\n")
        continue

    new_lines.append(line)

with open('generate_neo_final3.py', 'w') as f:
    f.writelines(new_lines)
