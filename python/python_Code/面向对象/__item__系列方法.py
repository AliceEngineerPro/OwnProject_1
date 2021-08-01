# __item__方法
class Foo:

    def __getitem__(self, item):
        print('__getitem__')

    def __setitem__(self, key, value):
        print('__setitem__')

    def __delitem__(self, key):
        print('__delitem__')


f = Foo()
