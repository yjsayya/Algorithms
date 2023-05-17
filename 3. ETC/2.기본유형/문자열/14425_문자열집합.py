# 문자열 - 단순 구현 문제

# *********** ㅈㄴ 개 중요 ***********
# python 에서 기본적으로 탐색해드는 시간을 보면
    # list는 탐색의 시간 복잡도가 O(n^2)
    # set은 탐색의 시간 복잡도가 O(1) ~ O(n)
        # set의 경우 hash table 구조를 사용하기 때문에 훨씬 빠름
        # set - key
        # dic - key:value
        # 이런 형식이라고 보면 된다
# *********** ㅈㄴ 개 중요 ***********

# 첫번쨰로 푼 풀이
    # --> 시간복잡도를 고려 안했더니 에러가 나버렸다
    # O(10,000*10,000*500)이라서 시간 초과 무조건이지
n, m = map(int, input().split())

sn = [""] * n
cnt = 0

for i in range(n):
    sn[i] = input()

for _ in range(m):
    a = input()
    if a in sn:
        cnt += 1

print(cnt)

# 두번째로 푼 풀이
    # --> 이번엔 시간 복잡도를 고려해보자
    # --> 동일한 풀이지만 set으로 바꿔서 풀면 시간초과가 안난다

n, m = map(int, input().split())
sn = set()
cnt = 0

for i in range(n):
    sn.add(input())

for _ in range(m):
    a = input()
    if a in sn:
        cnt += 1

print(cnt)