import { neoMap } from './src/utils/mappings/neo.js';

// Reverse map to see what the glyphs mean
const revMap: Record<string, string> = {};
for (const [k, v] of Object.entries(neoMap)) {
  revMap[v] = k;
}

const res = "".split('').map(c => revMap[c] || c);
console.log(res.join('|'));
