"""
    이걸 내가 풀어낼 수 있을지 모르겠다 ...
"""

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def bombArea(row, column, board, k, n):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in directions:
        for i in range(1, k + 1):
            nx = row + dx * i
            ny = column + dy * i

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 2:
                    break
                elif board[nx][ny] == 0:
                    board[nx][ny] = -1

    return board

def solution(board, k, ax, ay, bx, by):
    n = len(board)
    visited = [[[[False] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for row in range(n):
        for column in range(n):
            board = bombArea(row,column,board,k,n)

    queue = deque()
    queue.append((ax, ay, bx, by, 0))
    while queue:
        ax_, ay_, bx_, by_, time = queue.popleft()
        # 1. 종료 조건
        if board[ax_][ay_] == 0 and board[by_][by_] == 0:
            return time
        # 2. 문제 진행
        visited[ax_][ay_][bx_][by_] = True
        # 2-1. A 움직이기
        for i in range(4):
            next_ax, next_ay = ax + dx[i], ay + dy[i]
            if not is_valid(next_ax,next_ay,n) or board[next_ax][next_ay] == 1 or board[next_ax][next_ay] == 2:
                continue
            # 2-2. B 움직이기
            for j in range(4):
                next_bx, next_by = bx + dx[j], by + dy[j]
                if not is_valid(next_bx, next_by, n) or board[next_bx][next_by] == 1 or board[next_bx][next_by] == 2 or (next_ax == next_bx and next_ay == next_by):
                    continue
                if visited[next_ax][next_ay][next_bx][next_by]:
                    continue
                queue.append((next_ax, next_ay, next_bx, next_by, time+1))

    return -1

n = 4
visited = [[[[False] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
print(visited)
print(visited[0][1][0][1])