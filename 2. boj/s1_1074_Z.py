''''''
"""
    ** 아이디어
    - Z 모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출한다
"""


def solve(n,x,y): # n - 전체공간의 크기 / x,y - 좌표
    global result

    # 1. 종료조건
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    # 2. 문제에 대한 정의
    solve(n/2,x,y)
    solve(n/2,x,y+n/2)
    solve(n/2,x+n,y)
    solve(n/2,x+n,y+n/2)

import sys

result = 0
n,X,Y = map(int,sys.stdin.readline().rstrip().split())
solve(2**n,0,0)


