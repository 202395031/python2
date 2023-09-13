'''
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학과 202395031 천승용
    설명 : 90페이지 문제 3.9
            평균 시속과 이동시간을 입력받아
            이동시간은 시,분,초 단위로 출력하고,
            이동한 거리를 계산하여 출력하시오.
'''

km_h = float(input("평균 시속(km/h)을 입력하세요 : "))
hour_input = float(input("이동 시간(h)을 입력하세요 : "))
distance_traveled = km_h * hour_input
time = hour_input * 3600
hour = time // 3600
minute = time % 3600 / 60
second = time % 60
print("평균 시속 : {}".format(km_h))
print("이동 시간 : {:.0f} 시간 {:.0f} 분 {:.0f} 초".format(hour, minute, second))
print("이동 거리 : {} km".format(distance_traveled))
