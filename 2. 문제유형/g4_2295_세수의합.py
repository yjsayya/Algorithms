

import sys

n = int(sys.stdin.readline())
u = [int(sys.stdin.readline()) for _ in range(n)]
u.sort()

se = set()
for x in u:
    for y in u:
        se.add(x+y)

def check():
    global ans
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            if u[i] - u[j] in se:
                ans = u[i]
                return

ans = 0
check()
print(ans)