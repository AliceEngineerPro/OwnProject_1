# 实例属性

class Chinese:

    country = 'China'
    eg_list = [1, 2]

    def __init__(self, name, ball):
        self.name = name
        self.ball = ball

    def play(self):
        print('%s正在打%s' % (self.name, self.ball))


msg1 = Chinese('jack', 'ball')
msg1.country = 'JP'
print(Chinese.country)
print(msg1.country)

msg1.eg_list = [1, 2, 3]
print(Chinese.eg_list)
print(msg1.eg_list)

Chinese.country = 'jp'
print(Chinese.country)
print(msg1.country)
