""""""
"""

"""

import sys

n,m = map(int,sys.stdin.readline().split())

# 1. group별 member별 정리
groups = dict()
members = dict()
for _ in range(n):
    group = sys.stdin.readline().strip()
    num = int(sys.stdin.readline().strip())

    groups[group] = []
    for _ in range(num):
        member = sys.stdin.readline().strip()
        groups[group].append(member)
        members[member] = group
# 2. 퀴즈 진행시켜
for _ in range(m):
    string = sys.stdin.readline().strip()
    intger = int(sys.stdin.readline().strip())

    if intger == 0:
        for i in sorted(groups[string]):
            print(i)
    else:
        print(members[string])