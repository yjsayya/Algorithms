""""""
"""
    (w.f) PyPy3 말고 pyhon3로 제출할 것 !!
    
    행렬(row,colum) 읽는 방법은 결국 이중 for문 사용해야 하네 
    1. recur() - 변수에 무엇을 넣어야 하는가
    2. 문제에 대한 정의
    3. 종료 조건
    -- 흐름 파악이 정말 너무 종요하다
"""

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans = [0,0,0]

def recur(x,y,n):
    global ans
    # 1. 문제에 대한 정의
    ele = paper[x][y]
    # 1-1. paper 읽기
    for row in range(x,x+n):
        for column in range(y,y+n):
            # 1-2. (1) 조건이 성립하지 않는 경우
            if paper[row][column] != ele:
                # 1-3. 내부 paper 읽기
                for i in range(3):
                    for j in range(3):
                        recur(x+i*n//3, y+j*n//3, n//3)
                return
    # 종료 조건 - 조건(1)이 성립하는 경우
    if ele == -1:
        ans[0] += 1
    elif ele == 0:
        ans[1] += 1
    else:
        ans[2] += 1
    return

recur(0,0,n)

for i in ans:
    print(i)