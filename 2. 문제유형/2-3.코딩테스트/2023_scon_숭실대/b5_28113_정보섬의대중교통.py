'''
'''

import sys

li = sys.stdin.readline().rstrip().split(' ')
n = int(li[0])
a = int(li[1])
b = int(li[2])

if a > b:
    print("Subway")
elif a < b:
    print("Bus")
else:
    print("Anything")
# a - 버스
# b - 지하철