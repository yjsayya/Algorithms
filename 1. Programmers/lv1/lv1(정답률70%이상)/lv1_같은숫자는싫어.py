''''''
"""
    가장 기본적인 스택/큐 문제

"""

# 첫번째 풀이
def solution(arr):
    stack = []
    for i in arr:
        if stack:
            if stack[-1] != i:
                stack.append(i)
        else:
            stack.append(i)

    return stack


# 조금 더 깔끔하게 정리 해보았다
def solution2(arr):

    stack = []
    for i in arr:
        if stack and stack[-1] == i:
            continue
        stack.append(i)

    return stack