'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 함수에 일을 시키고 그 값을 받아 오기.

    원의 넓이 구하기
    반지름이 3인 원의 넓이를 구한다.
    반지름 값을 전달받아 원의 넓이를 구하고, 넓이를 돌려주는 함수를 작성한다.
    
    [알고리즘]
    (함수) area
        2. 반지름 값을 전달 받아 매개 변수에 저장한다.
        3. 반지름으로 원의 넓이를 계산한다.
        4. 계산된 넓이를 함수를 호출한 곳으로 돌려준다.
    
    (함수 호출하는 메인)
        1. 반지름을 가지고 함수를 호출한다.
        5. 돌려받은 넓이를 출력한다.
'''
print(":: 리턴값이 있는 함수 (원의 넓이 구하기) ::")

# 함수 선언
def area(radius):   # 전달받은 반지름을 매개 변수에 저장
    result = 3.14 * radius ** 2 # 원의 넓이 계산
    return result   # result 값을 호출한 곳으로 돌려준다.

result = area(3)
print(f"반지름이 3인 원의 넓이는 {result} 입니다.")

print(":: 반지름을 입력 받아 원의 넓이 게산하기 ::")

r = int(input("반지름을 입력하시오 : "))
result = area(r)    # 전달받은 결과를 result에 저장
print(f"반지름이 {r}인 원의 넓이는 {result} 입니다.")   # result에 저장된 결과 출력

                                    # 반지름을 가지고 함수 호출하고, 전달받아 바로 출력
print(f"반지름이 {r}인 원의 넓이는 {area(r)} 입니다.")