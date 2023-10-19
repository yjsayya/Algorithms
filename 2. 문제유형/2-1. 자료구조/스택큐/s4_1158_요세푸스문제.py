""""""
"""
    마지막 출력 부분을 str로 처리하면 된다 
    deque의 rotate() 함수 개꿀 
"""

import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

dq = deque([i for i in range(1,n+1)])
ans = []
while dq:
    dq.rotate(-k+1)
    ans.append(str(dq.popleft()))

print("<" + ", ".join(ans) + ">")