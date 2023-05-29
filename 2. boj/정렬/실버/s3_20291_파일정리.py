# 실버 3
'''
    제한사항 (1 <= n <= 50,000)
    제한사항이 높지 않아서 시간복잡도 큰 문제 없을 듯 

    dict을 어떻게 활용할 것인가? 
'''
import sys

n = int(input())
dic = dict()

for _ in range(n):
    file = list(input().split('.'))
    if file[1] in dic:
        dic[file[1]] += 1
    else:
        dic[file[1]] = 1

li = sorted(dic.keys())

for k in li:
    print(k + ' ' + str(dic[k]), end="\n")