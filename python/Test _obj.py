
def px():
    width = int(input('长(px)-->').strip())
    height = int(input('高(px)-->').strip())
    w = width / 10 * 4
    h = height / 10 * 4

    return_value = w, h
    return return_value


print(px())

