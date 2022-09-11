from tkinter import E
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

start_url='https://en.wikipedia.org/wiki/Tesla,_Inc'

download_url=requests.get(start_url)

soup = BeautifulSoup(download_url.text,'html.parser')

# with open('downloaded.html', 'w', encoding="utf-8") as file:
#     file.write(soup.prettify())

full_table=soup.select('table.wikitable tbody')[0]
# print (full_table)

table_head=full_table.select('tr th')
# for element in table_head:
#     print(element.text)

table_ele=[]
for element in table_head:
    column_label=element.getText(separator=" ",strip=True)
    table_ele.append(column_label)
    #print(column_label)

# print('----')
# print(table_ele)
regex=re.compile('_\[\w\]')
# for element in table_head:
#     column_label=element.getText(separator=" ",strip=True)
#     column_label=column_label.replace(' ','_')
#     column_label=regex.sub('',column_label)
#     table_ele.append(column_label)
#     print(column_label)
# print(table_ele)

table_rows=full_table.select('tr')

table_data=[]

for index,element in enumerate(table_rows):
    if index>0:
        row_list=[]
        values=element.select('td')
        for value in values:
            row_list.append(value.text.strip())
        table_data.append(row_list)
#print(table_data)            

df=pd.DataFrame(table_data,columns=table_ele)
print(df)