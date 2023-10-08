'''
    ** 제한사항
    - (1 ≤ N ≤ 500,000)
    - 제한사항이 굉장히 작기 때문에 while문을 돌렸다

    ** 아이디어
    1) B와 R의 중복은 모두 없앤다 ex) BBBRRRBBB --> BRB
    2) min(B의개수 + 1, R의개수 +1) 중 작은 값을 출력하면 된다

    푸는 아이디어가 중요한 문제였다
'''

import sys

n = int(input())
s = sys.stdin.readline()

while 'BB' in s:
    s = s.replace('BB', 'B')

while 'RR' in s:
    s = s.replace('RR', 'R')

print(min(s.count('B')+1, s.count('R')+1))