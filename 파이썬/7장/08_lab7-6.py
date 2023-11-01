'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : Lab 7-6  도시의 이름과 인구를 튜플로 묶어보자.
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울',9765), ('부산',3441),('인천',2954),('광주',1501),('대전',1531)]

# 최대 인구 비교 할때 쓸 변수
max_population = 0

# 최소 인구 비교 할때 쓸 변수
min_population = 99999999999999999

# 토탈 평균인구 구할때 쓸 변수
total_population = 0

# 최대 인구수를 가진 지역(튜플)을 저장할 변수
max_city = None

# 최소 인구수를 가진 지역(튜플)을 저장할 변수
min_city = None

# city_info 만큼 반복
for city in city_info:
    
    # city에 저장된 값을 total_population에 저장하는데 인구 수 만 저장함
    total_population += city[1]
    
    # city[1]이 인구수인데 그 인구수랑 max_population 즉 현 최대인구랑 비교 했을때
    if city[1] > max_population:
        
        # city[1] 이 최대 인구보다 크면 max_population에 city[1] 값을 저장
        max_population = city[1]
        
        # max_city에 city 값을 저장한다.
        max_city = city
    
    # city[1]이 인구수인데 그 인구수랑 min_population 즉 현 최소인구랑 비교 했을때
    if city[1] < min_population:
        
        # city[1] 이 최소 인구보다 크면 min_population에 city[1] 값을 저장
        min_population = city[1]
        
        # min_city에 city 값을 저장한다.
        min_city = city

# 최대 인구수와 지역을 저장한 튜플을 출력함      
print("최대인구: {}, 인구: {} 천명".format(max_city[0], max_city[1]))

# 최소 인구수와 지역을 저장한 튜플을 출력함      
print("최소인구: {}, 인구: {} 천명".format(min_city[0], min_city[1]))

# 인구수의 토탈을 city_info(지역 수) 만큼 나눔
print("리스트 도시 평균 인구: {} 천명".format(total_population / len(city_info)))