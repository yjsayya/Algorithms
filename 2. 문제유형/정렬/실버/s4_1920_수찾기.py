
"""
    특정 정수의 등장 여부만을 간단하게 체크하면 되는데
    - 이런 경우 set으로 풀면 시간 복잡도를 훨씬 줄일 수 있따!!!!!
    - 이거 꼭 알아두자!!!!!
"""


# 첫번째 풀이
    # --> 시간 초과가 났다
import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))

m = int(input())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)

import sys

n = int(input())
A = set(map(int, sys.stdin.readline().split()))

m = int(input())
B = list(map(int, sys.stdin.readline().split()))

for b in B:
    if b in A:
        print(1)
    else:
        print(0)



# 두번째 풀이 
    # --> 전형적인 이분탐색 문제라고 한다
import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))

m = int(input())
B = list(map(int, sys.stdin.readline().split())) 

A.sort()

def binary(i):
    first = 0
    end = n-1

    while first <= end:
        mid = (first + end) // 2
        if A[mid] == i:
            return True
        
        if i < A[mid]:
            end = mid -1
        elif i > A[mid]:
            first = mid + 1

for i in range(m):
    if binary(B[i]):
        print(1)
    else:
        print(0)



