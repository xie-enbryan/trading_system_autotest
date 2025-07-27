# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/27 20:53
# @Author: Enbryan Xie
import pymysql

from common.yaml_config import GetConf

class MysqlOperate:

    def __init__(self):
        mysql_conf = GetConf().get_mysql_config()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = mysql_conf["password"]
        self.conn = None
        self.cur = None

    def __conn_db(self):
        """
        连接数据库，获得connection还有cursor
        :return:
        """
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.password,
                                        db=self.db, port=self.port, charset="utf8")
        except Exception as e:
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        """
        关闭数据库连接，包括cursor还有connection
        :return:
        """
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        """
        提交sql语句的方法
        :return:
        """
        self.conn.commit()
        return True

    def query(self, sql):
        """
        数据库查询操作
        :param sql:
        :return:
        """
        # 连接数据库
        self.__conn_db()
        # 执行数据查询的操作
        self.cur.execute(sql)
        # 得到查询的结果
        query_data = self.cur.fetchall()

        # 如果查询的结果为空，即没有数据
        if query_data == ():
            query_data = None
            print("没有获取到数据，表为空")

        else:
            pass
        self.__close_conn()
        return query_data

    def insert_update_table(self, sql):
        # 连接数据库
        self.__conn_db()
        # 执行sql语句
        self.cur.execute(sql)
        # 提交sql语句的操作
        self.__commit()
        # 关闭数据库连接
        self.__close_conn()

if __name__ == '__main__':
    print(MysqlOperate().query("select * from user;"))





