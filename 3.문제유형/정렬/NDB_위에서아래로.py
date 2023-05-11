
n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

li.sort(reverse=True)
for j in li:
    print(j, end=" ")