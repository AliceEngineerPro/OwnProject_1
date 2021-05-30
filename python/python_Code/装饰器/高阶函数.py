import time
"""
高阶函数:
1, 高阶函数接受的参数是一个函数名
2, 高阶函数的返回值的一个函数名
满足任意一个条件称之为高阶函数
"""
# 第一种
#
#
# def foo():
#     time.sleep(1)
#     print('hello')
#
#
# def func(test):
#     start_time = time.time()
#     test()
#     stop_time = time.time()
#     print('运行时间为:%sS' % (stop_time - start_time))
#
#
# func(foo)
#

# 第二种
#
#
# def foo():
#     print('hello')
#
#
# def test(func):
#     return func
#
#
# foo = test(foo)
# foo()
#


def foo():
    time.sleep(1)
    print('hello')


# 不修改foo调用函数和源代码  ↓↓↓↓↓↓不能实现
def timer(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print('运行时间:%sS' % (stop_time - start_time))
    return func


timer(foo)
# foo = timer(foo)
# foo()

