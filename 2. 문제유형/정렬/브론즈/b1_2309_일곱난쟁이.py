'''
    전체 크기가 9명으로 고정되어있으니깐 
    combinations 써도 시간복잡도에 위반 되지 않음
'''

# 내 풀이
from itertools import combinations as comb
height = [int(input()) for _ in range(9)]

total = sum(height) - 100

for i,j in comb(height, 2):
    if i + j == total:
        height.remove(i)
        height.remove(j)
        break

for k in sorted(height):
    print(k, end="\n")


# 다른 사람이 푼 풀이 
