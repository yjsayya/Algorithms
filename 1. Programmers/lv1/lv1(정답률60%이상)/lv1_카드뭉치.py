"""
    문자열 문제 - 이 정도는 가볍게 풀 수 있어야지 ㅇㅋ
"""
def solution(cards1, cards2, goal):

    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.pop(0)
            goal.pop(0)
        elif cards2 and cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
        else:
            return "No"

    return "Yes"


# 나중에 다시 푼 문제 -- 이 정도 깔끔하게 해줘야함
from collections import deque
def solution2(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.popleft()
        elif cards2 and word == cards2[0]:
            cards2.popleft()
        else:
            return "No"
    return "Yes"