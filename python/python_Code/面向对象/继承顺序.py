# 继承顺序


class A:

    def print(self):
        print('A')

    pass


class B(A):

    def print(self):
        print('B')

    pass


class C(A):

    def print(self):
        print('C')

    pass


class D(B):

    def print(self):
        print('D')

    pass


class E(C):

    def print(self):
        print('E')

    pass


class F(D, E):

    def print(self):
        print('F')

    pass


f1 = F()
f1.print()

print(F.__mro__)  # 继承类顺序
