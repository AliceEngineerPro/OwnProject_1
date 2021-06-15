import os
import sys


os.chdir('../../file')
dic = "{'name': 'jack'}"

# 写
# f_w = open('文件', 'w')
# f_w.write(dic)

# 读
f_r = open('文件', 'r')
msg_r = f_r.read()
print(msg_r)
print(type(msg_r))
msg_r = eval(msg_r)
print(msg_r)
print(type(msg_r))
print(msg_r['name'])


os.chdir('../pythonBasicPackageUse/code_module')
print(os.getcwd())
