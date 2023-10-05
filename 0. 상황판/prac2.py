
def solution(prices):

    stack = []
    ans = [-1] * len(prices)

    for idx in range(len(prices)):

        while stack != [] and stack[-1][1] > prices[idx]:
            past = stack.pop()[0
            ans[past] = idx - past
        stack.append([idx,prices[idx]])



li = [(0,1),(1,2),(2,3),(3,2),(4,3)]




print(solution([1, 2, 3, 2, 3]))
# solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])