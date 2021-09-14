import emoji


init = input('输入要解码的表情代码:').strip()
emj = emoji.emojize(str(init), use_aliases=True)
print(emj)
