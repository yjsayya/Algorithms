""""""
"""
    이 정도는 쉽게 풀어야 되지 않나 싶다 
    -- 좌표 문제 이제 어렵지 않은 듯 
"""
def solution(dirs):
    udrl = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    se = set()
    x, y = 0, 0
    for key in dirs:
        dx = x + udrl[key][0]
        dy = y + udrl[key][1]
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            se.add((x, y, dx, dy))
            se.add((dx, dy, x, y))

            x = dx
            y = dy

    return len(se) // 2