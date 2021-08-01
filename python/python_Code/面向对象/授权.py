import time

class Open:

    def __init__(self, filename, mode='r', encoding='utf8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = open(filename, mode, encoding=encoding)

    def write(self, line):
        t = time.strftime('%Y-%m-%d %X')
        self.file.write('%s %s' % (t, line))

    def __getattr__(self, item):
        return getattr(self.file, item)


open1 = Open('授权/a.txt', 'r+')
open1.write('1\n')
open1.write('2\n')
open1.write('3\n')
# open1.write('4\n')
# open1.seek(0)1
# print(open1.read())
