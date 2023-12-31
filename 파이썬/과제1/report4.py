'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 파이선의 random.randint(1,100)을 이용하여 1에서 100 사이의 임의의 난수 2개를 생성하여라.
            다음으로 두 수의 합을 묻는 질문을 사용자에게 던지도록 하자. 만일 사용자가 두 수의 합을 
            맞추면 '잘했어요!!'를 출력하여라. 만일 틀릴 경우 '정답은 000입니다.'를 출력하여라
'''

# 1. random함수를 불러온다.
import random

# 2. 2개의 난수를 생성한다.
num1 = random.randint(1,100)
num2 = random.randint(1,100)

# 2. 정답을 입력받는다.
answer = int(input(f"{num1} + {num2} = "))

# 3. 만약 정답 일 경우 '잘했어요!!'를 출력
if answer == num1 + num2 :
    print('잘했어요!!')
# 4. 아니면 '정답은 000입니다.'를 출력
else :
    print(f"정답은 {num1+num2}입니다.")