# __*arrt__方法
class Foo:
    x = 1

    def __init__(self, y):
        self.y = y

    def __getattr__(self, item):  # 在函数调用中此类没有该方法时,调用getattr
        print('执行__getattt__')

    def __delattr__(self, item):
        print('执行__delattr__')  # 删除一个类方法

    def __setattr__(self, key, value):  # 添加或修改一个类方法
        print('修改/添加__setattr__')
        self.__dict__[key] = value


f1 = Foo(10)
# print(f1.y)
# f1.noll

del f1.y  # delattr 方法函数

print(f1.__dict__)
print(f1.y)
f1.z = 2  # setattr 方法函数
print(f1.__dict__)
print(f1.z)
