
'''

'''
import sys

n = int(input())
li = []

for _ in range(n):
    a,b,c,d = sys.stdin.readline().split()
    li.append([a, int(b), int(c), int(d)])

# 사전 순으로 배열하기 위해서 미리 한번 정렬해둔 후 
li.sort(key= lambda x : x[0])
# 해당 조건에 맞게 다시 배열 
for i in sorted(li, key= lambda x : (-x[1], x[2], -x[3])):
    print(i[0], end= "\n")
