import requests


headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'host': 'dig.chouti.com',  # 主机
    'Referer': 'https://dig.chouti.com/login',  # url
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
}

post_dict = {
    'phone': '+8616602195891',
    'password': 'a123123',
    'loginType': 2,
}

response = requests.post(
    url='https://dig.chouti.com/login',
    data=post_dict
)

print(response.text)
cookies_dict = response.cookies.get_dict()
print(cookies_dict)
print(response.status_code)
