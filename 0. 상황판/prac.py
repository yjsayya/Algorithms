
from collections import deque

def solution(board, k, ax, ay, bx, by):

    n = len(board)

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

