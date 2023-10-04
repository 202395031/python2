'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : while문으로 사용자가 입력한 숫자들을 더하는 프로그램 만들기
            교재 133 페이지
'''

print("::: break 없는 버전 :::")

# 1. 초기값이랑 변수 지정하기
total = 0
que = 'yes'

# 2. que 가 yes 일때 반복
#   2-1. 숫자를 입력받는다.
#   2-2. 합계를 더한다.
#   2-3. 계속할지 입력받는다.

while que == 'yes':     # yes가 아니면 종료임
    num = int(input("숫자를 입력하시오: "))
    total += num
    que = input("계속?(yes/no): ")
    
# 3. que에서 no를 입력받았을때 합계 total 출력
print(f"합계는 : {total}")



print("::: break 있는 버전 :::")

# 1. 초기값이랑 변수 지정하기
total = 0

# 2. que 가 yes 일때 반복
#   2-1. 숫자를 입력받는다.
#   2-2. 합계를 더한다.
#   2-3. 계속할지 입력받는다.
#   2-4. 만약 no를 입력받으면,
#       2-4-1.break

while True:
    num = int(input("숫자를 입력하시오: "))
    total += num
    que = input("계속?(yes/no): ")
    if que != 'yes':
        break
    
# 3. que에서 no를 입력받았을때 합계 total 출력
print(f"합계는 : {total}")