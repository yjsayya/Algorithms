''''''
"""
    예외 처리를 얼마나 깔끔하게 할 수 있는가? 
    스택 - 구현문제
"""

def solution(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return False if stack else True