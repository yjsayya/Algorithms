


import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = [0,0,0]
def recur(row,column,n):
    global ans

    ele = paper[row][column]
    for r in range(row, row+n):
        for c in range(column, column+n):
            if ele != paper[r][c]:
                for i in range(3):
                    for j in range(3):
                        recur(row+i*n//3, column+j*n//3, n//3)
                return
    # 1. 종료 조건
    if ele == -1:
        ans[0] += 1
    elif ele == 0:
        ans[1] += 1
    else:
        ans[2] += 1

    return

recur(0,0,n)

for _ in ans:
    print(_)