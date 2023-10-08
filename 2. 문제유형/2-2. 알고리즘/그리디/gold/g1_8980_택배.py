""""""
"""

"""

import sys

n,c = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

dic = dict()
for _ in range(m):
    frm,to,boxex = map(int,sys.stdin.readline().split())
    if frm in dic:
        dic[frm].append((to,boxex))
    else:
        dic[frm] = [(to,boxex)]

town = [0] * (n+1)
weight = 0
idx = 1
for num_box in sorted(dic.values(),key= lambda x : x[0]):
    # 1. 물건 하역
    if idx != 1:
        weight -= town[idx]
    # 2. 물건 적재
    for num in num_box:
        if c > weight + num[1]:
            town[num[0]] += num[1]
            weight += num[1]
        else:
            town[num[0]] += (c - weight)
            weight = c
    idx += 1

print(sum(town))