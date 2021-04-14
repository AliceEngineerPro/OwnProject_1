# 内置函数

print(abs(-1))  # abs 绝对值

# 0, None, [''] 为False, 其余都为True
print(all([1, 2, 3, '4']))  # all 序列全真,返回True
print(any([1, 0]))  # any 序列中只要有一个真,则返回True
print(bool(None))  # bool 判断布尔值

# 编码: encoding , 解码: decode ,ASCII不能用于中文
name = '码农'
print(bytes(name, encoding='utf-8'))
print(bytes(name, encoding='utf-8').decode('utf-8'))
print(bytes(name, encoding='gbk'))
print(bytes(name, encoding='gbk').decode('gbk'))

print(chr(97))  # chr 对应ASCII码表的十进制 只能传一个值
print(ord('a'))  # ord 和chr相反
print(dict({'name': '小明'}))  # dict 字典
print(dir(list))  # dir 查看 某一个对象对应的方法
print(divmod(10, 3))  # rdivmod() 求商取余

# 字典转字符串类型
dic = {'name': 'Jack'}
dic_str = str(dic)
print(type(dic_str), dic_str)  # str 转为字符串类型, int 转为整型, tuple 转为元组, dict 转为字典, set 转为集合, 等

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

print(globals())  # globals 查看全局变量
print('-' * 50)
print(locals())   # locals 查看局部变量

num_list = [1, 2, 3, 10, 20, 30, 100, 200, 300]
print(max(num_list))  # 取最大值
print(min(num_list))  # 取最小值

print(pow(10, 3))  # pow(n, x, y) 10**3 n的x次幂
print(pow(7, 5, 4))  # pwd 10**3%4 对n的x次幂除以y取余

print(list(reversed([1, 2, 3, 4])))  # reversed 翻转, 只做处理,不做存储
print(round(3.4))  # round 四舍五入
print(set('hello'))  # set 转换成集合

print(sum(range(5)))  # sum 做加法运算
print(type(1))  # type 查看数据类型

# slice 切片解码
test = 'hello'
# print(test[3:5])  # 硬解码
sl = slice(3, 4)
sli = slice(0, 4, 2)
print(test[sl])  # slice 切片, 可以加步长
print(test[sli])  # 取0到3 ,步长为2

# zip函数 一一对应
# print(list(zip(('a', 'b', 'c'), (1, 2, 3))))

msg_dic = {'name': 'Jack', 'age': '18', 'hobby': 'player'}
zip_mag_dic = zip(msg_dic.keys(), msg_dic.values())
# print(list(zip_mag_dic))
# print(list(msg_dic.keys()))
# print(list(msg_dic.values()))

# max, min 的高级用法

# people_manage = [
#     {'name': 'Jack', 'age': '18'},
#     {'name': 'alex', 'age': '20'},
#     {'name': 'seven', 'age': '22'}
# ]
#
# for i in people_manage:
#     if people_manage['age'] >= 20:
#         print(i)

age_dic = {'age1': 18, 'age2': 20, 'age3': 25}
print(max(age_dic.values()))
print(max(age_dic))  # 默认取字典的keys ,按照ASCII表得值作比较,一位一位比较

zip_age_dic = zip(age_dic.values(), age_dic.keys())
for i in zip_age_dic:
    print(i)

print(list(max(zip(age_dic.values(), age_dic.keys()))))

# 比较序列不能和不同数据类型做比较

people_manage = [
    {'name': 'Jack', 'age': '18'},
    {'name': 'alex', 'age': '20'},
    {'name': 'seven', 'age': '22'}
]

manage_age = max(people_manage, key=lambda dic: dic['age'])
print(manage_age)
# people_manage_age_list = []
# for i in people_manage:
#     people_manage_age_list.append(i['age'])
# print(people_manage_age_list)

# sorted 排序, 由小到大

age_1 = [2, 123, 14, 44, 3, 5, 1, 23, 4, 235, 6, 23]
# age_2 = [12, 2, 4, 56, 4, 2, '12', 'as']  # 不同类型不能排序
print(sorted(age_1))

people_manage = [
    {'name': 'jack', 'age': '18'},
    {'name': 'alex', 'age': '20'},
    {'name': 'seven', 'age': '22'}
]

print(sorted(people_manage, key=lambda x: x['age']))

people_age = {
    'alex': 22,
    'jack': 18,
    'seven': 35
}

print(sorted(people_age, key=lambda key: people_age[key]))
print(sorted(zip(people_age.values(), people_age.keys())))
# people_age, key=lambda key: people_age[key],

# import myprot  # import 不能导入字符串
#
# myprot.hello()
# module_name = 'myprot'
# m = __import__(module_name)  # __import__ 导入带有字符串的包
# m.hello()
