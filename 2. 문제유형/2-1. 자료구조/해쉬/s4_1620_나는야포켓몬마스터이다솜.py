""""""
"""

"""

import sys

n,m = map(int,sys.stdin.readline().split())
dic = dict()
li = list()

idx = 1
for _ in range(n):
    monster = sys.stdin.readline().rstrip()
    dic[monster] = idx
    idx += 1
    li.append(monster)

for _ in range(m):
    problem = sys.stdin.readline().rstrip()
    if problem.isdigit():
        print(li[int(problem)-1])
    else:
        print(dic[problem])