''''''
"""
    ** 투포인터_문자열 문제
    
    sum(sequence[left:right]) --> 이걸로 계속 하니깐 시간초과가 나네 
    하나씩 더해주는걸로 바꿔야했다
    
    
"""


# 첫번째 풀이 - 시간초과 // 아쉽다 잘 풀었는데
def solution(sequence, k):
    left, right = 0, 1
    li = []

    while left <= right <= len(sequence):
        tot = sum(sequence[left:right])
        if tot < k:
            right += 1
        elif tot > k:
            left += 1
        else:
            li.append([left, right - 1])
            right += 1
            left += 1

    li = sorted(li, key=lambda x: (x[1] - x[0]))

    return li[0]

# 두번째 풀이 -
def solution2(sequence,k):
    li = []
    left,right = 0,0
    tot = sequence[left]

    while left <= right <= len(sequence):
        if tot < k:
            right += 1
            tot += sequence[right]
        elif tot > k:
            left += 1
            tot -= sequence[left]
        else:
            li.append([left,right])

    li = sorted(li, key=lambda x: (x[1] - x[0]))
    return li[0]


def solution4(sequence, k):
    answers = []
    tot = 0
    l = 0
    r = -1

    while True:
        if tot < k:
            r += 1
            if r >= len(sequence):
                break
            tot += sequence[r]
        else:
            tot -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if tot == k:
            answers.append([l, r])

    return sorted(answers,key=lambda x: (x[1] - x[0], x[0]))[0]