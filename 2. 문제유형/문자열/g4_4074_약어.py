'''

'''

import sys

n = int(input())
meaningLess = set()

for _ in range(n):
    meaningLess.add(input())

while True:
    words = sys.stdin.readline().rstrip().split()
    if words == ['LAST', "CASE"]:
        break
    abb = word[0]
    word = {}
