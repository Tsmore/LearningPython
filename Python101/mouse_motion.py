# p.089

import tkinter

FNT = ("Times New Roman", 40) # フォントの定義
def move(e): # マウスを動かしたときに呼び出す関数
  cvs.delete("all") # キャンバスに描いたものを削除
  s = "({}, {})".format(e.x, e.y) # ポインタの座標の文字列を用意
  cvs.create_text(400, 200, text=s, font=FNT) # その文字をキャンバスに表示

root = tkinter.Tk()
root.title("マウスポインタの座標")
root.bind("<Motion>", move) # イベント発生時に呼び出す関数を指定
cvs = tkinter.Canvas(width=800, height=400)
cvs.pack()
root.mainloop()