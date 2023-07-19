# 문자열 문제를 가장한 정렬문제인 듯

# 첫번째 풀이
n = int(input())
words = [" "] * n
for i in range(n):
    words[i] = input()

for j in words:
    for k in range(1,51):
        if len(j) == k:

