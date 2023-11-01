'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''
# 리스트 생성
color_list = ['red', 'orange', 'yellow', 'green']

# 튜플 생성
color = ('red', 'orange', 'yellow', 'green', 'blue')

# 튜플 출력
print(f"color : {color}")

# color에 black 추가하기
# AttributeError: 'tuple' object has no attribute 'append'
# AttributeError: 'tuple' 개체에 'append' 속성이 없습니다.
# # 튜플은 안에 추가 하는 기능이 없음 수정, 고칠 수가 없음
# color.append("black") 

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print('color 튜플 :', color)
print('color 튜플 중 2,3,4번은?', color[1:4]) # 슬라이싱

# [a:b:c] a는 시작 위치 b는 끝나는 위치(b에 -1한 만큼) c는 증감식(ex: 2일경우 0 2 4 번으로 두칸 씩 넘기면서 출력됨)
print('color 튜플 중 1,2,3번은?', color[:3])
print('color 튜플 중 3,4,5번은?', color[2:])
print('color 튜플 중 1,3,5번은?', color[::2])
print('color 튜플 중 거꾸로 출력 :', color[::-1])   # 증감에 -1을 넣으면 거꾸로 출력됨

# 튜플 끼리의 결합 => + 연산자. 반복 => * 연산자.
colors = color + color
print("colors 튜플 :", colors)
print("color 튜플을 10번 반복 :", color * 10)