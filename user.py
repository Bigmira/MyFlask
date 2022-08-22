# -*- coding: utf-8 -*-
# Author：大米拉 2022年08月
# 功能：测试flask_user

from flask import Blueprint, render_template, session, url_for, request
from werkzeug.utils import redirect

user = Blueprint('user', __name__)   # 蓝图使用方法，参数里给定文件名，还可以给定url前缀

@user.route('/login')
def loginpage():
    return render_template("login.html")

@user.route('/loginProcess', methods = ['POST', 'GET'])
def loginProcesspage():
    if request.method == 'POST':
        nm = request.form['nm']
        pwd = request.form['pwd']
        if nm == 'Mira' and pwd == '123':
            session['username'] = nm
            print(session['username'])
            return redirect(url_for('index'))
        else:
            return 'the username or userpwd does not match!'
