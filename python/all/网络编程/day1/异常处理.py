# 语法错误

# 逻辑错误

# 异常
# res = 1/0
# 解释器抛出
"""
Traceback (most recent call last):
  File "E:/Self_file/self_git/VScodeNote/python/全栈/网络编程/day1/异常处理.py", line 6, in <module>
    res = 1/0
ZeroDivisionError: division by zero
"""

# 异常处理

# age = input('-->')
# if age.isdigit():
#     int(age)
# elif age.isspace():
#     print('空字符')
# elif len(age) == 0:
#     print('空')
# else:
#     print('其他非法输入')


# def run():
#     print('running')
#
#
# choice_dic = {
#     '1': run
# }
#
# while True:
#     choice = input('请输入-->').strip()
#     if not choice or choice not in choice_dic:
#         continue
#     choice_dic[choice]()


# try:
#     age = input('age-->')
#     int(age)
#
#     num = input('num-->')
#     int(num)
#
# except Exception as e:
#     print('异常%s' % e)
# else:
#     print('try中无异常执行else')
# finally:
#     print('无论异常,都执行')

# 断言

# first = 1
# print(first)
# # assert 1 == 1
# assert first == 2
# print('2')




