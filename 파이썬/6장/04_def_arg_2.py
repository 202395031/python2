'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 여려개의 값을 넘겨주고  여러개의 값을 돌려 받기.
    
    두 수를 전달하여 사칙연산의 결과값을 돌려주는 함수.
    
    [알고리즘]
    (함수)
        3. 두 수를 전달받아 매개변수에 저장한다.
        4. 두 수를 사칙연산(+,-,*,/,%)한다.
        5. 계산된 값들을 호출한 곳으로 돌려준다.
    (메인)
        1. 두 수를 입력 받는다.
        2. 두 수를 가지고 함수를 호출한다.
        6. 돌려받은 값을 출력한다.
'''
def cals(num1, num2):
    sum = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    rest = num1 % num2
    
    return sum, minus, mul, div, rest

num1 = int(input("첫번째 정수를 입력하시오. : "))
num2 = int(input("두번째 정수를 입력하시오. : "))
sum, minus, mul, div, rest = cals(num1,num2)
print(f"{num1}과 {num2}의 사칙연산 결과(+,-,*,/,% 순) : {sum}, {minus}, {mul}, {div}, {rest}")