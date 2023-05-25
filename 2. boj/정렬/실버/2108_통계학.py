# 실버 3
'''
    제한사항
    - (1 <= n <= 500,000)

    Counter 활용 잘 익혀두자
    n = 1인 경우는 예외처리 해줘야 한다
    round() 내장 함수 ㅇㅋ 
'''

import sys
from collections import Counter
# 1. 입력 받기
n = int(input())
li = [int(input()) for _ in range(n)]

if n == 1:
    print(li[0])
    print(li[0])
    print(li[0])
    print(0)
else:
    #2. 정렬
    li.sort()

    # 3-1. 평균값
    print(round(sum(li) / n))

    # 3-2. 중앙값
    print(li[n//2])

    # 3-3. 최빈값
    counter = Counter(li)
    a = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    if a[0][1] == a[1][1]: print(a[1][0])
    else: print(a[0][0])

    # 3-4. 범위
    print(li[-1] - li[0])