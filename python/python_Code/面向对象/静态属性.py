# 静态属性
class Room:

    tag = 100

    def __init__(self, name, owner, length, width, high):
        self.name = name
        self.owner = owner
        self.length = length
        self.width = width
        self.high = high

    @property
    def cal_area(self):
        msg1 = '%s 住的%s 的的面积为: %s ' % (self.owner, self.name, self.length * self.width)
        area = self.length * self.width
        return area

    @property
    def cal_volume(self):
        msg1 = '%s 住的%s 的的体积为: %s ' % (self.owner, self.name, self.length * self.width * self.high)
        volume = self.length * self.width * self.high
        return volume

    def test(self):
        print('from test', self.name)

    @classmethod  # 类方法
    def tell_info(cls, num):
        print(cls)
        print(cls.tag, num)

        pass


r1 = Room('room', 'alex', 100, 100, 1000)
r2 = Room('room', 'jack', 1, 1, 1)

# print('%s住的%s的的面积为:%s ' % (r1.owner, r1.name, r1.length * r1.width))
# print('%s住的%s的的面积为:%s ' % (r2.owner, r2.name, r2.length * r2.width))

# 面积
"""
print(r1.cal_area)
print(r2.cal_area)
"""
# 体积
"""
print(r1.cal_volume)
print(r2.cal_volume)
"""

# print(Room.tag)

Room.tell_info(10)











