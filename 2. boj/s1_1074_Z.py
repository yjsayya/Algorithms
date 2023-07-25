''''''
"""
    ** 아이디어
    - Z 모양을 구성하는 4가지 방향에 대하여 차례대로 재귀적으로 호출한다
    
"""
import sys

def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return

    solve(n / 2, x, y)
    solve(n / 2, x, y + n / 2)
    solve(n / 2, x + n / 2, y)
    solve(n / 2, x + n / 2, y + n / 2)

N,X,Y = map(int,sys.stdin.readline().split())
result = 0

solve(2**N,0,0)

# 1. 일단, n을 잘 보고

#2. 그 다음 4로 나누어 가면서 확인하면 될 것 같은데?


