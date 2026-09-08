import re

for filename in ['src/pages/index.astro', 'src/pages/[lang].astro']:
    with open(filename, 'r') as f:
        content = f.read()
    
    # We want to change the border-radii in links to match design
    # Actually wait, the design doesn't have links in the middle. It has "Features, Pricing, Docs, Toggle Theme, Sign up" on the right.
    # Which corresponds to our "Converter, About, Contact, Privacy, Terms" and "Language Selector" and "Theme Switcher"
    pass

with open('src/styles/global.css', 'r') as f:
    css_content = f.read()

# Add styles for the links buttons inside header
nav_btn_css = """
header nav a {
  border: 0;
  border-radius: 6px;
  color: var(--ink-secondary);
  font-size: 11px;
  font-weight: 700;
  padding: 8px 13px;
  cursor: pointer;
  transition: opacity 0.2s, background-color 0.2s, color 0.2s;
  background: transparent;
}
header nav a:hover {
  opacity: 0.8;
  color: var(--ink);
}
"""
css_content += nav_btn_css

with open('src/styles/global.css', 'w') as f:
    f.write(css_content)

