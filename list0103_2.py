# 배경 스크롤 하기.

import tkinter

x = 0
def scroll_bg():
    global x
    x = x + 1  # x 값 1증가.
    if x == 480:
        x = 0 #if x가 480이 되면 x 에 0 대입
    canvas.delete("BG") # 먼저 배경 이미지 삭제
    canvas.create_image(x -240, 150, image=img_bg, tag="BG") #배경 이미지 그리기 왼쪽
    canvas.create_image(x +240, 150, image=img_bg, tag="BG") #배경 이미지 오른쪽
    root.after(50, scroll_bg) #50밀리 초 후 함수 재실행.

root = tkinter.Tk()  #윈도우 객체 실행.
root.title("화면 스크롤") # 화면 타이틀.
canvas = tkinter.Canvas(width =480, height = 300)
canvas.pack()  #캔버스 배치.
#변수 img_bg에 이미지 로딩.
img_bg =tkinter.PhotoImage(file="park.png")
#화면 스크롤하는 함수 실행.
scroll_bg()
#윈도우 표시
root.mainloop()
    

    