with open('src/utils/converter.ts', 'r') as f:
    content = f.read()

replacement = """
    if (script === 'hindi') {
      // Move Reph (Ra + Halant) to AFTER the consonant it precedes
      resultText = resultText.replace(/\\u0C30\\u0C4D([\\u0C15-\\u0C39])/g, '$1\\u0C30\\u0C4D');
    }

    // Pre-process standalone modifiers"""

content = content.replace("    // Pre-process standalone modifiers", replacement)

with open('src/utils/converter.ts', 'w') as f:
    f.write(content)
