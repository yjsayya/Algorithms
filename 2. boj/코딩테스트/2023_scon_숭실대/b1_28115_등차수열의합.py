
'''
    
    idea 
    - 등차수열이 존재하는지 확인하려면 : Aarr이 등차수열이면 된다

'''

import sys

n = int(input())
Aarr = list(map(int,sys.stdin.readline().split()))

if n == 1:
    print("YES")
    print(Aarr[0] - 1)
    print(1)
else:
    check = True
    d = Aarr[1] - Aarr[0]

    for i in range(1,len(Aarr)):
        if Aarr[i] - Aarr[i-1] != d:
            check = False
            break

    if check:
        print("YES")
        print(i+1 for i in Aarr)
        print()

    else:
        print("NO")