# -*- coding: utf-8 -*-
# Author：大米拉 2022年08月
# 功能：测试flask_life\
# get,post,put,delete对应的就是对这个资源的查，改，增，删四个操作

from flask import Blueprint, render_template, request
import dbutil
import chatAI

chat = Blueprint('chat', __name__)  # news蓝图


@chat.route('/chat', methods=['GET'])
def chatpage():
    return render_template("chat.html")


@chat.route('/chatProcess', methods=['POST'])
def chatProcess():
    db = dbutil.dbUtils('MyFlask.db')
    maxidsql = f"select max(ID) from chat_list"
    ID =int(db.db_action(maxidsql, 1)[0][0])+1

    # print(ID)
    name = 'mira'
    chat = request.form['chat']
    try:
        sql1 = f"insert into chat_list(ID,name,chat) values('{ID}','{name}','{chat}')"
        db.insert_or_update_data(sql1)

        sql2 = f"select chat from chat_list where ID='{ID}'"
        chat_info = db.db_action(sql2, 1)  # 1 查询 0 其他
        chat_info = "Me : {}".format(chat_info[0][0])
        db.close()
        response = "十字坡揉面小AI : {}".format(chatAI.chatbot.get_response(chat))
        contents = {chat_info, response}
        return render_template("chat.html", data=contents)
    except:
        return render_template("chat.html", message='inputs false!!!')





