""""""
"""
    프로그래머스에서는 solution() 함수 형태의 유형을 가지고 있으니깐
    global을 이용하지 않고 할때 마다 모든 필요한 변수들을 파라미터로 넘겨주면 된다 
"""

import sys


def dfs(computers, com_num, check, n):
    # 1. 종료 조건
    if check[com_num - 1]:
        return
    # 2. 문제에 대한 정의
    check[com_num - 1] = True
    for idx in range(n):
        if com_num - 1 != idx and computers[com_num - 1][idx] == 1:
            dfs(computers, idx + 1, check, n)
    return


def solution(n, computers):
    check = [False] * n
    cnt = 0
    for com_num in range(1, n + 1):
        if not check[com_num - 1]:
            cnt += 1
            dfs(computers, com_num, check, n)

    return cnt