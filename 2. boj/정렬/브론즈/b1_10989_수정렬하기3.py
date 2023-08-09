a = '브론즈1'

"""
    2750번(수 정렬하기), 2751번(수 정렬하기2)와 문제가 똑같은데
    공간복잡도에 제한을 빡세게 줬다
    그냥 파이썬 라이브러리를 사용하면 안되는 문제인 것 같다
    
    [제한사항]
        - N(1 ≤ N ≤ 10,000,000)
        
        ** python은 대략적으로 1초에 2000만개 정도 연산이 가능하다
        - 현재 제한이 n(1 <= n <= 10,000,000)이기 때문에
        - 시간복잡도가 O(nlog(n))인 python 기본 라이브러리로는 해결하기 어렵다

    [해설] 
        - N 자체의 제한속도가 천만으로 굉장히 크지만
        - N의 자연수는 10,000보다 작거나 같은 자연수로 제한이 작다
        
        이럴 때는 계수 정렬 알고리즘을 이용하는 것이 딱이다!!
        
    +a) pypy로 제출하면 안되고 Python3로 제출을 해야한다!!!
"""

import sys
# 첫번째 풀이 - 만만하게 봤는데 메모리 초과가 났다
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

li.sort()

for i in li:
    print(i)

# 두번쨰 풀이 - 계수 정렬(counting sort) 알고리즘 이용
import sys

n = int(sys.stdin.readline())
li = [0] * 10_001

for _ in range(n):
    num = int(sys.stdin.readline())
    li[num] += 1

for j in range(10001):
    if li[j] != 0:
        for i in range(li[j]):
            print(i)


# 계수 정렬
n = int(input())
li = [0] * 10_001

for _ in range(n):
    num = int(input())
    li[num-1] += 1

for idx,ele in enumerate(li):
    if ele != 0:
        for _ in range(ele):
            print(idx+1)