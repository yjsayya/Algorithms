""""""
"""

"""

# import sys
# from collections import deque
#
# maxi = 100_000
# n,k = map(int,sys.stdin.readline().rstrip().split())
# dist = [0] * (maxi+1)
#
# dq = deque()
# dq.append(n)
# while dq:
#     x = dq.popleft()
#     if x == k:
#         print(dist[x])
#         break
#     for j in (x-1,x+1,x*2):
#         if 0 <= j <= maxi and not dist[j]:
#             dist[j] = dist[x] + 1
#             dq.append(j)















import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
dq = deque()

maxi = 100_000
table = [0] * maxi

dq.append(n)
while dq:
    x = dq.popleft()
    if x == k:
        print(table[x])
        break
    for j in (x+1,x-1,x*2):
        if 0 <= j <= maxi and not table[j]:
            dq.append(j)
            table[j] = table[x] + 1