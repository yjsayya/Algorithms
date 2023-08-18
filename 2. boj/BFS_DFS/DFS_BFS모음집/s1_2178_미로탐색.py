""""""
"""
    bfs는 기본적으로 queue를 많이 사용을 하니깐
    queue에 어떤 것을 언제 넣고 언제 뺄 것인가? 
    
    - 해당 조건이 될때 넣고
    - 뺀 다음 진행 시키는 것 
"""

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    tmp = list(map(int,list(sys.stdin.readline().rstrip())))
    graph.append(tmp)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
dq = deque()

def bfs(x,y):
    dq.append((x,y))
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                dq.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

bfs(0,0)
print(graph[n-1][m-1])
