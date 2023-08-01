''''''
"""
    여러 가지 방법이 있겠지만
    1. 이중 for문 이용
    2. stack을 이용하는 방법
    
    -- 이 문제의 경우 이중 for문 잘 돌리면 풀 수 있었다
    -- 그래도 stack을 쓰는 것이 빠른 듯 하다 
"""

# 첫번째로 푼 풀이
# --> 이제 stack/queue문제는 어렵지 않게 풀 수 있을 것 같다
def solution(prices):
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


# 두번째 풀이
#   - 첫번째에 되게 잘 풀었던 것 같은데
#   - 오랜만에 다시 풀었더니 어떻게 풀었는지 모르겠다 ㅋㅋㅋ
def solution2(prices):
    ans = []
    idx = -1
    while prices:
        standard = prices.pop(0)
        idx += 1
        time = 0
        for i in prices:
            time += 1
            if standard > i:
                break
        ans.append(time)

    return ans

# 다른 사람 풀이도 가져와 봤다 - 굉장히 깔끔하다
def solution3(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# stack을 이용한 풀이
def solution4(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        while not stack and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])

    for i, s in stack:
        answer[i] = len(prices) - 1 - i

    return answer











