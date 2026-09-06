import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const textPath = path.resolve('scratch/test_vattu2.html');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1400, height: 2600 });
    await page.goto('file://' + textPath, { waitUntil: 'networkidle0' });
    
    await page.evaluateHandle('document.fonts.ready');
    
    const screenshot = await page.screenshot({ fullPage: true });
    fs.writeFileSync('scratch/vattu2_result.png', screenshot);
    await browser.close();
}
main();
