'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 단을 입력 받아 해당 단의 구구단을 출력하시오.
            교재 130 페이지
            
            문제 분석 : 단을 입력 받는다. 입력 받을 변수가 필요함
                        해당 단의 구구단을 출력하기 위해 반복을 해야함 반복문때 변수 필요
                        반복을 하면서 구구단을 출력해줘야 할듯 
                        9까지 반복
                        
            필요한 변수 : num, dan
'''

# 1. 초기값 지정
num = 1

# 2. 변수를 입력받는다.
dan = int(input('원하는 단을 입력하시오 : '))

# 3. num 9 이상일때까지 반복
while num <= 9 :

# 3-1. 구구단 출력 dan * num
    print(f"{dan} x {num} = {num*dan}")

# 3-2. 증가값 num을 1씩 증가
    num += 1