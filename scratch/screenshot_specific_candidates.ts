import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const textPath = path.resolve('scratch/test_gha_nga_ma_ha_candidates.html');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1000, height: 1600 });
    await page.goto('file://' + textPath, { waitUntil: 'networkidle0' });
    
    await page.evaluateHandle('document.fonts.ready');
    
    const screenshot = await page.screenshot({ fullPage: true });
    fs.writeFileSync('scratch/gha_nga_ma_ha_search.png', screenshot);
    await browser.close();
    console.log("Saved scratch/gha_nga_ma_ha_search.png");
}

main().catch(console.error);
