
class School:
    """
    学校类
    """

    def __init__(self, school_name, school_address, school_type):
        self.school_name = school_name
        self.school_address = school_address
        self.school_type = school_type

        pass

    def only(self, school_profession, school_other):

        pass


class Teacher:
    """
    老师类
    """

    def __init__(self, teacher_name, teacher_age, teacher_gander, teacher_profession):
        self.teacher_name = teacher_name
        self.teacher_age = teacher_age
        self.teacher_gander = teacher_gander
        self.teacher_profession = teacher_profession

        pass

    def only(self, teacher_other):

        pass


class Course:
    """
    课程类
    """

    def __init__(self, course_time):
        self.course_time = course_time

        pass

    def only(self, course_other):

        pass


class ClassRoom:
    """
    班级类
    """

    def __init__(self, classroom_number, classroom_people, classroom_admin):
        self.classroom_number = classroom_number
        self.classroom_people = classroom_people
        self.classroom_admin = classroom_admin

        pass

    def only(self, classroom_other):

        pass


class Student:
    """
    学生类
    """

    def __init__(self, student_name, student_age, student_gender, student_profession):
        self.student_name = student_name
        self.student_age = student_age
        self.student_gender = student_gender
        self.student_profession = student_profession

        pass

    def only(self, student_score, student_other):

        pass


school_1 = School('清华大学', '北京市海淀区五道口', '985,211')
teacher_1 = Teacher('jack', 30, 'male', 'math')
course_1 = Course('45min')
classroom_1 = ClassRoom(1, 20, 'alex')
student_1 = Student('Steven', 18, 'female', 'computer')


print('学校名称:%s,地址:%s,学校类型:%s' % (school_1.school_name, school_1.school_address, school_1.school_type))
print('学生姓名:%s,就读学校:%s,所在班级:%s,专业:%s,班主任:%s'
      % (student_1.student_name,
         school_1.school_name,
         classroom_1.classroom_number,
         student_1.student_profession,
         teacher_1.teacher_name))
