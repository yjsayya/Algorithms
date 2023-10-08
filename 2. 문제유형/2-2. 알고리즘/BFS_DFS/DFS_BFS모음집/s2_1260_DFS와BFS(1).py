''''''
"""
    결국 배치를 어떻게 할 것이냐의 문제 
"""

import sys
from collections import deque

def dfs(v,isVisited):
    isVisited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not isVisited[i]:
            dfs(i,isVisited)

def bfs(v,isVisited):
    dq = deque()
    dq.append(v)
    isVisited[v] = True
    while dq:
        x = dq.popleft()
        print(x,end= ' ')
        for i in graph[x]:
            if not isVisited[i]:
                dq.append(i)
                isVisited[i] = True


n,m,v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

isVisited1 = [False] * (n+1)
isVisited2 = [False] * (n+1)

dfs(v, isVisited1)
print()
bfs(v, isVisited2)

