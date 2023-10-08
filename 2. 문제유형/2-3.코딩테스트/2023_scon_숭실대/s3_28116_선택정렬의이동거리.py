""""""
"""
    << 구현 >>
    알고리즘 자체는 어렵지 않지만 -- 구현이 어렵네
"""

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

# 1. 정답 dict 만들기
ans = dict()
for ele in a:
    if ele not in ans:
        ans[ele] = 0

# 2. 순환 돌리기
standard_idx = 0
standard_mini = min(a)
while standard_idx < n:
    idx = a.index(standard_mini)

    if idx != standard_idx:
        a[standard_idx],a[idx] = standard_mini,a[standard_idx]
        ans[standard_mini] += idx
        ans[a[idx]] += idx

    standard_idx += 1
    standard_mini

# 3. 출력하기
for i in sorted(ans.keys()):
    print(ans[i], end=" ")