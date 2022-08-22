# -*- coding: utf-8 -*-
# Author：大米拉 2022年08月
# 功能：测试flask

from flask import Flask, render_template, redirect, url_for, session, request
from user import user
from life import life
from work import work
from chat import chat

app = Flask(__name__)
app.secret_key = 'any random string'
urls = [life, user, work, chat]  # 将三个路由构建数组
for url in urls:
    app.register_blueprint(url)  # 将三个路由均实现蓝图注册到主app应用上


@app.route('/')
def index():
    userinfo = ''
    return render_template("index.html", data=userinfo)


if __name__ == "__main__":
    print(app.url_map)  # 打印url结构图
    app.run(port=2020, host="127.0.0.1", debug=True)
