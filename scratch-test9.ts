import { getMapping } from './src/utils/mappings/index';
const anu7 = getMapping("anu7", false);

for (const e of anu7) {
  if (e.to.includes(String.fromCharCode(0xF083))) {
    console.log(`${e.from} -> ${e.to.split('').map(c=>'\\u'+c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')).join('')}`);
  }
}
