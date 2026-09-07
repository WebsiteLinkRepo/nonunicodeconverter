import { getMapping } from './src/utils/mappings/index';
const anu7 = getMapping("anu7", false);

anu7.filter(e => e.from.startsWith("ఢి") || e.from.startsWith("ఢీ") || e.from.startsWith("డి")).forEach(e => {
  console.log(`${e.from} -> ${e.to.split('').map(c=>'\\u'+c.charCodeAt(0).toString(16).toUpperCase()).join('')}`);
});
