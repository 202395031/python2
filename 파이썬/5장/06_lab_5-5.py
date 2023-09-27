'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 반복문ㅇ로 펙토리얼 구하기.
'''
num = int(input("정수 n을 입력하시오. : "))
fac = 1
for i in range(1, num+1):
    fac = fac * i
print(f"{num}!은 {fac} 이다.")