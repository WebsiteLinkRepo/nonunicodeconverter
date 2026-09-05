/**
 * Annotated side-by-side comparison sheet, rendered in Chromium.
 *
 *   node scratch/telugu0908/cmpsheet.mjs rows.json out.png
 *
 * rows.json = [{ "label":"ka", "ref":"క", "cands":[{"id":"0x4d+tk","text":"Mæ"}, ...] }]
 *
 * Left cell is the Unicode reference in Noto Serif Telugu (real GSUB shaping); the rest
 * are legacy candidates in the sanitised Shree-Tel face, each captioned with its plat3
 * recipe. The matcher only ever produces a shortlist - this sheet is what the call is
 * actually made on.
 */
import { chromium } from 'playwright';
import { readFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';

const rows = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const out = process.argv[3] ?? 'scratch/telugu0908/out/cmp.png';
const SIZE = Number(process.env.SIZE ?? 46);
const LEGACY = resolve(process.env.LEGACY_TTF ?? 'public/SHREE-TEL-web.ttf');
const B64 = readFileSync(LEGACY).toString('base64');
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const body = rows.map((r) => `
  <div class="row">
    <div class="lab">${esc(r.label ?? '')}</div>
    <div class="cell ref"><div class="ink noto">${esc(r.ref)}</div><div class="cap">ref</div></div>
    ${r.cands.map((c) => `<div class="cell"><div class="ink leg">${esc(c.text)}</div>
       <div class="cap">${esc(c.id)}</div></div>`).join('')}
  </div>`).join('');

const html = `<!doctype html><meta charset="utf-8"><style>
  @font-face { font-family:'LEG'; src:url(data:font/ttf;base64,${B64}) format('truetype') }
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:#fff;font:12px/1.2 monospace}
  .row{display:flex;align-items:flex-end;border-bottom:1px solid #e8e8e8;padding:6px 4px}
  .lab{width:78px;color:#a00;font-weight:700;align-self:center}
  .cell{min-width:${Math.round(SIZE * 2.4)}px;padding:0 8px;text-align:center;border-left:1px solid #f0f0f0}
  .cell.ref{background:#f4f8ff;border-left:2px solid #9bf}
  .ink{font-size:${SIZE}px;line-height:1.35;white-space:pre;height:${Math.round(SIZE * 1.5)}px}
  .noto{font-family:'Noto Serif Telugu'} .leg{font-family:'LEG'}
  .cap{color:#666;font-size:11px;padding-top:2px}
</style>${body}`;

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2 });
await page.setContent(html);
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(120);
mkdirSync(dirname(resolve(out)), { recursive: true });
await page.screenshot({ path: out, fullPage: true });
await browser.close();
console.log(out, rows.length, 'rows');
