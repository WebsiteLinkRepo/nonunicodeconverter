const fs = require('fs');
const inLines = fs.readFileSync('telugu_all_combinations.txt', 'utf8').split('\n');
const outLines = fs.readFileSync('competitor_anu6_output.txt', 'utf8').split('\n');

if (inLines.length !== outLines.length) {
  console.log(`Error: Input has ${inLines.length} lines, output has ${outLines.length} lines.`);
  process.exit(1);
}

const map = [];
for(let i = 0; i < inLines.length; i++) {
    const unicode = inLines[i];
    const ascii = outLines[i].replace(/\\/g, '\\\\').replace(/"/g, '\\"');
    map.push(`  { from: "${unicode}", to: "${ascii}" },`);
}

// Add the fallback characters for Anu 6 that we got from previous tests (just in case they are missed)
map.push(`  { from: "ః", to: "'" },`);

const finalTs = `import type { MappingEntry } from './anu6';

export const ANU6_UNICODE_TO_NONUNICODE: MappingEntry[] = [
${map.join('\n')}
];
`;

fs.writeFileSync('src/utils/mappings/anu6.ts', finalTs);
console.log("Successfully built anu6.ts with", map.length, "rules!");
