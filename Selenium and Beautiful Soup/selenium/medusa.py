from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


start_url = 'http://localhost:8000/store'

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(start_url)

    time.sleep(10)

    phones = driver.find_elements("css selector",'span.font-semibold')
    for element in phones:
        #model = element.find_element("css selector",'span')
        print(element.text)
