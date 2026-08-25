import { ANU6_UNICODE_TO_NONUNICODE } from './src/utils/mappings/anu6';

// Add the missing complex ligatures manually at the top (sorted by length later)
ANU6_UNICODE_TO_NONUNICODE.push({ from: "శ్రీ", to: "N" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ష్ట్ర", to: "R" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ర్వ", to: "~¡Þ" });
ANU6_UNICODE_TO_NONUNICODE.push({ from: "ర్య", to: "~¡¼" });

// Sort by length descending
const sortedMap = [...ANU6_UNICODE_TO_NONUNICODE].sort((a, b) => b.from.length - a.from.length);

function convertAnu6(text: string): string {
    let result = text;
    // We can just iterate and replace? 
    // Wait, replacing 15000 items on every conversion is O(N) where N is 15000. It might be slow.
    // Let's use a regex like converter.ts does, but WITHOUT the pre-processing.
    
    // Actually, converter.ts uses a syllable regex and a lookup map.
    const lookupMap: Record<string, string> = {};
    for (const entry of sortedMap) {
        lookupMap[entry.from] = entry.to;
    }
    
    // Simple greedy replace based on sorted keys
    // Building a regex for 15000 keys is too big, let's just use the syllable parser from converter.ts
    // but we MUST add ష్ట్ర to the syllable regex if it isn't matched?
    // Let's just use simple string replacement for now to see if it works!
    for (const entry of sortedMap) {
        if (result.includes(entry.from)) {
            result = result.split(entry.from).join(entry.to);
        }
    }
    return result;
}

const test1 = "శ్రీ ష్ట్ర ర్వ ర్య";
console.log("Conjuncts:", convertAnu6(test1));

const test2 = "ఆంధ్రప్రదేశ్ మరియు తెలంగాణ రాష్ట్రాలలో తెలుగు భాషను అత్యంత సుందరంగా మాట్లాడుతారు; సార్వభౌమత్వంతో ముందుకు వెళ్దాం.";
console.log("Sentence:", convertAnu6(test2));

