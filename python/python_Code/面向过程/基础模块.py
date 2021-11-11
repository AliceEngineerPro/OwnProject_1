# 模块

"""
python标准库  直接 import 导入
第三方模块  pip 下载 , import 导入
程序自定义的模块库
"""

import configparser  # 配置文件模块
import datetime  # 日期时间
import hashlib  # hash算法, MD5
import json  # json 信息
import logging  # 日志文件
import os  # 操作系统交互
import pickle  # 序列化, 反序列化
import random  # 随机模块
import re  # 正则表达式, 字符串的匹配
import shelve  # 序列化模块, 比 pickle简单, 只有open一个函数, 返回字典, 可读写, key为字符串, value为python支持的所有类型
import sys  # 解释器交互
# 系统模块
import time  # 时间
import xml.etree.ElementTree as ET  # xml 模块

print('基础模块:time, datetime, random, os, sys, json, pickle, shelve, xml, re, logging, configparser, hashlib')


def time_module():
    print(time.time())  # 时间戳(秒数) float 格式, 从1970-1-1-00.00.00开始算起, 到现在的走过的秒 1622619938
    print(time.localtime())  # 结构化时间, 时间对象, 当前时区时间
    print(time.gmtime())  # 时区为0的结构化时间 世界标准时间UTC
    # 时间戳-->>结构化时间
    print(time.localtime(time.time()))
    # 结构化时间-->>时间戳
    print(time.mktime(time.localtime()))
    # 结构化时间-->>字符串时间
    print(time.strftime('%Y-%m-%d %X', time.localtime()))  # '%Y(年)-%m(月)-%d(日) %X(时分秒)' , localtime 为结构化时间
    # 字符串时间-->>结构化时间
    print(time.strptime('2021:06:02:15:57:49', '%Y:%m:%d:%X'))
    # 结构化时间-->>固定形式 '周 月 日 时 分 秒 年'
    print(time.asctime())  # 默认为time.localtime
    # 时间戳-->>固定形式 '周 月 日 时 分 秒 年'
    print(time.ctime())  # 默认为time.time

    massage = '\n↑↑↑以上为time模块\n'
    return massage


def data_time_module():
    print(datetime.datetime.now())  # 显示当前时间 '年-月-日 时:分:秒'

    massage = '\n↑↑↑以上为data time模块\n'
    return massage


def random_module():
    list_num = []
    for i in range(11):
        list_num.append(i)
    set_num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(random.random())  # 默认随机生成 (0-1) 的 float
    print(random.randint(1, 3))  # 随机生成 (1, 3) 的 int
    print(random.randrange(1, 3))  # 随机生成 (1, 3] 的 int
    print(random.choice(set_num))  # 随机生成 list, set等 里的一个元素
    print(random.sample(list_num, 3))  # 随机生成 list, set等 中的多个元素, 以 list 的方式输出
    print(random.uniform(1.5, 1.6))  # 随机生成 (1.5, 1.6) 中的一个 float
    # 随机排列列表 ***只限于列表***
    print('原列表', list_num)
    random.shuffle(list_num)
    print('执行random.shuffle后的列表', list_num)

    massage = '\n↑↑↑以上为random模块\n'
    return massage


def os_module():
    print(os.getcwd())  # 当前工作路径
    # print(os.environ)  # 查看系统环境变量
    # os.chdir('pythonBasicPackageUse')  # 更改当前路径下的其他文件夹为当前工作路径
    # os.makedirs('test1/test2')  # 在工作目录下新建文件夹, 可以递归
    # os.removedirs('test1/test2')  # 在工作目录下删除文件夹, 可以递归, 如果上层不为空则无法删除
    # os.mkdir()  # 新建一个文件夹
    # os.rmdir()  # 删除一个文件夹
    # os.remove()  # 删除一个文件
    # os.rename()  # 重命名一个文件
    # print(os.listdir())  # 获取当前工作目录的所有文件, 以列表方式输出
    # print(os.stat('Test _obj.py'))  # 查看文件的信息
    # print(os.path.dirname(os.getcwd()))  # 返回上级目录
    # print(os.path.split(r'E:\my_project\VScodeNote\python'
    #                     r'\python_Code\pythonBasicPackageUse\code_module\os1.py'))  # 返回文件夹和文件
    # print(os.path.dirname(r'E:\my_project\VScodeNote\python'
    #                       r'\python_Code\pythonBasicPackageUse\code_module\os1.py'))  # 返回上一级目录
    # print(os.path.basename(r'E:\my_project\VScodeNote\python'
    #                        r'\python_Code\pythonBasicPackageUse\code_module\os1.py'))  # 输出当前文件名字
    dirname1 = 'E:\my_project\VScodeNote\python'
    dirname2 = 'python_Code\pythonBasicPackageUse\code_os_module\os1.py'
    # print(os.path.join(dirname1, dirname2))  # 路径拼接

    massage = '\n↑↑↑以上为os模块\n'
    return massage


