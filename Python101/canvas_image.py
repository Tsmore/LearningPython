# p. 071
import tkinter
root = tkinter.Tk()
root.title("キャンバスに画像を表示")
cvs = tkinter.Canvas(width=1000, height=720)
img = tkinter.PhotoImage(file="image/chap3_illust.png") # 変数imgに画像を読み込む
cvs.create_image(540, 360, image=img) # キャンバスに画像を表示
cvs.pack()
root.mainloop()