""""""
"""
    여러 가지 방법이 있겠지만
    1. 이중 for문 이용
    2. stack을 이용하는 방법
    3. 투포인터 알고리즘을 이용하는 방법
    
    -- 이 문제의 경우 이중 for문 잘 돌리면 풀 수 있었다
    -- 어쨌든 stack을 활용하는 방법이 여기선 훨씬 빨랐다 
    -- 그래도 stack을 쓰는 것이 빠른 듯 하다 
"""


# [첫번째 풀이] - 이중 for문
def solution1(prices):
    answer = [0] * len(prices)
    for idx, ele in enumerate(prices):
        check = False
        for k in range(idx + 1, len(prices)):
            if ele > prices[k]:
                check = True
                answer[idx] = k - idx
                break

        if not check:
            answer[idx] = len(prices) - idx - 1

    return answer


# [두번째 풀이] - 투포인터
def solution5(prices):
    ans = [-1] * len(prices)
    n = len(prices)

    left, right = 0, 1
    cnt = 0
    while left <= n-1:
        # 1. 종료 조건 (1) - 마지막 일때
        if right == n:
            ans[left] = cnt
            left += 1
            right = left + 1
            cnt = 0
        # 2. 종료 조건 (2) - 가격이 떨어졌을 때
        elif prices[left] > prices[right]:
            ans[left] = cnt + 1
            left += 1
            right = left + 1
            cnt = 0
        else:
            right += 1
            cnt += 1

    return ans


# [세번째 풀이] stack
def solution3(prices):
    stack = []
    answer = [0] * len(prices)

    for idx in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[idx]:
            past, _ = stack.pop()
            answer[past] = idx - past
        stack.append([idx, prices[idx]])

    for i, s in stack:
        answer[i] = len(prices) - 1 - i

    return answer


# [다른 사람 풀이 (1)] - 이중 for문
def solution4(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


print(solution3([1, 2, 3, 2, 3]))