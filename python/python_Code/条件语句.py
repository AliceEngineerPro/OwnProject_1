print('######################')

text_1 = input('1=')
if int(text_1) == 1:
    print('1等于1')
else:
    print('你家' + text_1 + '等于1?...')

print('######################')

text_2 = input('2=')
if int(text_2) == 2:
    print('你真棒')
print('谁不知道2=2?')

print('######################')

text_3 = input('3=')
if int(text_3) != 3:
    if int(text_3) == int(text_3):
        print('谁教你3=' + text_3)
else:
    print('你真聪明' + text_3 + '=3')

print('######################')

vip = input('请输入会员级别:')
if vip == '高级会员':
    print('美女')
elif vip == '白金会员':
    print('大妈')
elif vip == '铂金会员':
    print('一线小明星')
else:
    print('城管')
print('开始享受你的服务吧....')

print('######################')

text_4 = input('4=')
print('4=' + text_4)
if text_4 == '4':
    pass  # if不执行,pass表示过
else:
    print('孩子回去好好学习吧,')

print('end')
