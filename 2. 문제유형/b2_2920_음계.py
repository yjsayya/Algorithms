"""
    구현 문제
"""

import sys

numList = list(map(int,sys.stdin.readline().split()))
ans = ""

for i in range(1,len(numList)):
    if numList[i] - numList[i-1] == 1:
        ans = "ascending"
    elif numList[i] - numList[i-1] == -1:
        ans = "descending"
    else:
        ans = "mixed"
        break

print(ans)
