# 迭代器和生成器
from typing import List
import time

l: List[int] = [1, 2, 3]
# for循环
"""
for i in l:  # l.__iter__() /l.__iter__.__next__()
    print(i)
"""

# while循环
"""
index = 0
while index < len(l):
    print(l[index])
    index += 1
"""

# 用__next__()
"""
iter_1 = l.__iter__()  # 迭代器协议,生成可迭代对象
print(iter_1.__next__())
print(iter_1.__next__())
print(iter_1.__next__())

"""

# 解析__next__
"""
x = 'hello'
iter_tools = x.__iter__()
print(iter_tools)
print(iter_tools.__next__())
print(iter_tools.__next__())
print(iter_tools.__next__())
print(iter_tools.__next__())
print(iter_tools.__next__())

"""


def setting():
    s = {1, 2, 3}
    for i in s:
        print(i)


def dic():
    d = {'a': '1', 'b': '2'}
    for j in d:
        print(j)  # 默认for循环字典的key的值


# 三元表达式
def expression():
    # name = 'steven'
    name = '小明'
    res = 'yes' if name == 'steven' else 'no'
    print(res)


# 列表解析egg
def egg():
    egg_list = []
    for i in range(1, 11):
        egg_list.append('egg%s' % i)
    print(egg_list)


# 生成器
def builder_a():
    # num = [i for i in range(1, 11)]
    # num = (i for i in range(1, 11))
    # print(num)
    # print(num.__next__())
    return [i for i in range(1, 11)]


def builder_b():
    yield 1  # 可保留函数的运行状态
    yield 2
    yield 3


# res_b = builder_b()
# print(res_b)
# print(res_b.__next__())
# time.sleep(2)
# print(res_b.__next__())


def cs_a():
    for i in range(len(builder_a())):
        if builder_a()[i] > 0:
            print(builder_a()[i], i)
            time.sleep(1)
        else:
            pass


def egg_a():
    egg_list = []
    for i in range(1, 101):
        egg_list.append('第%d个鸡蛋' % i)
    return egg_list


# print(egg_a())


def egg_b():  # 生成器(可迭代对象), 状态挂起
    for i in range(1, 11):
        yield '第%s个鸡蛋' % i


egg_chicken = egg_b()

for eggs in egg_chicken:
    print(eggs)