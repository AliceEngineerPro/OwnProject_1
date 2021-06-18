# 实例化
class Chinese:

    def __init__(self, chinese_name, chinese_age, chinese_gender):
        self.chinese_name = chinese_name
        self.chinese_age = chinese_age
        self.chinese_gender = chinese_gender

    # 函数属性
    def habit(self):
        print('%s like money' % self.chinese_name)

    def other_habit(self):
        print('%s has other habit' % self.chinese_name)

    def eat_foot(self, foot):
        print('%s正在吃%s' % (self.chinese_name, foot))


# 方法调用

s_number1 = Chinese('jack', 18, 'male')
# print(s_number1.chinese_name)  # print(s_number1.__dict__['chinese_name'])

s_number1.habit()
s_number1.other_habit()
s_number1.eat_foot(foot='饺子')

