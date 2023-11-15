import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().split())

graph = dict()
for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    if i in graph: graph[i].append(j)
    else: graph[i] = [j]
    if j in graph: graph[j].append(i)
    else: graph[j] = [i]

for ele in graph:
    graph[ele].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
ans_dfs = []
ans_bfs = []

def bfs(graph, visited, v, ans,n):
    dq = deque([v])
    while dq:
        if len(ans) == n:
            break
        ele = dq.popleft()
        visited[ele] = True
        ans.append(ele)
        for i in graph[ele]:
            if not visited[i]:
                dq.append(i)
    return ans

def dfs(graph, visited, ele, ans):
    visited[ele] = True
    ans.append(ele)
    for i in graph[ele]:
        if not visited[i]:
            dfs(graph, visited, i, ans)
    return ans

print(' '.join(map(str, dfs(graph,visited_dfs,v,ans_dfs))))
print(' '.join(map(str, bfs(graph,visited_bfs,v,ans_bfs,n))))

a = "123"
a.replace("1","a")

print(a)