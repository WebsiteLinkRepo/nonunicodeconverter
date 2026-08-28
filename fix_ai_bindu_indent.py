with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

with open('generate_neo_final3.py', 'w') as f:
    for line in lines:
        if line.startswith("    'ैं': '{get_char(248)}',"):
            continue
        if line.startswith("content +="):
            if "};\\n" in line and not "}" in line.split("=")[0]: # careful
                pass
        f.write(line)

