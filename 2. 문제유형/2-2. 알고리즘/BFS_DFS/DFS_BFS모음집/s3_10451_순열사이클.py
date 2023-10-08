""""""
"""
    dfs/bfs
    
    -- 이제 좀 dfs/bfs 문제가 풀리기 시작했다 
"""


import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n = int(sys.stdin.readline())
    numList = list(map(int,sys.stdin.readline().split()))

    visited = [False] * (n + 1)
    # 1. graph 만들기
    graph = dict()
    for i in range(1,n+1):
        graph[i] = numList[i-1]

    # 2. graph 순회하면서 확인하기
    def dfs(x):
        global cnt
        visited[x] = True
        if visited[graph[x]]:
            cnt += 1
            return
        else:
            dfs(graph[x])

    cnt = 0
    for j in graph:
        if not visited[j]:
            dfs(j)

    print(cnt)