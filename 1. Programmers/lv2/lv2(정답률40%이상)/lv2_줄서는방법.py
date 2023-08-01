''''''
"""

"""

# 첫번째 풀이 - 완전탐색으로 풀었다 : 역시 시간초과
from itertools import permutations as perm
def solution(n, k):
    li = list(perm(range(1, n + 1), n))
    return li[k - 1]