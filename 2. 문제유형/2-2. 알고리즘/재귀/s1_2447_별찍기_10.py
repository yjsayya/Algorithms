

import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline().rstrip())

def recur(length):
    # 1. 종료 조건
    if length == 1:
        return ["*"]

    stars = recur(length // 3)
    l = []

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s + ' '*(length//3)+s)
    for s in stars:
        l.append(s*3)
    return l

print('\n'.join(recur(n)))