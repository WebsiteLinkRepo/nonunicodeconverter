import re

with open('src/layouts/Layout.astro', 'r') as f:
    content = f.read()

# Replace header logo
header_old = r'<img src="/logo\.svg" alt="NonUnicodeConverter\.com Logo" class="w-7 h-7 rounded-lg shadow-xs flex-shrink-0 dark:invert" />'
header_new = r'''<img src="/logo-light.svg" alt="NonUnicodeConverter.com Logo" class="w-7 h-7 rounded-lg shadow-xs flex-shrink-0 dark:hidden" />
					<img src="/logo-dark.svg" alt="NonUnicodeConverter.com Logo" class="w-7 h-7 rounded-lg shadow-xs flex-shrink-0 hidden dark:block" />'''
content = re.sub(header_old, header_new, content)

# Replace footer logo
footer_old = r'<img src="/logo\.svg" alt="NonUnicodeConverter Logo" class="w-5 h-5 rounded dark:invert" />'
footer_new = r'''<img src="/logo-light.svg" alt="NonUnicodeConverter Logo" class="w-5 h-5 rounded dark:hidden" />
							<img src="/logo-dark.svg" alt="NonUnicodeConverter Logo" class="w-5 h-5 rounded hidden dark:block" />'''
content = re.sub(footer_old, footer_new, content)

with open('src/layouts/Layout.astro', 'w') as f:
    f.write(content)

print("Layout updated.")
