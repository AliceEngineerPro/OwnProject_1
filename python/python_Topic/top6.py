# 用户登陆（三次机会重试）
i = 1
while i < 4:
    username = input('please your username:')
    password = input('please your password:')
    if username == 'user' and password == '123':
        print("you are True")
        break
    else:
        print("you are False")
    i += 1
