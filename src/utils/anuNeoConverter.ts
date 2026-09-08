import { neoMap } from './mappings/neo';
import { upconvertFromANSI } from './pua';

export function unicodeToAnuNeo(text: string): string {
    if (!text) return "";

    let processedText = text;

    const clusterRegex = /((?:[क-हक़-य़]्)*[क-हक़-य़])ि/g;
    processedText = processedText.replace(clusterRegex, 'ि$1');

    processedText = processedText.replace(/ो/g, 'ाे');
    processedText = processedText.replace(/ौ/g, 'ाै');
    processedText = processedText.replace(/ॉ/g, 'ाॅ');

    processedText = processedText.replace(/ि((?:[क-हक़-य़]्)*[क-हक़-य़])[ँं]/g, '$1');

    processedText = processedText.replace(/([टठडढछ])्[रऱ]/g, '$1');
    processedText = processedText.replace(/([टठडढछ])्र/g, '$1');

    const rephRegex = /र्([क-हक़-य़][ा-ौॎ-ॏ]*)/g;
    processedText = processedText.replace(rephRegex, '$1');

    const mapKeys = Object.keys(neoMap).sort((a, b) => b.length - a.length);

    for (const key of mapKeys) {
        processedText = processedText.split(key).join(neoMap[key]);
    }

    const topBottomMatras = '';
    const bridgeRegex = new RegExp(`([][${topBottomMatras}]*)(?![])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1');

    processedText = processedText.replace(//g, '');

    return processedText;
}

const reverseNeoMap: Record<string, string> = {};
reverseNeoMap[''] = '्र';
reverseNeoMap[''] = 'ि_BINDI_'; 
reverseNeoMap[''] = 'र्';

for (const [key, value] of Object.entries(neoMap)) {
    if (value && key && !reverseNeoMap[value]) {
        reverseNeoMap[value] = key;
    }
}
const reverseNeoKeys = Object.keys(reverseNeoMap).sort((a, b) => b.length - a.length);

export function anuNeoToUnicode(text: string): string {
    if (!text) return "";

    text = upconvertFromANSI(text);

    let processedText = text;

    processedText = processedText.replace(//g, '');
    processedText = processedText.replace(//g, '');

    let result = '';
    let i = 0;
    while(i < processedText.length) {
        let matched = false;
        for (const key of reverseNeoKeys) {
            if (processedText.startsWith(key, i)) {
                result += reverseNeoMap[key];
                i += key.length;
                matched = true;
                break;
            }
        }
        if (!matched) {
            result += processedText[i];
            i++;
        }
    }

    result = result.replace(/([क-हक़-य़][ा-ौॎ-ॏ]*)र्/g, 'र्$1');

    result = result.replace(/ि_BINDI_((?:[क-हक़-य़]्)*[क-हक़-य़])/g, '$1िं');
    result = result.replace(/ि_BINDI_/g, 'िं');

    result = result.replace(/ि((?:[क-हक़-य़]्)*[क-हक़-य़])/g, '$1ि');

    result = result.replace(/ाे/g, 'ो');
    result = result.replace(/ाै/g, 'ौ');
    result = result.replace(/ाॅ/g, 'ॉ');

    return result;
}
