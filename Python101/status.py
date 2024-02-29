import tkinter
root = tkinter.Tk()
root.title("ゲームのステータス画面を作ろう")
cvs = tkinter.Canvas(width=960, height=640)
img = tkinter.PhotoImage(file="image/character1.png") # 変数imgに画像を読み込む
cvs.create_image(480, 320, image=img) # キャンバスに画像を表示
cvs.create_rectangle(540, 60, 900, 580, fill="black", outline="white", width=3) # 画面右側の枠を描く
ability = ["HP", "腕力", "防御力", "知力", "精神力", "素早さ"] # 能力値の名称を配列で定義
value = [1200, 800, 320, 9999, 3540, 780] # それらの値を配列で定義
for i in range(6): # iは0から5まで1ずつ増える
  y = 120+80*i # 文字を表示するy座標を計算
  cvs.create_text(660, y, text=ability[i], font=("Times New Roman", 20), fill="white") # 能力値の名称を表示
  cvs.create_text(800, y, text=value[i], font=("Times New Roman", 24), fill="white") # その値を表示

cvs.pack()
root.mainloop()