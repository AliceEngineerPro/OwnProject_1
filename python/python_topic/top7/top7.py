# 人口总和和各省人口占比


def people():
    with open('人口.txt', 'r', encoding='utf8') as f:
        for i in f:
            yield i


get = people()
# print(get)
#
# all_pop = (eval(i)['people'] for i in get)
# print(all_pop)
# print(type(all_pop))


p_dic_list = []
count = 0
for p in get:
    p_dic = eval(p)
    j = int(p_dic['people'])
    p_dic_list.append(j)
    count += 1


all_p = set(p_dic_list)

j = 1
for j in range(count):
    # if j > 0:
    print(p_dic_list[j] / sum(all_p))
    pass

# print(count)

get.close()
