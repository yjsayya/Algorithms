""""""
"""
    dfs 풀이 
    bfs 풀이 
"""

# 1. DFS 풀이
import sys
sys.setrecursionlimit(10**5)
def dfs(numbers, target, depth):
    ans = 0
    # 1. 종료 조건
    if depth == len(numbers):
        return 1 if sum(numbers) == target else 0
    # 2. 문제에 대한 정의
    ans += dfs(numbers, target, depth + 1)
    numbers[depth] *= -1
    ans += dfs(numbers, target, depth + 1)

    return ans

def solution_dfs(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer


# 2. BFS 풀이
from collections import deque
def solution_bfs(numbers, target):
    n = len(numbers)

    dq = deque()
    dq.append([numbers[0], 0, numbers[0]])
    dq.append([-numbers[0], 0, -numbers[0]])

    ans = 0
    while dq:
        num, depth, tot = dq.popleft()
        # 1. 종료 조건
        if depth == n - 1:
            if tot == target:
                ans += 1
            continue
        # 2. 문제에 대한 정의
        dq.append([numbers[depth + 1], depth + 1, tot + numbers[depth + 1]])
        dq.append([-numbers[depth + 1], depth + 1, tot - numbers[depth + 1]])

    return ans