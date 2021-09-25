import requests
import json
from bs4 import BeautifulSoup


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
tag_a = soup.find_all(name='a')
for a in tag_a:
    tag_a_attrs = a.attrs.get('href')
    print(tag_a_attrs)

# response.headers = dict(response.headers)
# headers = json.dumps(response.headers, indent=4)
# print(headers)
