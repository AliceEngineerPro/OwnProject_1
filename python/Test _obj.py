import requests


def px():
    width = int(input('长(px)-->').strip())
    height = int(input('高(px)-->').strip())
    w = width / 10 * 4
    h = height / 10 * 4

    return_value = w, h
    return return_value


# print(px())


def sum_input():
    start = int(input('开始-->').strip())
    stop = int(input('结束-->').strip())
    msg = '结果为:'
    if start >= 0 and stop >= 0:
        s = 0
        for i in range(start - 1, stop):
            i += 1
            s += i
        return msg + '%s' % s
        pass
    elif start == stop:
        return msg + '%s' % stop
    else:
        return_value = '请输入正数'
        return return_value


print(sum_input())


requests.request(
    # 常用
    method='',  # 提交方式
    url='',  # 提交地址
    params='',  # 在GET中的请求参数  url?k1=v1&k2=bv2
    data='',  # 在请求体中的传递数据  {'user': 'user', 'passwd': '123'}
    json='',  # 在请求体中的传递数据  {"user": "user1", "passwd": "123"}
    headers='',  # 请求头
    cookies='',  # cookies
    # 特殊
    files='',  # 上传文件
    auth='',  # 封装请求头, 多用于登录验证加密
    timeout='',  # 超时(connect time, read time)
    allow_redirects=True,  # 是否允许重定向
    proxies='',  # 代理
    verify=True,  # 是否忽略ssl证书
    stream='',  # 保存在磁盘
    cert='',  # ssl证书

)

headers = {
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
