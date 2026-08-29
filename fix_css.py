import re
with open('src/components/TextConverter.astro', 'r') as f:
    content = f.read()

content = re.sub(r'style="letter-spacing: 0px !important;[^"]+"', '', content)
content = content.replace(' tracking-normal"', '"')

with open('src/components/TextConverter.astro', 'w') as f:
    f.write(content)
