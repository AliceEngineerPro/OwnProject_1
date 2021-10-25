import requests
import json
from bs4 import BeautifulSoup
from bs4.element import Tag


url_list = [
    # 'https://github.com',
    'https://baidu.com',
]

proxy = {
    'http': 'http://127.0.0.1:1080',
}

# def url_index(url):
#     address = ''
#     for index in url:
#         address = index
#     return address


response = requests.request(
    method='GET',
    # url=url_index(url_list)
    url=url_list[0],
    # proxies=proxy,
    allow_redirects=True,
    timeout=(500, 3000),
    verify=True,
)

response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, features='lxml')
# 所有子标签
tag_body_children = soup.find(name='body').children
# 所有

# print(soup)
for body in tag_body_children:
    if type(body) == Tag:
        print(body, type(body))
    else:
        print('...')

