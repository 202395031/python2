'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 조건에 따라 반복하는 while문
            교재 127 페이지
'''
# while 조건식 : => : 반드시 사용.
#   들여쓰기로 반복하면서 할일 작성

# 반복문에서는 반드시 종료 조건이 있어야 한다.
# while True :      무한반복

under_construction = True   # 공사중.

# True일때 동안 계속 반복
while under_construction :
    response = input("공사가 완료 되었습니까? ")
    if response == "예":    # 종료 조건
        under_construction = False  # 공사 완료
        
print("루프 탈출!!!")
    