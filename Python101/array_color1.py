# p.073
import tkinter
root = tkinter.Tk()
root.title("配色で色を定義")
cvs = tkinter.Canvas(width=840, height=160)

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] # 配列で色を指定
for i in range(7): # iは0から6まで1つずつ増える
  X = i*120 # 地形を描くx座標を計算しXに代入
  cvs.create_rectangle(X, 0, X+120, 160, fill=rainbow[i], width=0)

cvs.pack()
root.mainloop()