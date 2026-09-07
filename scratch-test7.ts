const fs = require('fs');

let content = fs.readFileSync('src/utils/mappings/anu7.ts', 'utf8');

// The new entries we want to add
const newEntries = `
  // --- New User Mappings for కి variant and Ksha matra ---
  { from: "క్ష్మి", to: "\\uF0BF\\uF0A3\\uF08C\\uF088" },
  { from: "క్షి", to: "\\uF0BF\\uF0A3\\uF08C" },
  { from: "క్కి", to: "\\uF0BF\\uF0A3\\uF0D8" },
  { from: "కి", to: "\\uF0BF\\uF0A3" },
  { from: "డ్గ", to: "\\uF026\\uF083\\uF05A" },
  { from: "్ష", to: "\\uF08C" },
`;

// Just insert them at the top of anu7Map
if (!content.includes("New User Mappings")) {
  content = content.replace("export const anu7Map: Record[] = [", "export const anu7Map: Record[] = [" + newEntries);
  fs.writeFileSync('src/utils/mappings/anu7.ts', content);
  console.log("Updated!");
}
