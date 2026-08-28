with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("  'कू': '\uF04E\uF0EF',", f"  'कू': '\uF04E{chr(0xF000 + 238)}',")
content = content.replace("  'फू': '\uF0A2\uF0EF',", f"  'फू': '\uF0A2{chr(0xF000 + 238)}',")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
