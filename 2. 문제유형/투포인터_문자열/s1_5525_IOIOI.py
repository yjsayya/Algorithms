""""""
"""
    ** 서브태스크 1
    - [제한사항] N ≤ 100, M ≤ 10 000.
    - [풀이] : 단순하게 문자열 slicing
    
    ** 서브태스크 2
    - [제한사항] 없음 
    - [풀이] : 투포인터_문자열 알고리즘 
"""

import sys

# 1. <서브태스크 1> - 고려한 풀이
    # 문자열 슬라이싱을 이용해서 체크하는 방식
def getPn(n):
    string = 'IO' * n
    return string + 'I'

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

ans1 = 0
string1 = getPn(n)
l1 = len(string1)
for i in range(l1,m+1):
    if s[i-l1:i] == string1:
        ans1 += 1

print(ans1)

# 2. <서브 태스크 2> - 고려한 풀이
    # 투포인터_문자열

left,right = 0,0
cnt = 0

while right < m:
    if s[right:right+3] == 'IOI':
        right += 2
        if right - left == 2*n:
            cnt += 1
            left += 2
        else:
            right += 1
            left = right

print(cnt)