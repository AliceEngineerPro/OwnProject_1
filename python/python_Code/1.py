# 处理列表中的每个元素, 得到的结果也是一个'列表',列表中的元素和位置与原来的一样
# map()

# 遍历序列中的每一个元素,判断每个元素的布尔值,如果是True则留下来
# filter
people = [
    {'name': 'one', 'age': 18},
    {'name': 'two', 'age': 22},
    {'name': 'three', 'age': 16},
    {'name': 'four', 'age': 25}

]
people_new = filter(lambda x: x['age'] >= 18, people)
print(list(people_new))

# 处理一个序列, 把序列进行合并操作
# reduce

from functools import reduce

new_list = reduce(lambda x, y: x + y, range(101), 0)
print(new_list)