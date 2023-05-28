'''
    제한사항
    - 1 <= N <= 50
    - 1 <= 시리얼번호의 길이 <= 50

    제한사항이 굉장히 낮았기 때문에 - for문 그냥 돌려서 계산했다
'''

import sys

n = int(input())
dic = dict()

for _ in range(n):
    serial = sys.stdin.readline().rstrip() 
    tot = 0
    for i in serial:
        try:
            tot += int(i)
        except:
            continue
            
    dic[serial] = tot

for i in sorted(dic.keys(), key= lambda x : (len(x), dic[x], x)):
    print(i)