
'''
    제한사항
    - (1 ≤ n ≤ 100,000) 
    - (1 ≤ x ≤ 2,000,000)

    1. 이중 for문
        - 시간복잡도 : O(N^2)
    2. 투 포인터 
        - 

'''
# 첫번째 풀이 - 아니나 다를까 시간초과 ㅋㅋ 
# import sys

# # 1. 입력 받기
# n = int(input())
# a = list(map(int, sys.stdin.readline().split()))
# x = int(input())

# # 2. 일단 정렬하기
# a.sort()

# 3. 계산


# print(cnt)

import sys
# 1. 입력 받기
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
x = int(input())

# 2. 정렬하기
a.sort()

# 3. 투포인터로 답 구하기
cnt = 0
start = 0
end = len(a) -1

while start < end:
    if a[start] + a[end] > x:
        end -= 1
    elif a[start] + a[end] < x:
        start += 1
    else:
        start += 1
        end -= 1        
        cnt += 1
# 4. 출력하기
print(cnt)