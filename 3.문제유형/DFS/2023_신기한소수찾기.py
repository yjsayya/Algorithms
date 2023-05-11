import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True

# def DFS(number):
#     if len(str(number)) == N:
#         if i % 2 == 0:
#             pass
#         if isPrime(number * 10 + 1):
#             DFS(number * 10 + 1)

DFS(2)
DFS(3)
DFS(5)
DFS(7)