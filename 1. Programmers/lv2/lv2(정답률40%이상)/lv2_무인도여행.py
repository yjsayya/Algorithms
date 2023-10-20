
import sys
sys.setrecursionlimit(10**5)
def dfs(row ,column ,cnt ,dr ,dc ,r ,c ,maps ,visited):
    # 1. 종료 조건
    if visited[row][column]:
        return 0
    # 2. 문제에 대한 정의
    visited[row][column] = True
    for _ in range(4):
        nr = row + dr[_]
        nc = column + dc[_]
        if 0 <= nr < r and 0 <= nc < c:
            if maps[nr][nc] != 'X':
                cnt += dfs(nr ,nc ,int(maps[nr][nc]) ,dr ,dc ,r ,c ,maps ,visited)
    return cnt

def solution(maps):
    r ,c = len(maps) ,len(maps[0])
    visited = [[False ] *c for _ in range(r)]

    dr = [1 ,-1 ,0 ,0]
    dc = [0 ,0 ,1 ,-1]
    ans = []
    for row in range(r):
        for column in range(c):
            if maps[row][column] != 'X' and not visited[row][column]:
                ans.append(dfs(row ,column ,int(maps[row][column]) ,dr ,dc ,r ,c ,maps ,visited))

    return sorted(ans) if ans else [-1]