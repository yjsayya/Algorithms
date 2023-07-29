''''''
"""
    1. 첫번째 풀이
      - 시간 제한이 1.5초 였기 때문에 - 그냥 들이대도 가능한거였음
    2. 두번째 풀이
      - 투 포인터를 활용한 병합정렬 문제 
"""

# 첫번째 풀이
'''
import sys

n, m = map(int, input().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.extend(b)
print(sorted(a))
'''

# 두번째 풀이
import sys

n, m = map(int, input().split())
aList = list(map(int, sys.stdin.readline().rstrip().split()))
bList = list(map(int, sys.stdin.readline().rstrip().split()))

ans = []

a,b = 0,0
while a != len(aList) or b != len(bList):
    if a == len(aList):
        ans.append(bList[b])
        b += 1
    elif b == len(bList):
        ans.append(aList[a])
        a += 1
    else:
        if aList[a] < bList[b]:
            ans.append(aList[a])
            a += 1
        else:
            ans.append(bList[b])
            b += 1

print(*ans)