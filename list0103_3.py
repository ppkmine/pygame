#tkinter 모듈 임포트
import tkinter

#스크롤 위치 관리 변수
x = 0
# 개 애니메이션용 변수
ani = 0
# 함수 정의
def animation():
    #전역함수 선언.
    global x, ani
    # x값 4 증가시킴
    x = x + 4
    # x 값이 480 이라면.?
    if x == 480 :
        # x 값에 0 대입
        x = 0
    #먼저 배경 이미지 삭제
    canvas.delete("BG")
    #배경 이미지 그리기 왼쪽
    canvas.create_image(x -240, 150, image=img_bg, tag="BG")
    #배경 이미지 그리기 오른쪽
    canvas.create_image(x +240, 150, image=img_bg, tag="BG")
    #ani 값을 0~3 범위로 변경
    ani = (ani + 1) % 4
    #개 이미지 그림.
    canvas.create_image(240, 200, image=img_dog[ani], tag="BG")
    root.after(200, animation)  #200밀리초 후 함수 재실행.


#윈도우 객체 생성
root = tkinter.Tk()
root.title("애니")
#캔버스 컴포넌트 생성.
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack() #캔버스 배치.

#변수 img_bg에 이미지 로딩.
img_bg = tkinter.PhotoImage(file="park.png")
#리스트 img_dog에 개 이미지 로딩 4장
img_dog = [
    tkinter.PhotoImage(file="dog0.png"),
    tkinter.PhotoImage(file="dog1.png"),
    tkinter.PhotoImage(file="dog2.png"),
    tkinter.PhotoImage(file="dog3.png")
]
#애니메이션을 표시하는 함수 실행.
animation()
root.mainloop()
