import emoji


init = input('输入要解码的表情:')
emj = emoji.emojize(init, use_aliases=True)
print(emj)
