
'''

'''

import sys

n, m = map(int, input().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.extend(b)

print(sorted(a))

