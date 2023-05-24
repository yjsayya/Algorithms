from heapq import *

li = []
answer = 0

n = int(input())
for i in range(n):
    heappush(li, int(input()))

while len(li) != 1:
    a = heappop(li)
    b = heappop(li)
    answer += a+b
    heappush(li, a+b)

print(answer)