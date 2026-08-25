const comp = 'POã^ Îã„¬^Í‰˜ =°i†Çò `³ OQê} ~Œã‘ “ …Õ `³ °Q®° ƒ ì+¬#° J`Ç¼O`Ç ‹¬°O^Î~¡OQê =¶\\ìÁ_È°`Œ~¡°  ª ~¡Þƒ º=°`ÇÞO`Ë =òO^Î°ä›½ "³ˆìíO.';
const my = 'POã^ Îã„¬^Í‰˜ =°i†Çò `³ OQê} ~Œã‘ “ …Õ `³ °Q®° ƒ ì+¬#° J`Ç¼O`Ç ‹¬°O^Î~¡OQê =¶\\ìÁ_È°`Œ~¡°; ª ~¡Þƒ º=°`ÇÞO`Ë =òO^Î°ä›½ "³ˆìíO.';

for (let i = 0; i < comp.length; i++) {
    if (comp[i] !== my[i]) {
        console.log(`Mismatch at index ${i}: comp='${comp[i]}' (code ${comp.charCodeAt(i)}) vs my='${my[i]}' (code ${my.charCodeAt(i)})`);
    }
}
