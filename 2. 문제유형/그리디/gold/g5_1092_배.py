""""""

"""

"""

import sys

n = int(sys.stdin.readline())
crane_weight = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(int,sys.stdin.readline().split()))

time = 0
if max(boxes) > max(crane_weight):
    print(-1)
else:
    while len(boxes) > 0:
        time += 1
        for i in range(len(crane_weight)):
            for j in range(len(boxes)):
                if crane_weight[i] >= boxes[j]:
                    boxes.pop(j)
                    break
    print(time)


# 다른 사람 풀이
import sys
input = sys.stdin.readline

n = int(input())
weight = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
time = 0
if max(box) > max(weight):
    print(-1)
else:
    while len(box) > 0:
        time += 1
        for i in range(len(weight)):
            for j in range(len(box)):
                if weight[i] >= box[j]:
                    box.pop(j)
                    break
    print(time)




