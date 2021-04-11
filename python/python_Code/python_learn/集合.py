# set 方法
# s = {'xiaoming', 'xiaoming', 'xiaoming1'}
# print(s)
# s.add('s') # 添加元素
# s.clear(s) # 清空集合
# s1 = s.copy(s) # 复制集合
# s.pop() #删除元素 随机删除
# s.remove('xioaming1') #删除元素 指定删除
# s.discard('xioaming1') #删除元素 指定删除 删除元素不存在的不会报错

# 集合的运算
# 列表循环遍历
python = ['1', '2', '3', '5']
linux = ['1', '2', '3', '4', '5']
print('python =', python, '\t', 'linux =', linux)

python_and_linux = []
for python_p in python:
    if python_p in linux:
        python_and_linux.append(python_p)

print('列表python,linux的并集:', python_and_linux)

print('----------')
# 列表
python = ['1', '2', '3', '5', '5', '2', '6']
linux = ['1', '2', '3', '4', '5', '8']

# 把列表转换为set集合
set_python = set(python)
set_linux = set(linux)
print('集合1:', set_python, ',', '集合2:', set_linux)

print('----------')
# 交集 intersection() 或 &
print('交集:', set_python.intersection(set_linux))
print('交集:', set_python & set_linux)

print('----------')
# 并集 union() 或  |
print('并集:', set_python.union(set_linux))
print('并集:', set_python | set_linux)

print('----------')
# 差集 difference() 或 -
print('差集1-2:', set_python - set_linux)
print('差集1-2:', set_python.difference(set_linux))
print('差集2-1:', set_linux - set_python)
print('差集2-1:', set_linux.difference(set_python))

print('----------')
# 交叉补集 symmetic_difference() 或 ^
print('交叉补集:', set_python.symmetric_difference(set_linux))
print('交叉补集:', set_python ^ set_linux)

print('----------')
# 求完差集并更新 difference_update() 或 重新赋值
print('求完差集并更新')
set_python.difference_update(set_linux)
print('集合1:', set_python, ',', '集合2:', set_linux)
set_python = set_python - set_linux
print('集合1:', set_python, ',', '集合2:', set_linux)

# 求完交集并更新 intersection_update() 或 重新赋值
# 求完交叉补集并更新 symmetric_difference_update 或 重新赋值  //写法和difference_update一样

print('----------')

# 如果没有交集返回 True , 如果有交集则返回False isdisjoint()
set_1 = {1, 2}
set_2 = {3, 4}
set_3 = {2, 3}
print('set_1:', set_1, 'set_2:', set_2, 'set_3', set_3)
print('set_1和set_2没有交集:', set_1.isdisjoint(set_2))
print('set_1和set_3没有交集:', set_1.isdisjoint(set_3))

print('----------')

# 判断所属
'''
子集: issubset()
父集: issuperser()
'''
set_1 = {1, 2}
set_2 = {1, 2, 3}
print('set_1:', set_1, 'set_2:', set_2)
# 子集
# set_1是set_2的子集 , 如果是返回 True , 不是返回False
print('set_1是set_2的子集:', set_1.issubset(set_2))
# set_2是set_1的子集 , 如果是返回 True , 不是返回False
print('set_1是set_2的子集:', set_2.issubset(set_1))
# 父集
# set_1是set_2的父集 , 如果是返回 True , 不是返回False
print('set_1是set_2的父集:', set_1.issuperset(set_2))
# set_2是set_1的父集 , 如果是返回 True , 不是返回False
print('set_1是set_2的父集:', set_2.issuperset(set_1))
