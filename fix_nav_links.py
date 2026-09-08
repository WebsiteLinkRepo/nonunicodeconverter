import re

with open('src/layouts/Layout.astro', 'r') as f:
    content = f.read()

# Replace all old Tailwind styling on nav links with nothing so the global.css maps apply cleanly
link_pattern = r'class="px-2 py-1 rounded-md hover:text-\[var\(--ink\)\] hover:bg-\[var\(--canvas\)\] transition-colors( hidden md:inline-block)?( hidden lg:inline-block)?"'
def link_repl(match):
    hidden = ""
    if match.group(1): hidden += match.group(1)
    if match.group(2): hidden += match.group(2)
    return f'class="{hidden.strip()}"' if hidden else ''

content = re.sub(link_pattern, link_repl, content)

with open('src/layouts/Layout.astro', 'w') as f:
    f.write(content)
