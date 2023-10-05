'''
'''

import sys
sys.setrecursionlimit((100_000))

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

print(graph)