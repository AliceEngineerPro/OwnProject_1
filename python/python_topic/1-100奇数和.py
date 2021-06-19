

def num_sum(num):
    sum1 = 0
    for i in range(1, num):
        if i % 2 != 0:
            sum1 = sum1 + i
    return sum1


print(num_sum(101))

