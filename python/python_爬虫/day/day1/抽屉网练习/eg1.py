import re

import requests


url = [
    'https://dig.chouti.com/',
    'https://dig.chouti.com/login',
]

login_post_data = {
    'phone': '+8616602195891',
    'password': 'a123123',
    'loginType': 2,
}

for i in url:
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'host': 'dig.chouti.com',
        'Referer': i,
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
    }

    if re.findall('login$', i):
        headers['Cookie']='deviceId=web.eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqaWQiOiIzYzM1NjY5Yy05NmM4LTQ4NzYtYTA3Mi03YTIyNzIxYzg0MTgiLCJleHBpcmUiOiIxNjM0OTk3NTM0OTk4In0.3z-wG0DIYpetPKfZ3LFwmNz0FnIisjvxq6LSfu_8kiI; Hm_lvt_03b2668f8e8699e91d479d62bc7630f1=1632405536,1632406759; __snaker__id=l3NNNGVMDlu0MZPs; _9755xjdesxxd_=32; YD00000980905869%3AWM_NI=d24Rqlwj3242yDqgZcYLf0rRfFfWgrwC%2BdQIh7%2FxI29A1KELx5VciqjCXr1Bw%2BD7YqlNPDLlEpZsFr0pKOhGymOK5ozNbbJvpRlFwfHHhiL1i5KFJO8mchopYXU8vlphZUk%3D; YD00000980905869%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea2d27493efbe85ca6db3e78bb2c85f829a8bbaf4408292a0a2cb68b6adbaa8eb2af0fea7c3b92aa8eefcb3f468b5b6fdd3b73abb9cbf88d9699b94aad1f15aa69aaab8e67ab59de585d443ace9e199cc3afb9fffacc848bceb9a84ec7baa9d9893b44ab5f58cd8dc7bb092a0a5cf6887b09694c57af4b085b0eb4dbbb381acb865ba92ae83c97eb48ea4a7f66e8c98a88acf3babeb85a7c945fcb3ad89ee7c9b889bd9f568b4b896b6ea37e2a3; YD00000980905869%3AWM_TID=RhXbclqV5dxBAUARQRc%2FoVZLBS1%2Ft%2BW1; Hm_lpvt_03b2668f8e8699e91d479d62bc7630f1=1632410880; gdxidpyhxdE=KjSJQz9ldkbCGMPEiHdDGMbUkiYRCqiKpS3x8z03HpVlwVJLsZiki89T%2Bnytt7zh%2B%5CxZ8B49WM8NPqapmqnv%5CkXmPZwOjXi1twpTCw%2BPSNWGfao83EAisHwKLmgpY13H%2FfDfCm5cp%5CzSt%2B06p2qqhOKg%2BRZCeEtIXrQ9c%2B1B9rAg70pb%3A1632413553836'
        headers['Referer'] = i[0]
    if re.findall('login$', i):
        r1 = requests.post(
            url=i,
            headers=headers,
            data=login_post_data,
        )
    elif i == 'https://dig.chouti.com/':
        r1 = requests.get(
            url=i,
            headers=headers,
        )
    else:
        r1 = requests.get(
            url=i,
            headers=headers,
        )

    print(r1.text, '\n' + '=' * 20)
    print(r1.status_code, '\n' + '=' * 20)
        # print(headers, '\n' + '=' * 20)
    # print(r1.cookies.get_dict())
    # print(r1.status_code)
