'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 반복문을 제어하는 break, continue
            교재 137 페이지
            
    Test word : programming
    
    결과 예상 : pr
'''
# 1. 변수를 입력받는다.
word = input("단어를 선택하세요 : ")

print(":: break1 ::")

# 2. 입력 받은 단어 만큼 반복함 word 일 경우 4번 i에는 w o r d 순차적으로 하나씩 저장됨
for i in word :
    
#   2-1 만약에 i에 저장된 값이 a e i o u가 있으면 break(반복문을 멈춘다.)
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        break   
#   2-2 아니면 출력 줄바꿈없이
    else:
        print(i, end='')    # 결과 예상 : pr    위에 if문에서 i가 a e i o u 일때 반복을 중단하므로 pr 다음 o 때문에 반복문이 중단됨
        
print()

print(":: break2 ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :
        break   # 반복을 중단한다. 즉 반복을 빠져 나간다.
    else:
        print(i, end='')
        
print()

print(":: continue ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :
        continue    # 반복의 시작으로 돌아감, 아래 문장은 만날 수 없다.
    print(i, end='')  # 예상 결과 : prgrmmng