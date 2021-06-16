# 升高转换
i = int(input('请输入英尺:'))
j = int(input('请输入英寸:'))

con = 0.3048
jj = j / 12
tail = (i + jj) * con
print(tail)
print(round(tail, 2))  # round(浮点数, 取小数点后n位)