def sys_module():
    print(sys.argv)  # 工作路径, 含文件名
    for i in range(100):
        sys.stdout.write('#')
        time.sleep(0.2)
        sys.stdout.flush()
    print()
    # print(sys.version)  # python解释器的版本
    # print(sys.path)

    massage = '\n↑↑↑以上为sys模块\n'
    return massage


def json_module():
    dic = {'name': 'jack'}
    msg_json = json.dumps(dic)  # 转为str
    print(msg_json)
    print(type(msg_json))
    os.chdir('file')

    # 写json
    # f_w = open('new_file', 'w')
    # f_w.write(msg_json)
    # f_w.close()

    # 从文件中读json
    f_r = open('new_file', 'r')
    f_data = json.loads(f_r.read())  # 使用loads时必须符合json语法
    print(f_data)
    print(type(f_data))
    # print(f_data['name'])

    f_r.close()
    os.chdir('..')

    massage = '\n↑↑↑以上为json模块\n'
    return massage  # #


def pickle_module():  # 数据序列化类型更多
    dic = {'name': 'jack', 'age': '18', 'sex': 'male'}
    print(type(dic))
    pick_data = pickle.dumps(dic)  # 转为bytes
    # print(pick_data, type(pick_data))

    os.chdir('file')

    # 写pickle
    # f_w = open('pickle_file', 'wb')
    # f_w.write(pick_data)
    # f_w.close()

    # 读pickle
    f_r = open('pickle_file', 'rb')
    f_data = pickle.loads(f_r.read())
    print(f_data['name'], type(f_data))

    f_r.close()
    os.chdir('..')

    massage = '\n↑↑↑以上为pickle模块\n'
    return massage


def shelve_module():
    os.chdir('file')
    f_w = shelve.open(r'shelve_file')
    # f_w['stu1_info'] = {'name': 'jack', 'age': '18', 'sex': 'male'}
    # f_w['stu2_info'] = {'name': 'jack_f', 'age': '20'}
    # f_w['school_info'] = {'home': 'amfc.ltd', 'city': 'China'}
    #
    print(f_w.get('stu1_info')['name'])
    f_w.close()
    os.chdir('..')

    massage = '\n↑↑↑以上为shelve模块\n'
    return massage


