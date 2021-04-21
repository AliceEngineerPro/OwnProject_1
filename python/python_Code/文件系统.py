# 文件操作
"""
r, 只读
w, 只写
a, 追加
r+, 读写
w+, 写读
a+, 读写

"""

# find = open('文件', 'r', encoding='utf8')  # /文件目录, 'r w a'文件操作, encoding为编码
# data = find.read()
# print(data)

# 文件操作模式, 读
# find.readable()  # 查看是否可读
# find.readline()  # 读1行
# print(find.readlines(2))  # 读n行, 无参数读全部, 输出列表
# find.close()

# 文件操作模式, 写
# find2 = open('文件', 'w', encoding='utf8')  # 如果文件不存在建立文件 文件写必须都是字符串
# # 如果使用read进行读操作, 文件如果实在写的状态下,则文件内容全部删除
# # find2.read
# find2.write('11111111\n')  # 文件自动不会换行, 加\n表示换行
# find2.write('22222222\n')
# find2.write('33333333\n')
# # find2.writable()  # 查看是否可写
# find2.writelines(['444444\n', '5555555\n'])  # 写多行, 传入值为列表
# find2.close()


# 文件操作模式, 追加
# find3 = open('文件', 'a', encoding='utf8')
# find3.write('\n文件末尾')
# find3.close()


# 读写
# r_file = open('文件', 'r', encoding='utf8')
# save = r_file.readlines()
# r_file.close()
#
# w_file = open('文件new', 'w', encoding='utf8')
# # w_file.writelines(save)
# w_file.write(save[0])
# w_file.close()


# 文件处理b模式  /b的模式不能使用encoding
# r = open('文件', 'rb')
# data_r = r.read()
# print(data_r)

# w = open('文件', 'wb')
# w.write(bytes('111\n', encoding='utf8'))
# w.write(bytes('小明\n'.encode('utf8')))

# a = open('文件', 'ab')
# a.write(bytes('\n小明'.encode('utf8')))


# 文件其他操作方法
f = open('file/文件new', 'r+', encoding='')
data = f.read()
print(data)
f.write('111\n')
f.flush()  # 保存文件
# f.name  # 文件名
f.readlines()
f.tell()  # 光标所在位置 (以字节计算)
