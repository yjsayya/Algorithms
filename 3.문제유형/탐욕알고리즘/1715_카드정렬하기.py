# 난이도 : 골드 4
    # PriorityQueue 확인 --> 어렵지 않은 자료구조네
    # 그리디에 많이 나온다고 하니 꼭 확인할 걸

# 첫번째 푼 풀이
import sys
from queue import PriorityQueue

pq = PriorityQueue()
n = int(input())
count = 0
for _ in range(n):
    pq.put(int((sys.stdin.readline())))

while pq.qsize() > 1:
    a = pq.get()
    b = pq.get()
    count += (a+b)
    pq.put(a+b)

print(count)