"""
    ** 아이디어 - 이런건 역으로 추적하는 방식을 사용하는 것이 좋다

    굉장히 간단하게 풀어낼 수 있었다
    처음에는 DFS/BFS 문제인줄 알았지만
    거꾸로 추적할 경우 - 그리디 문제인 것 같다
"""


def solution(n):
    k = 0

    while n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            k += 1

    return k


# 이런 식으로 푸는 방법도 있네 (미춌다)
def solution1(n):
    return bin(n).count('1')