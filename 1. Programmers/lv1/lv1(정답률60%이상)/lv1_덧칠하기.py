"""
    ** 아이디어를 도출해내지 못했다 ㅠㅜㅡ
    - 좀 어려운데? 나중에 다시 한번 더 풀어보자
"""

def solution(n, m, section):
    answer = 1  # 칠하는 횟수
    paint = section[0]  # 덧칠 시작점

    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]

    return answer