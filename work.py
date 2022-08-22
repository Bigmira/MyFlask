# -*- coding: utf-8 -*-
# Author：大米拉 2022年08月
# 功能：测试flask_work

from flask import Blueprint, render_template

work = Blueprint('work', __name__)


@work.route('/work')
def workpage():
    return render_template("work.html")
