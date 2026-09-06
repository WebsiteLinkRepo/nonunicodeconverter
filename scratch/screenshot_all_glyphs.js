import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({width: 1200, height: 800});
  await page.goto('file://' + process.cwd() + '/scratch/all_glyphs.html');
  await page.screenshot({ path: 'scratch/all_glyphs.png' });
  await browser.close();
})();
