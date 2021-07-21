# 在子类中调用父类

# 普通调用
class Vehicle:

    country = 'China'

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('run')


class Subway(Vehicle):

    def __init__(self, name, speed, load, power, line):
        Vehicle.__init__(self, name, speed, load, power)
        self.line = line

    def show_info(self):
        print(self.name, self.speed, self.load, self.power, self.line)

    def run(self):
        # Vehicle.run(self)  # 实现父类方法
        print('%s %s 号线,开动了' % (self.name, self.line))


line13 = Subway('地铁', '80km/h', 1000000, '电', 13)

# line13.show_info()
# line13.run()


# super方法
class Vehicle1:

    country = 'China'

    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('run')


class Subway1(Vehicle1):

    def __init__(self, name, speed, load, power, line):
        # Vehicle1.__init__(self, name, speed, load, power)
        super().__init__(name, speed, load, power)  # 调用父类
        self.line = line

    def show_info(self):
        print(self.name, self.speed, self.load, self.power, self.line)

    def run(self):
        # Vehicle.run(self)  # 实现父类方法
        print('%s %s 号线,开动了' % (self.name, self.line))


line1 = Subway1('地铁', '80km/h', 1000000, '电', 13)

line1.show_info()
line1.run()
