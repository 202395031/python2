'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : while문으로 별그리기
            교재 131 페이지
'''
# turtle 모듈 불러오기
import turtle as t

t.shape('turtle')

# 1. 초기값 1로 지정
num = 1

# 2. num이 5이상일때까지 반복
while num <= 5:
    t.forward(100)
    t.right(144)
    num += 1    