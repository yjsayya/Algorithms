import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())

dq = deque([i for i in range(1,n+1)])
ans = []
while dq:
    dq.rotate(-k+1)
    ans.append(str(dq.popleft()))

print("<" + ", ".join(ans) + ">")


def dfs(numbers, target, depth):
    ans = 0
    if depth == len(numbers):
        return 1 if sum(numbers) == target else 0
    else:
        ans += dfs(numbers, target, depth + 1)
        numbers[depth] *= -1
        ans += dfs(numbers, target, depth + 1)

        return ans


def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer