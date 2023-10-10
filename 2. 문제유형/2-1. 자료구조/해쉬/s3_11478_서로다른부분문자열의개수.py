""""""
"""
    접근 방식
    -- 이중 반복문으로 문자열의 부분 문자열을 구한다.
    -- 구한 부분 문자열을 빈 집합에 추가하여 len으로 길이를 구해 출력해준다.
"""

import sys

s = sys.stdin.readline().strip()
length = len(s)

se = set()
for i in range(1,length+1):
    for j in range(i,length+1):
        se.add(s[j-i:j])

print(len(se))