def xml_module():
    os.chdir('file')
    tree_file = ET.parse('xml_file')
    root_file = tree_file.getroot()
    # print(root_file.tag)

    # 遍历xml文件
    """
    for i in root_file:
        tag_1 = i.tag  # tag: 标签, 节点  eg: <tag>text</tag>
        attrib_1 = i.attrib  # attrib: 标签属性  eg: <tag attrib[key] = 'attrib[value]'>text</tag>
        text_1 = i.text  # text: 标签中包含的数据  eg: <tag>text</tag>

        print(tag_1)  # 只会输出节点的名字
        print(attrib_1)  # 输入每个tag的属性
        # print(text_1)

        print('-' * 50)

        for j in i:  # 第二个循环
            tag_2 = j.tag  # 子标签  eg: <tag>text</tag>
            attrib_2 = j.attrib  # 子标签属性  eg: <tag attrib[key] = 'attrib[value]'>text</tag>
            text_2 = j.text  # 字标签中包含的数据  eg: <tag>text</tag>

            print(tag_2)
            print(attrib_2)
            print(text_2)

            print('-' * 20)
        print('-' * 50)

    for singer in root_file.iter('year'):  # 取单一标签中的信息
        print(singer.tag, singer.text)
        """

    # 修改xml文件
    """
    for tag_file in root_file.iter('year'):
        # 修改标签中的信息
        new_year = int(tag_file.text) + 1
        tag_file.text = str(new_year)
        # 修改标签属性
        tag_file.set('updated', 'yes')  # key和value用 ', ' 分割
    tree_file.write('xml_file')  # 文件名字不变 == 覆盖文件
    """

    # 删除xml文件内容
    """
    for tag_file in root_file.findall('country'):  # findall 找多个标签
        rank = int(tag_file.find('rank').text)  # find找一个标签
        if rank >= 50:
            root_file.remove(tag_file)
    tree_file.write('new_xml_file')
    """

    # 创建xml文件
    """
    # Element: 创建一个根节点为 'member' 标签
    new_xml = ET.Element('member')
    # SubElement: 创建子标签(哪个父标签创建, 子标签名, attrib(属性) = {'key(标签属性)': 'value(值)'})
    name_tag1 = ET.SubElement(new_xml, 'name', attrib={'enrolled': 'yes'})
    age_tag1 = ET.SubElement(name_tag1, 'age', attrib={'checked': 'no'})
    sex_tag1 = ET.SubElement(name_tag1, 'sex')
    # sex标签中的数据
    age_tag1.text = 'male'
    sex_tag1.text = '20'

    name_tag2 = ET.SubElement(new_xml, 'name', attrib={'enrolled': 'yes'})
    age_tag2 = ET.SubElement(name_tag2, 'age', attrib={'checked': 'no'})
    sex_tag2 = ET.SubElement(name_tag2, 'sex')
    age_tag2.text = 'male'
    sex_tag2.text = '22'

    name_tag3 = ET.SubElement(new_xml, 'name', attrib={'enrolled': 'yes'})
    age_tag3 = ET.SubElement(name_tag3, 'age', attrib={'checked': 'no'})
    sex_tag3 = ET.SubElement(name_tag3, 'sex')
    age_tag3.text = 'female'
    sex_tag3.text = '30'

    xml_file = ET.ElementTree(new_xml)  # 生成文档对象
    xml_file.write('own_xml', encoding='utf8', xml_declaration=True)  # 写入文档

    ET.dump(new_xml)
    """

    os.chdir('..')

    massage = '\n↑↑↑以上为xml模块\n'
    return massage


def re_module():
    file = " . ^ $ * + ? {} [] | () \ "  # 元字符
    """
    .  通配符 每个 '.' 代表1个字符, 除了 "\n"
    ^  表示开头, 必须放在开头
    $  表示结尾,放在结尾
    *  表示重复
    +  表示重复, 最后一个字符重复
    ?  同样的字符多取一个 字符个数区间-->?(0, 1)
    {}  {0, } == *
        {1, } == +
        {0, 1} == ?
    []  字符集, 功能符号: - eg:[0-9], [a-z]
                        ^ 表示非
                        / 转为普通字符
    |  表示或
    ()  表示分组 
    \  转义符
        \d == 匹配任何10进制的数[0, 9]
        \D == 匹配任何非10进制的数
        \s == 匹配任何空白字符
        \S == 匹配任何非空白字符
        \w == 匹配任何字母数字[0-9a-zA-Z]
        \W == 匹配任何非字母数字[^0-9a-zA-Z]
        \b == 匹配一个特殊符号边界, eg: & # 等
    """

    # findall  # 满足匹配条件 存在列表里
    # print(re.findall('..ja..ck', 'asjaasckkkkdafgrthdasdajaasckkkqwefaszxvaajaqeckkkk'))
    # print(re.findall('jac[abcdefghijklmnopqrstuvwxyz]', 'jack'))
    # print(re.findall('jac[^a-z]*', 'jac1kq123'))
    # print(re.findall('jack|l', 'jack1jacljack1lljack'))
    # print(re.findall(r'I\b', 'I am jack'))

    # search  匹配成功返回对象, 匹配失败,返回空, 只会匹配第一个; 通过group()方法得到匹配成功后的字符串, 函数本身返回为对象(object)类型

    test_b = re.search('a((bc)|(ac))d', 'abcd')
    print(test_b.group())
    # print(type(test_b.group()))

    module_search = re.search('(?P<name>[a-z]+)(?P<age>\d+)', 'jack18alex36xiaoming33')
    print(module_search.group('name', 'age'))

    # split  分隔
    module_split1 = re.split('[ |]', 'hello world|!')
    print(module_split1)
    module_split2 = re.split('[ab]', 'abcab')
    print(module_split2)

    # sub 替换
    module_sub = re.sub('\d', 'A', 'asdasd654asd654asd541sad3asd4asd4q')
    print(module_sub)

    # subn 替换 返回元组, (返回内容, 返回匹配次数)
    module_subn = re.subn('\d', 'A', 'asdasd654asd654asd541sad3asd4asd4q')
    print(module_subn)

    # compile  编译封装正则表达式的方法
    module_compile = re.compile('\d')
    compile_file = module_compile.findall('asd74asd447664as465d654qw654asd321')
    print(compile_file)

    # finditer 封装到迭代器
    finditer_module = re.finditer('\d', 'asd546as546d513as1d53as1d54a6sd')
    ll = []
    for i in finditer_module:
        i = i.group()
        ll.append(i)
    print(ll)

    massage = '\n↑↑↑以上为re模块\n'
    return massage


