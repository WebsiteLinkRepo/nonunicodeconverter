import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const textPath = path.resolve('scratch/test_compare.html');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1400, height: 1600 });
    await page.goto('file://' + textPath, { waitUntil: 'networkidle0' });
    
    await page.evaluateHandle('document.fonts.ready');
    
    const screenshot = await page.screenshot({ fullPage: true });
    fs.writeFileSync('scratch/compare_result.png', screenshot);
    await browser.close();
    console.log("Saved scratch/compare_result.png");
}

main().catch(console.error);
