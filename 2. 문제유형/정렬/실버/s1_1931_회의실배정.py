# 실버 1
'''
    제한사항
    - (1 <= n <= 100,000)
'''

import sys

n = int(input())
li = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

li.sort(key=lambda x : x[0])
cnt = 0

for _ in range(n):
    

# 0-6 6-10
# 1-4 5-7 8-11 12-14 --> 4개
# 2-13
# 3-5 5-9
# 3-8 8-12 