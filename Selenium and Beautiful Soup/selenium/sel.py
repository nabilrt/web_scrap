from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


start_url = 'https://www.daraz.com.bd/catalog/?_keyori=ss&from=input&q=xioami&spm=a2a0e.searchlist.search.go.5cce6567NTTDQQ&style=list'

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(start_url)

    time.sleep(10)

    phones = driver.find_elements("css selector",'div.title--vuYqg')
    for element in phones:
        model = element.find_element("css selector",'a')
        print(model.text)
