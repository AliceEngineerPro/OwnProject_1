# 组合

class Hand:

    pass


class Foot:

    pass


class Head:

    pass


class Trunk:

    pass


class Person:

    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name
        self.hand = Hand()
        self.foot = Foot()
        self.trunk = Trunk()
        self.head = Head()


p1 = Person('1xx1xx19xx0x1x12xx', 'alex')


class School:

    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address

    def admissions(self):
        print('%s 正在招生' % self.school_name)


class Course:

    def __init__(self, course_name, course_price, course_period, course_school):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period
        self.course_school = course_school


# School
s1 = School('清华大学', '北京五道口')
s2 = School('南开大学', '天津八里台')
# # Course
# c1 = Course('linux', '100', '24h', )
# c2 = Course('python', '100', '24h', s1)
# c3 = Course('java', '100', '24h', s1)
# c4 = Course('c语言', '100', '24h', s1)


# 调用
# print(c1.course_school.school_name)

while True:
    msg_school = {
        '1': '清华大学',
        '2': '南开大学',

    }

    menu_school = {
        '1': s1,
        '2': s2,

    }

    print('*' * 50, '\n', msg_school)
    select_school = input('>>>:')
    msg_new_school = menu_school[select_school]
    print(msg_new_school.school_name, msg_new_school.school_address)

    c1 = Course('linux', '100', '24h', msg_new_school)
    c2 = Course('python', '100', '24h', msg_new_school)
    c3 = Course('java', '100', '24h', msg_new_school)
    c4 = Course('c语言', '100', '24h', msg_new_school)

    msg_course = {
        '1': 'linux',
        '2': 'python',
        '3': 'java',
        '4': 'c语言'
    }

    menu_course = {
        '1': c1,
        '2': c2,
        '3': c3,
        '4': c4,

    }

    print('*' * 50, '\n', msg_course)
    select_course = input('>>>:')
    msg_new_course = menu_course[select_course]
    print(msg_new_course.course_school.school_name, msg_new_course.course_name, msg_new_course.course_school.school_address)

