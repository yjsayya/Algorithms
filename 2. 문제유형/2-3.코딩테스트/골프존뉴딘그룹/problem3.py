""""""
"""
    python - heapq를 이용해서 푸는 문제
    예전 - 강의실 예약 문제 풀어봐서 참고해서 풀어냈다 
    개인적으로 이게 3번으로 나온 것이 신의 한수였다
    올해 네이버 상반기에서도 비슷한 문제 나왔던 것 같은데 
    여러번의 코딩테스트 경험이 도움이된 듯 하다 
"""

from heapq import heappop, heappush

def solution(N, simulation_data):
    ans = 0

    left = 0
    heap = []
    for s, e in simulation_data:
        if not heap:
            heappush(heap, e + s)
            left += 1
            continue

        time = heap[0]
        if time <= s:
            heappop(heap)
            heappush(heap, s + e)
        else:
            if left < N:
                heappush(heap, s + e)
                left += 1
            else:
                ans += time - s
                heappop(heap)
                heappush(heap, time + e)

    return ans