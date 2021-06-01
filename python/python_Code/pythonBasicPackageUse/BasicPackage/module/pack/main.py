import python.python_Code.pythonBasicPackageUse.BasicPackage.module.pack.cal as cal
from python.python_Code.pythonBasicPackageUse.BasicPackage.module.pack.cal import add
import sys
# from python.python_Code.pythonBasicPackageUse.BasicPackage.module.pack.cal import *  # 不推荐


def main():

    print(add(1, 1))
    print(cal.sub(1, 1))
    print(sys.path)
