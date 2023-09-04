""""""
"""
    2차원은 ez하게 해결
    
"""

import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dq = deque()
for x in range(n):
    for y,ele in enumerate(tomato[x]):
        if ele == 1:
            dq.append((x,y)) # 행렬

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while dq:
    x,y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
            dq.append((nx,ny))
            tomato[nx][ny] = tomato[x][y] + 1

ans = max(map(max,tomato)) -1
for i in tomato:
    for j in i:
        if j == 0:
            ans = -1

print(ans)