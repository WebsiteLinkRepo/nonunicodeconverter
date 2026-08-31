const fs = require('fs');
const opentype = require('opentype.js');

function inspect(fontPath) {
  try {
    const buffer = fs.readFileSync(fontPath).buffer;
    const font = opentype.parse(buffer);
    console.log(`Loaded ${fontPath}`);
    const glyphs = font.glyphs.glyphs;
    const keys = Object.keys(glyphs);
    console.log(`Glyph count: ${keys.length}`);
    let namedGlyphs = 0;
    for (const key of keys) {
      const g = glyphs[key];
      if (g.name && g.name !== '.notdef') {
        namedGlyphs++;
        if (namedGlyphs <= 40) {
          console.log(`Glyph ${key}: name=${g.name}, unicode=${g.unicode}, unicodes=${g.unicodes}`);
        }
      }
    }
    console.log(`Total named glyphs: ${namedGlyphs}`);
  } catch (err) {
    console.error(err);
  }
}

inspect('public/Fonts folder/AnuSM/ttf/MANGAL.TTF?v=2');
inspect('public/Fonts folder/AnuSM/ttf/PADMINI_.TTF?v=2');
