# 단순 문자열 문제
    # 어렵지 않게 풀어낼 수 있었다 

import sys
n = int(input())
chz = list(sys.stdin.readline().split())

cnt = 0
chz = list(set(chz))

for i in chz:
    if "Cheese" == i[-6:]:
        cnt += 1

if cnt >= 4:
    print('yummy')
else:
    print('sad')


