import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file://' + process.cwd() + '/scratch/render_all.html');
  await page.screenshot({ path: 'scratch/all_chars.png' });
  await browser.close();
})();
