import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({headless: "new"});
  const page = await browser.newPage();
  await page.setViewport({width: 1200, height: 600});
  await page.goto('file://' + process.cwd() + '/scratch/render_all2.html');
  await page.screenshot({path: 'scratch/all_chars2.png'});
  await browser.close();
})();
