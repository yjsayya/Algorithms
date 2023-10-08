""""""
"""
    dfs/bfs 추천문제 (4)
    다시 풀어보니깐 - 너무 dfs로 풀려고 틀 안에서 생각했던 것 같다
    두번째 풀이가 훨씬 깔끔한 것 같다
    그냥 dic으로 풀면 되는거였는데 잘 기억해두도록 하자 
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
    # 2-2. 알고리즘. 순열의 다음 수로 처리하기
    if next not in numList:
        numList.add(next)
    else:
        numList.discard(next)
        rmvList.add(next)
    recur(next)

recur(a)

print(len(numList))


# 두번째 풀이
# - 두 번째로 푸니깐 훨씬 낫네
a,p = map(int,input().split())

def seq(x):
    ans = 0
    for i in str(x):
        ans += int(i)**p
    return ans


dic = {a : 1}
while dic[a] != 3:
    a = seq(a)
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

res = []
for j in dic:
    if dic[j] == 1:
        res.append(j)

print(len(res))