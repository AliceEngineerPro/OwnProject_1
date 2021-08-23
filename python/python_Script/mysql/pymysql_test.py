# encoding=utf-8

import time

import pymysql

# 打开数据库连接
start_time = time.time()
db = pymysql.connect(
    host='amfc.ltd',
    user='root',
    password='root',
    port=13306,
    database='discuss',
    charset='utf8'

)

try:

    curses = db.cursor()

    sql = "select id, name from discommon_district where upid like 0"

    curses.execute(sql)
    results_1 = curses.fetchall()
    for row in results_1:
        id = row[0]
        name = row[1]
        print('ID=%s,name=%s' % (id, name))


    upid0 = input('省-->')
    sql0 = "select id, name from discommon_district where upid like %s" % upid0

    curses.execute(sql0)
    resource = curses.fetchall()
    for row in resource:
        id = row[0]
        name = row[1]
        print('ID=%s,name=%s' % (id, name))


    upid1 = input('市/州-->')
    sql1 = "select id, name from discommon_district where upid like %s" % upid1

    curses.execute(sql1)
    resource = curses.fetchall()
    for row in resource:
        id = row[0]
        name = row[1]
        print('ID=%s,name= %s' % (id, name))


    upid2 = input('区/县-->')
    sql2 = "select id, name from discommon_district where upid like %s" % upid2

    curses.execute(sql2)
    resource = curses.fetchall()
    for row in resource:
        id = row[0]
        name = row[1]
        print('ID=%s,name=%s' % (id, name))


    upid3 = input('街道/镇-->')
    sql3 = "select id, name from discommon_district where upid like %s" % upid3

    curses.execute(sql3)
    resource = curses.fetchall()
    for row in resource:
        id = row[0]
        name = row[1]
        print('ID=%s,name=%s' % (id, name))

    sql_1 = "select name from discommon_district where id like %s" % upid0
    sql_2 = "select name from discommon_district where id like %s" % upid1
    sql_3 = "select name from discommon_district where id like %s" % upid2
    sql_4 = "select name from discommon_district where id like %s" % upid3

    curses.execute(sql_1)
    resource = curses.fetchall()
    s = ()
    for row in resource:
        s = row[0]

    curses.execute(sql_2)
    resource = curses.fetchall()
    z = ()
    for row in resource:
        z = row[0]

    curses.execute(sql_3)
    resource = curses.fetchall()
    q = ()
    for row in resource:
        q = row[0]

    curses.execute(sql_4)
    resource = curses.fetchall()
    c = ()
    for row in resource:
        c = row[0]

    print('\n\n地址为%s,%s,%s,%s' % (s, z, q, c))

except:
    print('Data error')


db.close()
