""""""
"""
    어렵네 ...
    
    답을 결국 봤다
    진짜 쉽지 않은 듯 하다 
    
"""

import sys
from collections import deque

d = [[-1,0],[1,0],[0,1],[0,-1]]

def bfs(y,x):
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True

    while queue:
        r,c = queue.popleft()
        for i in range(4):
            dr = r + d[i][0]
            dc = c + d[i][1]

            if (0<=dr<n) and (0<=dc<m):
                if iceberg[dr][dc] == 0:
                    visited[r][c] += 1

                if not visited[dr][dc] and iceberg[dr][dc] != 0 :
                    queue.append([dr,dc])
                    visited[dr][dc] = True

n,m = map(int,sys.stdin.readline().split())
iceberg = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

time = 0
while True:
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    for row in range(n):
        for column in range(m):
            if not visited[row][column] and iceberg[row][column] != 0:
                bfs(row,column)
                cnt += 1

    for row in range(n):
        for column in range(m):
            if visited[row][column]:
                iceberg[row][column] -= (visited[row][column]-1)
                if iceberg[row][column] < 0:
                    iceberg[row][column] = 0

    time += 1
    if cnt == 0:
        print(0)
        exit()
    if cnt >= 2:
        break

print(time-1)
