import pprint
import asyncio
from pyppeteer import launch


async def get_browser():
    return await launch({"headless": False})


async def get_page(browser, url):
    page = await browser.newPage()
    await page.goto(url)
    return page


async def extract_data(page):
    # Select tr with a th and td descendant from table
    elements = await page.xpath(
        '//table[@class="infobox"]/tbody/tr[th and td]')
    # Extract data
    result = {}
    for element in elements:
        title, content = await page.evaluate(
            '''(element) =>
                [...element.children].map(child => child.textContent)''',
            element)
        result.update({title: content})
    return result


async def extract(browser, name, url):
    page = await get_page(browser, url)
    return {name: await extract_data(page)}


async def extract_all(languages):
    browser = await get_browser()
    result = {}
    for name, url in languages.items():
        result.update(await extract(browser, name, url))
    return result


if __name__ == "__main__":
    languages = {
        "python": "https://en.wikipedia.org/wiki/Python"
    }

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(extract_all(languages))

    pprint.pprint(result)