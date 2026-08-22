import re

with open('unibamini.js', 'r') as f:
    content = f.read()

# Extract all b.replace(/pattern/g, "replacement")
matches = re.findall(r'b\.replace\(/([^\/]+)/g,"([^"]*)"\)', content)

# Output as TS array
print("export const BAMINI_TAMIL_UNICODE_TO_NONUNICODE = [")
for from_str, to_str in matches:
    # Handle escaping
    if from_str == '\\+':
        from_str = '+'
    elif from_str == '\\@':
        from_str = '@'
    elif from_str == '\\*':
        from_str = '*'
    elif from_str == '\\/':
        from_str = '/'
    elif from_str == '\\\\':
        from_str = '\\'
    
    # Escape quotes and backslashes for TS
    from_str = from_str.replace('\\', '\\\\').replace('"', '\\"')
    to_str = to_str.replace('\\', '\\\\').replace('"', '\\"')
    print(f'  {{ from: "{from_str}", to: "{to_str}" }},')
print("];")
