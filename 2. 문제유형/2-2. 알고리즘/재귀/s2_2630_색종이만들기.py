""""""
"""
    ** 분할정복
    
"""

# import sys
# sys.setrecursionlimit(10**6)

# # n = int(sys.stdin.readline().rstrip())
# n = 8
# paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# white_0 = 0
# blue_1 = 0
# def recur(row,column,k):
#     global white_0, blue_1
#     # 1. 문제에 대한 정의
#     ele = paper[row][column]
#     for r in range(k):
#         for c in range(k):
#             if paper[r][c] != ele:
#                 recur(row,column,n//2)
#                 recur(row,column+n//2,n//2)
#                 recur(row+n//2,column,n//2)
#                 recur(row+n//2,column+n//2,n//2)
#                 return
#     # 2. 종료 조건
#     if ele == 0: white_0 += 1
#     else: blue_1 += 1

# recur(0,0,n)

# print(white_0)
# print(blue_1)

import sys
input = sys.stdin.readline

n = int(input())
papers = []

for _ in range(n):
    row = list(map(int,input().rsplit()))
    papers.append(row)

blue_cnt, white_cnt = 0, 0

def check(row,col,n):
    global blue_cnt, white_cnt

    curr = papers[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if curr != papers[i][j]:
                next_n = n // 2
                check(row, col, next_n)
                check(row, col + next_n, next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                return
    if curr == 0:
        white_cnt += 1
    else:
        blue_cnt += 1
    return

check(0,0,n)
print(white_cnt)
print(blue_cnt)