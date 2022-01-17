# coding=utf8

import MySQLConnect

# 用户查询
sql_user = "select * from pytest.sys_user"

user_msg = MySQLConnect.MySQLConnect(
    host='cloud.mysql.superamfc.top',
    user='work',
    passwd='Work@123',
    port=23306,
    database='pytest',

).query(sql=sql_user)


if __name__ == '__main__':

    print(user_msg)

