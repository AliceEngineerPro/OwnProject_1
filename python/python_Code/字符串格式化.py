# % 格式化
# %s 全能
print('I am %s , my hobby is %s' % ('Jack', 'play computer games'))
print('I am %s , I`m %s year old' % ('Jack', 20))

# %d 整型
# name = input('你的姓名:')
# age = int(input('你的年龄'))
# print('I am %s , I`m %d year old ' % (name , age))

# %f 浮点小数,默认小数点后6位
print('π为:%f' % 3.1415926535)

# %.nf 浮点小数,n为保留小数点后n位
print('π为:%.2f' % 3.1415926535)
print('π为:%.8f' % 3.1415926535)

# %.2f %%  百分比 添加百分号
print('π为:%.2f%%' % 3.1415926535)

# %(null)s/d/f 适用于字典传值
manage = 'I am %(name)s , I`m %(age)d year old' % {'name': 'Jack', 'age': 1}

# sep=' ' 拼接字符串
# print('root', 'x', '0', '0', sep=':')

print('----------')
# format格式化
# 元组顺序取值
msg_1 = 'I am {} , I`m {} year old , I like {}'.format('Jack', 13, 'eat and sleep')

# 元组索引取值
msg_2 = 'I am {1} , I`m {0} year old , I like {2}'.format(13, 'Jack', 'eat and sleep')

msg_3 = 'I am {1} , I like {1}'.format(13, 'Jack', 'eat and sleep')

# 赋值取值
msg_4 = 'I am {name} , I`m {age} year old , I like {hobby}'.format(age=13, name='Jack', hobby='eat and sleep')

# 字典取值
msg_5 = 'I am {name} , I`m {age} year old , I like {hobby}'.format(**{'age': '13', 'name': 'Jack', 'hobby': 'eat'})

# 列表顺序取值
msg_6 = 'I am {:s} , I`m {:d} year old , I like {:s}'.format(*['Jack', 13, 'eat'])

# 列表索引取值
msg_7 = 'I am {0} , I`m {1} year old , I like {2}'.format(*['Jack', 13, 'eat and sleep'])

# 数值的进制:b:2, o:8, d:10(整形), x,X:16(x小写,X大写), %:百分比(默认小数点后6位)
msg_8 = 'num: 二进制:{:b}, 八进制:{:o}, 十进制:{:d}, 十六进制:{:x}, 十六进制:{:X}, 百分比:{:%}'.format(15, 15, 15, 15, 15, 15.3333333)
