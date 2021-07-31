import pymysql

# 连接数据库

line_mysql = pymysql.connect(host='localhost',
                             user='root',
                             passwd='root',
                             database='learn_db',
                             charset='utf8')


cursor = line_mysql.cursor()

sql_state = "drop table mysql_db ;"
sql_state1 = "create table mysql_db(id int primary key  auto_increment comment 'ID', name varchar(20) comment '姓名'"\
             ", money int comment '金额');"
sql_state2 = "insert into mysql_db(name,money) values ('name1',8000),('name2',8000) ;"
sql_state3 = "update mysql_db set money=money-5000 where name='name1' ;"
sql_state4 = "update mysql_db set money=money+5000 where name='name2' ;"

cursor.execute(sql_state)
cursor.execute(sql_state1)


try:
    cursor.execute(sql_state2)
    line_mysql.commit()
    cursor.execute(sql_state3)
    Exception('异常')
    print('异常')
    cursor.execute(sql_state4)
    line_mysql.commit()

except Exception as e:

    line_mysql.rollback()
    line_mysql.commit()

cursor.close()
line_mysql.close()