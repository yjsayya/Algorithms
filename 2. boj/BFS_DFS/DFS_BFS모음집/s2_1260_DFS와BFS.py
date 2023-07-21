''''''
"""
    
"""

from collections import deque
import sys

n,m,v = map(int,sys.stdin.readline().split())

graph = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (n+1) # dfs 방문기록
visited2 = [False] * (n+1) # bfs 방문 기록





