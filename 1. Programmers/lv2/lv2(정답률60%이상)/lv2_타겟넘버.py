''''''
"""
    dfs문제 
"""

# 일단 다른 사람 풀이 보고 넘겼는데 dfs문제는 진짜 연습 좀 해야겠다
def dfs(numbers, target, depth):
    ans = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        ans += dfs(numbers, target, depth + 1)
        numbers[depth] *= -1
        ans += dfs(numbers, target, depth + 1)

        return ans


def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer