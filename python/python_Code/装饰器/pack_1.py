import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        run = func(*args, **kwargs)
        stop_time = time.time()
        print('运行时间:%sS' % (stop_time - start_time))
        return run  # 加上return是返回被装饰的函数返回值
    return wrapper


# @timer  # @timer = test = timer(test)
# def test():
#     time.sleep(0.01)
#     run = '这是test的返回值'
#     print('函数运行完毕')
#     return run
#
#
# # # test = timer(test)
# print(test())  # 在运行wrapper()



