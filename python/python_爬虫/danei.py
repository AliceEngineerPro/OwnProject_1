import requests
from bs4 import BeautifulSoup
import hashlib


post_url='https://uc.tmooc.cn/login'

login_user = '2536215246@qq.com'

passwd_data = hashlib.md5()
passwd_data.update('35739667'.encode('utf8'))

from_data = {
	"loginName": login_user,
	"password": passwd_data.hexdigest(),
	"imgCode": "",
	"accountType": "1",
	"whetherIntranet": "10121002"
}

headers_data = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Connection': 'keep-alive',
	'host': 'uc.tmooc.cn',
	'Referer': 'https://www.tmooc.cn/',
	'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 '
				  'Edg/93.0.961.38',
	'Cookie': 'TMOOC-SESSION=0a02db9dff86432e9375eedc91bf33fb;Hm_lvt_51179c297feac072ee8d3f66a55aa1bd=1636632904"\
	";Hm_lpvt_51179c297feac072ee8d3f66a55aa1bd=1636633271; JSESSIONID=147932FA65FC24156F590B4161C3E8FD',
	'Origin': 'https://www.tmooc.cn',
}


response_one =  requests.request(
    method='post',
    url=post_url,
    json=from_data,
	headers=headers_data,
)

print(response_one.text)

# soup = BeautifulSoup.find()