'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임
            
            random함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보

            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''

import random

print(":: 가위 바위 보 게임 시작 ::")

player1 = input("player1의 이름을 입력하시오 : ")
player2 = input("player2의 이름을 입력하시오 : ")

num1 = random.randrange(3)  #player1의 랜덤 번호
num2 = random.randrange(3)  #player2의 랜덤 번호


# player1의 가위 바위 보 출력
print(player1,": ", end='')
if num1 == 0 :
    print("가위")
elif num1 == 1 :
    print("바위")
else:
    print("보")
    
# player2의 가위 바위 보 출력
print(player2,": ", end='')
if num2 == 0 :
    print("가위")
elif num2 == 1 :
    print("바위")
else:
    print("보")
    
    
if (num1 == 1 and num1 > num2) or (num1 == 2 and num2 == 1) or (num1 == 0 and num2 == 2) :
    print(f"{player1}이(가) {player2}에게 이겼습니다.")
elif num1 == num2 :
    print(f"{player1}와(과) {player2}은(는) 무승부입니다.")
else :
    print(f"{player2}이(가) {player1}에게 이겼습니다.")