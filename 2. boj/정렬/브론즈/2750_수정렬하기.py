# 브론즈 2

n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

li.sort()

for i in li:
    print(i, end=" ")