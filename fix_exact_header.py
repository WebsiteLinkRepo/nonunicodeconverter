import re

with open('src/layouts/Layout.astro', 'r') as f:
    content = f.read()

pattern = r'<header class="mx-auto max-w-6xl mt-4 z-40 relative rounded-xl border border-\[var\(--hairline\)\] bg-\[var\(--canvas-soft\)\]/90 backdrop-blur-xl">\s*<div class="max-w-6xl mx-auto px-3 sm:px-6 h-14 flex items-center justify-between gap-2">'
replacement = """<header class="mx-auto max-w-6xl w-[96vw] lg:w-full mt-4 z-40 relative rounded-[7px] border border-[var(--hairline)] bg-[var(--canvas-soft)] backdrop-blur-[10px]">
			<div class="px-3 sm:px-4 h-[47px] flex items-center justify-between gap-2">"""
content = re.sub(pattern, replacement, content)

with open('src/layouts/Layout.astro', 'w') as f:
    f.write(content)
