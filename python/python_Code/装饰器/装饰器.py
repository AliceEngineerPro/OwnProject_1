"""
装饰器本质就是函数,功能就是为其他的函数添加附加的功能

原则:
1, 不能修改被修饰函数的源代码
2, 不能修改被装饰函数的调用方法

知识储备
装饰器 = 高阶函数 + 函数嵌套 + 闭包

"""
import time
import pack_1


def func1(num):
    start_time = time.time()
    res = 0
    for i in num:
        time.sleep(0.01)
        res += i
    # stop_time = time.time()
    # print('运行时间为:%s ' % (stop_time - start_time))
    return res


# print(func1(range(10)))


# 测试函数

@pack_1.timer
def func_test(name, age):
    time.sleep(0.01)
    run = '这是func_test的return'
    return run, name, age


print(func_test('jack', 18))
print('-' * 50)


@pack_1.timer
def func_test1(name, age, gender):
    time.sleep(0.1)
    run = ('这是func_test1的返回值,', name, age, gender)
    return run


print(func_test1(name='jack', age='18', gender='man'))


def func_test2():
    print('1')
    pass


def func_test3():
    print('1')
    pass


def func_test4():
    print('1')
    pass

