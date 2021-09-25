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



