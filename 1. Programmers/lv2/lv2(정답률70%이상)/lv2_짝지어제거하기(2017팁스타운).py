"""
    stack으로 푸는 문제였다 !!!
    아 이걸 왜 생각 못했지? ㅅㅂ
"""

# 이것도 시간초과 시부레
def solution(s):
    frstChar = "1"

    while frstChar != s:
        frstChar = s
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                s = s.replace(s[i - 1:i + 1], '', 1)
                break

    return 1 if len(s) == 0 else 0


# stack을 사용하니깐 깔끔!!!
def solution2(s):
    stack = []

    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    return 1 if len(stack) == 0 else 0