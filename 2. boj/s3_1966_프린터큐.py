import sys
"""
    queue = [(ele,idx) for idx,ele in enumerate(queue)]
    이런 방법도 있으니깐 꼭 확인 해보자   
"""

testCases = int(input())

for _ in range(testCases):
    n, m = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    queue = [(imp,idx) for idx,imp in enumerate(queue)]

    cnt = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.pop()
        else:
            queue.append(queue.pop(0))