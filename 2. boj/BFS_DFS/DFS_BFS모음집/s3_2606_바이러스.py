""""""
"""
    dfs와 bfs 모두 가능하다 
    -- 이 두 버전 모두 풀어보도록 하자 
    -- 조금씩 개념은 잡혀가는 듯 하다 ...
"""

# import sys
# from collections import deque
#
# num = int(sys.stdin.readline())
# pair = int(sys.stdin.readline())
#
# network = dict()
# for _ in range(pair):
#     i,j = map(int,sys.stdin.readline().rstrip().split())
#     if i in network:
#         network[i].append(j)
#     else:
#         network[i] = [j]
#
# visited = [0] * (num+1)
#
# # print(network)
#
# dq = deque()
# cnt = 0
# dq.append(1)
#
# def bfs(x):
#     global cnt
#     while dq:
#         com = dq.popleft()
#         if visited[com] != 1:
#             visited[com] = 1
#             if com in network:
#                 for i in network[com]:
#                     dq.append(i)
#
# bfs(1)
# # print(visited)
# print(visited.count(1)-1)
#
#


n = int(input())
m = int(input())

graph = [[]*n for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (n+1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)

n = int(input())
m = int(input())

network = dict()
for _ in range(m):
    a,b = map(int,input().split())
    if a in network: network[a].append(b)
    else: network[a] = [b]
    if b in network: network[b].append(a)
    else: network[b] = [a]

cnt = 0
visited = [0] * n

def dfs(com):
    global cnt
    visited[com-1] = 1
    for i in network[com]:
        if visited[i-1] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)