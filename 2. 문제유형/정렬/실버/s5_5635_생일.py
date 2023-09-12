
'''

'''
import sys

n = int(input())
stu = []
for _ in range(n):
    li = list(sys.stdin.readline().split())
    li[1] = int(li[1])
    li[2] = int(li[2])
    li[3] = int(li[3])
    stu.append(li)

stu = sorted(stu, key= lambda x : (x[3], x[2], x[1]))

print(stu[-1][0])
print(stu[0][0])