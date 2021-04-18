# tkinter 모듈 임포트
import tkinter

#함수 정의
def mouse_click(e):
    #px에 마우스 포인터 x 좌표 대입
    px = e.x
    #py에 마우스 포인터 y 좌표 대입
    py = e.y
    #px와 py 값 출력,
    print("마우스 포인터 좌표: ({},{})".format(px, py))
    #mx에 px/ 48으 ㅣ정수값 대입.
    mx = int(px/48)
    #my에 py/ 48의 정수값 대입.
    my = int(py/48)
    #mx 와 my가 데이터 범위 안이면
    if 0<= mx and mx <= 6 and 0<= my and my <= 4:
        #n에 맵 칩 번호 대입
        n = map_data[my][mx]
        #맵 칩 이름 출력.
        print("여기에 있는 맵 칩은" + CHIP_NAME[n])



#윈도우 객체 생성
root = tkinter.Tk()
root.title("맵 데이터")
canvas = tkinter.Canvas(width="336", height="240")
canvas.pack()

#캔버스 클릭시 실행할 함수 지정.
canvas.bind("<Button>", mouse_click)
#맵 칩 이름을 리스트로 정의.
CHIP_NAME =["풀" , "꽃", "숲", "바다"]
#리스트에 이미지 로딩.
img = [
    tkinter.PhotoImage(file="chip0.png"), #풀
    tkinter.PhotoImage(file="chip1.png"), #꽃
    tkinter.PhotoImage(file="chip2.png"), #숲
    tkinter.PhotoImage(file="chip3.png"), #바다
]

#2 차원 리스트로 맵 데이터 정의.
map_data = [
    [0,1,0,2,2,2,2],
    [3,0,0,0,2,2,2],
    [3,0,0,1,0,0,0],
    [3,3,0,0,0,0,1],
    [3,3,3,3,0,0,0]
]

#반복 y값은 0~4 에서 1씩 증가.
for y in range(5):
    for x in range(7):
        canvas.create_image(x * 48 + 24, y * 48 + 24, 
        image=img[map_data[y][x]])

root.mainloop()

        