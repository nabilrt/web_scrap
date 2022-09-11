import asyncio
from pyppeteer import launch

async def get_article_titles():
   # launch browser in headless mode
   browser = await launch({"headless": False, "args": ["--start-maximized"]})
   # create a new page
   page = await browser.newPage()
   # set page viewport to the largest size
   await page.setViewport({"width": 1600, "height": 900})
   # navigate to the page
   await page.goto("http://localhost:8000/store")
   # locate the phone titles
   topics = await page.querySelectorAll("div.text-base-regular span")
   for topic in topics:
           title = await topic.getProperty("textContent")
           # print the article titles
           print(await title.jsonValue())


print("Starting...")
asyncio.get_event_loop().run_until_complete(
   get_article_titles()
)
