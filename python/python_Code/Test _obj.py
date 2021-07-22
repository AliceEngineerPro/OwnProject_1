# 弹药编码生成器

def ammo():
    for_word = input('弹药前17位: ')
    if len(for_word) == 17:
        count = int(input('弹药个数: '))
        bank_word = []
        for count_1 in range(count):
            bank_word_x = input('弹药后3位为: ')
            bank_word.append(bank_word_x)
        print('-' * 50, '\n弹药编号如下:\n')
        for count_2 in bank_word:
            ammo_num = '\'' + for_word + count_2
            print(ammo_num)
    else:
        return_value = '输入有误请重新输入!!!'
        return return_value
    return_value = '\n请复制弹药编号,如需继续请继续输入,结束请退出!'
    return return_value


if __name__ == '__main__':

    msg = """
    
    1-->[弹药编号生成]
    2-->[退出]
    
    """

    msg_dome = {
        1: ammo,

    }

    while True:
        print(msg)
        in_num = int(input('请输入功能编号>>>'))
        if not in_num:
            continue
        if in_num == 2:
            break
        if in_num == 1:
            print(msg_dome[in_num]())
