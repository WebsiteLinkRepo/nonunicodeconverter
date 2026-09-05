/**
 * Renders text in Chromium so the Unicode side gets real HarfBuzz shaping, which the
 * Python rasteriser cannot do (Telugu matras and conjuncts need GSUB).
 *
 * Reads a JSON array on stdin (or from argv[2]):
 *   [{ "id": "ka-u", "text": "కు", "font": "noto" }, { "id": "cand-1", "text": "Mî", "font": "legacy" }]
 *
 * Writes <out>.png (one screenshot of a deterministic grid) and <out>.json (per-id
 * bounding boxes) so Python can crop each cell and score it.
 *
 *   node scratch/telugu0908/refsheet.mjs items.json scratch/telugu0908/out/ref
 */
import { chromium } from 'playwright';
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';

const itemsPath = process.argv[2];
const outBase = process.argv[3] ?? 'scratch/telugu0908/out/ref';
const items = JSON.parse(readFileSync(itemsPath, 'utf8'));

// Inline the legacy face as a data: URL. A file:// @font-face is blocked by Chromium's
// CORS check on a setContent page (opaque origin), which fails silently: the text just
// renders in a Latin fallback and every score comes out as noise.
const LEGACY = resolve(process.env.LEGACY_TTF ?? 'public/SHREE-TEL-web.ttf');
const LEGACY_B64 = readFileSync(LEGACY).toString('base64');
const COLS = Number(process.env.COLS ?? 12);
const SIZE = Number(process.env.SIZE ?? 56);
// ALIGN=left pins every cell's text origin to the same offset inside its cell, which is
// what dsearch.py needs: with the default centred layout, adding a mark shifts the base
// sideways, so subtracting one render from another leaves ghost outlines instead of the
// mark. Generous padding keeps marks that draw to the left of the origin inside the crop.
const LEFT = process.env.ALIGN === 'left';

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const cells = items.map((it, i) => `
  <div class="cell">
    <div class="ink ${it.font}" id="c${i}">${esc(it.text)}</div>
  </div>`).join('');

const html = `<!doctype html><meta charset="utf-8"><style>
  @font-face { font-family: 'LEG'; src: url(data:font/ttf;base64,${LEGACY_B64}) format('truetype'); }
  * { margin:0; padding:0; box-sizing:border-box }
  body { background:#fff }
  .grid { display:grid; grid-template-columns: repeat(${COLS}, ${Math.round(SIZE * 3.2)}px); }
  .cell { height:${Math.round(SIZE * 2.4)}px; display:flex;
          align-items:${LEFT ? 'flex-start' : 'center'};
          justify-content:${LEFT ? 'flex-start' : 'center'};
          padding:${LEFT ? `${Math.round(SIZE * 0.6)}px 0 0 ${Math.round(SIZE * 0.9)}px` : '0'};
          border:1px solid #eee; overflow:${LEFT ? 'visible' : 'hidden'} }
  .ink { font-size:${SIZE}px; line-height:1.4; white-space:pre; color:#000 }
  .noto { font-family:'Noto Serif Telugu' }
  .notosans { font-family:'Noto Sans Telugu' }
  .legacy { font-family:'LEG' }
</style><div class="grid">${cells}</div>`;

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2 });
await page.setContent(html);
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(150);

const boxes = {};
for (let i = 0; i < items.length; i++) {
  const el = await page.$(`#c${i}`);
  const b = await el.boundingBox();
  boxes[items[i].id] = { ...b, text: items[i].text, font: items[i].font };
}
mkdirSync(dirname(outBase), { recursive: true });
await page.screenshot({ path: `${outBase}.png`, fullPage: true });
writeFileSync(`${outBase}.json`, JSON.stringify({ scale: 2, boxes }, null, 1));
await browser.close();
console.log(`${outBase}.png  ${items.length} cells`);
