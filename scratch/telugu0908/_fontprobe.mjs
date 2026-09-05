import { chromium } from 'playwright';
import { readFileSync } from 'node:fs';
const files = process.argv.slice(2);
const b = await chromium.launch();
const p = await b.newPage();
p.on('console', m => console.log('  console:', m.text()));
await p.setContent('<div id=x>x</div>');
for (const f of files) {
  const b64 = readFileSync(f).toString('base64');
  const r = await p.evaluate(async ([name, b64]) => {
    try {
      const ff = new FontFace(name, `url(data:font/ttf;base64,${b64})`);
      await ff.load();
      document.fonts.add(ff);
      return 'LOADED ' + ff.status;
    } catch (e) { return 'FAILED ' + e.name + ': ' + e.message; }
  }, [f, b64]);
  console.log(f, '->', r);
}
await b.close();
