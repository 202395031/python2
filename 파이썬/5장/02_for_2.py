'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 반복문 for 사용하기
'''
# 본인 이름 5개 출력하기
print(":: 내 이름 5개 출력하기 ::")
for i in range(5):
    print(i, ": 천승용")

print() # 빈줄 출력

print(":: 내 이름 5개 출력하기(리스트) ::")
for i in [1,2,3,4,5]: # 리스트
    print(i, ": 천승용")

print() # 빈줄 출력
   
print(":: 리스트로 구구단 19단 출력 ::")
for num in [1,2,3,4,5,6,7,8,9]: # range(1, 10)
    print(f"19 x {num} = {num*19}")

print(":: 문자열 내용 출력 ::")
for i in "Hello":
    print("i =",i) # i 값 출력
    
print("::: BTS 멤버 명단 출력 :::")

bts = ['뷔', '제이홉', 'RM', '정국', '진', '지민', '슈가']

for i in bts:
    print(i, end=' ')

print()