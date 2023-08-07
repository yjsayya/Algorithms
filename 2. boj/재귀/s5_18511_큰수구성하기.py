''''''
"""
    [제한사항]
    - (10 ≤ N ≤ 100_000_000)
    - (1 ≤ K의 원소의 개수 ≤ 3)
"""

import sys

n,k = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))

li.sort()


# for i in str(map):
#