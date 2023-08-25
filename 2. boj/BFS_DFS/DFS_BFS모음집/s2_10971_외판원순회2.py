""""""
"""

"""

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    isVisited = [False] * n

    dq = deque()
    dq.append(i)
    while dq:
        x = dq.popleft()
        for k in range(n):
            