def foo():
    print('hello')

    def test():
        print('world')

        def test1():
            print('!')
        test1()
    test()


foo()

