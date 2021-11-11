from concurrent.futures import ThreadPoolExecutor
import requests
import time


def task(url_eg):
    response_one = requests.request(
        method='get',
        url=url_eg,
    )
    return_value = url_eg, response_one.status_code
    print(return_value)
    # return return_value


pool = ThreadPoolExecutor(5)
url_list = [
    'https://www.cnblogs.com/alicehome',
    'https://www.ak47s.cn/',
    'https://www.bing.com',
    'https://www.sina.com/cn',
    'https://www.baidu.com',
]


def function_url():
    for url in url_list:
        # pool.submit(task, url)
        print()
    pool.shutdown()


print(function_url())

