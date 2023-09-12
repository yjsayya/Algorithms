'''
뭐 별로 어렵지 않은 문제 
    짝수인 경우와 짝수가 아닌 경우 고려해서 계산하면 된다 
'''
import sys 

n = int(input())
li = list(map(int, sys.stdin.readline().split()))

total = sum(li)

if total % 2 == 0:
    print(total)
else:
    li.sort()
    for i in li:
        if i % 2 == 1:
            total -= i
            break
    if total % 2 == 0:
        print(total)
    else:
        print(0)