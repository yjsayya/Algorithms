""""""
"""


"""

import sys

k = int(sys.stdin.readline())

stack = []
for _ in range(k):
    input = int(sys.stdin.readline().strip())
    if stack and input == 0:
        stack.pop()
    else:
        stack.append(input)

print(sum(stack))