import { ANU7_UNICODE_TO_NONUNICODE } from './src/utils/mappings/anu7';
for (const entry of ANU7_UNICODE_TO_NONUNICODE) {
    if (entry.from === 'ఘే') {
        for (let i=0; i<entry.to.length; i++) {
            console.log("Char code:", entry.to.charCodeAt(i));
        }
    }
}
