import pack_2


@pack_2.auth()
def index():
    print('这里是登录:欢迎登录JD')


@pack_2.auth()
def home(name):
    print('这里是主页:欢迎%s回家' % name)
    return name


@pack_2.auth()
def shopping_car(name):
    car = '这里是是购物车:'
    if name == 'jack':
        print('%s%s购物车里有:[%s, %s, %s]' % (car, name, '奶茶', '妹妹', '娃娃'))
    if name == 'jack1':
        print('%s%s购物车里有:[%s, %s, %s]' % (car, name, '奶茶1', '妹妹1', '娃娃1'))
    if name == 'jack2':
        print('%s%s购物车里有:[%s, %s, %s]' % (car, name, '奶茶2', '妹妹2', '娃娃2'))
    if name == 'jack3':
        print('%s%s购物车里有:[%s, %s, %s]' % (car, name, '奶茶3', '妹妹3', '娃娃3'))
    if name == 'jack4':
        print('%s%s购物车里有:[%s, %s, %s]' % (car, name, '奶茶4', '妹妹4', '娃娃4'))


index()
home(pack_2.userID_save['user_name'])
shopping_car(pack_2.userID_save['user_name'])
