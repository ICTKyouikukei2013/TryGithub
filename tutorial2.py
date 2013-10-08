#coding: utf-8

import sys, random, datetime

from flask import Flask
app = Flask(__name__)

@app.route("/<name>")
def root(name):
  l = [hello, konnichiha, date]
  return random.choice(l)(name)

def hello(name):
  return "Hello, %s!" % name

def konnichiha(name):
  return u"こんにちは、%s。" % name

def date(name):
  d = datetime.datetime.today()
  return u"%sさん、今日の日付は%s/%s/%sです。" % (name, d.year, d.month, d.day)

if __name__ == "__main__":
    app.debug = True
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
