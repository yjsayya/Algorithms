import sys
n = int(input())

dic = dict()

for i in range(n):
    a, b = sys.stdin.readline().split()
    dic[a] = int(b)

for k in sorted(dic.keys(), key= lambda x : dic[x]):
    print(k, end=" ")

