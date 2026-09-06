import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file://' + process.cwd() + '/scratch/render_specific2.html');
  await page.screenshot({ path: 'scratch/specific2.png' });
  await browser.close();
})();
