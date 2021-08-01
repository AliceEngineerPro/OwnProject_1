# __del__方法
class Foo:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        return_value = '析构函数'
        return return_value


f = Foo('alex')

print('-' * 20 + '>>>')
