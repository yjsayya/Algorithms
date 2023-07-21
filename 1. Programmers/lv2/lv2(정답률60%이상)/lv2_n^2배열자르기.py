''''''
"""
    이중 배열에 대한 공부가 필요한 개념인 것 같다 
    -- 이런건 아마 직관력이 가장 중요할텐데 
    
    난 단계별로 공략을 해야한다고 생각했으나
    좋은 풀이를 보니 그렇지 않고 한번에 끝냈다 
"""

# 내가 처음에 시도 했던 방식이다 - 어림도 없었다
def solution(n, left, right):
    # 1. 2차원 배열 만들기
    arr = []
    for i in range(n):
        li = [0] * n
        arr.append(li)
    a =0
    # 2. 숫자 넣기
    for i in range(1, n + 1):
        for ar in arr:
            a += 1

    # 3. 1차원 배열로 만들기

    return arr[left:right + 1]


# ㅅㅂ 이렇게 푸는 거라고 한다
# 아이디어 - 인덱스의 몫과 나머지로 n x n 배열의 행과 열을 알 수 있다
# 그 중 큰 값에 1을 더하면 배열의 값입니다
def solution2(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n  # 몫
        b = i % n  # 나머지

        answer.append(max(a, b) + 1)

    return answer