# def calc(n):
#     print(n)
#     if int(n/2) == 0:
#         return n
#     return calc(int(n/2))
#
#
# calc(50)


# 求阶乘
import time


def factorial(x):
    if x == 1:
        return x
    # return x+1
    else:
        y = x * factorial(x - 1)
        return y
        pass


print(factorial(5))
print('-' * 20)

people_list = ['1号', '2号', '3号', '4号']


def way(people_lists):
    print('-' * 20)
    if len(people_lists) == 0:
        return '没有知道'
    people = people_lists.pop(0)
    if people == '4号':
        return '%s说:我知道' % people
    print('Hi, %s,你知道吗?' % people)
    print('%s说:我不知道,我帮你问问%s' % (people, people_lists))
    # time.sleep(1)
    asks = way(people_lists)
    print('%s问的结果是:%s' % (people, asks))
    return asks


ask = way(people_list)
print(ask)
print('-'*50)


def calc(n):
    print(n)
    if int(n / 2) == 0:
        return n
    else:
        return calc(int(n / 2))


calc(10)
