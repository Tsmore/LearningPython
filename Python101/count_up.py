# p.084 リアルタイム処理

import tkinter

n = 0 # 初期値0の変数を用意
def count(): # リアルタイム処理を行う関数
  global n # nをグローバル関数として扱う
  n = n + 1
  cvs.delete("all") # キャンバスに描いたものを削除
  cvs.create_text(200, 100, text=n, font=("System", 80)) # キャンバスにnの値を表示
  root.after(1000, count) # 1000ミリ秒後にcount()を呼び出す

root = tkinter.Tk()
root.title("リアルタイム処理")
cvs = tkinter.Canvas(width=400, height=200)
cvs.pack()
count() # count()関数を呼び出す
root.mainloop()

# cvs.create_text(x座標, y座標, text=文字列, font=(フォントの種類, 文字サイズ))
# フォント"System"は半角文字がドット風になる
# delete("all")を入れないと描いたものが消えずにどんどん重なる
# なんども上書きすると処理が重くなるため全て消してから表示する(どんどん重くなるゲームなんか嫌だ)
# 数のカウントに使う変数nをcount()変数の外側で宣言しているため(関数の外で宣言した変数をグローバル変数という)
# 関数の冒頭でglobal 変数名と記述する