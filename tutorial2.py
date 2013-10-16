#coding: utf-8

import sys
import datetime

from flask import Flask
app = Flask(__name__)

"""
@app.route('/<username>')は
 http://a2c.bitbucket.org/flask/quickstart.html
の変数ルールってところを見る。
型を指定しないとおそらくstring型になる

キャストの仕方は
 (変換後の型)(値や変数)
とする。値や変数が1個だったとしても()でくくる。

日本語を含んだ文字列はASCⅡの文字コードと認識されるらしく、そのままusernameをぶち込むとエラーが起きるので、文字列の最初にuをつけて文字コードがutf-8だと認識させる
 u"~~~"
"""
@app.route('/<username>')
def show_username(username):
	now = datetime.datetime.now()
	random = (int)(now.microsecond) % 3
	if(random == 0):
		return 'Hello, %s!' % username
	elif(random == 1):
		return u'こんにちは、%s。' % username
	else:
		return u'%sさん、今日の日付は%sです。' % (username, now.strftime('%Y/%m/%d'))

"""
if __name__ == "__main__":
    app.run()
は一番下にないと@app.routeが反応しなかった

500 internal server error
app.runn()にdebug=Trueを渡すとエラーが出た時にどのへんがダメなのか教えてくれる
"""
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