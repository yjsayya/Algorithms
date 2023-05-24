
'''
    이걸 문제라고 내다니 ...
'''

import sys

li = list(map(int, sys.stdin.readline().split()))
for i in sorted(li):
    print(i, end= " ")