const fs = require('fs');
let content = fs.readFileSync('src/utils/converter.ts', 'utf8');

# I need to find the forward conversion block.
# "if (encoding === 'anu7' && script === 'telugu') {"
# I'll add my Hindi Reph swap right above it.

replacement = """
    if (script === 'hindi') {
      // Move Reph (Ra + Halant) to AFTER the consonant it precedes
      resultText = resultText.replace(/\\u0C30\\u0C4D([\\u0C15-\\u0C39])/g, '$1\\u0C30\\u0C4D');
    }

    // Pre-process standalone modifiers
"""

content = content.replace("// Pre-process standalone modifiers", replacement.strip() + "\n\n    // Pre-process standalone modifiers")

fs.writeFileSync('src/utils/converter.ts', content);
