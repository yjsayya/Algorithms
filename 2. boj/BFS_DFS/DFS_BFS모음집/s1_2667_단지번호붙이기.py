""""""
"""
    ** 항상 dfs인지 bfs인지 고민할 필요가 있다 
    -- 여기는 좌표 문제이다. 
"""

# 1. BFS로 풀어보기
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

print(graph)
def bfs(graph,a,b):
    length = len(graph)
    dq = deque()
    dq.append((a,b))

    graph[a][b] = 0
    count = 1

    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx,ny))
                count += 1

    return count

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph,i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])



