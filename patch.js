const fs = require('fs');
let code = fs.readFileSync('src/utils/anu6Converter.ts', 'utf8');

// replace ౠ to |°¶ ... wait, we already have it.
if (!code.includes('from: "ృ"')) {
   code = code.replace('ANU6_UNICODE_TO_NONUNICODE.push({ from: "ౠ", to: "|°¶" });',
`ANU6_UNICODE_TO_NONUNICODE.push({ from: "ౠ", to: "|°¶" }); 
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ృ", to: "$" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ౄ", to: "$ì" });`);
}

// Add the smart quote replacement
if (!code.includes('result = result.replace(/(\\S)\\'/g, "$1Ñ");')) {
   code = code.replace('export function unicodeToAnu6(text: string): string {\n  let result = text;',
`export function unicodeToAnu6(text: string): string {
  let result = text;

  // Handle straight single quotes (open vs closed)
  result = result.replace(/(\\S)'/g, "$1Ñ");`);
}

fs.writeFileSync('src/utils/anu6Converter.ts', code);
