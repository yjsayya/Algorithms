import sys

n, m = map(int, input().split())
num = [[]] * n

print(num)

for i in range(n):
    num[i] = list(map(int, sys.stdin.readline().split()))


