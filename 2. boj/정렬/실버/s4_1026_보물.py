# 실버 4
'''
    제한사항도 별로 크지 않고
    매우 쉬운 문제

    제한사항
    - N은 50보다 작거나 같은 자연수이고, 
    - A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.
'''

import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

answer = 0

for a,b in zip(A,B):
    answer += a*b

print(answer)