""""""
"""
    아이디어는 똑같았는데 - 왜 내 풀이는 틀렸고 다른 사람 풀이는 맞았다 ㅠㅜ
    행렬과 (x,y)가 헷갈려서 그런건데 행 - 렬 변수 값 정확히 잘 넣도록 하자    
"""

import sys
from collections import deque

m,n,h = map(int,sys.stdin.readline().split())

tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dq = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                dq.append((i, j, k))

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while dq:
    z,y,x = dq.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomato[nz][ny][nx] == 0:
            tomato[nz][ny][nx] = tomato[z][y][x] + 1
            dq.append((nz,ny,nx))

ans = max(max(map(max,tomato)))-1
for i in tomato:
    for j in i:
        if 0 in j:
            ans = -1
print(ans)



import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 익은 토마토를 큐에 넣음
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k, 0))

# 방향지시자
df = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while queue:
    f, x, y, days = queue.popleft()

    # 인접위치 토마토 확인
    for i in range(6):
        nf = f + df[i]
        nx = x + dx[i]
        ny = y + dy[i]
        ndays = days + 1

        # 박스 영역 안인지 확인
        if 0 <= nx < n and 0 <= ny < m and 0 <= nf < h:
            # 안익은 토마토일 경우 익힘 처리 후 큐에 삽입
            if box[nf][nx][ny] == 0:
                box[nf][nx][ny] = 1
                queue.append((nf, nx, ny, ndays))

# 익지 않은 토마토가 있을 경우 결과값 -1로 변경
for i in range(h):
    for j in range(n):
        if box[i][j].count(0) > 0:
            days = -1
            break
print(days)