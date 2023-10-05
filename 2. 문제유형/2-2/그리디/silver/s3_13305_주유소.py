
'''
    아이디어 - 뒤에서부터 역 추적하는 탐욕 알고리즘 방식이 가장 깔끔해보인다
'''
import sys

n = int(input())
length = list(map(int, sys.stdin.readline().split()))
oilMoney = list(map(int, sys.stdin.readline().split()))
oilMoney.pop()

answer = 0
while len(oilMoney) != 0:

    if len(oilMoney) == 1:
        answer += (oilMoney[0] * length[0])
        break

    mini = min(oilMoney)   # 가장 작은 수
    idx = oilMoney.index(mini)   # 가장 작은 수의 인덱스 값
    answer += (sum(length[idx:]) * mini)

    oilMoney = oilMoney[:idx]
    length = length[:idx]

print(answer)