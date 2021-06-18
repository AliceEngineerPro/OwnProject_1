# 全局数据类型变量
country = '中国'


class Chinese:

    country = 'China'

    def __init__(self, name):
        self.name = name
        print('>>>', country)

    def play_ball(self, ball):
        print('%s正在玩%s' % (self.name, ball))


msg1 = Chinese('jack')
print(msg1.country, msg1.name)
msg1.play_ball('ball')


# def shi_li_hua():
#     name = input('请输入名字>>>:')
#     ball = input("请输入动作>>>:")
#     msg1 = Chinese(name)
#
#     return msg1.play_ball(ball)
#
#
# shi_li_hua()



