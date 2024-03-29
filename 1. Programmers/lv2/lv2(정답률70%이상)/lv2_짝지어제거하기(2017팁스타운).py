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
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    return 0 if stack else 1

'''
구현 문제니깐 - 예외처리를 좀 더 깔끔하게 정리 해보았다
** 여기서 포인트는 
    if stack and i == stack[-1]:
    if i == stack[-1] and stack:
    
    이 두코드가 다르다는 것이다
    --> 이는 파이썬이 인터프리터 방식을 사용하기 때문이다
'''
def solution3(s):

    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return 0 if stack else 1