def logging_module():
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     filename='../python_Code/file/logger.log',
    #     filemode='w',
    #     format='%(asctime)s %(filename)s [%(lineno)d] :%(message)s'
    # )

    logger1 = logging.getLogger('my_logging')
    logger1.setLevel(logging.DEBUG)  # 日志输出优先级
    fh1 = logging.FileHandler('../python_Code/file/log.log')  # 日志输入文件地址
    ch1 = logging.StreamHandler()  # 输出到控制台

    fm = logging.Formatter('%(asctime)s %(filename)s [%(lineno)d] :%(message)s')  # 输入格式

    # 格式化日志输出格式
    fh1.setFormatter(fm)
    ch1.setFormatter(fm)

    logger1.addHandler(fh1)
    logger1.addHandler(ch1)

    logger2 = logging.getLogger('my_log.log')
    logger2.setLevel(logging.INFO)
    fh2 = logging.FileHandler('../python_Code/file/log_new.log')
    ch2 = logging.StreamHandler()

    fh2.setFormatter(fm)
    ch2.setFormatter(fm)

    logger2.addHandler(fh2)
    logger2.addHandler(ch2)

    logger1.debug('1 debug message')
    logger1.info('1 info message')
    logger1.warning('1 warning message')
    logger1.error('1 error message')
    logger1.critical('1 critical message')

    logger2.debug('2 debug message')
    logger2.info('2 info message')
    logger2.warning('2 warning message')
    logger2.error('2 error message')
    logger2.critical('2 critical message')

    # logging.debug('debug message')
    # logging.info('info message')
    # logging.warning('warning message')
    # logging.error('error message')
    # logging.critical('critical message')

    print()

    message = '\n↑↑↑以上为logging模块\n'
    return message


def configparser_module():
    # 生成一个配置文件
    config = configparser.ConfigParser()  # config = {}
    config['DEFAULT'] = {'ServerAliveInterval': '45',
                         'Compression': 'yes',
                         'CompressionLevel': '9',
                         'ForWardX11': 'yes'}

    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'

    config['topsecret.server.com'] = {}
    top = config['topsecret.server.com']
    top['Host Port'] = '50022'
    top['ForwardX11'] = 'no'

    with open('../python_Code/file/configfile_new', 'w') as configfile:
        config.write(configfile)

    # 读配置文件
    config.read('../python_Code/file/configfile')
    print(config.sections())  # 读取文件的所有键

    # 判断
    # print('server.com' in config)

    # 查询
    # print(config['bitbucket.org']['User'])

    # 循环遍历
    for key in config['topsecret.server.com']:
        # print(key)
        pass

    # 取键, 返回列表
    # print(config.options('bitbucket.org'))  # 默认把[DEFAULT]一起取出

    # 取键值对, 键值对返回元组, 列表嵌套
    # print(config.items('bitbucket.org'))

    # 取值
    # print(config.get('bitbucket.org', 'compression'))

    # 删,改(覆盖),增
    # 增(块)
    config.add_section('Other')
    config.add_section('Other1')
    # 增(配置)
    config.set('Other', 'other1', '1')  # 用逗号分隔
    config.set('Other', 'other2', '2')
    # 删(块)
    config.remove_section('Other1')
    # 删(配置)
    config.remove_option('Other', 'Other1')

    config.write(open('../python_Code/file/configfile_new', 'w'))

    configfile.close()

    print()
    message = '\n↑↑↑以上为configparser模块\n'
    return message


def hashlib_module():
    obj1 = hashlib.md5()
    obj2 = hashlib.sha256()
    obj1.update('Amfc0-./'.encode('utf8'))

    print(obj1.hexdigest())

    print()
    message = '\n↑↑↑以上为hashlib模块\n'
    return message


print(time_module())
# print(data_time_module())
# print(random_module())
# print(os_module())
# print(sys_module())
# print(json_module())
# print(pickle_module())
# print(shelve_module())
# print(xml_module())
# print(re_module())
# print(logging_module())
# print(configparser_module())
# print(hashlib_module())

