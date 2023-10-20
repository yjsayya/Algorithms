""""""
"""
    1. 그리디로 푸는 문제가 아니었다 
        -- greedy로 풀었더니 틀렸다 
    2. BFS로 풀어야 될 거 같기도 하고 
"""


# 1. 첫번재 풀이 - Greedy 풀이
def solution1(storey):
    num = str(storey)
    ans = 0
    change = 0
    for i in range(len(num) - 1, -1, -1):
        a = int(num[i]) + change
        if a <= 5:
            ans += a
            change = 0
        else:
            ans += (10 - a)
            change = 1

    return ans

def solution2():
    pass