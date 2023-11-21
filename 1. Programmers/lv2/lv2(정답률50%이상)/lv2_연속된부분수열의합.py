''''''
"""
    ** 투포인터_문자열 문제
    sum(sequence[left:right]) --> 이걸로 계속 하니깐 시간초과가 나네 
    하나씩 더해주는걸로 바꿔야했다
    
    -- 오름차순으로 정렬 되어있다는 것도 잘 봐야한다!!
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

    return sorted(li, key=lambda x: (x[1] - x[0]))[0]

def solution1(sequence, k):
    ans = []
    left, right = 0, 1
    tot = sequence[left] + sequence[right]
    length = len(sequence)
    # 1. [0,0]인 경우 예외 처리
    if sequence[left] == k:
        return [0, 0]
    # 2. 투포인터로 답 구하기
    while True:
        if tot < k:
            right += 1
            if right == length:
                break
            tot += sequence[right]
        elif tot > k:
            tot -= sequence[left]
            left += 1
            if left == length:
                break
        else:
            ans.append([left, right])
            tot -= sequence[left]
            left += 1

            right += 1
            if right == length or left == length:
                break
            tot += sequence[right]

    return sorted(ans, key=lambda x: (x[1] - x[0], x[0]))[0]