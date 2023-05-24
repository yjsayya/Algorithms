
'''

'''
import sys

n = int(input())
li = []

for _ in range(n):
    a,b,c,d = sys.stdin.readline().split()
    li.append([a, int(b), int(c), int(d)])

li.sort(key= lambda x : x[0])

for i in sorted(li, key= lambda x : (-x[1], x[2], -x[3])):
    print(i[0], end= "\n")
