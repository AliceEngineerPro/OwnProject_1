# 实例属性的增删改查
class Chinese:

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print('%s正在完%s' % (self.name, ball))


person1 = Chinese('alex')

# 查看
print(person1.name)
# 增加
person1.age = 18
print(person1.age)
# 修改
person1.age = 20
print(person1.age)
print(person1.__dict__)
# 删除
del person1.age
print(person1.__dict__)
