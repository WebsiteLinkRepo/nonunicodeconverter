import re

with open('src/layouts/Layout.astro', 'r') as f:
    content = f.read()

# Fix the stray divs left from replacing the background glow
pattern = r'<!-- Pink/Magenta glow on right -->.*?<!-- Purple glow in center/bottom -->.*?</div>\n\t\t</div>'
content = re.sub(pattern, '', content, flags=re.DOTALL)

with open('src/layouts/Layout.astro', 'w') as f:
    f.write(content)
