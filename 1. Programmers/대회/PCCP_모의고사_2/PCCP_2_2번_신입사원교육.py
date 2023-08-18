""""""
"""
    heapq를 이용해서 푸는 문제라는 것을 알아차리는게 중요한 문제였다 
    -- 깔끔하게 잘 풀었다
    -- python에서 heapq 사용법 다시 한번 쳌해두자
"""
import heapq

# 첫번째 풀이
def solution(ability, number):
    heapq.heapify(ability)

    for _ in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)

        heapq.heappush(ability, a+b)
        heapq.heappush(ability, a+b)

    return sum(ability)
