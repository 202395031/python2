'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 8.1 키와 값을 가지는 딕셔너리

    튜플 : () 리스트 : [] 딕셔너리 : {}
'''
# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리에 값 저장. 1번 방법 key, value 를 쌍으로 저장함 key를 기준으로 value 저장
# [key] = value
phone_book1['천승용'] = '010-7640-2671'

print("phone_book1 :",phone_book1) # 출력 결과 : {'천승용': '010-7640-2671'}

# 딕셔너리에 값 저장. 2번 방법 {key : value}
phone_book2 = {"김경현" : "010-9932-8517", "천승용" : "010-7640-2671"}
print("phone_book2 :",phone_book2)

phone_book3 = {}

phone_book3['천승용'] = '010-7640-2671'
phone_book3['김경현'] = '010-9932-8517'
phone_book3['홍길동'] = '010-1234-5678'
phone_book3['이순신'] = '010-1234-5679'
phone_book3['삼순신'] = '010-1234-5670'

print("phone_book3 :",phone_book3)

print()
print(":: 전화번호 phone_book3 ::")
# 모든 key값 출력
print(phone_book3.keys())
# 모든 value값 출력
print(phone_book3.values())
# 모든 key, value 출력
print(phone_book3.items()) # items 는 값을 튜플 형식으로 바꿔서 출력함

print()

print(":: 전화번호 phone_book3 items() 츨력::")
for name, phone_num in phone_book3.items():
    print(name, ":", phone_num)
    
print()

print(":: 전화번호 phone_book3[keys]로 접근하여 츨력::")
for key in phone_book3.keys():
    print(key,":", phone_book3[key]) # 변수 key에 대한 value 값이 출력됨
    
print()

print("딕셔너리 작성 시 :(콜론) 을 기준으로 key:value로 작성")
person_dict = {'name' : '천승용', 'age' : 20, 'class' : '1학년'}

print('name :', person_dict['name'])    # 딕셔너리의 'name' 키로 값을 조회하여 출력 
print('age :', person_dict['age'])  # 딕셔너리의 'age' 키로 값을 조회하여 출력 

print()

print(":: 정렬 ::")
# phone_book3를 정렬
# 딕셔너리를 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))

print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0]) # lambda는 먼가 가벼운 함수 느낌 레또르트 음식 같이 먼가가 먼가 하게 편하게 쓰는 근데 많으면 별로인 그런
print(sort_phone_book3)
print(":: 값를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1]) # lambda는 이름 없는 함수임 함수를 만들지 않고 함수화된 기능만을 불러 사용하고자 할때 씀
print(sort_phone_book3)

# lambda x,y(매개변수) : x + y (함수 몸체)

print()

print(":: 항목 삭제 ::")

del phone_book3['삼순신']
print(phone_book3)

print(":: 전체 삭제 ::")

phone_book3.clear()

print(phone_book3)