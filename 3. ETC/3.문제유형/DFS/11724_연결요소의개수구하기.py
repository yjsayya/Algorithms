import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


# n : 노드 개수, m : 엣지 개수
n, m = map(int, input().split())
# 인접리스트 만들기 
A = [[] for _ in range(n+1)]
# 방문자 리스트
visited = [False] * (n+1)

# 1. DFS() 함수 만들기
def DFS(v):
    # 방문 리스트 check하고
    visited[v] = True
    # 2. 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행(재귀 함수 형태)
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# 2. 받은 값을 각 인접 리스트에 넣기
for _ in range(m):
    # 들어온 수를 받고
    s, e = map(int, input().split())
    # 양방향 edge이므로 양쪽에 다 edge를 넣어줘야한다 
    A[s].append(e)
    A[e].append(s)

# 3. 여기서부터 이제 count 하면 됨 
count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)