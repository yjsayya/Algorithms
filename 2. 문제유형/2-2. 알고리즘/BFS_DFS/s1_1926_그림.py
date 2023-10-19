""""""
"""
    dfs로 푸니깐 -- 메모리 초과가 나버렸다
"""
# import sys
# sys.setrecursionlimit(10**6)
#
# # row, column / y, x
# n,m = map(int,sys.stdin.readline().split())
# board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# visited = [[False]*m for _ in range(n)]
#
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
#
# a = 0
# def dfs(row,column,size):
#     global visited, a
#     # 1. 종료 조건
#     if visited[row][column]:
#         if size > a:
#             a = size
#         return
#     # 2. 문제에 대한 정의
#     visited[row][column] = True
#     for _ in range(4):
#         nr = row + dr[_]
#         nc = column + dc[_]
#         if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
#             dfs(nr,nc,size+1)
#     return
#
# cnt = 0
# for row in range(n):
#     for column in range(m):
#         if board[row][column] == 1 and not visited[row][column]:
#             cnt += 1
#             dfs(row,column,0)
#
# print(cnt)
# print(a)

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

cnt = 0
maxi = 0
for row in range(n):
    for column in range(m):
        if board[row][column] == 1 and not visited[row][column]:
            cnt += 1
            visited[row][column] = True
            dq = deque()

            dq.append((row,column,1))
            while dq:
                r,c,size = dq.popleft()
                for _ in range(4):
                    nr = r + dr[_]
                    nc = c + dc[_]
                    if 0 <= nr < n and 0 <= nc < m:
                        if not visited[nr][nc] and board[nr][nc] == 1:
                            visited[nr][nc] = True
                            if maxi < size+1:
                                maxi = size+1
                            dq.append((nr,nc,size+1))


print(cnt)
print(maxi)