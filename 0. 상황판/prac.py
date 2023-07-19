

import sys

aN = int(input())
A = list(map(int, sys.stdin.readline().split()))

bN = int(input())
B = list(map(int, sys.stdin.readline().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)
