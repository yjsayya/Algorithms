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
        if nZroNum != bin(n)[2:].count('1'):
            continue
        else:
            return n