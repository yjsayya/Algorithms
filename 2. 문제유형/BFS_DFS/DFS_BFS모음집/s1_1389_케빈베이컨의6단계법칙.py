""""""
"""
    이건 bfs로 풀어야하는 문제였다
    
    ** dfs로 푸는 문제 vs bfs로 푸는 문제 vs 둘다 상관 없는 문제
    --> 이걸 구분할 줄 아는 능력이 가장 중요한 것 같다!!
    
    dfs푸는 것보다 bfs로 푸는게 맞았다 
"""

import sys
from collections import deque

def bfs(user,visited,num):
    dq = deque()
    dq.append(user)
    visited[user] = True
    while dq:
        x = dq.popleft()
        for i in graph[x]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True
                num[i] = num[x] + 1

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

ans = dict()
for user in range(1,n+1):
    visited = [False] * (n+1)
    num = [0] * (n+1)

    bfs(user,visited,num)
    ans[user] = sum(num)

print(sorted(ans.keys(), key=lambda x : ans[x])[0])