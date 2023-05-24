'''
    제한사항이 (N,M <= 500_000) 이기 때문에 
        첫번째 풀이 시간 복잡도 500_000 ** 2 이기 떄문에 시간 초과가 나버렸다

    그렇다면 역시 빠른 set을 사용하면 된다
    set의 교집합을 이용해서 중복된 것들을 빠르게 구할 수 있었다 
'''

# 첫번째 풀이
# n,m = map(int,input().split())

# nohear = [input() for _ in range(n)]
# answer = []

# for i in range(m):
#     nosee = input()
#     if nosee in nohear:
#         answer.append(nosee)

# print(len(answer))
# for k in sorted(answer):
#     print(k, end="\n")

# 두번째 풀이
import sys

n,m = map(int,sys.stdin.readline().split())
nohear = set()
nosee = set()

for _ in range(n):
    name = input()
    nohear.add(name)

for _ in range(m):
    name = input()
    nosee.add(name)

answer = nohear.intersection(nosee)

print(len(answer))
for i in sorted(answer):
    print(i, end="\n")