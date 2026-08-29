with open('src/styles/global.css', 'r') as f:
    content = f.read()

content = content.replace("url('/MANGAL.TTF')", "url('/Mangal.ttf')")

with open('src/styles/global.css', 'w') as f:
    f.write(content)
