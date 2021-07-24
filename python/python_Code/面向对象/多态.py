class H2o:
    def __init__(self, status, c):
        self.status = status
        self.c = int(c)

    def main(self):
        if 100 > self.c > 0:
            print('水在%s度下是水' % self.c)
        if self.c >= 100:
            print('水在%s度下是蒸汽' % self.c)
        if self.c <= 0:
            print('水在%s度下是冰' % self.c)


class Water(H2o):
    pass


class Ice(H2o):
    pass


class Steam(H2o):
    pass


w = Water('水', 50)
i = Ice('冰', -20)
s = Steam('蒸汽', 300)

w.main()
i.main()
s.main()
