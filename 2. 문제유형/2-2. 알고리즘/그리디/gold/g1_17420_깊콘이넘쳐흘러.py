"""

"""
import sys
import heapq

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
# a는 남은 기한
# bi일 뒤에 사용할 계획
dic = dict()
for i,j in zip(a,b):
    dic[i] = j
cnt = 0
li = sorted(dic.items(), key= lambda x : x[0])

heapq.heapify(li)
if li[0][0] > li[0][1]:
    cnt += 1