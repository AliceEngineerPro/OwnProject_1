# 继承

class Dad:

    money = 100

    def __init__(self, name):
        print('Dad')
        self.name = name

    def hit(self):
        print('%s在打儿子' % self.name)


class Son(Dad):

    money = 10000000

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hit(self):
        print('来自Class Son')


d1 = Dad('Dad')

s1 = Son('son', 20)
s2 = Son('alex', 30)

# print(Son.money)
s2.hit()

# d1.hit()

# print(Son.money)
#
# print(s1)

