""""""
"""

"""

import sys

n,m = map(int,sys.stdin.readline().split())

dic = dict()
for _ in range(n):
    site, pw = sys.stdin.readline().split()
    dic[site] = pw

for _ in range(m):
    print(dic[sys.stdin.readline().strip()])