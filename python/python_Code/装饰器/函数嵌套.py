# 参数向上寻找

def foo():
    print('hello')

    def test():
        print('world')

        def test1():
            print('!')
        test1()
    test()


foo()

