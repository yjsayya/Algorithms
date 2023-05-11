# 실버 3 난이도

# 그리디 문제의 가장 대표적인 문제라서 사실 상 외운 문제 ㅋㅋ

# 첫번쨰 풀이
n, total = map(int,input().split())
cnt = 0
coin_type = [0] * n

for i in range(n):
    coin_type[n-1 - i] = int(input())

for coin in coin_type:
    if coin <= total:
        cnt += (total // coin)
        total %= coin

print(cnt)