import sys
from itertools import permutations as perm

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))
print(li)
maxi = max(li)
new_li = list(perm(li,len(li)))

check = False

cnt = 0
for lis in new_li:
    isCnt = False
    for idx in range(1,len(lis)):
        if lis[idx] == maxi:
           check = True
        if not check and lis[idx-1] > lis[idx]:
            break
        elif check and lis[idx-1] < lis[idx]:
            break
    if isCnt:
        cnt += 1

print(cnt)
