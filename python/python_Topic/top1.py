# 使用while循环输入1 2 3 4 5 6 8 9 10
num = 0
while True:
    num += 1
    if num == 7:
        continue
    if num == 11:
        break
    print(num)
