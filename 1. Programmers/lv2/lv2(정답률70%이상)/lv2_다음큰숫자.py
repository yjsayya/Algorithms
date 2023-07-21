''''''
"""
    - 2진법 다루기
    - lv2 이진변환반복하기와 같이 풀어보자
"""

def solution(n):
    answer = 0
    binaryN = bin(n)
    a = n + 1
    while True:
        binaryA = bin(a)
        if bin(n).count('1') == binaryA.count('1'):
            answer = a
            break

        a += 1

    return answer


def solution2(n):
    nZroNum = bin(n)[2:].count('1')
    while True:
        n += 1
        if bin(n)[2:].count('1') == nZroNum:
            return n