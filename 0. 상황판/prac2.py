

import sys
sys.setrecursionlimit(10*6)

n = int(sys.stdin.readline().strip())

tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [-1] * (n+1)

for _ in range(2, n+1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(x):
    visited[x] = True
    if not tree[x]:
        return
    for idx in tree[x]:
        if not visited[idx]:
            dfs(idx)
            ans[idx] = x

dfs(1)

for idx in range(2,n+1):
    print(ans[idx])