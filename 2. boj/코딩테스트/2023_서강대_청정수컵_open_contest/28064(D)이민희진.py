
'''
제한사항 
    (1 <= N <= 100)
    이름 최대 1~20자

제한사항 보면 완전탐색으로 풀어도 괜찮을 것 같긴 한데 ...
'''
import sys
from itertools import combinations as comb

n = int(input())
li = []
for i in range(n):
    li.append(input())

for names in comb(li,2):
    for name in names:
        if 