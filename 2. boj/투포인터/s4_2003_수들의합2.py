''''''
"""
    ** 투포인터를 이용하는 문제 
    
    << solution >>
    - 시간 복잡도 : O(n)
    
    - 구간의 합 < Target(M) : 오른쪽 포인터 → 이동 (합을 늘리기 위함)
    - 구간의 합 > Target(M) : 왼쪽 포인터 → 이동  (합계 줄이기 위함)
    
    - 구간의 합 = Target(M) : 카운트 증가,  오른쪽 포인터 → 이동
"""
import sys

n,m = map(int,sys.stdin.readline().split())
numList = list(map(int,sys.stdin.readline().split()))

left, right = 0, 1
cnt = 0

while left <= right <= n:
    total = sum(numList[left:right])

    if total == m:
        cnt += 1
        left += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(cnt)