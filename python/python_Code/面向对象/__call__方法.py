# __call__ 方法
class Foo:

    def __call__(self, *args, **kwargs):
        print('这是call')


f = Foo()

f()  # Foo下的__call__

Foo()()
