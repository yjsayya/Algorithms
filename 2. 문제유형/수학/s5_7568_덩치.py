""""""
"""

"""

import sys

n = int(sys.stdin.readline())

size = []
for _ in range(n):
    tu = tuple(map(int,sys.stdin.readline().split()))
    size.append(tu)


ans = [0] * n
for idx in range(n):
    cnt = 0
    for i,j in size:
        weight, height = size[idx]
        if weight < i and height < j:
            cnt += 1
    ans[idx] = cnt + 1

for i in ans:
    print(i, end=" ")