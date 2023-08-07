''''''
"""
    ** 아이디어
    - Z 모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출한다
"""

import sys

n,r,c = map(int,sys.stdin.readline().split())
cnt = 0

def solve(x,y,n): # (x,y) --> (r,c)에 도착했을 때;
    global cnt
    # 1. 종료 조건
    if x == r and y == c:
        print(cnt)
        exit(0)
    if n == 1:
        cnt += 1
        return
    if not (x <= r < x+n and y <= c < y+n):
        cnt += n*n
        return
    # 2. 문제에 대한 정의
    temp = n // 2
    solve(x,y,temp)
    solve(x,y+temp,temp)
    solve(x+temp,y,temp)
    solve(x+temp,y+temp,temp)

solve(0,0,2**n)
print(cnt)
