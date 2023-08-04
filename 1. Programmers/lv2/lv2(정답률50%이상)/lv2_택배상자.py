''''''
"""
    문제유형 : 스택/큐 
    
    
"""

def solution(order):

    # 1.
    n = len(order)

    stack = []
    cnt = 0
    for box in range(1,n+1):
        if box == order[-1]:
            cnt += 1
            order.pop()

            while stack and stack[-1] == order[-1]:
                cnt += 1
                stack.pop()
                order.pop()

        else:
            stack.append(box)

    return cnt