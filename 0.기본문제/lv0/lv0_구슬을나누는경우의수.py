from itertools import permutations, combinations

# 단순 무식하게 푼 방법 --> 시간 복잡도 전혀 고려 안함
def solution(balls, share):
    n = 1
    r = 1
    a = 1

    for i in range(1, balls + 1):
        n *= i

    for j in range(1, share + 1):
        r *= j

    for k in range(1, balls - share + 1):
        a *= k

    return n / a / r


# 라이브러리를 사용하는 방법
    # --> 시간 초과 나옴
    # --> 시간 복잡도가 안 좋네 : 안쓰는게 좋을 듯?
def solution2(balls, share):
    ball = [i for i in range(1, balls+1)]
    return len(list(combinations(ball,share)))