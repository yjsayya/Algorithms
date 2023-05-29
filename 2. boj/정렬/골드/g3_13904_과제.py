'''
'''

import sys

n = int(input())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in sorted(li, key= lambda x : (x[0], -x[1])):
    pass



# [[1, 20], [2, 50], [3, 30], [4, 60], [4, 40], [4, 10], [6, 5]]

# 20 + 50 + 30 + 60 + 5
# 50 + 30 + 60 + 40 + 5