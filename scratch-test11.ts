import { getMapping } from './src/utils/mappings/index';

const mapping = getMapping('anu7', false);
const lookupMap: Record<string, string> = {};
for (const entry of mapping) {
    if (entry.from) {
        lookupMap[entry.from] = entry.to;
    }
}

console.log("Lookup for క్ష్మి:", lookupMap["క్ష్మి"]);
console.log("Lookup for క్షి:", lookupMap["క్షి"]);
console.log("Lookup for క్కి:", lookupMap["క్కి"]);
console.log("Lookup for డ్గ:", lookupMap["డ్గ"]);
