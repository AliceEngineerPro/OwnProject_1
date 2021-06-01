import os


def check(keyword, file_location):
    print('--你所使用的功能为:<查询>')
    print('--查询关键字为>>>%s' % keyword)
    keyword_data = 'backend %s' % keyword
    with open(file_location, 'r') as read_f:  # with...as... 打开的文件赋值给as后的变量
        check_data = []  # 默认空列表
        tag = False  # 默认tag = False
        for read_line in read_f:  # for循环遍历打开的文件(一行一行)
            if read_line.strip() == keyword_data:  # .strip() 移除字符串前后的空字符
                # print(read_line, end='')
                check_data.append(read_line)
                tag = True
                continue  # 终止当前循环
            if tag and read_line.startswith('backend'):  # 检查字符串是否以 'backend' 开头：
                break
                # tag = False
                # continue
            if tag:  # 默认tag = True
                # print(read_line, end='')
                check_data.append(read_line)
    read_f.close()  # 关闭文件
    return check_data


def add():
    print('--你所使用的功能为:<添加>')
    pass


def change(root_data, file_location, new_file_location):
    print('--你所使用的功能为:<修改>')
    backend = root_data[0]['backend']  # 文件中的一条记录
    backend_data = 'backend %s' % backend
    old_server = '%sserver %s %s weight %s maxconn %s\n'\
                 % (' ' * 8, root_data[0]['record']['server'], root_data[0]['record']['server'],
                    root_data[0]['record']['weight'], root_data[0]['record']['maxconn'])
    new_server = '%sserver %s %s weight %s maxconn %s\n'\
                 % (' ' * 8, root_data[1]['record']['server'], root_data[1]['record']['server'],
                    root_data[1]['record']['weight'], root_data[1]['record']['maxconn'])
    print('--即将为您查询关键字为<%s>的信息' % backend)
    check_data = check(backend, file_location)
    print('--来自查询函数-->>>', check_data, '\n')
    print('--你想修改的server信息为->>> %s' % old_server)
    if not check_data or old_server not in check_data:
        not_message = '--你要修改的记录不存在,请重新输入--'
        print(not_message)
    else:
        index = check_data.index(old_server)
        check_data[index] = new_server
    with open(file_location, 'r') as read_f, open(new_file_location, 'w') as write_f:
        tag = False
        new_write = False
        for read_line in read_f:
            if read_line.strip() == backend_data:
                tag = True
                continue
            if tag and read_line.startswith('backend'):
                tag = False
            if not tag:
                write_f.write(read_line)
            else:
                if not new_write:
                    for record in check_data:
                        write_f.write(record)
                    new_write = True
    read_f.close(), write_f.close()
    massage = '--已修改'
    return massage


def delete():
    print('--你所使用的功能为:<删除>')
    pass


if __name__ == '__main__':
    msg = """
    1:[查询]
    2:[添加]
    3:[修改]
    4:[删除]
    5:[退出]
    """

    msg_dic = {
        '1': check,
        '2': add,
        '3': change,
        '4': delete,

    }

    while True:
        print(msg)
        choice = input('--请输入你要执行的选项>>>').strip()
        file_1 = 'haproxy.conf'  # 文件的路径
        file_1_bak = file_1 + '.bak'
        new_file = 'File_management/new.conf_bak'  # 新文件的路径
        eg_format = [{'old_keyA': 'old_valueA', 'old_keyB': {'old_key1': 'old_value1', 'old_key2': 'old_value2'}},
                     {'new_keyA': 'new_valueA', 'new_keyB': {'new_key1': 'new_value1', 'new_key2': 'new_value2'}}]
        if not choice:
            continue
        if choice == '5':
            break
        if choice == '1':
            data_1 = input('--输入你的关键字>>>').strip()
            print(msg_dic[choice](data_1, file_1))
        if choice == '3':
            data_3 = eval(input('--输入要修改的源数据(格式为:dict嵌套list)\n--示例: %s>>>\n>>>' % eg_format).strip())
            print(msg_dic[choice](data_3, file_1, new_file))
            os.rename(file_1, file_1_bak)
            os.rename(new_file, file_1)
            os.remove(file_1_bak)
        if '1' < choice < '5' and choice != '3':
            msg_dic[choice]()
    pass
