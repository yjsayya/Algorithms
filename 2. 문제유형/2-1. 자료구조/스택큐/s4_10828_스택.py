""""""
"""
    문제 오류가 있는 듯 하다
    -- 입력 길이가 주어지지 않았는데 
    -- 그래서 1번 예시를 끝낼 수가 없게 되어있다
    -- 다행히 일단 테스트케이스에서는 그런 경우가 없는지 문제 없이 정답을 맞출 수는 있었다 
"""

import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "pop":
        if stack: print(stack.pop())
        else: print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if stack: print(0)
        else: print(1)
    elif cmd == "top":
        if stack: print(stack[-1])
        else: print(-1)
    else:
        stack.append(cmd.split(' ')[1])