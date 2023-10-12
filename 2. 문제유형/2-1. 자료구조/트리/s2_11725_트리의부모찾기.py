""""""
"""
    ** 메모리 초과가 나니깐 - Python3로 제출
    -- 결국 재귀구만 시부레 
"""

# 그래프 이론에 대해서 공부해보도록 하자

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())

tree = [[] for _ in range(n+1)]
roots = [-1] * (n+1)
visited = [False] * (n+1)

for i in range(1,n):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x):
    visited[x] = True
    if not tree[x]:
        return
    for idx in tree[x]:
        if not visited[idx]:
            visited[idx] = True
            dfs(idx)
            roots[idx] = x

dfs(1)
for i in range(2,n+1):
    print(roots[i])