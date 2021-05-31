userID_list = [
    {'user_name': 'jack', 'user_passwd': '123'},
    {'user_name': 'jack1', 'user_passwd': '123'},
    {'user_name': 'jack2', 'user_passwd': '123'},
    {'user_name': 'jack3', 'user_passwd': '123'},
    {'user_name': 'jack4', 'user_passwd': '123'},
]

userID_save = {'user_name': ' ', 'login': False}


def auth(auth_type='filedb'):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'filedb':
                if userID_save['user_name'] and userID_save['login']:
                    res = func(*args, **kwargs)
                    return res
                print('认证类型为:%s' % auth_type)
                user_name = input('用户名:').strip()
                user_passwd = input('密码:').strip()
                for user_dic in userID_list:
                    if user_name == user_dic['user_name'] and user_passwd == user_dic['user_passwd']:
                        userID_save['user_name'] = user_name
                        userID_save['login'] = True
                        res = func(*args, **kwargs)
                        return res
                else:
                    print('用户名或密码错误')
            elif auth_type == 'LDAP':
                print('认证类型为:%s......' % auth_type)
            else:
                print('不知道%s......' % auth_type)
        return wrapper
    return auth_func
