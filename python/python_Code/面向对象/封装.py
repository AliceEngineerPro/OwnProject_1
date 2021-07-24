class People:
    __stat = 'earth'

    def __init__(self, people_id, people_name):
        self.id = people_id
        self.name = people_name

    def get(self):
        return_value = '我是%s,ID为:%s,' % (self.name, self.id)
        return return_value


p1 = People('001', 'alex')

# print(p1.get())


class S:

    def __init__(self, long, wide, high):
        self.__long = long
        self.__wide = wide
        self.__high = high

    def s(self):
        return self.__long * self.__wide

    def long(self):
        return self.__long

    def wide(self):
        return self.__wide


s1 = S(3, 2, 2)
print(s1.s())
