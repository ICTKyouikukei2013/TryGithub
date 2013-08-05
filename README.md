# Github練習用リポジトリ
## Githubをいろいろいじって遊んでみる
  
## pull requestの流れ
1. ローカルにない場合、Githubからリポジトリファイルをcloneします。  
git clone URL

2. 初めての場合、作業ブランチを作る。  
git checkout -b 作業ブランチ名

3. 作業ブランチへ切り替えてmasterの更新に追随します   
git checkout master  
git pull

4. 作業します(ブランチ切り替えからコミットまで)  
git checkout 作業ブランチ名  
git add ~  
git commit ~

5. Githubにブランチをpushします。  
git push origin 作業ブランチ名

6. Github上でmasterへpull requestを送ります。  
githubのページに行ってpull requestボタンを探して押す

参考
  
* http://d.hatena.ne.jp/hnw/20110528
* http://blog.basyura.org/entry/20100323/p1

メモ

* git branch で 現在のブランチを確認できる