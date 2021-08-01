# __module__ 和 __class__ 方法
from module.module_1 import Name

n = Name()
print(n.massage())

print(n.__module__)  # 来着那个模块
print(n.__class__)  # 那个类产生
