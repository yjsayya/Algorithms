import sys

n = int(input())
li = []
for i in range(n):
    input_data = sys.stdin.readline().split()
    li.append((input_data[0], int(input_data[1])))

li = sorted(li, key=lambda student: student[1])

for student in li:
    print(student[0], end=' ')
