"""

"""

def solution(n, a, b):
    cnt = 0

    while max(a, b) % 2 != 0 or abs(a - b) != 1:
        # a처리
        if a % 2 == 0: a //= 2
        else: a = a // 2 + 1
        # b처리
        if b % 2 == 0: b //= 2
        else: b = b // 2 + 1

        cnt += 1

    return cnt + 1

# 개쩌는 풀이 하나 가져왔다 시부레 ...
def solution2(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer