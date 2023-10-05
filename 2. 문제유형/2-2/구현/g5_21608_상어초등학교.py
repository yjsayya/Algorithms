""""""
"""
    우선, 구현 문제의 경우 - 4중 for문까지 나올 각오를 해야하는 것 같다
    핵심은
    일단 문제의 주어진 조건에 해당하는 부분을 다 체크하고 디테일한 부분가지 신경쓰면 된다 
    결국 -- 근성이 필요하다 
"""

import sys

n = int(sys.stdin.readline())

classroom = [[0]*n for _ in range(n)]
like_room = [[] for _ in range(n*n+1)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n*n):
    arr = list(map(int,sys.stdin.readline().split()))
    like = arr[1:]
    like_room[arr[0]] = like

    if n*n == 0:
        classroom[1][1] = arr[0]
        continue

    temp = []
    for i in range(n):
        for j in range(n):
            sum_like, sum_empty = 0,0
            if classroom[i][j] != 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                    continue
                if classroom[nx][ny] in like:
                    sum_like += 1
                if classroom[nx][ny] == 0:
                    sum_empty += 1
            temp.append((sum_like, sum_empty, (i, j)))
    temp.sort(key=lambda x: (-x[0], -x[1], x[2]))

    classroom[temp[0][2][0]][temp[0][2][1]] = arr[0]

sum_answer = 0

for i in range(n):
    for j in range(n):
        answer = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            if classroom[nx][ny] in like_room[classroom[i][j]]:
                answer += 1
                continue
        if answer != 0:
            sum_answer += (10 ** (answer - 1))

print(sum_answer)