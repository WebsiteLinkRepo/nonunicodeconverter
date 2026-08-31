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
    // Unicode range for Devanagari consonants: क-ह, क़-य़
    // Virama: ्
    // Regex matches a sequence of (Consonant + Virama)* + Consonant, followed by ि
    const clusterRegex = /((?:[क-हक़-य़]्)*[क-हक़-य़])ि/g;
    processedText = processedText.replace(clusterRegex, 'ि$1');

    // े (e matra) and ै (ai matra) stay AFTER the consonant in Anu Neo glyph order.
    // No reordering needed for these — they map to top matras that sit on the consonant.

    // Decompose composite vowel signs into components:
    // ो (o) = ा (aa) + े (e)
    // ौ (au) = ा (aa) + ै (ai)
    // ॉ (candra o) = ा (aa) + ॅ (candra e)
    processedText = processedText.replace(/ो/g, 'ाे');
    processedText = processedText.replace(/ौ/g, 'ाै');
    processedText = processedText.replace(/ॉ/g, 'ाॅ');

    // Handle short i with bindi (िं)
    processedText = processedText.replace(/ि((?:[क-हक़-य़]्)*[क-हक़-य़])[ँं]/g, '$1');

    // Handle Reph (र्) र्
    // In Unicode, 'र्' + Consonant means the Reph flies on top of the Consonant.
    // In Anu Neo, the Reph glyph (byte 220 = ) must be placed AFTER the
    // consonant cluster and its matras. We swap it and directly insert the Reph glyph
    // to avoid conflict with half-Ra (र् = byte 124) in the neoMap.
    const rephRegex = /र्([क-हक़-य़][ा-ौॎ-ॏ]*)/g;
    processedText = processedText.replace(rephRegex, '$1');

    // Now map all substrings to Anu Neo ASCII characters
    const mapKeys = Object.keys(neoMap).sort((a, b) => b.length - a.length);

    for (const key of mapKeys) {
        processedText = processedText.split(key).join(neoMap[key]);
    }

    // Ka () and Pha () need a bridge () to complete their width.
    // In Anu Neo fonts, top/bottom matras AND nasal dots MUST come BEFORE the right vertical stem (bridge).
    // The nasal dots (ं, ँ) are zero-width or negative-offset mapped so that when placed on the half-consonant,
    // they hover exactly where the bridge will be drawn next.
    // Therefore, the bridge must always be inserted AFTER them to render correctly in PageMaker and Word.
    // Items to include before bridge:
    //   े (), ै (), ु (), ू (), ृ (),
    //   ं (), ँ (), ॅ (), nukta (),
    //   ें (), ैं ()
    //
    // Example: कं =  +  +  (Næþ)
    //
    // Right-side structural matras (ा , ी ) and visarga (ः ) extend rightward visually, so bridge comes BEFORE them.
    // Example: का =  +  +  (Nþ + aa), कः =  +  +  (Nþ:)
    //
    // Do NOT add bridge if followed by halant () or existing bridge ().
    const topBottomMatras = '';
    const bridgeRegex = new RegExp(`([][${topBottomMatras}]*)(?![])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1');

    return processedText;
}
