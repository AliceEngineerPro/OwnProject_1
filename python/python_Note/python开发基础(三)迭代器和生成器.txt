# 迭代器和生成器
from typing import List

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
