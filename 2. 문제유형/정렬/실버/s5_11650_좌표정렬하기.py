a = '실버5'

"""
    이제 뭐 python 기본 라이브러리 이용하는 정렬 문제는 어렵지 않다
"""

import sys

n = int(sys.stdin.readline())

li = []
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    li.append([x,y])

for i in sorted(li, key=lambda x : (x[0], x[1])):
    print(i[0], i[1])