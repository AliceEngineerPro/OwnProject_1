# 面向对象编程

class Dog:
    def __init__(self, dog_name, dog_gender, dog_type):
        self.name = dog_name
        self.gender = dog_gender
        self.type = dog_type

    def wang(self):
        print('一条名字为[%s]的[%s], 汪汪汪' % (self.name, self.type))

    def yao_ren(self):
        print('一条名字为[%s]的[%s], 在咬人' % (self.name, self.type))

    def eat(self):
        print('一条名字为[%s]的[%s], 在吃狗粮' % (self.name, self.type))


dog1 = Dog('alex', 'female', 'dog')
dog2 = Dog('alex1', 'female', 'dog')
dog3 = Dog('alex2', 'female', 'dog')


# dog1.wang()
# dog3.yao_ren()
# dog2.eat()



'''
数据属性
函数属性
'''


class Chinese:
    # 数据属性
    hello = '你好'

    # 函数属性
    def habit():
        print('like money')

    def other_habit(self):
        print('other habit')


# 方法调用

# print(dir(Chinese))
# print(Chinese.hello)
# Chinese.habit()  # Chinese.__dict__['habit']()
# Chinese.other_habit(' ')
# print(Chinese.__dict__)  # 查看类的属性字典
