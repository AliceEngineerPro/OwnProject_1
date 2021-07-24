class Black:

    ture = 'Ugly'

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    # def sell_house(self):
    #     return_value = '%s 正在卖房子' % self.name
    #     return return_value

    def rent_house(self):
        return_value = '%s 正在租房子' % self.name
        return return_value


c1 = Black('alex', '北京')

if hasattr(c1, 'sell_house'):  # 判断c1后的的方法,如果有返回True
    func = getattr(c1, 'sell_house')
    print(func())
else:
    print('没有此方法')
    pass
