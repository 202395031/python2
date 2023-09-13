'''
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : turtle 그리기
'''


import turtle as t  # turtle 모듈을 사용하기 위한 준비
                    # turtle 클래스 객체를 t로 생성. (별명)

t.shape('turtle')
t.speed(2)
# 선 그리기
# t.forward(200)  # 200픽셀 이동.

# 삼각형 그리기
# t.forward(200)  # 200픽셀 만큼 이동.
# t.left(120)     # 왼쪽으로 60도 회전.
# t.forward(200)
# t.left(120)
# t.forward(200)
# t.left(120)

# 반복문으로 삼각형 그리기
for i in range(5):
    t.forward(200)
    t.left(144)

t.mainloop()    # 그림판이 사라지지 않는다.