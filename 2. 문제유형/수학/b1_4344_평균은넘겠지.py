
'''
    뒤에 이상하게 처리해야할게 있어서
    사실상 문자열 문제였다고 할 수 있다 
'''

import sys

c = int(input())
li = [list(map(int,sys.stdin.readline().split())) for _ in range(c)]

result = []

for i in li:
    avg = sum(i[1:]) / i[0]
    tot = 0
    for k in i[1:]:
        if k > avg:
            tot += 1
    result.append(round(tot/i[0]*100, 3))

for j in result:
    a = str(j).split('.')[0]
    b = str(j).split('.')[1]
    if len(b) != 3:
        while len(b) != 3:
            b += '0'
        print(a+'.'+ b+'%')
    else:
        print(str(j) + '%')