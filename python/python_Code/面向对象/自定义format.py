class Date:

    def __init__(self,year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def __format__(self, format_spec):
        x = '{0.year}-{0.mon}-{0.day}'
        return '%s' % x .format(self)


d = Date(2021, 7, 31)
print(d.__format__(d))

