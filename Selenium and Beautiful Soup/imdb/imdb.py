import requests
from bs4 import BeautifulSoup
import pandas as pd



start_url = 'https://www.imdb.com/search/title/?genres=Thriller&ref_=nv_sr_srsg_0'

# Download the HTML from start_url
downloaded_html = requests.get(start_url)

# Parse the HTML with BeautifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.text,'html.parser')


movie_titles  = soup.select('h3.lister-item-header a')
movie_genres  = soup.select('span.genre')

m_t=[]
m_g=[]

for element in movie_titles:
    m_t.append(element.get_text().strip())

for element in movie_genres:
    m_g.append(element.get_text().strip())

import csv 
with open('./top-50-thriller-imdb.csv', 'wb') as csvfile: 
    writer = csv.writer(csvfile)  
    writer.writerow(m_t) 
    writer.writerow(m_g) 







