''''''
"""

"""
# [함수의반환값, 호출횟수]
# import sys
# sys.setrecursionlimit(10_000)
#
# def recursion(s,l,r):
#     global n
#     n += 1
#
#     if l >= r:
#         print(1, end=' ')
#     elif s[l] != s[r]:
#         print(0, end=' ')
#     else:
#         recursion(s,l+1,r-1)
#
# def isPalindrome(s):
#     recursion(s,0,len(s)-1)
#
# t = int(sys.stdin.readline())
# for _ in range(t):
#     s = sys.stdin.readline()
#     n = 0
#
#     isPalindrome(s)
#     print(n)

import sys
sys.setrecursionlimit(10_000)

testCase = int(input())

for _ in range(testCase):
    string = intpu()
