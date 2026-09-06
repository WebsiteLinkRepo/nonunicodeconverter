import puppeteer from 'puppeteer';
import path from 'path';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(`file://${path.resolve('scratch/test_space2.html')}`);
  await page.screenshot({path: 'scratch/test_space2.png'});
  await browser.close();
})();
