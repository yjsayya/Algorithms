"""
a = [-39, -37, -29, -28, -6, 2, 11]
# print(39 + 29*2 + 6*2 + 11*2) = 131
b = [-45, -26, -18, -9, -4, 22, 40, 50]
"""
import sys

n,m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

minu = []
plus = []
for i in li:
    if i < 0: minu.append(i)
    else: plus.append(i)

# minu.sort()
# plus.sort()
#
# mlen = len(minu)
# plen = len(plus)
#
# mmin = 0
# pmax = 0
#
# answer = 0
# if mlen >= m:
#     mmin = minu[0]
#     while len(minu) >= m:
#         answer += (abs(min(minu[:m]))*2)
#         del minu[:m]
#
#     if len(minu) > 0:
#         answer += abs(minu[0]) * 2
# elif 0 < mlen < m:
#     answer += abs(minu[0])*2
#
# if plen > 0:
#     pmax = plus[-1]
#     while len(plus) >= m:
#         answer += (max(plus[-m:])*2)
#         del plus[-m:]
#
#     if len(plus) > 0:
#         answer += (plus[-1]*2)
# elif 0 < plen < m:
#     answer += plus[-1]*2
#
# print(answer - abs(max(abs(mmin), pmax)))

minu.sort()
plus.sort(reverse=True)

mmin = abs(minu[0])
pmax = plus[0]

answer = 0
for i in range(len(minu)//m):
    answer += abs(minu[i*m-1])

if 0 < len(minu) < m:
    answer += abs(minu[0])

for j in range(len(plus)//m):
    answer += plus[j*m]

if 0 < len(plus) < m:
    answer += plus[0]

print(answer*2 - max(mmin, pmax))