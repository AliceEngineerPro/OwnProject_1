# __doc__方法
class Foo:
    "描述信息"
    pass


class Bar:
    pass
# print(Bar.__doc__)  # 无法继承之类


print(Bar.__dict__)
print(Foo.__doc__)
