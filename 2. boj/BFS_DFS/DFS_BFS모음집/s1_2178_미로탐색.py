""""""
"""
    bfs로 푸는 문제였다 
    ** 결국 포인트는 언제 queue에 넣고 언제 뺄 것인가에 대한 조건을 잘 생각 해야한다 
"""

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

dq = deque()
dq.append((0,0))
while dq:
    x,y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            dq.append((nx,ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n-1][m-1])