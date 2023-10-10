""""""
"""
    문제 오류가 있는 듯 하다
    -- 입력 길이가 주어지지 않았는데 
    -- 그래서 1번 예시를 끝낼 수가 없게 되어있다
    -- 다행히 일단 테스트케이스에서는 그런 경우가 없는지 문제 없이 정답을 맞출 수는 있었다 
"""

import sys

n,m,k = map(int,sys.stdin.readline().split())
strArr = []
for _ in range(n):
    strArr.append(sys.stdin.readline().split())

print(strArr)