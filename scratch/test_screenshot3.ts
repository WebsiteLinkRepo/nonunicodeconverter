import puppeteer from 'puppeteer';
import * as fs from 'fs';
import * as path from 'path';

async function main() {
    const textStr = "Mæ Q Væ œè \\ ^æ bæ f m p r uæ yæ Éæ × ™æ £æ §æ «§æ ¯è ³ ¸ º ¿æ ˜ Äç Ææ Ë Ðè Ôæ Ù Ü à âæ „æ ‚";
    const html = `
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @font-face {
                font-family: 'Shree-Tel';
                src: url('file://${path.resolve('public/SHREE-TEL-web.ttf')}');
            }
            body { font-family: 'Shree-Tel', serif; font-size: 72px; padding: 20px; text-align: left; background: white; white-space: pre-wrap; line-height: 1.5; }
        </style>
    </head>
    <body>
        ${textStr}
    </body>
    </html>
    `;
    const htmlPath = path.resolve('scratch/temp_alphabet.html');
    fs.writeFileSync(htmlPath, html);

    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('file://' + htmlPath);
    const bodyHandle = await page.$('body');
    const { width, height } = await bodyHandle.boundingBox();
    const screenshot = await page.screenshot({ 
        clip: { x: 0, y: 0, width: Math.ceil(width) + 40, height: Math.ceil(height) + 40 }
    });
    fs.writeFileSync('scratch/alphabet.png', screenshot);
    await browser.close();
    console.log("Saved scratch/alphabet.png");
}

main().catch(console.error);
