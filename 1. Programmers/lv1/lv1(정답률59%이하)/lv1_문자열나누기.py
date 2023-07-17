"""
    아이디어 --> 어떻게 풀어야 깔끔할까?

"""

def solution(s):
    cnt = 0
    idx = 2

    while idx < len(s):
        li = s[:idx]

        if len(li) == 2 and li[0] != li[1]:
            cnt += 1
            s = s[idx:]
        else:
            if len(li) // 2 == li.count(li[0]):
                idx = 2
                s = s[idx:]
                cnt += 1
            idx += 2

    if len(s) == 0:
        return cnt
    else:
        return cnt + 1


def solution2(s):
    answer = 0
    cnt1 = 0
    cnt2 = 0

    for i in s:
        if cnt1 == cnt2:
            answer += 1
            x = i

        if i == x:
            cnt1 += 1
        else:
            cnt2 += 1

    return answer
