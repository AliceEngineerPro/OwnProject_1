# 求1-2+3-4+5..99的所有数的和
first_num = 1
num = 0
while first_num < 100:
    if first_num % 2 != 0:
        num = num + first_num
    else:
        num = num - first_num
    first_num += 1

print(num)