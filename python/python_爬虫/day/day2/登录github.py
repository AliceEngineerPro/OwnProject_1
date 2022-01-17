# 登录github
import requests
from bs4 import BeautifulSoup
import lxml
import time
from bs4.element import Tag

proxy = {
    'http': 'http://127.0.0.1:1080',
}
init_time = time.time()
# 1. 访问登录页面, 获取authenticity_token
login1_get = requests.request(
    method='get',
    url='https://github.com/login',
    # proxies=proxy,
)
# 第一次访问获取token和cookies
soup_login = BeautifulSoup(login1_get.text, features='lxml')
tag_token = soup_login.find(name='input', attrs={'name': 'authenticity_token'})  # 找input标签中的属性带有name=authenticity_token的标签
login_token = tag_token.get('value')  # 获取authenticity_token的值
# 获取第一次访问的cookies
first_cookies = login1_get.cookies.get_dict()
login1_get.close()

# 2. 发送用户登录请求
from_data = {
    'authenticity_token': login_token,
    'commit': 'Sign+in',
    'login': 'amfc-super',
    'password': 'Amfc0-./',
}
# 发送请求
login1_post = requests.request(
    method='post',
    url='https://github.com/session',
    data=from_data,
    cookies=first_cookies,
)
# 获取第二次的cookies
second_cookies = login1_post.cookies.get_dict()
first_cookies.update(second_cookies)
homepage_get = requests.request(
    method='get',
    url='https://github.com/settings/repositories',
    cookies=first_cookies,
)
soup_homepage = BeautifulSoup(homepage_get.text, features='lxml')
tag_project = soup_homepage.find(name='div', class_='js-collab-repo')

print(soup_homepage.text)

for child in tag_project.children:
    if isinstance(child, Tag):
        project_name = child.find(name='a', class_='mr-1')
        size_name = child.find(name='text-small')
        temp = '项目:%s(%s):%s' % (project_name.get('href'), size_name.string, project_name.name)
        # print(temp)
# print(homepage_get.text)
print('程序运行%s秒' % int(time.time() - init_time))