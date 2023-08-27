""""""
"""
    이런건 bfs로 푸는 문제이다 ㅇㅇ 
    가는 최솟값을 구해야하니깐 ㅇㅋ
    
    
    ** 첫번째 풀이 - 다 풀었는데 뭔가 하나 놓친게 있는 듯 하나 알아내지 못했다
    두번째 풀이 처럼 처음에 1을 넣고 마지막에 1을 빼서 제출해야하는데 
    나중에 다시 풀어보면서 다시 원인을 찾아보도록 하자 
"""

# 1. 첫번째 풀이
from collections import deque

f,g,s,u,d = map(int,input().split())

stairs = [0] * (f+1)
dq = deque()
dq.append(g)
while dq:
    now = dq.popleft()
    if now == s:
        break
    for i in (u,-d):
        next = now + i
        if 1 <= next <= f and stairs[next] == 0:
            dq.append(next)
            stairs[next] = stairs[now] + 1

if stairs[s] == 0:
    print("use the stairs")
else:
    print(stairs[s])


# 두번째 풀이
from collections import deque

f,g,s,u,d = map(int,input().split())

stairs = [0] * (f+1)
dq = deque()
dq.append(g)
stairs[g] = 1
while dq:
    now = dq.popleft()
    if now == s:
        break
    for i in (u,-d):
        next = now + i
        if 1 <= next <= f and stairs[next] == 0:
            dq.append(next)
            stairs[next] = stairs[now] + 1

if stairs[s] == 0:
    print("use the stairs")
else:
    print(stairs[s]-1)