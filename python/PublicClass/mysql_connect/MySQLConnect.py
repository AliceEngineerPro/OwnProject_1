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
    #     # ���ݿ���Ϣ(�������ݿ�)
    #     connect = self.connect
    #     cur = connect.cursor()  # �α�
    #     cur.execute(sql)  # ִ��sql, ���ز�ѯ���������
    #     data_all = cur.fetchall()  # ����һ����άԪ��-->sql��ѯ�ý��
    #     # ѭ�����д���µ��б���
    #     for row in data_all:
    #         query_list.append(list(row))  # ���ݿ���ҵ��, list[[SQLData],]
    #     cur.close()  # �α����
    #     connect.close()  # �ر�MySQL����
    #
    #     return query_list
    #
    # def updata_mysql(self, sql=None):
    #
    #     # ���ݿ���Ϣ(�������ݿ�)
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

