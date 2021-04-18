#tkinter 모듈 임포트
import tkinter

#윈도우 객체 생성.
root = tkinter.Tk()
#윈도우 타이틀 지정.
root.title("맵 데이터")
#캔버스 컴포넌트 생성.
canvas = tkinter.Canvas(width=336, height=240)
#캔버스 배치
canvas.pack()
#리스트에 이미지 로딩.
img = [
    tkinter.PhotoImage(file="chip0.png"),
    tkinter.PhotoImage(file="chip1.png"),
    tkinter.PhotoImage(file="chip2.png"),
    tkinter.PhotoImage(file="chip3.png")
]

# 2차원 리스트로 맵 데이터 정의.
map_data =[
    [0,1,0,2,2,2,2],
    [3,0,0,0,2,2,2],
    [3,0,0,1,0,0,0],
    [3,3,0,0,0,0,1],
    [3,3,3,3,0,0,0]
]

# 반복, y값은 0~4에서 1씩 증가.
    #반복 x 값은 0~6에서 1씩 증가.
        #변수 n에 리스트값 대입.
            #맵 칩 그리기.

for y in range(5):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x * 48 + 24, y * 48 + 24, image=img[n])

root.mainloop()
