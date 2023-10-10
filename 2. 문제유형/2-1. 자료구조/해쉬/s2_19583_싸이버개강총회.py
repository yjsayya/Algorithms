""""""
"""
    문제 오류가 있는 듯 하다
    -- 입력 길이가 주어지지 않았는데 
    -- 그래서 1번 예시를 끝낼 수가 없게 되어있다
    -- 다행히 일단 테스트케이스에서는 그런 경우가 없는지 문제 없이 정답을 맞출 수는 있었다 
"""

import sys

def changeTime(time):
    """ 시간을 초단위로 분해"""
    hour, minu = time.split(":")
    return int(hour) * 3600 + int(minu) * 60

# 1. 시간 구하기
s,e,q = sys.stdin.readline().split()
start_time = changeTime(s)
end_time = changeTime(e)
quit_time = changeTime(q)

dic = {
    1 : set(),
    2 : set()
}
while True:
    line = sys.stdin.readline()
    if not line:  # 입력이 없으면 break
        break

    time, name = line.split()
    time = changeTime(time)

    if quit_time < time:
        break

    if time <= start_time:
        dic[1].add(name)
    elif end_time <= time <= quit_time:
        dic[2].add(name)

print(len(dic[2].intersection(dic[1])))