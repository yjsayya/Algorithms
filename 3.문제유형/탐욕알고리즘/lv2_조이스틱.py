# min(a,b) --> 이런식으로 쓸 수 있다는거 기억하고
# 내장함수 --> ord(), chr() 한번 보고 가자 좋네


def solution(name):
    cnt = 0
    abc = 'ABCDEFGHIJKLMN'
    xyz = 'AZYXWVUTSRQPO'

    # 예외처리 - 전부 A인 경우
    if name.count('A') == len(name):
        return 0

    # 1단계 - 알파벳 바꾸기
    for i in range(len(name)):
        if name[i] == 'A':
            pass
        elif name[i] in abc:
            cnt += abc.index(name[i])
        elif name[i] in xyz:
            cnt += xyz.index(name[i])

    # 2단계 - 이동
    length = len(name)
    if name.count("A") > 1:
        pass
    elif name.count('A') == 1:
        if name[-1] == 'A' or name[1] == 'A':
            cnt += length - 2
        else:
            cnt += length
    else:
        cnt += (length - 1)

    return cnt

print(solution("ABCDEFGHIJKLMON"))
print(solution("AAAAAABBBAACAAAA"))


# 알파벳 이동은 ord() 내장함수를 이용하는 방법도 있다
    # 다른 분들 의견에 의하면 -- 그리디 문제 아니라고 한다
def solution1(name):
    min_move = len(name) - 1
    changeAbc = 0

    abc = "BCDEFGHIJKLMN"
    zyx = "ZYXWVUTSRQPO"

    # 예외처리 - 전부 A인 경우
    if name.count('A') == len(name):
        return 0

    # 1단계 - 알파벳 변환
    for i in name:
        if i == "A":
            pass
        elif i in abc:
            changeAbc += abs(ord("A") - ord(i))
        elif i in zyx:
            changeAbc = 26 - (abs(ord("A") - ord(i)))

    # 2단계 - 이동
    for ind, ele in enumerate(name):
        next_ind = ind + 1

        while next_ind < len(name) and name[next_ind] == "A":
            next_ind += 1

        min_move = min(min_move, 2*ind + len(name) - next_ind, 2*(len(name)-next_ind) + ind)
        # 일반 vs 왼쪽먼저탐색 vs 오른쪽 먼저탐색

    return changeAbc + min_move


# a0 b1 c2 d3 e4
# f5 g6 h7 i8 j9
# k10 l11 m12 n13
# o12 p11 q10 r9 s8
# t7 u6 v5
# w4 x3 y2 z1



# 주현이 풀이
def solution(name):
    [spl] = name.split()
    cA = ord("A")
    cZ = ord("Z")
    cc = (cZ-cA)
    answer = -1


    for idx, s in enumerate(spl):
        offset = ord(s)-cA
        print("offset: ", offset, ", ", cc - offset, ";", answer)
        answer += min(offset, (cc-offset+1))

        if (idx != 1) or offset > 0:
            answer += 1

    print(cc)

    return answer

def solution(name):
    [spl] = name.split()
    cA = ord("A")
    cc = 26
    answer = 0
    prevA = -1
    idx = 0
    siz = len(spl)
    firstA = -1
    seqA = 0

    
    while idx<siz:
        s = spl[idx]
        offset = ord(s)-cA
        print("offset: ", offset, ", ", cc-offset, ";", answer)
        if offset == 0:
            if prevA == idx-1: seqA += 1
            else: seqA = 1
            prevA = idx
        else:
            answer+=min(offset, (cc-offset+1))
        idx += 1
    print(cc)
    print("s:", siz, ", ", seqA)
    return answer + siz-(seqA+1)