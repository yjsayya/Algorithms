""""""
"""
    1. 첫번째 풀이 --> 효율성 테스트에서 시간초과
"""

# 1. 첫번째 풀이
from collections import deque
def solution1(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    ans = []

    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        row, column, time = dq.popleft()

        if row == n - 1 and column == m - 1:
            ans.append(time)
            continue

        visited[row][column] = True
        for _ in range(4):
            nr = row + dr[_]
            nc = column + dc[_]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1 and not visited[nr][nc]:
                    dq.append((nr, nc, time + 1))

    return min(ans) if ans else -1



print(solution1([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


# def solution2(maps):
