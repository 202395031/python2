'''
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 직각 삼각형의 빗변의 길이를 구하시오.
            빗변 공식 : c = (a제곱 + b제곱)*0.5
'''

bottom = int(input("밑변의 길이를 적으시오 : "))
height = int(input("높이의 길이를 적으시오 : "))  

hypotenuse = (bottom ** 2 + height ** 2) ** 0.5

print("밑변이 {} 높이가 {} 인 직각 삼각형의 빗변은 {} 입니다.".format(bottom,height,hypotenuse))