import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const htmlPath = path.resolve('scratch/test_gha_nga_ma_ha_clean.html');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 800, height: 1200 });
    await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
    const screenshot = await page.screenshot({ fullPage: true });
    fs.writeFileSync('scratch/gha_nga_ma_ha_clean.png', screenshot);
    await browser.close();
    console.log("Saved scratch/gha_nga_ma_ha_clean.png");
}

main().catch(console.error);
