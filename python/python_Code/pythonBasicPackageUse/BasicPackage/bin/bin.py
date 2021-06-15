import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
sys.path.append(BASE_DIR)

from python.python_Code.pythonBasicPackageUse.BasicPackage.module.pack.cal import add
# from  import cal

print(os.path.dirname(os.path.realpath('__file__')))  # 当前路径
print(add(1, 2))


