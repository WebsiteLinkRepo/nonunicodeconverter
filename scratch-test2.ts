import { getMapping } from './src/utils/mappings/index';
const anu7 = getMapping("anu7", false);

for (const entry of anu7) {
  if (entry.to.includes("")) console.log(`Matched F0BF F0A3: ${entry.from}`);
  if (entry.to.includes("")) {
    // console.log(`${entry.from} uses F0BF: ${entry.to.split('').map(c => '\\u'+c.charCodeAt(0).toString(16)).join('')}`);
  }
}
