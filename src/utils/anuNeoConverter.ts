import { neoMap } from './mappings/neo';

export function unicodeToAnuNeo(text: string): string {
    if (!text) return "";

    let processedText = text;

    // In Devanagari, short 'i' matra (ि) comes after the consonant in Unicode,
    // but in legacy Anu Neo, it must be printed BEFORE the consonant cluster.
    // Example Unicode: क + ि -> Anu: u + N
    // Example Unicode: क + ् + क + ि -> Anu: u + M + N
    
    // So we first swap the Unicode 'ि' to the left of the preceding consonant cluster!
    // A consonant cluster can be one or more consonants joined by virama.
    // Unicode range for Devanagari consonants: \u0915-\u0939, \u0958-\u095F
    // Virama: \u094D
    // Regex matches a sequence of (Consonant + Virama)* + Consonant, followed by ि
    const clusterRegex = /((?:[\u0915-\u0939\u0958-\u095F]\u094D)*[\u0915-\u0939\u0958-\u095F])\u093F/g;
    processedText = processedText.replace(clusterRegex, '\u093F$1');

    // Handle Reph (र्) \u0930\u094D
    // In Unicode, 'र्' + Consonant means the Reph flies on top of the Consonant.
    // But in Anu Neo, the Reph character (160) must be placed AFTER the consonant cluster and its matras.
    // Actually, let's just swap 'र्' with the following character cluster.
    // Match 'र्' followed by a consonant and any trailing matras
    const rephRegex = /\u0930\u094D([\u0915-\u0939\u0958-\u095F][\u093E-\u094C\u094E-\u094F]*)/g;
    processedText = processedText.replace(rephRegex, '$1\u0930\u094D');

    // Now map all substrings to Anu Neo ASCII characters
    const mapKeys = Object.keys(neoMap).sort((a, b) => b.length - a.length);

    for (const key of mapKeys) {
        processedText = processedText.split(key).join(neoMap[key]);
    }

    return processedText;
}
