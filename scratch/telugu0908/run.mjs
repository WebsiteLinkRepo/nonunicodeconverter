/** Bundles the TS converter and exposes it to the verification scripts. */
import { build } from 'esbuild';
import { writeFileSync } from 'node:fs';
const out = '/tmp/tel0908.mjs';
await build({
  entryPoints: ['src/utils/shreeLipiTelugu0908Converter.ts'],
  bundle: true, format: 'esm', platform: 'node', outfile: out, logLevel: 'error',
});
export const mod = await import(out + '?t=' + Date.now());
export const F = mod.convertUnicodeToShreeLipiTelugu0908;
export const R = mod.convertShreeLipiTelugu0908ToUnicode;
