#coding: utf-8

import sys
import datetime
import random

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

 神谷先生のコードレビュー
 *マジックナンバーは使わない
 *そのためにreternする文を関数にする
 *そうすると文の追加や編集がしやすくなる
 *追加した関数を配列にする
 *random.choiceの引数に関数の配列を与えて、その中からランダムに返す
 *その値を変数に代入してその変数を実行する
 →マジックナンバーが使われず、文の追加の方法も分かりやすく簡単になった。
"""
def hello1(username):
	return 'Hello, %s!' % username

def hello2(username):
	return u'こんにちは、%s。' % username

def hello3(username):
	now = datetime.datetime.now()
	return u'%sさん、今日の日付は%sです。' % (username, now.strftime('%Y/%m/%d'))

hello_func = [hello1, hello2, hello3]

@app.route('/<username>')
def show_username(username):
	hello = random.choice(hello_func)
	return hello(username)

"""
if __name__ == "__main__":
    app.run()
は一番下にないと@app.routeが反応しなかった

500 internal server error
app.runn()にdebug=Trueを渡すとエラーが出た時にどのへんがダメなのか教えてくれる
"""
if __name__ == "__main__":
    app.run(debug=True)

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