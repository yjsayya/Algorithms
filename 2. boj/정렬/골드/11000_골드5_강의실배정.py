
'''

'''

import sys, heapq

# 1. 입력 받기
n = int(input())
li = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 2. 정렬해줌
li.sort()

# 3. 
lecture_queue = []
heapq.heappush(lecture_queue, li[0][1])

for i in range(1, n):
    if li[i][0] < lecture_queue[0]:
        heapq.heappush(lecture_queue, li[i][1])
    else:
        heapq.heappop(lecture_queue)
        heapq.heappush(lecture_queue, li[i][1])

print(len(lecture_queue))