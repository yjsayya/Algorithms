""""""
"""

"""

import sys

n = int(sys.stdin.readline())

dic = dict()
for _ in range(n):
    name,in_or_out = sys.stdin.readline().split()
    dic[name] = in_or_out

li = []
for i in dic:
    if dic[i] == "enter":
        li.append(i)

for k in sorted(li, reverse=True):
    print(k)