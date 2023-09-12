'''
    이런 식으로 푸는거구나 ㅇㅋ
    제일 큰 것부터 하나씩 내려서 확인해보면 되는거였네
'''

import sys
# 1. 입력 받기
n = int(sys.stdin.readline())
homeworks = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 2. 방문처리
visited = [False] * 1001
# 3. 점수를 기준으로 정렬
homeworks.sort(key=lambda x : -x[1])

answer = 0
for d,w in homeworks:
    while d > 0 and visited[d]:
        d -= 1

    if d == 0:
        continue
    else:
        visited[d] = True
        answer += w

print(answer)