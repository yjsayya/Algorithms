""""""
"""

"""
import sys
from collections import deque
# 0. 입력 받기
k = int(sys.stdin.readline())
w,h = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(w)]

visited = [[False] * w for _ in range(h)]
kx = [-2,-1,1,2,-2,-1,1,2]
ky = [1,2,2,1,-1,-2,-2,-1]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

dq = deque()
dq.append((0,0))
while dq:
    x,y = dq.popleft()
    if k > 0:
        for i in range(8):
            kx = x + kx[i]
            ky = y + ky[i]
            if 0 <= kx < w and 0 <= ky < h and graph[kx][ky] != 1:
                k -= 1
                dq.append()

    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and graph[nx][ny] != 1:
                dq.append((nx,ny))
                visited[nx][ny] = True

