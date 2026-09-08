import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import obfuscator from 'vite-plugin-javascript-obfuscator';

// https://astro.build/config
export default defineConfig({
  site: 'https://unicode2nonunicode.com',
  integrations: [sitemap()],
  vite: {
    plugins: [
      tailwindcss(),
      // Only obfuscate in production to keep development fast
      process.env.NODE_ENV === 'production' && obfuscator({
        include: ['src/utils/converter.ts', 'src/utils/security.ts', 'src/utils/*Converter.ts'], // Obfuscate logic, but exclude massive mappings arrays to prevent OOM
        exclude: [/node_modules/, /mappings/],
        apply: 'build',
        options: {
          compact: true,
          // Lowered control flow to prevent OOM
          controlFlowFlattening: true,
          controlFlowFlatteningThreshold: 0.1,
          deadCodeInjection: false, // Disabled to prevent OOM
          debugProtection: false,
          disableConsoleOutput: true,
          identifierNamesGenerator: 'hexadecimal',
          log: false,
          numbersToExpressions: true,
          renameGlobals: false,
          selfDefending: true,
          simplify: true,
          splitStrings: false, // Too memory intensive
          stringArray: true,
          stringArrayCallsTransform: true,
          stringArrayCallsTransformThreshold: 0.5,
          stringArrayEncoding: ['base64'], // Simplified from rc4 due to massive string arrays
          stringArrayIndexShift: true,
          stringArrayRotate: true,
          stringArrayShuffle: true,
          stringArrayWrappersCount: 1,
          stringArrayWrappersChainedCalls: true,
          stringArrayWrappersParametersMaxCount: 2,
          stringArrayWrappersType: 'variable',
          stringArrayThreshold: 0.8,
          transformObjectKeys: true,
          unicodeEscapeSequence: false
        }
      })
    ]
  }
});