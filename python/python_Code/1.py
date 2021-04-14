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
