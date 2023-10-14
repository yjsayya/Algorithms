
import sys

n,r,c = map(int,sys.stdin.readline().split())


def recur(row,column,n):
    # 1. 종료 조건
    if row == r and column == c:
        return
    # 2. 문제에 대한 정의
    for i in range(n):
        for j in range(n):
            if