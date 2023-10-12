""""""
"""
    그냥 재귀로 들어가는 것도 아니고 
    -- 지수법칙으로 어느 정도 풀어서 재귀를 적용해야하는 것 같다
"""

# 1. 재귀로 안 푸니깐 시간 초과 났음
import sys
a,b,c = map(int,sys.stdin.readline().split())
print(pow(a,b) % c)


# 2. 재귀로 풀어보자
# import sys
# sys.setrecursionlimit(10**6)
# a,b,c = map(int,sys.stdin.readline().split())
#
# res = 1
# def dfs(time):
#     global res
#     if time == b:
#         return
#     res *= a
#     dfs(time+1)
#
# print(res % c)



# 다른 사람 풀이 --
import sys

a, b, c = map(int, sys.stdin.readline().split())
def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c


print(multi(a, b))
