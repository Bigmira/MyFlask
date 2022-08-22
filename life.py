# -*- coding: utf-8 -*-
# Author：大米拉 2022年08月
# 功能：测试flask_life\
# get,post,put,delete对应的就是对这个资源的查，改，增，删四个操作

from flask import Blueprint, render_template, request
import dbutil

life = Blueprint('life', __name__)  # news蓝图

class DataStore():
    a = None
data = DataStore()

@life.route('/life', methods=['GET'])
def lifepage():
    db = dbutil.dbUtils('MyFlask.db')
    sql = 'select * from lifes'
    lieflist = db.db_action(sql, 1)  # 1 查询 0 其他
    db.close()
    return render_template("life.html", data=lieflist)

@life.route('/lifepageadd', methods=['POST'])
def lifepageadd():
    id = request.form['id']
    data.a = id
    f_type = request.form['f_type']
    s_type = request.form['s_type']
    content = request.form['content']
    try:
        id = str(id)
        db = dbutil.dbUtils('MyFlask.db')
        # sql1 = "INSERT INTO list_daily (id,f_type,s_type,content) VALUES (?,?,?,?)", (id, f_type, s_type, content)
        sql1 = f"insert into list_daily(id,f_type,s_type,content) values('{id}','{f_type}','{s_type}','{content}')"
        db.insert_or_update_data(sql1)

        sql2 = f"select * from list_daily"
        list_daily = db.db_action(sql2, 1)  # 1 查询 0 其他
        db.close()
        return render_template("life.html", data=list_daily)
    except:
        return render_template("life.html", message='inputs false!!!')



@life.route('/life/edit')
def lifeEditpage():
    return '/life/edit'

