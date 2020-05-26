# -*- coding: utf8 -*-
import pymysql


class BaseMysql(object):
    def __init__(self):
        self.MYSQL_HOST = None
        self.MYSQL_USER = None
        self.MYSQL_PW = None
        self.MYSQL_DATABASE = None
        self.MYSQL_PORT = 3306
        self.conn = None
        self.cur = None
        self.init_conf()

    def init_conf(self):
        self.MYSQL_HOST = ""
        self.MYSQL_USER = ""
        self.MYSQL_PW = ""
        self.MYSQL_DATABASE = ""
        self.MYSQL_PORT = 3306

    def __enter__(self):
        self.init()
        return self

    def query_sql(self, sql):
        try:
            count = self.cur.execute(sql)
            data = self.cur.fetchall()
            return count, data
        except Exception as e:
            raise Exception('sql: {}, error: {}'.format(sql, e))

    def do_sql(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            raise Exception("sql: {}, error: {}".format(sql, e))

    def init(self):
        self.conn = pymysql.connect(
            host=self.MYSQL_HOST,
            user=self.MYSQL_USER,
            password=self.MYSQL_PW,
            database=self.MYSQL_DATABASE,
            port=self.MYSQL_PORT
        )
        self.cur = self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
