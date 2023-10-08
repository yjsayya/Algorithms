
'''

'''

import sys

# 1. 입력 받기
n,m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))


# 2. 개수 확인
cnt1 = 0
cnt2 = 0
# 2-1. '-' 개수 확인
for i in range(n):
    pre = "/"
    for j in range(m):
        forward = '/'
        if board[i][j] == '|':
            if forward == '-':
                cnt1 += 1
        forward = board[i][j]

        # if board[i][j] == '-':
        #     if board[i][j] != pre:
        #         cnt1 += 1
        #     pre = board[i][j]

print(cnt1)

# 2-2. 알고리즘. '|' 개수 확인
for j in range(m):
    pre = '/'
    for i in range(n):
        if board[i][j] == '|':
            if board[i][j] != pre:
                cnt2 += 1
            pre = board[i][j] 

print(cnt2)


# 9개
# 10