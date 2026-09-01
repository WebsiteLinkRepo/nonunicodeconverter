with open("src/components/TextConverter.astro", "r") as f:
    text = f.read()

text = text.replace("{ value: 'anu7', label: 'Anu Script Manager (Tamil)' }", "{ value: 'anutamil', label: 'Anu Script Manager (Tamil)' }")

with open("src/components/TextConverter.astro", "w") as f:
    f.write(text)

print("Patched src/components/TextConverter.astro")
