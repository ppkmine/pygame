import tkinter

def key_down(e):
    key_c = e.keycode
    label1["text"] = "keycode " + str(key_c)
    key_s = e.keysym
    label2["text"] = "keysym " + key_s


#객체 생성
root = tkinter.Tk()
root.geometry("400x200") #윈도우 크기
root.title("키 입력")
root.bind("<KeyPress>", key_down)
fnt = ("Times New Roman", 30) #폰트 정의
label1 = tkinter.Label(text="keycode", font=fnt)
label1.place(x = 0, y = 0)
label2 = tkinter.Label(text="keysym",  font=fnt)
label2.place(x = 0, y = 80)
root.mainloop()