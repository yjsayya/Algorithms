# lv0수준의 문제

import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(1, len(li)):
    if li[i-1] > li[i]:
        answer += 1

print(n - answer)