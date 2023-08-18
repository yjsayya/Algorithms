
# 타겟 넘버

def dfs(numbers,target,depth):
    ans = 0
    if depth == len(numbers):
        return 1 if sum(numbers) == target else 0
    else:
        ans += dfs(numbers,target, depth+1)
        numbers[depth] *= -1
        ans += dfs(numbers,target,depth+1)

        return ans
def solution(numbers,target):
    answer = dfs(numbers,target,0)
    return answer

