import { ANU7_UNICODE_TO_NONUNICODE } from './src/utils/mappings/anu7';
for (const entry of ANU7_UNICODE_TO_NONUNICODE) {
    if (entry.to.includes('y')) console.log("Anu 7 uses 'y' for:", entry.from);
}
