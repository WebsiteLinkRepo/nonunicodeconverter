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

    // Handle short i with bindi (िं)
    processedText = processedText.replace(/\u093F((?:[\u0915-\u0939\u0958-\u095F]\u094D)*[\u0915-\u0939\u0958-\u095F])[\u0901\u0902]/g, '\uF0F3$1');

    // Handle Reph (र्) \u0930\u094D
    // In Unicode, 'र्' + Consonant means the Reph flies on top of the Consonant.
    // In Anu Neo, the Reph glyph (byte 220 = \uF0DC) must be placed AFTER the
    // consonant cluster and its matras. We swap it and directly insert the Reph glyph
    // to avoid conflict with half-Ra (र् = byte 124) in the neoMap.
    const rephRegex = /\u0930\u094D([\u0915-\u0939\u0958-\u095F][\u093E-\u094C\u094E-\u094F]*)/g;
    processedText = processedText.replace(rephRegex, '$1\uF0DC');

    // Now map all substrings to Anu Neo ASCII characters
    const mapKeys = Object.keys(neoMap).sort((a, b) => b.length - a.length);

    for (const key of mapKeys) {
        processedText = processedText.split(key).join(neoMap[key]);
    }


    // Anu Script Manager inserts a bridge (254 / ) after short characters like 'क' and 'फ'
    // when followed by certain consonants like 'म'.
    // In the user's manual output for 'कर्म', it produced 'Nþª|' (   ).
    processedText = processedText.replace(//g, ''); // क + म -> क + bridge + म
    processedText = processedText.replace(//g, ''); // फ + म -> फ + bridge + म
    
    // The user's manual output for 'धर्म' produced '‡ª||' (   )
    // which is two Rephs! Anu Script Manager might be duplicating it or it was a typo.
    // Let's replicate it just to perfectly match Anu if it's expected.
    // Wait, replacing single reph with double reph for everything?
    // Let's just fix the bridge first.

    // Insert bridge  after क () and फ () if they are NOT followed by matras that attach directly.
    // Matras that DO NOT need a bridge:  (ा),  (ी),  (ु),  (ू),  (ृ),  (्),  (ं),  (ः),  (ँ),  (ॅ)
    // Also  itself (so we don't double bridge)
    // Ka and Pha need a bridge (\uF0FE) to complete their width (they advance 400, but ink goes to 600).
    // The bridge should be added AFTER any narrow matras (like ु, ू, ृ, ं) attached to them.
    // Do NOT add a bridge if they are followed by wide matras (ा, ी) or halant (्).
    const narrowMatras = '\uF0EC\uF0EE\uF077\uF0E6\uF0E5\uF07D\uF024\uF03A';
    const bridgeRegex = new RegExp(`([\uF04E\uF0A2][${narrowMatras}]*)(?![\uF07E\uF0FE])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\uF0FE');

    return processedText;
}

