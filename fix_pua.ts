import fs from 'fs';
import path from 'path';

const win1252_to_unicode: { [key: number]: number } = {
    128: 0x20AC, 129: 0x0081, 130: 0x201A, 131: 0x0192,
    132: 0x201E, 133: 0x2026, 134: 0x2020, 135: 0x2021,
    136: 0x02C6, 137: 0x2030, 138: 0x0160, 139: 0x2039,
    140: 0x0152, 141: 0x008D, 142: 0x017D, 143: 0x008F,
    144: 0x0090, 145: 0x2018, 146: 0x2019, 147: 0x201C,
    148: 0x201D, 149: 0x2022, 150: 0x2013, 151: 0x2014,
    152: 0x02DC, 153: 0x2122, 154: 0x0161, 155: 0x203A,
    156: 0x0153, 157: 0x009D, 158: 0x017E, 159: 0x0178
};

const filesToFix = ['anu6.ts', 'anu7.ts', 'neo.ts', 'shreeLipi.ts', 'nudiKannada.ts', 'baminiTamil.ts', 'ismMalayalam.ts'];
const dir = './src/utils/mappings';

for (const file of filesToFix) {
    const p = path.join(dir, file);
    if (!fs.existsSync(p)) continue;
    
    let content = fs.readFileSync(p, 'utf-8');
    let modified = false;
    
    // 1. Replace raw PUA characters
    let newContent = content.replace(/[\uF000-\uF0FF]/g, match => {
        modified = true;
        let code = match.charCodeAt(0);
        let winByte = code - 0xF000;
        
        let charToInsert = '';
        if (winByte >= 128 && winByte <= 159) {
            charToInsert = String.fromCharCode(win1252_to_unicode[winByte]);
        } else {
            charToInsert = String.fromCharCode(winByte);
        }
        
        if (charToInsert === '\\') return '\\\\';
        if (charToInsert === '"') return '\\"';
        if (charToInsert === "'") return "\\'";
        if (charToInsert === '\n') return "\\n";
        if (charToInsert === '\r') return "\\r";
        return charToInsert;
    });

    // 2. Replace escaped PUA characters like \uF040
    newContent = newContent.replace(/\\uF0([0-9A-Fa-f]{2})/g, (match, hex) => {
        modified = true;
        let winByte = parseInt(hex, 16);
        
        let charToInsert = '';
        if (winByte >= 128 && winByte <= 159) {
            charToInsert = String.fromCharCode(win1252_to_unicode[winByte]);
        } else {
            charToInsert = String.fromCharCode(winByte);
        }
        
        if (charToInsert === '\\') return '\\\\';
        if (charToInsert === '"') return '\\"';
        if (charToInsert === "'") return "\\'";
        if (charToInsert === '\n') return "\\n";
        if (charToInsert === '\r') return "\\r";
        
        return charToInsert;
    });

    if (modified) {
        fs.writeFileSync(p, newContent, 'utf-8');
        console.log(`Fixed ${file}`);
    }
}
