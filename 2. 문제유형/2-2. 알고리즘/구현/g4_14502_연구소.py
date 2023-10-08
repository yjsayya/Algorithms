""""""
"""
    1. 벽 3개 세우기
    2. 바이러스 퍼뜨리기
    3. 안전 영역 - 개수 세기
    
    --> 이렇게 도식화를 하면서 접근 해야한다 
"""

import sys

n,m = map(int, sys.stdin.readline().split())
lab = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


