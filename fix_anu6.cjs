const fs = require('fs');
const content = fs.readFileSync('map_anu6.txt', 'utf8');

// map_anu6.txt contains lines like: { from: "J", to: "అ" },
const map = [];
const lines = content.split('\n');
for (const line of lines) {
  const match = line.match(/{ from: "(.*?)", to: "(.*?)" }/);
  if (match) {
    const ascii = match[1];
    const unicode = match[2];
    map.push(`  { from: "${unicode}", to: "${ascii.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}" },`);
  }
}
fs.writeFileSync('anu6_fixed.ts', `export const ANU6_UNICODE_TO_NONUNICODE = [\n${map.join('\n')}\n];`);
console.log("Done generating anu6_fixed.ts");
