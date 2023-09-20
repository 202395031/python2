'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임
            
            random함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보
'''

import random

print(":: 가위 바위 보 게임 시작 ::")
num = random.randrange(3)

game = input("가위 바위 보 중에 선택하시오. : ")

if num == 0 :
    print("가위")
elif num == 1 :
    print("바위")
else:
    print("보")


