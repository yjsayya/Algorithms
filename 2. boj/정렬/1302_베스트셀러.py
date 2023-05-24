
from collections import Counter

n = int(input())
dic = dict()

for _ in range(n):
    i = input()
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

a = sorted(dic.values()).count(max(dic.values()))

print(sorted(dic, key= lambda x : dic[x], reverse=True)[a-1])
