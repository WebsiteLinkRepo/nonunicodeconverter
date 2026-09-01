import { SHREE_LIPI_MAPPINGS } from './mappings/shreeLipi';

/**
 * Converts Unicode Devanagari Hindi text to Shree-Lipi (Shree-Dev7) legacy encoding.
 * Uses greedy token replacement along with pre-reordering logic for accurate conversion
 * matching standard 1-to-1 competitor tools.
 */
export function unicodeToShreeLipi(text: string): string {
    if (!text) return "";

    let result = text;

    // 1. Normalize Decomposed Nuktas
    result = result.split('ड़').join('‹S>');
    result = result.split('ढ़').join('‹T>');

    // 2. Reorder short 'i' + anusvara (िं) and short 'i' (ि)
    // Convert cluster + िं -> {cluster§
    const iAnusvaraRegex = /((?:[क-हक़-य़]्)*[क-हक़-य़])िं/g;
    result = result.replace(iAnusvaraRegex, '{$1§');

    // Convert cluster + ि -> {cluster
    const iRegex = /((?:[क-हक़-य़]्)*[क-हक़-य़])ि/g;
    result = result.replace(iRegex, '{$1');

    // 3. Handle composite vowel matras
    result = result.split('ो').join('mo');
    result = result.split('ौ').join('m¡');
    result = result.split('ॉ').join('m°');
    result = result.split('ों').join('mo§');
    result = result.split('ें').join('o§');
    result = result.split('ैं').join('¢');

    // 4. Apply the mapped entries longest-first
    // (they are already generated and sorted in SHREE_LIPI_MAPPINGS)
    for (const entry of SHREE_LIPI_MAPPINGS) {
        if (entry.from && result.includes(entry.from)) {
            result = result.split(entry.from).join(entry.to);
        }
    }

    // Additional Standalone Fallbacks are now in SHREE_LIPI_MAPPINGS
    // but keep as a safety net in case they were missed
    const fallbacks: Record<string, string> = {
        '।': '&', '॥': '&&', 'ा': 'm', 'ी': 'r', 'ु': 'w', 'ू': 'y',
        'ृ': '¥', 'ॄ': '¦', 'े': 'o', 'ै': '¡', 'ं': '§', 'ः': '…',
        'ँ': '±', 'ॅ': '°', '्': '²', '़': 'µ', '|': '&',
        '१': '1', '२': '2', '३': '3', '४': '4', '५': '5',
        '६': '6', '७': '7', '८': '8', '९': '9', '०': '0',
    };
    for (const [k, v] of Object.entries(fallbacks)) {
        result = result.split(k).join(v);
    }

    // 5. Fix top matras on right-bracket glyphs (e.g. ट, ठ, ड, ढ shifted left visually)
    // S>o -> So>
    result = result.replace(/([QTRNSL])>([o¡¢])/g, '$1$2>');
    result = result.replace(/‹([QTRNSL])>([o¡¢])/g, '‹$1$2>');

    // 6. Specific structural fixes post-processing
    // {H$§ -> qH$ (short 'i' with anusvara on standard width characters)
    result = result.split('{H$§').join('qH$');
    result = result.split('{R>§').join('qR>');
    result = result.split('{S>§').join('qS>');
    result = result.split('{T>§').join('qT>');
    result = result.split('{a§').join('qa');
    result = result.split('{i§').join('qi');

    return result;
}
