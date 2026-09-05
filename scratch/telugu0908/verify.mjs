/**
 * Full-coverage verification. Renders every cluster the tables can produce twice - the
 * Unicode string in Noto Serif Telugu (real HarfBuzz shaping) and the converter's legacy
 * output in the sanitised Shree-Tel face - and reports the ones that do not match.
 *
 *   node scratch/telugu0908/verify.mjs roundtrip   # pure logic, no rendering
 *   node scratch/telugu0908/verify.mjs spec > /tmp/spec.json   # emit cases for bmatch
 */
import { F, R } from './run.mjs';

const CONS = [...'కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలళవశషసహఱ'];
const VOW = [...'అఆఇఈఉఊఋౠఎఏఐఒఓఔ'];
const MAT = ['', 'ా', 'ి', 'ీ', 'ు', 'ూ', 'ృ', 'ె', 'ే', 'ై', 'ొ', 'ో', 'ౌ'];

function cases() {
  const out = [];
  for (const v of VOW) out.push(v);
  for (const c of CONS) for (const m of MAT) out.push(c + m);
  for (const c of CONS) out.push(c + '్');
  for (const a of CONS) for (const b of CONS) out.push(a + '్' + b);
  for (const c of CONS) { out.push(c + 'ం'); out.push(c + 'ః'); }
  out.push('క్ష', 'శ్రీ', 'క్షి', 'క్ష్మ');
  return out;
}

const mode = process.argv[2] ?? 'roundtrip';
const all = cases();

if (mode === 'roundtrip') {
  let bad = 0, empty = 0, unmapped = 0;
  for (const s of all) {
    const f = F(s);
    if (!f.text) { empty += 1; console.log('EMPTY     ', s); continue; }
    if (f.unmapped.length) { unmapped += 1; if (unmapped <= 20) console.log('UNMAPPED  ', s, f.unmapped.join('')); }
    const r = R(f.text);
    if (r.text !== s) { bad += 1; if (bad <= 40) console.log('ROUNDTRIP ', s, '->', JSON.stringify(f.text), '->', r.text); }
  }
  console.log(`\n${all.length} cases: ${bad} round-trip failures, ${empty} empty, ${unmapped} with unmapped parts`);
  process.exit(bad || empty ? 1 : 0);
}

if (mode === 'sheet') {
  // Reference above, converter output below, same cell - the only check that matters in the
  // end is whether a Telugu reader recognises the bottom row as the top row.
  const { writeFileSync, readFileSync, mkdirSync } = await import('node:fs');
  const worst = process.env.WORST
    ? new Set(JSON.parse(readFileSync('scratch/telugu0908/paired_scores.json', 'utf8'))
        .slice(0, Number(process.env.WORST)).map(([, id]) => id))
    : null;
  const pick = all.filter((s) => (worst ? worst.has(s) : true));
  const items = [];
  for (const s of pick) {
    const f = F(s);
    if (!f.text) continue;
    items.push({ id: `u:${s}`, text: s, font: 'noto' });
    items.push({ id: `l:${s}`, text: f.text, font: 'legacy' });
  }
  mkdirSync('scratch/telugu0908/out', { recursive: true });
  writeFileSync('/tmp/sheet_items.json', JSON.stringify(items));
  const { execFileSync } = await import('node:child_process');
  execFileSync('node', ['scratch/telugu0908/refsheet.mjs', '/tmp/sheet_items.json',
                        'scratch/telugu0908/out/contact'],
               { stdio: 'inherit', env: { ...process.env, COLS: '16', SIZE: '44' } });
  console.log(`${items.length / 2} clusters, reference and output interleaved`);
  process.exit(0);
}

if (mode === 'spec') {
  const refs = [], cands = [];
  for (const s of all) {
    const f = F(s);
    if (!f.text) continue;
    refs.push({ id: s, text: s });
    cands.push({ id: s, text: f.text });
  }
  console.log(JSON.stringify({ refs, cands, reffont: 'noto' }));
}
