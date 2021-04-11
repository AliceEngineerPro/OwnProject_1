# 全局变量 顶头写的变量
Name = '小明'

print('name=', Name)
# 局部变量 ,先调用局部变量, 如果局部变量没有定义, 则使用全局变量
def change_name():
    """
    局部变量只在局部定义里生效
    函数具有的功能
    如果函数的内容无global关键字, 优先读取局部变量
    如果函数中的内容有global, 变量的本质就是全局的变量, 可读取可赋值
    """
    global Name
    Name = '小小明'
    age = 3
    print(Name, age)
    pass


change_name()
print('name=', Name)


def change_name_1():
    """

    """
    global Name
    Name = '小明明'
    age = 5
    print(Name, age)
    pass


change_name_1()
print('name=', Name)


"""
# 代码块
name = '刚娘'


def weihuo():
    name = '沉着'

    def weiweihuo():
        global name
        name = '冷静'

    weiweihuo()
    print(name)


print(name)
weihuo()
print(name)

"""


# 前项引用 函数即变量
def bar():
    print('bar')


def foo():
    print('foo')
    bar()


foo()

