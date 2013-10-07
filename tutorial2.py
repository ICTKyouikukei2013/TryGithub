#coding: utf-8

import sys

from flask import Flask
app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"

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
