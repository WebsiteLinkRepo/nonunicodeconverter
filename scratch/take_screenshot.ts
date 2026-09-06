import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const inputPath = process.argv[2] || 'scratch/test_gha_nga_ma_ha_candidates.html';
    const outputPath = process.argv[3] || 'scratch/test_gha_nga_ma_ha_candidates.png';
    const htmlPath = path.resolve(inputPath);
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 1600 });
    await page.goto('file://' + htmlPath);
    await page.screenshot({ path: outputPath, fullPage: true });
    await browser.close();
    console.log(`Saved ${outputPath}`);
}
main().catch(console.error);
