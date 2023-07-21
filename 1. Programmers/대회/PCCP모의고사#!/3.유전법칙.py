''''''
"""
    아이디어 - 순서 p를 4로 나누면 형제 중 몇번째였는지 알 수 있따 
    -- 그렇게 쭉 4로 나누어줘서 가장 꼭대기까지 파악한 후 하나씩 꺼내서 분석하는 방식으로 간다
    1. stack 이용하기
    2. 재귀 함수 이용하기
    3. 
"""

def get_gene(n,p):
    stack = []

    p -= 1
    while n > 1:
        stack.append(p%4)
        n -= 1
        p //= 4

    while stack:
        num = stack.pop()
        if num == 0:
            return 'RR'
        elif num == 3:
            return 'rr'
        else:
            return 'Rr'

def solution(queries):
    return [get_gene(i[0], i[1]) for i in queries]