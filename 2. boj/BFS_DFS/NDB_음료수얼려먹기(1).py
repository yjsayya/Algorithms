'''
    제한사항 - (1 ≤ N.M ≤ 1_000)

'''

import sys
sys.setrecursionlimit((100_000))

# 0. 입력 받기
n,m = map(int, input().split())

# 1. 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 2. DFS
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] == 1
        # 상,하,좌,우 위치 모두 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)