# 类

def school(school_name, school_address, school_type):
    def init(s_name, s_address, s_type):
        school1_mag = {
            'school_name': s_name,
            'school_address': s_address,  # XX省XX市XX区XX街道XX
            'school_type': s_type,
            'school_exam': exam,
            'school_admission': admission,

        }
        return school1_mag

    def exam(school_exam):
        print('%s 学校正在考试' % school_exam['school_name'])

    def admission(school_admission):
        print('%s %s 学校正在考试' % (school_admission['school_type'], school_admission['school_name']))

    return init(school_name, school_address, school_type)


s1 = school('school', 'XX', '私立')
print(s1)
s1['school_exam'](s1)
