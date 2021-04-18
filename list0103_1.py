import tkinter

root = tkinter.Tk() #윈도우 객체 생성.
root.title("Canvas에 화면 그리기") #윈도우 타이틀지정
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack() #캔버스 배치.
img_bg = tkinter.PhotoImage(file="park.png")
canvas.create_image(240, 150, image=img_bg)
#캔버스에 이미지 그리기
root.mainloop()     