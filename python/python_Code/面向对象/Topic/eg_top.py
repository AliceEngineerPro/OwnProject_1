# eg
import pickle


class Base:

    def save(self):
        with open('school.db', 'wb') as f:
            pickle.dump(self, f)


class School(Base):

    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address


class Student:

    def __init__(self, student_name, student_classroom):
        self.student_name = student_name
        self.student_classroom = student_classroom


class Class:

    def __init__(self, class_name, class_period, class_price):
        self.class_name = class_name
        self.class_period = class_period
        self.class_price = class_price


class Teacher:
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name


# msg

msg = {
    '1': '学校',
    '2': '建立学员',
    '3': '建立课程',
    '4': '建立老师',
    '5': '退出程序',

}

school_mag = {
    '1': '查询',
    '2': '建立',
}

while True:

    print(msg)
    select_msg = int(input('输入选项>>>'))
    if select_msg == 1:
        print(school_mag)
        select_school_msg = int(input('输入选项>>>'))
        if select_school_msg == 1:
            read_school = pickle.load(open('school.db', 'rb'))
            print(read_school.school_name, read_school.school_address)
            select_end = input('继续请输入1, 任意键退出:>>>')
            if select_end != str(1):
                break
        if select_school_msg == 2:
            ipt_school_name = input('输入学校名字>>>')
            ipt_school_address = input('输入学校地址>>>')
            School(ipt_school_name, ipt_school_address).save()
    if select_msg > 5:
        print('>>>输入错误,请重新输入\n')
    if select_msg == 5:
        break
