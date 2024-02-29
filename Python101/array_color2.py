# p.075

import tkinter
root = tkinter.Tk()
root.title("2次元配列で色を定義")
cvs = tkinter.Canvas(width=800, height=600, bg="black")

color = [ # 2次元配列で色を定義
  ["brown", "red", "orange", "gold"],
  ["darkgreen", "green", "limegreen", "lime"],
  ["navy", "blue", "skyblue", "cyan"]
]

for y in range(3): # yは0から2まで1ずつ増える
  for x in range(4): # xは0から3まで1ずつ増える
    X = x*200 # 円を描くx座標を計算
    Y = y*200 # 円を描くy座標を計算
    cvs.create_oval(X, Y, X+200, Y+200, fill=color[y][x]) # 色を指定して円を描く

cvs.pack()
root.mainloop()