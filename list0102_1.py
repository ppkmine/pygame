import tkinter
import datetime

def time_now():
    d = datetime.datetime.now()
    t = "{0}:{1}:{2}".format(d.hour, d.minute, d.second)
    label["text"] = t
    root.after(1000, time_now)


root = tkinter.Tk() #윈도우 객체 생성.
root.geometry("400x100")  #윈도우 크기 지정.
root.title("간이 계산")  #윈도우 title
label = tkinter.Label(font =("Times New Roman", 60)) #폰트 정의
label.pack()  #라벨 배치.
time_now()    #time_now()실행.
root.mainloop()    #윈도우 표시.