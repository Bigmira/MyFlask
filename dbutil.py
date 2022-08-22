# -*- coding: utf-8 -*-
# Author：大米拉 2022年08月
# 功能：测试flask 数据库互动部分

class dbUtils:
    def __init__(self, dbName):  # 连接数据库
        import sqlite3
        self.conn = sqlite3.connect(dbName)

    def db_action(self, sql, actionType=0):  # 进行相关业务操作
        try:
            res = self.conn.execute(sql)
            if actionType == 1:  # 当操作类型为1时代表为查询业务，返回查询列表
                return res.fetchall()
            else:  # 当操作类型不为1时代表为新增、删除或更新业务，返回逻辑值
                return True
        except ValueError as e:
            print(e)

    def insert_or_update_data(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            print('写入数据库成功')
        except:
            print('Error')

    def close(self):  # 关闭数据库
        self.conn.commit()
        self.conn.close()

'''
# 1.创建数据库
db = dbUtils('MyFlask.db')
# 2.创建life表
sql = 'create table lifes (lifeid int, content text, author text)'
if db.db_action(sql, 0) == True:
    print("创建life表成功！")
else:
    print("try again1")
# 3.新增life内容
sql = "insert into lifes values(1,'画画','cao')," \
      "(2,'摄影','cao')"
if db.db_action(sql, 0) == True:
    print("新增life表成功！")
else:
    print("try again")
db.close()
'''