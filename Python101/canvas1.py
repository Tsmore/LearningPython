import tkinter
root = tkinter.Tk()
root.title("キャンバスに線を書く") # タイトルを指定
cvs = tkinter.Canvas(width=600, height=400, bg="black") # キャンバスを用意
cvs.create_line(0, 0, 500, 300, fill="red", width=5) # キャンバスに幅5の赤い線を引く
cvs.pack() # キャンバスをウィンドウに配置
root.mainloop()

# キャンバスの変数名 = tkinter.Canvas(width=幅, height=高さ, bg=背景色)