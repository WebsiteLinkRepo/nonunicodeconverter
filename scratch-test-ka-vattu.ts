import { getMapping } from './src/utils/mappings/index';

const anu7 = getMapping("anu7", false);
anu7.forEach(entry => {
  if (entry.to.includes("")) {
    console.log(`F0D8: ${entry.from} -> ${entry.to.split('').map(c => '\\u'+c.charCodeAt(0).toString(16)).join('')}`);
  }
  if (entry.to.includes("")) {
    console.log(`F0BF: ${entry.from} -> ${entry.to.split('').map(c => '\\u'+c.charCodeAt(0).toString(16)).join('')}`);
  }
  if (entry.to.includes("")) {
    console.log(`F08C: ${entry.from} -> ${entry.to.split('').map(c => '\\u'+c.charCodeAt(0).toString(16)).join('')}`);
  }
});
