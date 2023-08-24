""""""
"""
    dfs/bfs 추천문제 (4)
    
    -- 이거 나중에 다시 한번 풀어보자
    -- 조금 더 코드를 정리할 수 있을 것 같은데
    정리가 안되네 시부레 일단 넘어 간다 
"""

import sys
a,p = map(int,sys.stdin.readline().rstrip().split())

numList = set()
numList.add(a)
rmvList = set()

def recur(n):
    global numList
    global rmvList

    # 2-1. 순열의 다음 수 구하기
    next = 0
    for num in str(n):
        next += pow(int(num),p)

    if next in rmvList:
        return
    # 2-2. 순열의 다음 수로 처리하기
    if next not in numList:
        numList.add(next)
    else:
        numList.discard(next)
        rmvList.add(next)
    recur(next)

recur(a)

print(len(numList))