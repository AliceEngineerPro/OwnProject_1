import pymysql


class MySQLConnect:

    def __init__(self, passwd, host='127.0.0.1', user='root', port=3306, database=None, charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.database = database
        self.charset = charset

        self.connect = pymysql.Connect(
            host=self.host,
            user=self.user,
            password=self.passwd,
            port=self.port,
            database=self.database,
            charset=self.charset,

        )

    def query(self, sql):

        query_list = []
        connect = self.connect
        cursor = connect.cursor()
        try:
            cursor.execute(sql)
            query_data = cursor.fetchall()
            for row_data in query_data:
                query_list.append(row_data)
            cursor.close()
            connect.close()
            return query_list
        except Exception as error:
            return error
        pass

    def commit(self):
        pass

    # def query_mysql(self, sql=None):
    #     query_list = []
    #
    #     # 数据库信息(连接数据库)
    #     connect = self.connect
    #     cur = connect.cursor()  # 游标
    #     cur.execute(sql)  # 执行sql, 返回查询结果的行数
    #     data_all = cur.fetchall()  # 返回一个二维元组-->sql查询得结果
    #     # 循环结果写入新的列表中
    #     for row in data_all:
    #         query_list.append(list(row))  # 数据库作业点, list[[SQLData],]
    #     cur.close()  # 游标结束
    #     connect.close()  # 关闭MySQL连接
    #
    #     return query_list
    #
    # def updata_mysql(self, sql=None):
    #
    #     # 数据库信息(连接数据库)
    #     connect = self.connect
    #     cur = connect.cursor()
    #     try:
    #         cur.execute(sql)
    #         connect.commit()
    #     except:
    #         connect.rollback()
    #         return False
    #     cur.close()
    #     connect.close()
    #
    #     return True

