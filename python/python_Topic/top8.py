# 根据范围获取其中的3个7整除的所有数的和,并返回调用者
# 符合条件的数据个数以及符合条件的数字的总和, 如def func(start,end)

def func(start, end, num=0, num_sum=0):  # num为个数,num_sun为符合个数的和
    if start == end:
        return num, num_sum
    if start % 3 == 0 and start % 7 == 0:
        add = [start]
        num += 1
        num_sum += start
        print(add)  # 输出
    ret = func(start+1, end, num, num_sum)
    return ret


print(func(0, 51))
