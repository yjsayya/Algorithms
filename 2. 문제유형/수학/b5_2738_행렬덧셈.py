""""""
"""

"""
import sys

n,m = map(int,sys.stdin.readline().split())
v1 = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
v2 = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

v3 = []
for i in range(n):
    li = []
    for j in range(m):
        li.append(v1[i][j] + v2[i][j])
    v3.append(li)

for row in v3:
    for idx in range(len(row)):
        if idx == len(row)-1:
            print(row[idx])
        else:
            print(row[idx], end=" ")
