import re

with open('src/layouts/Layout.astro', 'r') as f:
    content = f.read()

header_pattern = r'<header class="border-b border-\[var\(--hairline\)\] bg-\[var\(--canvas-soft\)\]/90 sticky top-0 z-40 backdrop-blur-xl">'
new_header = '<header class="mx-auto max-w-6xl mt-4 z-40 relative rounded-xl border border-[var(--hairline)] bg-[var(--canvas-soft)]/90 backdrop-blur-xl">'
content = re.sub(header_pattern, new_header, content)

with open('src/layouts/Layout.astro', 'w') as f:
    f.write(content)
