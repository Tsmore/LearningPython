# p.069 (2)
import tkinter
root = tkinter.Tk()
root.title("キャンバスに図形を描く")
cvs = tkinter.Canvas(width=800, height=500, bg="white")
cvs.create_line(0, 0, 100, 160, 200, 20, 300, 60, fill="black", smooth=True) # 黒い曲線
cvs.create_rectangle(50, 150, 300, 400, fill="red", width=0) # 赤い正方形
cvs.create_oval(400, 50, 700, 200, outline="blue", width=20) # 青い楕円
cvs.create_polygon(450, 250, 350, 450, 550, 450, fill="green", outline="lime", width=10) # 緑の三角形
cvs.create_arc(600, 220, 780, 400, start=45, extent=270, fill="orange", outline="") # オレンジのパックマン
cvs.pack()
root.mainloop()