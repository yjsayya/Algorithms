'''

'''


import sys
from collections import Counter

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

answer = []

dic = Counter(card)
for j in check:
    if j in dic:
        answer.append(dic[j])
    else:
        answer.append(0)

for k in answer:
    print(k, end=" ")