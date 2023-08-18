

from collections import deque

def bfs(x,y):
    dq = deque()
    dq.append((x,y))

    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

