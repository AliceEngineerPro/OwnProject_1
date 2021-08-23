# 生产者消费模型
import time


def eat():

    def producer():  # 生产
        bun = []
        for i in range(11):
            bun.append(i)
            time.sleep(1)
            print(time.asctime(time.localtime(time.time())))  # 打印服务器时间
        return bun

    def consumption(bun):  #消费
        for n, nn in enumerate(bun):
            if n >= 1:
                print("第%s个人,吃了第%s个包子" % (n, nn))
                time.sleep(1)
                print(time.asctime(time.localtime(time.time())))  # 打印服务器时间

    buns = producer()
    consumption(buns)


# eat()

# yield相当与return的返回值
# x = yield 接受send传来的值,赋值给x


def eat_bun():
    def producer(name):
        print("我是[%s], 开始吃包子" % name)
        while True:
            bun = yield
            time.sleep(1)
            print('[%s] 很开心的把%s吃了' % (name, bun))

    def consumption():
        c1 = producer('1')
        c2 = producer('2')
        c1.__next__()
        c2.__next__()
        for i in range(10):
            if i >= 1:
                c1.send("[包子%s]" % i)
                c2.send("[包子%s]" % i)
                time.sleep(1)
    consumption()


eat_bun()
