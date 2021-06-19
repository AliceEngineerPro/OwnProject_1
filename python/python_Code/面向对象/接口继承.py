# 接口继承

import abc  # 接口类


class Allfile(metaclass=abc.ABCMeta):  # 父类接口继承原则
    """
    接口类
    没必要写逻辑
    不用实例化
    只是为了规范子类
    """

    @abc.abstractmethod
    def read(self):
        print('All read')

        pass

    @abc.abstractmethod
    def write(self):
        print('All write')

        pass


class Disk(Allfile):

    def read(self):
        print('Disk read')

    def write(self):
        print('Disk write')

    pass


class Cd(Allfile):

    def read(self):
        print('Cd read')

    def write(self):
        print('Cd write')

    pass


class Mem(Allfile):

    def read(self):
        print('Mem read')

    def write(self):
        print('Mem write')

    def other(self):
        print('Mem other')

    pass


m1 = Mem()

m1.read()
m1.write()
m1.other()
