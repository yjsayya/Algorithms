# 실버 5


n = int(input())
li = [0] * n

for _ in range(n):
    li[_] = int(input())

li.sort()

for j in li:
    print(j)