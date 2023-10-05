""""""
"""
    dfs/bfs
    
    이제 실력이 조금 붙은 듯 ..!
    이 정도는 이제 가볍게 풀 수 있다 !!
    dfs가 생각하는 재미가 분명히 있다 ㅋㅋ 
"""

import sys

def dfs(x,visited):
    if x == b:
        return
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = visited[x] + 1
            dfs(i,visited)
# 0. 입력 받기
n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 1. 필요한 변수들 선언
visited = [0] * (n+1)
# 2. dfs 돌리기
dfs(a,visited)
# 3. 출력
if visited[b] == 0:
    print(-1)
else:
    print(visited[b])