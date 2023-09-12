'''
    그리디 문제 뭔가 귀찮은데 ..?
    가장 단순한 문제이면서 -- 그리디인걸 모르면서도 자동적으로 그리디로 푸는 경우도 많은 것 같다

    ** 아이디어 --> '역추적'
    특정 과정이 있는 경우는 -- 이렇게 역추적 탐욕 알고리즘으로 풀면 된다
'''

import sys
a,b = map(int,sys.stdin.readline().rstrip().split())

cnt = 0
while a != b:
    if b % 2 != 0:
        if str(b)[-1] == '1':
            b = str(b)[:-1]
            b = int(b)
            cnt += 1
        else:
            cnt = -1
            break
    elif b % 2 == 0:
        b //= 2
        cnt += 1

    if a > b:
        cnt = -1
        break

if cnt != -1:
    print(cnt + 1)
else:
    print(cnt)