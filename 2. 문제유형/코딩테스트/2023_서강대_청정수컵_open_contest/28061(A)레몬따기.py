import sys

n = int(input())
li = list(map(int,sys.stdin.readline().split()))

cnt = []

for idx, ele in enumerate(li):
    cnt.append(ele - n + idx)

print(max(cnt))



'''
x=0 || x=1 --- x=n || x = n+1
'''