""""""
"""
    [플로이드-워셜 알고리즘] 
    - 모든 정점에서 모든 정점으로의 최단 경로를 찾는 알고리즘이다.
    - 가중치가 음인 그래프, 가중치가 양인 방향 그래프, 무방향 그래프 : 모두 적용이 가능
    - 그래프 이론에서 매우 중요한 알고리즘
    
    - 시간복잡도 : O(n^3) // 모든 정점 쌍에 대해 다른 모든 정점을 한 번씩 거쳐보는 방식
"""

import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(' '.join(map(str, row)))