'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 터틀 그래픽으로 여러 개의 원을 그려보자
'''
import turtle as t

t.shape('turtle')

# 원 하나 그리기
# t.circle(100) # 반지름이 100인 원

t.speed(100)
for count in range(10):
    t.circle(100)
    t.left(360/10)

t.mainloop # 종료
# t.done()