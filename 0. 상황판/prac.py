
import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline().rstrip())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

white_0 = 0
blue_1 = 0

def recur(row, column, n):
    global white_0, blue_1

    ele = paper[row][column]
    for r in range(row,row+n):
        for c in range(column, column+n):
            if ele != paper[r][c]:
                for i in range(2):
                    for j in range(2):
                        recur(row+i*n//2, column+j*n//2, n//2)
                return

    if ele == 0:
        white_0 += 1
    else:
        blue_1 += 1
    return

recur(0,0,n)

print(white_0)
print(blue_1)
