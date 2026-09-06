import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const textPath = path.resolve('scratch/render_all_candidates.html');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1400, height: 2600 });
    await page.goto('file://' + textPath, { waitUntil: 'networkidle0' });
    
    // Evaluate if fonts loaded
    await page.evaluateHandle('document.fonts.ready');
    
    const screenshot = await page.screenshot({ fullPage: true });
    fs.writeFileSync('scratch/all_candidates.png', screenshot);
    await browser.close();
    console.log("Saved scratch/all_candidates.png");
}

main().catch(console.error);
