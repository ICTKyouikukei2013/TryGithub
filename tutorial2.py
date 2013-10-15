#coding: utf-8

import sys
import random
import datetime

from flask import Flask
app = Flask(__name__)

@app.route("/yuto")
def hello():
    d = datetime.datetime.today()
    a=random.randint(1,3)
    if a==1:
        return "Hello, yuto！"
    if a==2:
        return "こんにちは、yuto。"
    if a==3:
        return "yutoさん、今日の日付は｢%s/%s/%s｣です。" % (d.year, d.month, d.day)

if __name__ == "__main__":
    app.run()

# http://flask.pocoo.org/
# このドキュメントを読んで勉強しつつ、
# http://localhost:5000/「名前」
# とウェブブラウザのバーに入れると、
# ランダムに以下のいずれかを表示する。

# Hello, 「名前」!
# こんにちは、「名前」。
# 「名前」さん、今日の日付は「YYYY/MM/DD」です。

# 「名前」の部分はアルファベット
# 「YYYY/MM/DD」の部分は実際の日付
