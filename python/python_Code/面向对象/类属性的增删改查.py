# 类属性的增删改查
import time


class Chinesepeople:

    country = 'China'
    person_type = '人'

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print('%s正在玩%s' % (self.name, ball))

    def eat_foot(self, foot):
        print('%s正在吃%s' % (self.name, foot))


# 查看类属性
print(Chinesepeople.country)
# 修改类属性
Chinesepeople.country = 'CHINA'
print(Chinesepeople.country)
# 增加类属性
Chinesepeople.time_now = time.asctime()
# 删除类属性
print(Chinesepeople.__dict__)
del Chinesepeople.person_type
print(Chinesepeople.__dict__)

person1 = Chinesepeople('jack')
person1.play_ball(ball='ball')
print(person1.time_now)



