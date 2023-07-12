"""
날짜, 알파벳 같은 것 처럼 개수가 몇개 없는 것은 아싸리 이렇게 만들어놓고
하는것이 더 이득인 듯 하다
"""

def solution(a, b):
    month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
        6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }
    # 1. 전체 일 수 구하기
    totDay = b
    for i in range(1, a):
        totDay += month[i]
    # 2. 요일 구하기
    if totDay % 7 == 1:
        return "FRI"
    elif totDay % 7 == 2:
        return "SAT"
    elif totDay % 7 == 3:
        return "SUN"
    elif totDay % 7 == 4:
        return "MON"
    elif totDay % 7 == 5:
        return "TUE"
    elif totDay % 7 == 6:
        return "WED"
    else:
        return "THU"