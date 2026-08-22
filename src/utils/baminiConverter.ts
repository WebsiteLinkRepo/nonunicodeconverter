import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from './mappings/baminiTamil';

export function unicodeToBamini(text: string): string {
    if (!text) return "";
    let result = text;
    
    // Now run through Bamini mapping table
    for (const entry of BAMINI_TAMIL_UNICODE_TO_NONUNICODE) {
        if (entry.from) {
            result = result.split(entry.from).join(entry.to);
        }
    }

    return result;
}
