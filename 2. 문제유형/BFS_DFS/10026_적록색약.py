import sys

sys.setrecursionlimit(10**6)
n = int(input())

matrix = [list(sys.stdin.readline()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

a = 0

def dfs(x,y):
    visited[x][y] = True
    color = matrix[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == False:
                global a
                a += 1
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)

print(a)