import fs from 'fs';

const path = 'src/utils/converter.ts';
let code = fs.readFileSync(path, 'utf8');

// Insert after the + replacement
const target = 'resultText = resultText.replace(/\\u0C03/g, "\\u00A6");\n    }';
const replacement = target + '\n\n    // Handle isolated standalone vattus correctly\n    if (encoding === "anu7" && script === "telugu") {\n      resultText = resultText.replace(/(^|[^\\u0C15-\\u0C39\\u0C58-\\u0C5A])\\u0C4D\\u0C37/g, "$1\\uF08C");\n    }';

if (code.includes('isolated standalone vattus')) {
  console.log("Already fixed.");
} else {
  code = code.replace(target, replacement);
  fs.writeFileSync(path, code);
  console.log("Added isolated fallback.");
}
