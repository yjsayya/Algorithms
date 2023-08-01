''''''
"""
    1. 순열을 이용해서 구하기
    
    2. 백트래킹을 이용하기
    
"""

# 이것도 해결 가능!!
'''
from itertools import permutations as perm
def solution(k,dungeons):
    ans = 0

    for p in perm(dungeons, len(dungeons)):
        tmp = k
        cnt = 0

        for need, spend in p:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        ans = max(ans,cnt)

    return ans
'''

# 두번째 풀이 - DFS
ans = 0

def dfs(k, cnt, dungeons, visited):
    global ans
    if cnt > ans:
        ans = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global ans
    visited = [False] * len(dungeons)
    dfs(k,0,dungeons,visited)
    return ans

테스트 8 - 47.47
테스트 17 - 34.39