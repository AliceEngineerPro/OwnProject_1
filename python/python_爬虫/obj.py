import uuid

import requests
from bs4 import BeautifulSoup
import re
import uuid
import os


response = requests.get(
    url='https://www.autohome.com.cn/news/'
)

response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, features='html.parser')
target = soup.find(id='auto-channel-lazyload-article')
li_list = target.find_all('li')

print(os.getcwd())

for i in li_list:
    a = i.find('a')
    if a:
        txt = a.find('h3').text
        print(txt)

        row_url = a.attrs.get('href')
        if re.findall('^https:', row_url):
            pass
        else:
            row_url = 'https:' + row_url
        print(row_url)

        img_url = a.find('img').attrs.get('src')
        if re.findall('^https:', img_url):
            pass
        else:
            img_url = 'https:' + img_url
        print(img_url)

        img_response = requests.get(url=img_url)
        # img_name = txt + '.jpg'
        img_name = './loads/' + str(uuid.uuid4()) + '.jpg'
        with open(file=img_name, mode='wb') as f:
            f.write(img_response.content)
