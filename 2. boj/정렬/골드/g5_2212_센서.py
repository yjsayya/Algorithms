
'''
    제한사항
    - (1 <= n <= 10_000)
    - (1 <= k <= 1_000)
'''

import sys

n = int(input())
k = int(input())
li = list(map(int, sys.stdin.readline().split()))

li.sort()

print(li)

# [1,3,6,6,7,9]

# [3, 6, 7, 8, 10, 12, 14, 15, 18, 20]
