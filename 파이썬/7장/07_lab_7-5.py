'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : Lab 7-5 함수는 튜플을 돌려줄 수 있다.
    
        반지름을 입력받아 원의 넓이와 둘레를 계산하시오.
        넓이와 둘레를 계산하는 함수를 작성하시오.
        함수는 넓이와 둘레를 함께 돌려줍니다.(return)
        
        [함수]
            # 3. 반지름을 받아서 매개변수에 저장한다.
            # 4. 넓이와 둘레를 계산한다.
            # 5. 넓이와 둘레를 돌려준다. (함수를 호출한 곳으로)
                return 넓이(area), 둘레(round)
            
        [메인]
            # 1. 반지름을 입력 받기
            # 2. 함수 호출 -> 반지름을 가지고 호출한다.
            # 6. 돌려받은 넓이와 둘레 튜플로 저장한다.
            # 7. 출력한다.
'''
def calCircle(r):
    area = 3.14 * r ** 2
    circum = 2 * 3.14 * r
    return area, circum # 얘들은 지역변수

radius = float(input("반지름을 입력하시오. : "))
(area, circum) = calCircle(radius) # 여기있는 변수는 전역 변수
print("반지름 : {} 인 원의 넓이 : {:.2f} 둘레 : {:.2f}".format(radius, area, circum))

circle = calCircle(radius)
print("반지름 : {} 인 원의 넓이 : {:.2f} 둘레 : {:.2f}".format(radius, circle[0], circle[1]))