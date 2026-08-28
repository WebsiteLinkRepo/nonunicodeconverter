with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

with open('generate_neo_final3.py', 'w') as f:
    for line in lines:
        if line.startswith("  'ैं':"):
            continue
        if line.startswith("content +="):
            if "};\\n" in line and "}" not in line.split("=")[0]:
                f.write('content += "  \'ैं\': \'{get_char(248)}\',\\n"\n')
        f.write(line)
