# 提醒用户输入:用户名和密码

# 等待输入一个值
# user = input('请输入用户名:')
# passwd = input('请输入密码:')
#
# if user == 'root':
#     if passwd == 'root':
#         print('登录成功')
#     else:
#         print('登录失败,密码错误')
# else:
#     print('登录失败,用户名错误')

# 输入3次密码

count = 0
while count < 3:
    user = input('请输入用户名:')
    passwd = input('请输入密码:')
    if user == 'root' and passwd == 'root':
        print('登录成功')
        break
    else:
        print('用户名或密码错误')
    count = count + 1
print('___End___')