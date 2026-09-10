with open("src/components/TextConverter.astro", "r") as f:
    lines = f.readlines()

textarea_start = -1
textarea_end = -1
toolbar_start = -1
toolbar_end = -1

for i, line in enumerate(lines):
    if '<textarea' in line and 'id="output-text"' in lines[i+1]:
        textarea_start = i
    if textarea_start != -1 and '></textarea>' in line and i > textarea_start and toolbar_start == -1:
        textarea_end = i
    if '<!-- Action Toolbar (Download .txt & Copy Button) -->' in line:
        toolbar_start = i
    if toolbar_start != -1 and '</div>' in line and 'COPY OUTPUT' in lines[i-3]:
        # just find the ending div for toolbar
        toolbar_end = i + 1

print(f"textarea: {textarea_start} to {textarea_end}")
print(f"toolbar: {toolbar_start} to {toolbar_end}")
