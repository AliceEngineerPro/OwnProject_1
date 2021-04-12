# 内置函数

print(abs(-1))  # 绝对值

# 0, None, [''] 为False, 其余都为True
print(all([1, 2, 3, '4']))  # 序列全真,返回True
print(any([1, 0]))  # 序列中只要有一个真,则返回True
print(bool(None))  # 判断布尔值

# 编码: encoding , 解码: decode ,ASCII不能用于中文
name = '码农'
print(bytes(name, encoding='utf-8'))
print(bytes(name, encoding='utf-8').decode('utf-8'))
print(bytes(name, encoding='gbk'))
print(bytes(name, encoding='gbk').decode('gbk'))

print(chr(97))  # chr 对应ASCII码表的十进制 只能传一个值
print(dict({'name': '小明'}))  # dict 字典
print(dir(list))  # dir 查看 某一个对象对应的方法
print(divmod(10, 3))  # rdivmod() 求商取余

# 字典转字符串类型
dic = {'name': 'Jack'}
dic_str = str(dic)
print(type(dic_str), dic_str)

# eval 将字符串中的数据结构提出出来
print(type(eval(dic_str)), eval(dic_str))  # eval

# eval 吧字符串的表达式做数据运算
var_1 = '1+2*(3/2-1)+10'
print(var_1)
print(eval(var_1))  # eval

# hash 运算 ,可hash的数据类型即不可变数据类型,反之则为可变数据类型
# hash 固定值得位数
print(hash('小明'))
name_1 = 'Jack'
print(hash(name_1))
name_1 = 'hashJack'
print(hash(name_1))

print(help(all))
print(help(dir(all)))  # help 查看帮助

print(bin(2))
print(oct(8))
print(hex(16))  # 进制转换

print(isinstance(1, int))
print(isinstance('1', str))
print(isinstance((1, '2'), tuple))
print(isinstance([1, '2'], list))
print(isinstance({1, 2}, set))
print(isinstance({'one': '1'}, dict))  # isinstance 判断对应类型

print(globals())  # 查看全局变量
print('-' * 50)
print(locals())   # 查看局部变量

num_list = [1, 2, 3, 10, 20, 30, 100, 200, 300]
print(max(num_list))  # 取最大值
print(min(num_list))  # 取最小值
