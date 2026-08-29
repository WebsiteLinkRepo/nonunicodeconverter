import { neoMap } from './src/utils/mappings/neo';
let found = false;
for (let key in neoMap) {
    if (key === 'प्र' || key.includes('प्र')) {
        console.log("Found Pra mapping in neoMap: " + key + " -> " + neoMap[key].split('').map(c => c.charCodeAt(0).toString(16)).join(' '));
        found = true;
    }
}
if (!found) console.log("No Pra mapping found.");
