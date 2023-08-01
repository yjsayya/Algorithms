''''''
"""
    전형적인 greedy로 푸는 문제였다 
    -- key point : 그리디 문제 였다는 것을 알아 차리는 것이 가장 중요한 요소였다
    
    (w.f) python은 문자열인 숫자도 그냥 대소비교가 가능하다!!
    
    아이디어가 떠오르지 않았다 
    1. stack으로 처리 하였고
    2. 마지막 예외처리까지 해줘야 한다(다 stack에 넣었는데도 k가 0이 아닐때)
"""

# 첫번째 풀이
def solution(number, k):
    stack = []
    for num in number:
        if not stack:
            stack.append(num)
        else:
            while stack and k > 0 and stack[-1] < num:
                k -= 1
                stack.pop()

            stack.append(num)

    while k > 0:
        k -= 1
        stack.pop()

    return "".join(stack)


# 첫번째 풀이를 좀 정리해볼까 한다
def solution2(number,k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)

    return "".join(stack) if k == 0 else "".join(stack[:-k])
