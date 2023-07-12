"""
    문자열 문제 - 이 정도는 가볍게 풀 수 있어야지 ㅇㅋ
"""

def solution(cards1, cards2, goal):

    while len(goal) != 0:
        if len(cards1) != 0 and cards1[0] == goal[0]:
            cards1.pop(0)
            goal.pop(0)
        elif len(cards2) != 0 and cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
        else:
            return "No"

    return "Yes"