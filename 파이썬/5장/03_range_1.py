'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : range() 함수
'''
for i in range(3):  # i 변수에 0~2의 값이 저장 됨.
    print(i, end='. ')  # end='' 로 지정 하면 줄바꿈 하지 않는다.
    print("안녕하세요")
    print("   천승용입니다.")
    
# range(시작값, 숫자 앞까지, 증가값 or 감소값)
# c일경우 for(초기값;조건식;증감식);

for i in range(1,6):
    print(i, end=' ')

print() # 빈 줄 출력

# 10 ~ 1까지 출력
for i in range(10,0,-1):
    print(i, end=' ')
    
print()