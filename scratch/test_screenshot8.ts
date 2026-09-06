import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const htmlPath = path.resolve('scratch/test_gha_nga_ma_ha_clean.html');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 800, height: 1600 });
    // Wait for the font to load by using networkidle0
    await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });
    
    // Inject a tiny script to wait specifically for fonts if needed,
    // though networkidle0 usually catches local fonts.
    await page.evaluateHandle('document.fonts.ready');
    
    // Take screenshot of the exact content area
    const bodyHandle = await page.$('body');
    const { width, height } = await bodyHandle.boundingBox();
    const screenshot = await page.screenshot({ 
        clip: { x: 0, y: 0, width: Math.max(width, 800), height: Math.ceil(height) + 100 }
    });
    fs.writeFileSync('scratch/gha_nga_ma_ha_clean3.png', screenshot);
    await browser.close();
    console.log("Saved scratch/gha_nga_ma_ha_clean3.png");
}

main().catch(console.error);
