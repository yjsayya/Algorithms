""""""
"""
    bitwiseXOR 알고리즘을 물어보는 괴상한 문제였따
    python의 경우 num1 ^ num2 이렇게 비트 연산을 할 수 있었다 
"""

def solution(data, col, row_begin, row_end):
    # 1. 정렬하기
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    # 2. bitwise XOR
    res = 0
    for i in range(row_begin, row_end + 1):
        ans = 0
        for j in data[i - 1]:
            ans += j % i
        if res == 0:
            res = ans
        else:
            res = res ^ ans

    return res