""""""
"""
    dfs,bfs 추천문제 (6)
    
    ** 이중 배열에서 최댓값 구하기 : 최댓값 = max(map(max,이중배열)))
    이건 꼭 알아두자 ㅋㅋㅋ 
"""

import sys
sys.setrecursionlimit(100_000)

def sink_dfs(x,y,h):
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if (0 <= nx < n) and (0 <= ny < n) and not isSink_table[nx][ny] and graph[nx][ny] > h:
            isSink_table[nx][ny] = True
            sink_dfs(nx,ny,h)

n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 1
for k in range(max(map(max,graph))):
    isSink_table = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not isSink_table[i][j]:
                cnt += 1
                isSink_table[i][j] = True
                sink_dfs(i,j,k)
    ans = max(ans,cnt)

print(ans)