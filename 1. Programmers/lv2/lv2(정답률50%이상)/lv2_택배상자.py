''''''
"""
    문제유형 : 스택/큐 
    
    첫번째 풀이 vs 두번째 풀이 : 시간복잡도 한번 확인해보자
    어렵지 않게 잘 풀어냈다
"""

# 첫번째 풀이 - 뒤집은 후 pop()을 쉽게 했는데
def solution(order):

    order.reverse()

    stack = []
    cnt = 0
    for box in range(1,len(order)+1):
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


# 두번째 풀이 - 안 뒤집고 그냥 해보겠다
#   --> 이렇게 하면 시간초과 나네
def solution2(order):
    n = len(order)

    stack = []
    cnt = 0
    for box in range(1,n+1):
        if box == order[0]:
            cnt += 1
            order.pop(0)
            while stack and stack[-1] == order[0]:
                cnt += 1
                stack.pop()
                order.pop(0)
        else:
            stack.append(box)
    return cnt


# 다른 사람 풀이
#   --> 이게 젤 깔끔한 거 같다
#   --> order[cnt] 이런 스킬을 꼭 알아두자
def solution3(order):
    stack = []
    i = 1
    cnt = 0

    while i != len(order) + 1:
        stack.append(i)
        while stack and stack[-1] == order[cnt]:
            cnt += 1
            stack.pop()

        i += 1
    return cnt

