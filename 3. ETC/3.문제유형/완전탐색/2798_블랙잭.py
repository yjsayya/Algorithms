"""
    ** 배열, 완전탐색 문제

    combinations 라이브러리 사용하면 쉽다
    - 제한사항이 그렇게 높지 않았기 때문에 combinations로 돌려버렸다
    - n <= 100
    100C3 = 161,700 경우의 수 얼마 안된다
"""

import sys
from itertools import combinations as comb

n,m = map(int,sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
ans = []
for i in comb(cards,3):
    if sum(i) <= m:
        ans.append(sum(i))

print(max(ans))

