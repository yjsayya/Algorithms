'''
    stack을 통해서 푸는 대표적인 문제 !!
'''
def solution(s):

    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return false
    
    if len(stack) == 0:
        return True
    else:
        return false