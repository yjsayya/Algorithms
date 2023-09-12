""""""
"""

"""

import sys
def dfs(x,isVisited):
    isVisited[x] = True
    for j in graph[x]:
        if j in graph and not isVisited[j]:
            dfs(j,isVisited)

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = dict()
for _ in range(m):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    if u in graph: graph[u].append(v)
    else: graph[u] = [v]
    if v in graph: graph[v].append(u)
    else: graph[v] = [u]

isVisited = [False] * (n+1)

cnt = 0
for i in graph:
    if i in graph and not isVisited[i]:
        dfs(i,isVisited)
        cnt += 1

print(cnt)