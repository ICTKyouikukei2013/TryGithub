# -*- coding: utf-8 -*-
import sys

# 誰がどのTODOをやってもかまいません。ひとりで全部やってしまうもよし(多分できる)
# 必ずブランチを切って作業してください。
# masterは常に最新で、動くものにしてください。
# 面白い機能の追加、問題の追加は大歓迎です。
# 不明点などあれば中野まで

# TODO:
# 引数２つを受け取って、足し算して返す
# addメソッドを作成
def add(x,y):
    return x+y

# TODO:
# 引数２つを受け取って、引き算して返す
# minusメソッドを作成
def minus(x,y):
    return x-y

# TODO:
# 引数２つを受け取って、掛け算して返す
# multiplyメソッドを作成
def multiply(x,y):
    return x*y

# TODO:
# 引数２つを受け取って、割り算して返す
# devideメソッドを作成
def devide(x,y):
    if y!=0:
        return x/y
    else:
        return 0

if __name__ == "__main__":
	# TODO:
	# コマンドラインから引数２つを取得してnumberへ保存
	# 応用：メソッドにする
    number = sys.argv
	# 引数の数
    length = len(number)
	# 引数を取得したものが足りなかったらエラーを吐いてプログラム終了
    if length < 3:
        print '引数が %d 個少ないです。' % (3 - length)
        quit()

    if length > 3:
        print '引数が %d 個多いです。' % (length - 3)
        quit()

	# TODO:
	# 最初の引数を使ってFizzBuzz問題を解こう！

    for value in range(int(number[1]),int(number[2])+1):
        flag = True
    # TODO:
    # 3の倍数の時にFizzを表示
        if value%3==0:
            flag = False
            print "Fizz",
    # TODO:
    # 5の倍数の時にBuzzを表示
        if value%5==0:
            flag = False
            print "\bBuzz",
        
        if flag:
            print value
        else:
            print ""
    # TODO:
    # 3と5の倍数の時にBuzzを表示
    
    #そんなもの必要ない

    # TODO:
    # リファクタリング
    # if 引数 % 3 && 引数 % 5を使わない書き方
    # FizzBuzzの位置はきっとここではない

    # TODO:
    # numberを使って計算した結果を表示しよう
    # 足し算、引き算、割り算、掛け算
