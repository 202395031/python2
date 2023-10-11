'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수.
    
    (함수)
            5) 두 값을 전달받아 매개변수에 저장한다.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다.
    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min 과 생성된 리스트를 가지고 함수 호출     
            8) 돌려받은 최대값 또는 최소값을 출력한다.
'''
# 1. 랜덤 함수 불러오기
import random as r
# 2. 최대값 최소값 구분하는 함수 만들기
def num_MaxorMin(list, que):
    if que == 'max':
        num = 0
        for i in list:
            if num < i:
                num = i
    elif que == 'min':
        num = 999
        for i in list:
            if num > i:
                num = i
    return num
# 3. 위에 메인 알고리즘 따라간거
while True:
    num = []
    for i in range(10):
        num.append(r.randrange(10,99))
    print(num)
    que = input("최대값과 최소값 중에 알고 싶은걸 적으시오.(max/min) : ")
    if que == 'min' or que == 'max':
        if que == 'max':
            print("최대값은 :",num_MaxorMin(num,que))
        else :
            print("최소값은 :",num_MaxorMin(num,que))
    else:
        print("다시 입력 해주세요.")
    