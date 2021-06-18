"""
爬虫流程
    1. 下载页面
        url = https://www.autohome.com.cn/news/

    2. 筛选
        正则表达式

    ======================
    requests

    beautisoup

"""
import re
import time
import requests
from bs4 import BeautifulSoup
import uuid

# requests 模块
url_list = [
    'https://www.autohome.com.cn/news/',
    'https://www.autohome.com.cn/news/2/#liststart',

]


response = requests.get(
    url=url_list[0]

)

response.encoding = response.apparent_encoding
# print(response.text)

# beautisoup 模块
soup = BeautifulSoup(response.text, features='html.parser')
tag = soup.find(id='auto-channel-lazyload-article')
li_list = tag.find_all('li')
s_number = 139

for i in li_list:
    a = i.find('a')
    s_number += 1
    print(s_number)
    if a:
        msg_url = 'https:' + a.attrs.get('href')
        print(msg_url)
        h3 = a.find('h3')
        if h3:
            txt = h3.text  # 加.text后去标签, 类型改为srt
            print(txt)
        img = a.find('img').attrs.get('src')
        if re.findall('^https:', img):
            img = img
        else:
            img = 'https:' + img
        print(img)
        print()

        # # 下载图片
        #
        # img_response = requests.get(
        #     url=img
        #
        # )
        #
        # file_name = '../python_Code/file/car/' + str(s_number) + '.jpg'
        # with open(file_name, 'wb') as f:
        #     f.write(img_response.content)
        #     f.close()

        # # 保存文本

        # file_name_txt = '../python_Code/file/car/car.txt'
        # with open(file_name_txt, 'a', encoding='utf8') as f:
        #     f.write(str(s_number) + '\t' + h3.text + '\n' + msg_url + '\n')
        #     f.close()







