n, m, k = map(int,input().split())
num = list(map(int,input().split()))

num = list(set(num))
num.sort()

print(num)

answer = max(num) * k * (m // k)
num.pop()
answer += max(num) * (m % k)

print(answer)
