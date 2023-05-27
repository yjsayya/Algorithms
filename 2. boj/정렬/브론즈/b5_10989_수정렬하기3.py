'''
    제한사항
    - N(1 ≤ N ≤ 10,000,000)

    2750번(수 정렬하기), 2751번(수 정렬하기2)와 문제가 똑같은데
    공간복잡도에 제한을 빡세게 줬다
    그냥 파이썬 라이브러리를 사용하면 안되는 문제인 것 같다
    ** 계수 정렬을 사용해서 푸는 문제 인 것 같

'''
import sys
# 첫번째 풀이 - 만만하게 봤는데 메모리 초과가 났다
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

li.sort()

for i in li:
    print(i)

# 두번쨰 풀이 
import sys

n = int(input())
li = [0] * n

for _ in range(n):
    num = int(sys.stdin.readline())
    li[num-1] += 1

for i in range(n):
    if li[i] != 0:
        print(li[i])


# 