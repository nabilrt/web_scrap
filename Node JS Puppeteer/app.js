const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on");

  title = await page.evaluate(() => {
    return document.querySelector("._4rR01T").textContent.trim();
  });
  console.log(title);
  await browser.close();
})();
