# 静态方法

class Room:

    tag_msg = True

    def __init__(self, name, owner, length, width, high):
        self.name = name
        self.owner = owner
        self.length = length
        self.width = width
        self.high = high

    @property
    def cal_area(self):
        return self.length * self.width

    @property  # 和实例绑定
    def cal_volume(self):
        return self.length * self.width * self.high

    @classmethod  # 和类绑定
    def tell_info(cls):
        return Room.tag_msg

    @staticmethod  # 不绑定, 类的工具包
    def lave(a, b, c):
        print('%s %s %s正在洗澡' % (a, b, c))


# print(Room.tell_info())

Room.lave('a', 'b', 'c')


