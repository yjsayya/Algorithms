n = int(input())

li = [int(input()) for _ in range(n)]
li.sort(reverse=True)

for i in li:
    print(li, end=" ")