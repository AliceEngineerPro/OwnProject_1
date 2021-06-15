# random 的应用 -->>随机生成验证码

import random


def random_code():
    massage = ''
    for i in range(6):
        num = chr(random.randint(48, 57))  # 利用ASCII表
        letter_big = chr(random.randint(65, 90))
        letter_small = chr(random.randint(97, 122))
        produce_massage = str(random.choice([num, letter_small, letter_big]))
        massage += produce_massage
    return massage


print(random_code())

