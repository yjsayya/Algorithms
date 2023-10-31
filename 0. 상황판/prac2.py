from collections import deque

def solution(board, k, ax, ay, bx, by):
    n = len(board)
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    def can_reach_safely(x, y, time):
        visited = [[False] * n for _ in range(n)]
        visited[x][y] = True
        queue = deque([(x, y, time)])

        while queue:
            cx, cy, ct = queue.popleft()

            if ct == 0:
                return True  # 캐릭터가 시간 내에 안전한 장소에 도달

            for dx, dy in dirs:
                for step in range(1, k + 1):
                    nx, ny = cx + dx * step, cy + dy * step

                    if is_valid(nx, ny) and not visited[nx][ny] and board[nx][ny] != 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny, ct - 1))

        return False  # 캐릭터가 시간 내에 안전한 장소에 도달하지 못함

    # 초기 위치가 안전한지 확인
    if not can_reach_safely(ax, ay, k) or not can_reach_safely(bx, by, k):
        return -1  # 초기 위치로부터 안전한 장소로 이동할 수 없음

    # 이동 시간을 기록할 DP 배열 초기화
    dp = [[float('inf')] * n for _ in range(n)]
    dp[ax][ay] = dp[bx][by] = 0
    queue = deque([(ax, ay), (bx, by)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            for step in range(1, k + 1):
                nx, ny = x + dx * step, y + dy * step

                if is_valid(nx, ny) and dp[nx][ny] == float('inf') and board[nx][ny] != 2:
                    dp[nx][ny] = dp[x][y] + 1
                    queue.append((nx, ny))

    # 두 캐릭터가 동시에 이동하면서 겹치지 않도록 최소 이동 시간을 찾음
    min_time = float('inf')

    for i in range(n):
        for j in range(n):
            if dp[i][j] < min_time and can_reach_safely(i, j, k):
                min_time = dp[i][j]

    return min_time