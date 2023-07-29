''''''
"""
    첫번쨰 풀이 -- 완전탐색으로 풀어봤다 : 바로 메모리 초과
    
    두번째 풀이 -- 투포인터로 풀어봤다
"""


'''
import sys
from itertools import combinations as comb

n = int(sys.stdin.readline()) # 재료의 개수
m = int(sys.stdin.readline()) # 갑옷을 만드는데 필요한 수

gredient = list(map(int,sys.stdin.readline().split())) # n개의 재료들

cnt = 0
for i in list(comb(gredient,2)):
    if sum(i) == m:
        cnt += 1

print(cnt)
'''

import sys

n = int(sys.stdin.readline()) # 재료의 개수
m = int(sys.stdin.readline()) # 갑옷을 만드는데 필요한 수

gredient = list(map(int,sys.stdin.readline().split())) # n개의 재료들
gredient.sort()

left,right = 0,n-1
cnt = 0
while left < right:
    if gredient[left] + gredient[right] == m:
        cnt += 1
        left += 1
        right -= 1
    elif gredient[left] + gredient[right] < m:
        left += 1
    else:
        right -= 1

print(cnt)