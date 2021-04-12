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
print(divmod(10, 3))  # divmod() 求商取余

dict = {'name': 'Jack'}
dic_str = str(dict)
print(dic_str)