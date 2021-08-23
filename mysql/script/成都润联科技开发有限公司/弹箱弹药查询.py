import msvcrt
import os

import pymysql


class Mysql:

    def __init__(self, mysql_host, mysql_user, mysql_password, mysql_database, mysql_port=3306, mysql_charset='utf8'):
        self.host = mysql_host
        self.user = mysql_user
        self.password = mysql_password
        self.database = mysql_database
        self.port = mysql_port
        self.charset = mysql_charset

    def ammo_code(self):
        db_code = pymysql.connect(host=self.host,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  port=int(self.port),
                                  charset=self.charset
                                  )
        cursor = db_code.cursor()
        find_ammo_code = input('请输入弹药ID>>>')
        mysql_statement_ammo = "select * from (select tb_ammo_info.id as ammo_id, tb_ammo_info.code as ammo_code, tb_ammo_box_info.id as box_id, tb_ammo_box_info.boxCode as box_code, tb_storage_info.id as storage_id, tb_storage_info.name as storage_name, tb_storage_info.code as storage_china_code, tb_storage_info.deptCode as storage_depatment_code, tb_ammo_box_info.storageState as storage_status, tb_ammo_box_info.ammoState as ammo_status from tb_ammo_info ,tb_ammo_box_info, tb_storage_info where tb_ammo_info.boxId=tb_ammo_box_info.id and tb_ammo_info.storageId=tb_storage_info.id) as msg where msg.ammo_code='%s';" % (
            find_ammo_code)
        cursor.execute(mysql_statement_ammo)
        all_msg = cursor.fetchall()
        hand = '(ammo_id, ammo_code, box_id, box_code, storage_id, storage_name, storage_china_code, storage_department, storage_status, ammo_status)'
        print(hand)
        for row in all_msg:
            ammo_id = row[0]
            ammo_code = row[1]
            box_id = row[2]
            box_code = row[3]
            storage_id = row[4]
            storage_name = row[5]
            storage_china_code = row[6]
            storage_department = row[7]
            storage_status = row[8]
            ammo_status = row[9]
            print(ammo_id, ammo_code, box_id, box_code, storage_id, storage_name, storage_china_code,
                  storage_department, storage_status, ammo_status)

        db_code.close()

    def box_code(self):
        db_box = pymysql.connect(host=self.host,
                                 user=self.user,
                                 password=self.password,
                                 database=self.database,
                                 port=int(self.port),
                                 charset=self.charset
                                 )
        cursor = db_box.cursor()
        find_box_code = input('请输入弹箱ID>>>')
        mysql_statement_box = "select * from (select tb_ammo_info.id as ammo_id, tb_ammo_info.code as ammo_code, tb_ammo_box_info.id as box_id, tb_ammo_box_info.boxCode as box_code, tb_storage_info.id as storage_id, tb_storage_info.name as storage_name, tb_storage_info.code as storage_china_code, tb_storage_info.deptCode as storage_depatment_code, tb_ammo_box_info.storageState as storage_status, tb_ammo_box_info.ammoState as ammo_status from tb_ammo_info ,tb_ammo_box_info, tb_storage_info where tb_ammo_info.boxId=tb_ammo_box_info.id and tb_ammo_info.storageId=tb_storage_info.id) as msg where msg.box_code='%s';" % (
            find_box_code)
        cursor.execute(mysql_statement_box)
        all_msg = cursor.fetchall()
        hand = '(ammo_id, ammo_code, box_id, box_code, storage_id, storage_name, storage_china_code, storage_department, storage_status, ammo_status)'
        print(hand)
        for row in all_msg:
            ammo_id = row[0]
            ammo_code = row[1]
            box_id = row[2]
            box_code = row[3]
            storage_id = row[4]
            storage_name = row[5]
            storage_china_code = row[6]
            storage_department = row[7]
            storage_status = row[8]
            ammo_status = row[9]
            print(ammo_id, ammo_code, box_id, box_code, storage_id, storage_name, storage_china_code,
                  storage_department, storage_status, ammo_status)

        db_box.close()

if __name__ == '__main__':

    msg = """
    1-->> 根据弹药编号查询
    2-->> 根据弹箱编号查询
    任意键退出
    """

    msg_msg = {1: '根据弹药编号查询', 2: '根据弹箱编号查询',}

    while True:
        print(msg)
        msg_in = int(input('请输入操作-->>'))
        if msg_in in msg_msg.keys():
            msg_db_host = input('输入数据库主机IP-->')
            msg_db_user = input('输入数据库用户名-->')
            msg_db_passwd = input('输入数据库密码-->')
            msg_db_database = input('输入数据库名-->')
            msg_db_port = input('输入数据库端口号(默认3306)-->')
            if msg_db_port == '':
                msg_db_port = 3306

            select_db = Mysql(msg_db_host, msg_db_user, msg_db_passwd, msg_db_database, int(msg_db_port))
            if msg_in == 1:
                select_db.ammo_code()
            if msg_in == 2:
                select_db.box_code()
        else:
            stop = '123'
            msvcrt.getch(stop)
            os.system('pause')


