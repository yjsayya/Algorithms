""""""
"""
    kakao 코딩테스트 문제
    - 전반적으로 매우 귀찮지만 어렵지는 않은 문제가 나오는 듯 하다
"""

import math
def solution(fees, records):
    # 1. 차량 별 입/출차 기록 정리
    dic = dict()
    for record in records: # [시각, 차량번호, In/OUT]
        time, car, in_out = record.split(" ")
        if car in dic:
            dic[car].append(time)
        else:
            dic[car] = [time]

    # 2. 차량 별 주차 시간 및 요금 계산
    car_totalfee = dict()
    for car in dic:
        time_li = dic[car]
        length = len(time_li)
        # 출차 기록 없으면 넣어주고
        if len(time_li) % 2 != 0:
            time_li.append('23:59')
        # 2-1. 주차 시간 계산
        total_time = 0
        for i in range(1, length + 1, 2):
            a, b = time_li[i-1].split(":")
            c, d = time_li[i].split(":")

            total_time += (int(c) * 60 + int(d)) - (int(a) * 60 + int(b))
        # 2-2. 알고리즘. 요금 계산
        if total_time <= fees[0]:
            car_totalfee[car] = fees[1]
        else:
            car_totalfee[car] = math.ceil((total_time - fees[0]) / fees[2]) * fees[3] + fees[1]
    # 3. return 값 정리
    ans = []
    car_list = sorted(dic.keys())  # 차량 번호 - 내림차순
    for i in car_list:
        ans.append(car_totalfee[i])

    return ans