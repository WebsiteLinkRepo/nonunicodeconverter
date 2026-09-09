import re

with open('src/layouts/Layout.astro', 'r') as f:
    content = f.read()

# Replace header logo classes
content = content.replace('class="w-7 h-7 rounded-lg shadow-xs flex-shrink-0 dark:hidden"', 'class="logo-light w-7 h-7 rounded-lg shadow-xs flex-shrink-0"')
content = content.replace('class="w-7 h-7 rounded-lg shadow-xs flex-shrink-0 hidden dark:block"', 'class="logo-dark w-7 h-7 rounded-lg shadow-xs flex-shrink-0"')

# Replace footer logo classes
content = content.replace('class="w-5 h-5 rounded dark:hidden"', 'class="logo-light w-5 h-5 rounded"')
content = content.replace('class="w-5 h-5 rounded hidden dark:block"', 'class="logo-dark w-5 h-5 rounded"')

with open('src/layouts/Layout.astro', 'w') as f:
    f.write(content)

print("Layout classes updated.")
