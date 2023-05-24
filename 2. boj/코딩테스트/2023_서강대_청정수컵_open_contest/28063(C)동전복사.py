'''
    뭔가 어려워 보이지만 -- 경우의 수가 3개 밖에 없는 간단한 문제였다 
    1. 양 끝인 경우 (1,1), (1,n), (n,1), (n,n) --> 2가 정답
    2. x,y 중 하나만 1인 경우 --> 3이 정답
    3. 가장자리가 아닌 내부에 있는 경우 --> 4가 정답
    ** 예외처리 --> n == 1인 경우 --> 0이 정답
'''
import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))
x = li[0]
y = li[1]

if n == 1:
    print(0)
else:
    if x == 1 or x == n:
        if y == 1 or y == n:
            print(2)
        else:
            print(3)
    elif y == 1 or y == n:
        if x == 1 or x == n:
            print(2)
        else:
            print(3)
    else:
        print(4)