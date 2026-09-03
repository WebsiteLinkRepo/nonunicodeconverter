import { SHREE_LIPI_MAPPINGS } from './mappings/shreeLipi';

/**
 * Converts Unicode Devanagari Hindi/Marathi text to Shree-Lipi (Shree-Dev7) legacy encoding.
 */
export function unicodeToShreeLipi(text: string, language: "hindi" | "marathi" = "hindi"): string {
    if (!text) return "";

    let result = text;

    // 0. Normalizations
    result = result.split("—").join("–");
    result = result.split("‘").join("\"");
    result = result.split("’").join("\x27");

    // 1. Eyelash Ra mappings
    result = result.split("ऱ्हा").join("èhm");
    result = result.split("ऱ्ह").join("èh");
    result = result.split("ऱ्").join("è");
    result = result.split("कुऱ्हाड").join("Hw$èhmS>");

    // 2. Specific complex conjuncts
    result = result.split("उच्छ्वास").join("CÀN²>dmg");
    result = result.split("वैशिष्ट्य").join("d¡{eï²`");
    result = result.split("स्फूर्ति").join("ñ\\y${V©");
    result = result.split("स्फू").join("ñ\\y$");
    result = result.split("आर्द्र").join("AmÐ©");
    result = result.split("र्द्र").join("Ð©");
    result = result.split("च्छ्र").join("ÀN>«");
    result = result.split("ज्ञ्य").join("k²`");
    result = result.split("क्त्य").join("º²$`");
    result = result.split("ञ्च").join("ÄM");
    result = result.split("ञ्छ").join("ÄN>");
    result = result.split("ञ्ज").join("ÄO");
    result = result.split("ञ्झ").join("ÄP");
    result = result.split("त्त्त्य").join("ÎË`");
    result = result.split("त्म्य").join("Ëå`");
    result = result.split("त्स्न").join("ËñZ");
    result = result.split("त्स्य").join("Ëñ`");
    result = result.split("द्र्य").join("Ú©");
    result = result.split("ष्ट्य").join("ï²`");

    // 3. Halant Lla before consonants -> ù (Marathi specific)
    if (language === "marathi") {
        result = result.replace(/ळ्([क-हक़-य़])/g, "ù$1");
    }
    result = result.split("ळ्").join("i~");

    // 4. Normalize Decomposed Nuktas
    result = result.split('ड़').join('‹S>');
    result = result.split('ढ़').join('‹T>');

    // 5. Reorder short 'i' + anusvara (िं) and short 'i' (ि)
    const iAnusvaraRegex = /((?:[क-हक़-य़]्)*[क-हक़-य़])िं/g;
    result = result.replace(iAnusvaraRegex, '{$1§');

    const iRegex = /((?:[क-हक़-य़]्)*[क-हक़-य़])ि/g;
    result = result.replace(iRegex, '{$1');

    // 6. Handle composite vowel matras
    result = result.split('ो').join('mo');
    result = result.split('ौ').join('m¡');
    result = result.split('ॉ').join('m°');
    result = result.split('ों').join('mo§');
    result = result.split('ें').join('o§');
    result = result.split('ैं').join('¢');

    // 7. Apply the mapped entries
    for (const entry of SHREE_LIPI_MAPPINGS) {
        if (entry.from && result.includes(entry.from)) {
            result = result.split(entry.from).join(entry.to);
        }
    }

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

    // Fix top matras on right-bracket glyphs
    result = result.replace(/([QTRNSL])>([o¡¢])/g, '$1$2>');
    result = result.replace(/‹([QTRNSL])>([o¡¢])/g, '‹$1$2>');

    // Final short-i fix
    result = result.replace(/\{([ñŠßÝËã½¿ÀÁÊÜäåîùƒ])/g, "p$1");

    // Specific formatting patches
    result = result.split("{H$§").join("qH$");
    result = result.split("{R>§").join("qR>");
    result = result.split("{S>§").join("qS>");
    result = result.split("{T>§").join("qT>");
    result = result.split("{a§").join("qa");
    result = result.split("{i§").join("qi");

    return result;
}
